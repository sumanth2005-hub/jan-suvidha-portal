"""
Flask AI Microservice for Jan Suvidha Portal.
Handles Gemini-powered dynamic questioning and language simplification.
"""
import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')

# Try to import Gemini
genai = None
try:
    import google.generativeai as google_genai
    if GEMINI_API_KEY:
        google_genai.configure(api_key=GEMINI_API_KEY)
        genai = google_genai
except ImportError:
    pass

LOCATIONS = {
    "Karnataka": {
        "Bangalore Urban": ["Yelahanka", "Whitefield", "Electronic City"],
        "Bangalore Rural": ["Hoskote", "Devanahalli", "Nelamangala"],
        "Mysore": ["Nanjangud", "T. Narasipura", "Hunsur"],
    },
    "Maharashtra": {
        "Pune": ["Haveli", "Baramati", "Junnar"],
        "Nagpur": ["Kamptee", "Hingna", "Saoner"],
    },
    "Tamil Nadu": {
        "Chennai": ["Ambattur", "Tiruvottiyur", "Madhavaram"],
        "Coimbatore": ["Pollachi", "Mettupalayam", "Sulur"],
    },
    "Uttar Pradesh": {
        "Lucknow": ["Mohanlalganj", "Bakshi Ka Talab", "Malihabad"],
        "Varanasi": ["Pindra", "Sevapuri", "Arajiline"],
    },
}

QUESTIONS_FLOW = [
    {"key": "state", "en": "Which state do you live in?", "hi": "आप किस राज्य में रहते हैं?", "kn": "ನೀವು ಯಾವ ರಾಜ್ಯದಲ್ಲಿ ವಾಸಿಸುತ್ತೀರಿ?", "type": "select", "options": list(LOCATIONS.keys())},
    {"key": "district", "en": "Which district?", "hi": "कौन सा जिला?", "kn": "ಯಾವ ಜಿಲ್ಲೆ?", "type": "select"},
    {"key": "village", "en": "Which village?", "hi": "कौन सा गाँव?", "kn": "ಯಾವ ಗ್ರಾಮ?", "type": "select"},
    {"key": "name_input", "en": "What is your name?", "hi": "आपका नाम क्या है?", "kn": "ನಿಮ್ಮ ಹೆಸರೇನು?", "type": "text"},
    {"key": "age", "en": "How old are you?", "hi": "आपकी उम्र क्या है?", "kn": "ನಿಮ್ಮ ವಯಸ್ಸು ಎಷ್ಟು?", "type": "number"},
    {"key": "gender", "en": "What is your gender?", "hi": "आपका लिंग?", "kn": "ನಿಮ್ಮ ಲಿಂಗ?", "type": "select", "options": ["male", "female", "other"]},
    {"key": "category", "en": "What is your social category?", "hi": "आपकी सामाजिक श्रेणी?", "kn": "ನಿಮ್ಮ ಸಾಮಾಜಿಕ ವರ್ಗ?", "type": "select", "options": ["General", "OBC", "SC", "ST"]},
    {"key": "occupation", "en": "What do you do for a living?", "hi": "आप क्या काम करते हैं?", "kn": "ನೀವು ಏನು ಕೆಲಸ ಮಾಡುತ್ತೀರಿ?", "type": "select", "options": ["farmer", "labourer", "self_employed", "student", "homemaker", "unemployed"]},
    {"key": "income", "en": "What is your annual family income (₹)?", "hi": "आपकी वार्षिक पारिवारिक आय (₹)?", "kn": "ನಿಮ್ಮ ವಾರ್ಷಿಕ ಕುಟುಂಬ ಆದಾಯ (₹)?", "type": "number"},
    {"key": "has_land", "en": "Do you own agricultural land?", "hi": "क्या आपके पास कृषि भूमि है?", "kn": "ನಿಮ್ಮ ಬಳಿ ಕೃಷಿ ಭೂಮಿ ಇದೆಯೇ?", "type": "yesno"},
    {"key": "bpl_card", "en": "Do you have a BPL card?", "hi": "क्या आपके पास बीपीएल कार्ड है?", "kn": "ನಿಮ್ಮ ಬಳಿ BPL ಕಾರ್ಡ್ ಇದೆಯೇ?", "type": "yesno"},
    {"key": "disability", "en": "Do you have any disability (40% or more)?", "hi": "क्या आपको कोई विकलांगता है (40% या अधिक)?", "kn": "ನಿಮಗೆ ಯಾವುದೇ ಅಂಗವಿಕಲತೆ ಇದೆಯೇ?", "type": "yesno"},
]


def get_gemini_question(current_responses, language):
    """Use Gemini to generate a simplified, conversational question."""
    if not genai:
        return None
    try:
        model = genai.GenerativeModel('gemini-pro')
        answered = list(current_responses.keys())
        next_q = None
        for q in QUESTIONS_FLOW:
            if q['key'] not in answered:
                next_q = q
                break
        if not next_q:
            return None
        lang_map = {'en': 'English', 'hi': 'Hindi', 'kn': 'Kannada'}
        lang_name = lang_map.get(language, 'English')
        prompt = f"""You are a friendly village assistant helping a rural citizen find government schemes.
Ask this question in simple {lang_name}: "{next_q['en']}"
Make it warm, simple, and easy for a person with low literacy to understand.
Keep it to ONE short sentence. Do not add any explanation."""
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception:
        return None


@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json or {}
    current = data.get('current_responses', {})
    lang = data.get('language', 'en')

    for q in QUESTIONS_FLOW:
        if q['key'] not in current:
            options = q.get('options', [])
            if q['key'] == 'district' and 'state' in current:
                options = list(LOCATIONS.get(current['state'], {}).keys())
            elif q['key'] == 'village' and 'district' in current and 'state' in current:
                options = LOCATIONS.get(current['state'], {}).get(current['district'], [])

            # Try Gemini for simplified question
            gemini_q = get_gemini_question(current, lang)
            question_text = gemini_q if gemini_q else q.get(lang, q['en'])

            return jsonify({
                'done': False,
                'question': question_text,
                'key': q['key'],
                'type': q['type'],
                'options': options,
            })

    return jsonify({'done': True, 'message': 'All questions answered'})


@app.route('/simplify', methods=['POST'])
def simplify_text():
    """Simplify complex scheme text using Gemini."""
    data = request.json or {}
    text = data.get('text', '')
    lang = data.get('language', 'en')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    if genai:
        try:
            model = genai.GenerativeModel('gemini-pro')
            lang_map = {'en': 'English', 'hi': 'Hindi', 'kn': 'Kannada'}
            prompt = f"""Simplify this government scheme text for a rural citizen with low literacy.
Use simple {lang_map.get(lang, 'English')} words. Keep it short (2-3 sentences max).
Text: "{text}"
"""
            response = model.generate_content(prompt)
            return jsonify({'simplified': response.text.strip()})
        except Exception as e:
            return jsonify({'simplified': text, 'note': 'AI unavailable'})
    return jsonify({'simplified': text, 'note': 'AI not configured'})


@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'ok', 'service': 'Jan Suvidha AI',
        'gemini': 'configured' if genai else 'not configured'
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
