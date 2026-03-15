/**
 * Jan Suvidha Portal — Voice Assistant (Enhanced)
 * Text-to-Speech: Web Speech API + Google TTS fallback
 * Speech-to-Text: Web Speech Recognition API
 * Supports: English, Hindi, Kannada, Telugu, Tamil
 *
 * The key fix: Chrome on Windows only has native voices for English & Hindi.
 * For Kannada, Telugu, Tamil we use Google Translate TTS as a reliable fallback.
 */

let speechSynth = window.speechSynthesis;
let currentUtterance = null;
let isVoiceEnabled = true;
let audioPlayer = null; // For Google TTS fallback

// Language to BCP 47 code mapping
const langVoiceMap = {
    'en': { code: 'en-IN', gttsCode: 'en', name: 'English' },
    'hi': { code: 'hi-IN', gttsCode: 'hi', name: 'Hindi' },
    'kn': { code: 'kn-IN', gttsCode: 'kn', name: 'Kannada' },
    'te': { code: 'te-IN', gttsCode: 'te', name: 'Telugu' },
    'ta': { code: 'ta-IN', gttsCode: 'ta', name: 'Tamil' },
};

// Language display names
const langDisplayNames = {
    'en': 'English',
    'hi': 'हिन्दी',
    'kn': 'ಕನ್ನಡ',
    'te': 'తెలుగు',
    'ta': 'தமிழ்',
};

// Track which languages have working native voices
let nativeVoiceSupport = {};

/**
 * Check if a native speech synthesis voice exists for a language
 */
function hasNativeVoice(langCode) {
    if (!speechSynth) return false;
    const voices = speechSynth.getVoices();
    const config = langVoiceMap[langCode];
    if (!config) return false;
    return voices.some(v =>
        v.lang === config.code ||
        v.lang.startsWith(config.code.split('-')[0])
    );
}

/**
 * Clean text for speech — remove emojis and special chars
 */
function cleanTextForSpeech(text) {
    return text
        .replace(/[\u{1F600}-\u{1F64F}\u{1F300}-\u{1F5FF}\u{1F680}-\u{1F6FF}\u{1F1E0}-\u{1F1FF}\u{2702}-\u{27B0}\u{24C2}-\u{1F251}]/gu, '')
        .replace(/[⬆️⬇️➡️⬅️✅❌🎉🎯💡🔍📋📄🏛️🤖🎧]/g, '')
        .replace(/\s+/g, ' ')
        .trim();
}

/**
 * Split long text into chunks (Google TTS has a ~200 char limit per request)
 */
function splitTextForTTS(text, maxLen = 180) {
    if (text.length <= maxLen) return [text];

    const chunks = [];
    const sentences = text.split(/(?<=[।.!?\n])\s*/);
    let current = '';

    for (const sentence of sentences) {
        if ((current + ' ' + sentence).trim().length <= maxLen) {
            current = (current + ' ' + sentence).trim();
        } else {
            if (current) chunks.push(current);
            // If single sentence is too long, split by commas or spaces
            if (sentence.length > maxLen) {
                const parts = sentence.split(/(?<=[,，、])\s*/);
                let sub = '';
                for (const part of parts) {
                    if ((sub + ' ' + part).trim().length <= maxLen) {
                        sub = (sub + ' ' + part).trim();
                    } else {
                        if (sub) chunks.push(sub);
                        sub = part;
                    }
                }
                if (sub) current = sub;
            } else {
                current = sentence;
            }
        }
    }
    if (current) chunks.push(current);
    return chunks.length > 0 ? chunks : [text.substring(0, maxLen)];
}

/**
 * Play audio via Google Translate TTS (fallback for languages without native voices)
 */
function playGoogleTTS(text, langCode) {
    return new Promise((resolve, reject) => {
        const config = langVoiceMap[langCode] || langVoiceMap['en'];
        const gttsLang = config.gttsCode || 'en';

        const chunks = splitTextForTTS(text);
        let currentChunk = 0;

        function playNextChunk() {
            if (currentChunk >= chunks.length) {
                setSpeakingState(false);
                resolve();
                return;
            }

            const chunk = chunks[currentChunk];
            const encodedText = encodeURIComponent(chunk);
            const url = `https://translate.google.com/translate_tts?ie=UTF-8&q=${encodedText}&tl=${gttsLang}&client=tw-ob`;

            // Stop previous audio
            if (audioPlayer) {
                audioPlayer.pause();
                audioPlayer = null;
            }

            audioPlayer = new Audio(url);
            audioPlayer.volume = 1.0;
            audioPlayer.playbackRate = 0.9; // Slightly slower for clarity

            audioPlayer.onended = () => {
                currentChunk++;
                playNextChunk();
            };

            audioPlayer.onerror = (e) => {
                console.warn(`Google TTS error for ${gttsLang}, chunk ${currentChunk}:`, e);
                currentChunk++;
                // Try next chunk even if one fails
                if (currentChunk < chunks.length) {
                    playNextChunk();
                } else {
                    setSpeakingState(false);
                    reject(e);
                }
            };

            setSpeakingState(true);
            audioPlayer.play().catch(err => {
                console.warn('Audio play failed:', err);
                // Fallback: try native speech even if voice isn't ideal
                tryNativeSpeech(text, langCode);
                resolve();
            });
        }

        playNextChunk();
    });
}

/**
 * Use native Web Speech API synthesis
 */
function tryNativeSpeech(text, langCode) {
    if (!speechSynth) return;

    speechSynth.cancel();

    const utterance = new SpeechSynthesisUtterance(text);
    const config = langVoiceMap[langCode] || langVoiceMap['en'];
    utterance.lang = config.code;
    utterance.rate = 0.85;
    utterance.pitch = 1.0;
    utterance.volume = 1.0;

    // Find best voice
    const voices = speechSynth.getVoices();
    let voice = voices.find(v => v.lang === config.code);
    if (!voice) voice = voices.find(v => v.lang.startsWith(config.code.split('-')[0]));
    if (!voice && langCode !== 'en') voice = voices.find(v => v.lang === 'en-IN');
    if (!voice) voice = voices.find(v => v.lang.startsWith('en'));
    if (voice) utterance.voice = voice;

    utterance.onstart = () => setSpeakingState(true);
    utterance.onend = () => setSpeakingState(false);
    utterance.onerror = () => setSpeakingState(false);

    currentUtterance = utterance;
    speechSynth.speak(utterance);
}

/**
 * Main speak function — automatically picks best method per language
 * Priority: Native voice (if available) → Google TTS → fallback native
 */
function speakText(text, lang = 'en') {
    if (!isVoiceEnabled) return;

    const cleanText = cleanTextForSpeech(text);
    if (!cleanText) return;

    // Stop anything currently playing
    stopSpeech();

    // Check if native voice exists for this language
    const hasNative = hasNativeVoice(lang);

    if (hasNative) {
        // Use native Web Speech API (best quality for en, hi)
        console.log(`[Voice] Using native speech for ${lang}`);
        tryNativeSpeech(cleanText, lang);
    } else {
        // Use Google Translate TTS (works for kn, te, ta and all languages)
        console.log(`[Voice] Using Google TTS for ${lang} (no native voice found)`);
        playGoogleTTS(cleanText, lang).catch(() => {
            // Last resort: try native anyway
            console.log(`[Voice] Google TTS failed, trying native for ${lang}`);
            tryNativeSpeech(cleanText, lang);
        });
    }
}

/**
 * Stop all speech
 */
function stopSpeech() {
    if (speechSynth) speechSynth.cancel();
    if (audioPlayer) {
        audioPlayer.pause();
        audioPlayer.currentTime = 0;
        audioPlayer = null;
    }
    setSpeakingState(false);
}

/**
 * Update speaking UI state
 */
function setSpeakingState(isSpeaking) {
    document.querySelectorAll('.voice-btn').forEach(btn => {
        btn.classList.toggle('speaking', isSpeaking);
    });
}

/**
 * Check if currently speaking
 */
function isSpeaking() {
    const synthSpeaking = speechSynth && speechSynth.speaking;
    const audioPlaying = audioPlayer && !audioPlayer.paused;
    return synthSpeaking || audioPlaying;
}

/**
 * Toggle voice on/off
 */
function toggleVoice() {
    isVoiceEnabled = !isVoiceEnabled;
    if (!isVoiceEnabled) stopSpeech();
    return isVoiceEnabled;
}

/**
 * Get available voices info for debugging
 */
function getAvailableVoices() {
    if (!speechSynth) return {};
    const voices = speechSynth.getVoices();
    const available = {};
    for (const [lang, config] of Object.entries(langVoiceMap)) {
        const nativeMatch = voices.find(v => v.lang === config.code || v.lang.startsWith(lang));
        available[lang] = {
            name: config.name,
            nativeVoice: !!nativeMatch,
            nativeVoiceName: nativeMatch ? nativeMatch.name : 'None',
            googleTTS: true,  // Always available as fallback
            method: nativeMatch ? 'Native' : 'Google TTS',
        };
    }
    return available;
}

// ═══════════════════════════════════════════════════════
// SPEECH-TO-TEXT (Voice Input)
// ═══════════════════════════════════════════════════════

let recognition = null;

/**
 * Start voice input (speech-to-text)
 */
function startVoiceInput(lang = 'en', onResult) {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
        console.warn('Speech recognition not supported');
        return false;
    }

    recognition = new SpeechRecognition();
    const config = langVoiceMap[lang] || langVoiceMap['en'];
    recognition.lang = config.code;
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;
    recognition.continuous = false;

    recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        const confidence = event.results[0][0].confidence;
        console.log(`[Voice Input] "${transcript}" (confidence: ${(confidence * 100).toFixed(1)}%, lang: ${lang})`);
        if (onResult) onResult(transcript, confidence);
    };

    recognition.onerror = (event) => {
        console.warn('Voice input error:', event.error);
        document.querySelectorAll('.mic-btn, .btn-mic').forEach(btn => btn.classList.remove('recording', 'listening'));
    };

    recognition.onend = () => {
        document.querySelectorAll('.mic-btn, .btn-mic').forEach(btn => btn.classList.remove('recording', 'listening'));
    };

    recognition.start();
    document.querySelectorAll('.mic-btn, .btn-mic').forEach(btn => btn.classList.add('recording'));
    return true;
}

/**
 * Stop voice input
 */
function stopVoiceInput() {
    if (recognition) {
        recognition.stop();
        recognition = null;
    }
}

// ═══════════════════════════════════════════════════════
// INITIALIZATION
// ═══════════════════════════════════════════════════════

// Preload voices
if (speechSynth) {
    speechSynth.getVoices();
    speechSynth.onvoiceschanged = () => {
        const voices = speechSynth.getVoices();
        console.log(`[Voice] ${voices.length} native voices loaded`);

        // Log support status
        const status = Object.entries(langVoiceMap).map(([lang, config]) => {
            const found = voices.find(v => v.lang === config.code || v.lang.startsWith(lang));
            nativeVoiceSupport[lang] = !!found;
            return `${config.name}: ${found ? 'Native ✓' : 'Google TTS ↗'}`;
        });
        console.log('[Voice] Language support:', status.join(', '));
    };
}

console.log('[Voice] Jan Suvidha Voice Assistant loaded — 5 languages: English, Hindi, Kannada, Telugu, Tamil');
console.log('[Voice] Using Google TTS fallback for languages without native browser voices');
