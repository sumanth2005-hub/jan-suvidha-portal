"""
Dummy scheme data for Jan Suvidha Portal.
15 schemes across 6 categories. All data is fictional — for academic/hackathon use only.
"""

DUMMY_SCHEMES = [
    # ── FARMER SCHEMES ──
    {
        "scheme_id": "SCH001",
        "name": {
            "en": "Kisan Samman Yojana",
            "hi": "किसान सम्मान योजना",
            "kn": "ಕಿಸಾನ್ ಸಮ್ಮಾನ್ ಯೋಜನೆ"
        },
        "description": {
            "en": "Financial support of ₹6,000 per year for small and marginal farmers to supplement their income.",
            "hi": "छोटे और सीमांत किसानों को उनकी आय बढ़ाने के लिए ₹6,000 प्रति वर्ष की वित्तीय सहायता।",
            "kn": "ಸಣ್ಣ ಮತ್ತು ಅತಿ ಸಣ್ಣ ರೈತರಿಗೆ ವಾರ್ಷಿಕ ₹6,000 ಆರ್ಥಿಕ ನೆರವು."
        },
        "category": "farmer",
        "eligibility": {
            "income_limit": 300000,
            "gender": "all",
            "min_age": 18,
            "max_age": 70,
            "categories": ["SC", "ST", "OBC", "General"],
            "occupation": ["farmer"],
            "has_land": True,
            "bpl_required": False,
            "disability": False,
            "location": {"states": ["Karnataka", "Maharashtra", "Tamil Nadu", "Uttar Pradesh"]}
        },
        "required_documents": ["aadhaar_card", "land_record", "bank_passbook"],
        "benefit_amount": "₹6,000/year",
        "last_date": "2026-12-31",
        "apply_link": "#apply",
        "is_active": True
    },
    {
        "scheme_id": "SCH002",
        "name": {
            "en": "Crop Insurance Scheme",
            "hi": "फसल बीमा योजना",
            "kn": "ಬೆಳೆ ವಿಮಾ ಯೋಜನೆ"
        },
        "description": {
            "en": "Insurance coverage for crop loss due to natural calamities, pests, and diseases at minimal premium.",
            "hi": "प्राकृतिक आपदाओं, कीटों और बीमारियों से फसल हानि के लिए न्यूनतम प्रीमियम पर बीमा कवरेज।",
            "kn": "ನೈಸರ್ಗಿಕ ವಿಪತ್ತು, ಕೀಟ ಮತ್ತು ರೋಗಗಳಿಂದ ಬೆಳೆ ನಷ್ಟಕ್ಕೆ ಕನಿಷ್ಠ ಪ್ರೀಮಿಯಂನಲ್ಲಿ ವಿಮಾ ರಕ್ಷಣೆ."
        },
        "category": "farmer",
        "eligibility": {
            "income_limit": 500000,
            "gender": "all",
            "min_age": 18,
            "max_age": 65,
            "categories": ["SC", "ST", "OBC", "General"],
            "occupation": ["farmer"],
            "has_land": True,
            "bpl_required": False,
            "disability": False,
            "location": {"states": ["Karnataka", "Maharashtra", "Tamil Nadu", "Uttar Pradesh"]}
        },
        "required_documents": ["aadhaar_card", "land_record", "bank_passbook", "crop_sowing_certificate"],
        "benefit_amount": "Up to ₹2,00,000",
        "last_date": "2026-09-30",
        "apply_link": "#apply",
        "is_active": True
    },
    {
        "scheme_id": "SCH003",
        "name": {
            "en": "Farm Equipment Subsidy",
            "hi": "कृषि उपकरण सब्सिडी",
            "kn": "ಕೃಷಿ ಉಪಕರಣ ಸಬ್ಸಿಡಿ"
        },
        "description": {
            "en": "50% subsidy on purchase of agricultural equipment like tractors, tillers, and irrigation pumps.",
            "hi": "ट्रैक्टर, टिलर और सिंचाई पंप जैसे कृषि उपकरणों की खरीद पर 50% सब्सिडी।",
            "kn": "ಟ್ರ್ಯಾಕ್ಟರ್, ಟಿಲ್ಲರ್ ಮತ್ತು ನೀರಾವರಿ ಪಂಪ್‌ಗಳಂತಹ ಕೃಷಿ ಉಪಕರಣಗಳ ಖರೀದಿಯ ಮೇಲೆ 50% ಸಬ್ಸಿಡಿ."
        },
        "category": "farmer",
        "eligibility": {
            "income_limit": 400000,
            "gender": "all",
            "min_age": 21,
            "max_age": 60,
            "categories": ["SC", "ST", "OBC"],
            "occupation": ["farmer"],
            "has_land": True,
            "bpl_required": False,
            "disability": False,
            "location": {"states": ["Karnataka", "Maharashtra"]}
        },
        "required_documents": ["aadhaar_card", "land_record", "income_certificate", "caste_certificate"],
        "benefit_amount": "50% subsidy (max ₹1,50,000)",
        "last_date": "2026-11-30",
        "apply_link": "#apply",
        "is_active": True
    },

    # ── WOMEN SCHEMES ──
    {
        "scheme_id": "SCH004",
        "name": {
            "en": "Mahila Shakti Yojana",
            "hi": "महिला शक्ति योजना",
            "kn": "ಮಹಿಳಾ ಶಕ್ತಿ ಯೋಜನೆ"
        },
        "description": {
            "en": "Skill development and micro-enterprise support for women from economically weaker sections.",
            "hi": "आर्थिक रूप से कमजोर वर्ग की महिलाओं के लिए कौशल विकास और सूक्ष्म-उद्यम सहायता।",
            "kn": "ಆರ್ಥಿಕವಾಗಿ ದುರ್ಬಲ ವರ್ಗದ ಮಹಿಳೆಯರಿಗೆ ಕೌಶಲ್ಯ ಅಭಿವೃದ್ಧಿ ಮತ್ತು ಸೂಕ್ಷ್ಮ-ಉದ್ಯಮ ಬೆಂಬಲ."
        },
        "category": "women",
        "eligibility": {
            "income_limit": 250000,
            "gender": "female",
            "min_age": 18,
            "max_age": 55,
            "categories": ["SC", "ST", "OBC", "General"],
            "occupation": ["any"],
            "has_land": False,
            "bpl_required": False,
            "disability": False,
            "location": {"states": ["Karnataka", "Maharashtra", "Tamil Nadu", "Uttar Pradesh"]}
        },
        "required_documents": ["aadhaar_card", "income_certificate", "bank_passbook"],
        "benefit_amount": "₹50,000 grant + training",
        "last_date": "2026-10-31",
        "apply_link": "#apply",
        "is_active": True
    },
    {
        "scheme_id": "SCH005",
        "name": {
            "en": "Maternity Benefit Program",
            "hi": "मातृत्व लाभ कार्यक्रम",
            "kn": "ಹೆರಿಗೆ ಪ್ರಯೋಜನ ಕಾರ್ಯಕ್ರಮ"
        },
        "description": {
            "en": "Cash benefit of ₹5,000 for pregnant women for first two live births for nutrition and partial wage loss.",
            "hi": "गर्भवती महिलाओं को पहले दो जीवित जन्मों के लिए पोषण और आंशिक मजदूरी हानि हेतु ₹5,000 का नकद लाभ।",
            "kn": "ಗರ್ಭಿಣಿ ಮಹಿಳೆಯರಿಗೆ ಮೊದಲ ಎರಡು ಜೀವಂತ ಜನನಗಳಿಗೆ ಪೋಷಣೆ ಮತ್ತು ಭಾಗಶಃ ವೇತನ ನಷ್ಟಕ್ಕಾಗಿ ₹5,000 ನಗದು ಪ್ರಯೋಜನ."
        },
        "category": "women",
        "eligibility": {
            "income_limit": 350000,
            "gender": "female",
            "min_age": 18,
            "max_age": 45,
            "categories": ["SC", "ST", "OBC", "General"],
            "occupation": ["any"],
            "has_land": False,
            "bpl_required": False,
            "disability": False,
            "location": {"states": ["Karnataka", "Maharashtra", "Tamil Nadu", "Uttar Pradesh"]}
        },
        "required_documents": ["aadhaar_card", "pregnancy_certificate", "bank_passbook"],
        "benefit_amount": "₹5,000",
        "last_date": "2026-12-31",
        "apply_link": "#apply",
        "is_active": True
    },

    # ── BPL / HOUSING SCHEMES ──
    {
        "scheme_id": "SCH006",
        "name": {
            "en": "Awas Gramin Yojana",
            "hi": "आवास ग्रामीण योजना",
            "kn": "ಆವಾಸ್ ಗ್ರಾಮೀಣ ಯೋಜನೆ"
        },
        "description": {
            "en": "Financial assistance of ₹1,20,000 to BPL families for construction of pucca houses in rural areas.",
            "hi": "ग्रामीण क्षेत्रों में पक्के मकान के निर्माण के लिए बीपीएल परिवारों को ₹1,20,000 की वित्तीय सहायता।",
            "kn": "ಗ್ರಾಮೀಣ ಪ್ರದೇಶಗಳಲ್ಲಿ ಪಕ್ಕಾ ಮನೆಗಳ ನಿರ್ಮಾಣಕ್ಕಾಗಿ BPL ಕುಟುಂಬಗಳಿಗೆ ₹1,20,000 ಆರ್ಥಿಕ ನೆರವು."
        },
        "category": "housing",
        "eligibility": {
            "income_limit": 200000,
            "gender": "all",
            "min_age": 21,
            "max_age": 70,
            "categories": ["SC", "ST", "OBC", "General"],
            "occupation": ["any"],
            "has_land": False,
            "bpl_required": True,
            "disability": False,
            "location": {"states": ["Karnataka", "Maharashtra", "Tamil Nadu", "Uttar Pradesh"]}
        },
        "required_documents": ["aadhaar_card", "bpl_card", "income_certificate", "bank_passbook"],
        "benefit_amount": "₹1,20,000",
        "last_date": "2026-12-31",
        "apply_link": "#apply",
        "is_active": True
    },

    # ── SC/ST SCHEMES ──
    {
        "scheme_id": "SCH007",
        "name": {
            "en": "SC/ST Scholarship Program",
            "hi": "अनुसूचित जाति/जनजाति छात्रवृत्ति कार्यक्रम",
            "kn": "ಎಸ್‌ಸಿ/ಎಸ್‌ಟಿ ವಿದ್ಯಾರ್ಥಿವೇತನ ಕಾರ್ಯಕ್ರಮ"
        },
        "description": {
            "en": "Full tuition scholarship and monthly stipend for SC/ST students pursuing higher education.",
            "hi": "उच्च शिक्षा प्राप्त करने वाले अनुसूचित जाति/जनजाति छात्रों के लिए पूर्ण ट्यूशन छात्रवृत्ति और मासिक वजीफा।",
            "kn": "ಉನ್ನತ ಶಿಕ್ಷಣ ಪಡೆಯುತ್ತಿರುವ SC/ST ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ ಪೂರ್ಣ ಟ್ಯೂಷನ್ ವಿದ್ಯಾರ್ಥಿವೇತನ ಮತ್ತು ಮಾಸಿಕ ಸ್ಟೈಪೆಂಡ್."
        },
        "category": "education",
        "eligibility": {
            "income_limit": 350000,
            "gender": "all",
            "min_age": 16,
            "max_age": 35,
            "categories": ["SC", "ST"],
            "occupation": ["student", "any"],
            "has_land": False,
            "bpl_required": False,
            "disability": False,
            "location": {"states": ["Karnataka", "Maharashtra", "Tamil Nadu", "Uttar Pradesh"]}
        },
        "required_documents": ["aadhaar_card", "caste_certificate", "income_certificate", "education_certificate"],
        "benefit_amount": "Full tuition + ₹3,000/month",
        "last_date": "2026-08-31",
        "apply_link": "#apply",
        "is_active": True
    },
    {
        "scheme_id": "SCH008",
        "name": {
            "en": "SC/ST Self Employment Loan",
            "hi": "अनुसूचित जाति/जनजाति स्वरोजगार ऋण",
            "kn": "ಎಸ್‌ಸಿ/ಎಸ್‌ಟಿ ಸ್ವಯಂ ಉದ್ಯೋಗ ಸಾಲ"
        },
        "description": {
            "en": "Low-interest loan up to ₹5,00,000 for SC/ST individuals to start small businesses.",
            "hi": "अनुसूचित जाति/जनजाति व्यक्तियों को छोटा व्यवसाय शुरू करने के लिए ₹5,00,000 तक का कम ब्याज ऋण।",
            "kn": "SC/ST ವ್ಯಕ್ತಿಗಳು ಸಣ್ಣ ವ್ಯಾಪಾರ ಪ್ರಾರಂಭಿಸಲು ₹5,00,000 ವರೆಗೆ ಕಡಿಮೆ ಬಡ್ಡಿ ಸಾಲ."
        },
        "category": "employment",
        "eligibility": {
            "income_limit": 300000,
            "gender": "all",
            "min_age": 21,
            "max_age": 55,
            "categories": ["SC", "ST"],
            "occupation": ["unemployed", "self_employed", "any"],
            "has_land": False,
            "bpl_required": False,
            "disability": False,
            "location": {"states": ["Karnataka", "Maharashtra", "Tamil Nadu"]}
        },
        "required_documents": ["aadhaar_card", "caste_certificate", "income_certificate", "business_plan", "bank_passbook"],
        "benefit_amount": "Loan up to ₹5,00,000 at 4% interest",
        "last_date": "2026-12-31",
        "apply_link": "#apply",
        "is_active": True
    },

    # ── ELDERLY SCHEMES ──
    {
        "scheme_id": "SCH009",
        "name": {
            "en": "Senior Citizen Pension Scheme",
            "hi": "वरिष्ठ नागरिक पेंशन योजना",
            "kn": "ಹಿರಿಯ ನಾಗರಿಕ ಪಿಂಚಣಿ ಯೋಜನೆ"
        },
        "description": {
            "en": "Monthly pension of ₹2,000 for senior citizens above 60 years from BPL families.",
            "hi": "बीपीएल परिवारों के 60 वर्ष से अधिक आयु के वरिष्ठ नागरिकों के लिए ₹2,000 मासिक पेंशन।",
            "kn": "BPL ಕುಟುಂಬಗಳ 60 ವರ್ಷಕ್ಕಿಂತ ಮೇಲ್ಪಟ್ಟ ಹಿರಿಯ ನಾಗರಿಕರಿಗೆ ₹2,000 ಮಾಸಿಕ ಪಿಂಚಣಿ."
        },
        "category": "elderly",
        "eligibility": {
            "income_limit": 200000,
            "gender": "all",
            "min_age": 60,
            "max_age": 100,
            "categories": ["SC", "ST", "OBC", "General"],
            "occupation": ["any"],
            "has_land": False,
            "bpl_required": True,
            "disability": False,
            "location": {"states": ["Karnataka", "Maharashtra", "Tamil Nadu", "Uttar Pradesh"]}
        },
        "required_documents": ["aadhaar_card", "age_proof", "bpl_card", "bank_passbook"],
        "benefit_amount": "₹2,000/month",
        "last_date": "2026-12-31",
        "apply_link": "#apply",
        "is_active": True
    },

    # ── DISABILITY SCHEMES ──
    {
        "scheme_id": "SCH010",
        "name": {
            "en": "Disability Support Allowance",
            "hi": "विकलांगता सहायता भत्ता",
            "kn": "ಅಂಗವಿಕಲ ಬೆಂಬಲ ಭತ್ಯೆ"
        },
        "description": {
            "en": "Monthly allowance of ₹2,500 for persons with 40% or more disability for essential needs.",
            "hi": "40% या अधिक विकलांगता वाले व्यक्तियों के लिए आवश्यक जरूरतों हेतु ₹2,500 मासिक भत्ता।",
            "kn": "40% ಅಥವಾ ಹೆಚ್ಚಿನ ಅಂಗವಿಕಲತೆ ಹೊಂದಿರುವ ವ್ಯಕ್ತಿಗಳಿಗೆ ಅಗತ್ಯ ಅವಶ್ಯಕತೆಗಳಿಗಾಗಿ ₹2,500 ಮಾಸಿಕ ಭತ್ಯೆ."
        },
        "category": "disability",
        "eligibility": {
            "income_limit": 300000,
            "gender": "all",
            "min_age": 5,
            "max_age": 100,
            "categories": ["SC", "ST", "OBC", "General"],
            "occupation": ["any"],
            "has_land": False,
            "bpl_required": False,
            "disability": True,
            "location": {"states": ["Karnataka", "Maharashtra", "Tamil Nadu", "Uttar Pradesh"]}
        },
        "required_documents": ["aadhaar_card", "disability_certificate", "income_certificate", "bank_passbook"],
        "benefit_amount": "₹2,500/month",
        "last_date": "2026-12-31",
        "apply_link": "#apply",
        "is_active": True
    },

    # ── HEALTH SCHEMES ──
    {
        "scheme_id": "SCH011",
        "name": {
            "en": "Jan Arogya Health Insurance",
            "hi": "जन आरोग्य स्वास्थ्य बीमा",
            "kn": "ಜನ ಆರೋಗ್ಯ ಆರೋಗ್ಯ ವಿಮೆ"
        },
        "description": {
            "en": "Health insurance cover of ₹5,00,000 per family per year for secondary and tertiary hospitalization.",
            "hi": "माध्यमिक और तृतीयक अस्पताल में भर्ती के लिए प्रति परिवार प्रति वर्ष ₹5,00,000 का स्वास्थ्य बीमा कवर।",
            "kn": "ಪ್ರತಿ ಕುಟುಂಬಕ್ಕೆ ವಾರ್ಷಿಕ ₹5,00,000 ಆರೋಗ್ಯ ವಿಮಾ ಕವರ್."
        },
        "category": "health",
        "eligibility": {
            "income_limit": 250000,
            "gender": "all",
            "min_age": 0,
            "max_age": 100,
            "categories": ["SC", "ST", "OBC", "General"],
            "occupation": ["any"],
            "has_land": False,
            "bpl_required": True,
            "disability": False,
            "location": {"states": ["Karnataka", "Maharashtra", "Tamil Nadu", "Uttar Pradesh"]}
        },
        "required_documents": ["aadhaar_card", "bpl_card", "family_id_card", "bank_passbook"],
        "benefit_amount": "₹5,00,000/year insurance",
        "last_date": "2026-12-31",
        "apply_link": "#apply",
        "is_active": True
    },

    # ── EDUCATION SCHEMES ──
    {
        "scheme_id": "SCH012",
        "name": {
            "en": "Girl Child Education Grant",
            "hi": "बालिका शिक्षा अनुदान",
            "kn": "ಹೆಣ್ಣು ಮಕ್ಕಳ ಶಿಕ್ಷಣ ಅನುದಾನ"
        },
        "description": {
            "en": "Annual grant of ₹25,000 for education of girl children from economically weaker families.",
            "hi": "आर्थिक रूप से कमजोर परिवारों की बालिकाओं की शिक्षा के लिए ₹25,000 का वार्षिक अनुदान।",
            "kn": "ಆರ್ಥಿಕವಾಗಿ ದುರ್ಬಲ ಕುಟುಂಬಗಳ ಹೆಣ್ಣು ಮಕ್ಕಳ ಶಿಕ್ಷಣಕ್ಕಾಗಿ ₹25,000 ವಾರ್ಷಿಕ ಅನುದಾನ."
        },
        "category": "education",
        "eligibility": {
            "income_limit": 300000,
            "gender": "female",
            "min_age": 5,
            "max_age": 25,
            "categories": ["SC", "ST", "OBC", "General"],
            "occupation": ["student", "any"],
            "has_land": False,
            "bpl_required": False,
            "disability": False,
            "location": {"states": ["Karnataka", "Maharashtra", "Tamil Nadu", "Uttar Pradesh"]}
        },
        "required_documents": ["aadhaar_card", "income_certificate", "education_certificate", "bank_passbook"],
        "benefit_amount": "₹25,000/year",
        "last_date": "2026-07-31",
        "apply_link": "#apply",
        "is_active": True
    },

    # ── DIGITAL LITERACY ──
    {
        "scheme_id": "SCH013",
        "name": {
            "en": "Digital Saksharta Abhiyan",
            "hi": "डिजिटल साक्षरता अभियान",
            "kn": "ಡಿಜಿಟಲ್ ಸಾಕ್ಷರತಾ ಅಭಿಯಾನ"
        },
        "description": {
            "en": "Free digital literacy training for one member per rural household to bridge the digital divide.",
            "hi": "डिजिटल विभाजन को पाटने के लिए प्रति ग्रामीण परिवार एक सदस्य के लिए मुफ्त डिजिटल साक्षरता प्रशिक्षण।",
            "kn": "ಡಿಜಿಟಲ್ ಅಂತರವನ್ನು ಕಡಿಮೆ ಮಾಡಲು ಪ್ರತಿ ಗ್ರಾಮೀಣ ಕುಟುಂಬದ ಒಬ್ಬ ಸದಸ್ಯರಿಗೆ ಉಚಿತ ಡಿಜಿಟಲ್ ಸಾಕ್ಷರತಾ ತರಬೇತಿ."
        },
        "category": "digital",
        "eligibility": {
            "income_limit": 500000,
            "gender": "all",
            "min_age": 14,
            "max_age": 60,
            "categories": ["SC", "ST", "OBC", "General"],
            "occupation": ["any"],
            "has_land": False,
            "bpl_required": False,
            "disability": False,
            "location": {"states": ["Karnataka", "Maharashtra", "Tamil Nadu", "Uttar Pradesh"]}
        },
        "required_documents": ["aadhaar_card", "address_proof"],
        "benefit_amount": "Free training + certificate",
        "last_date": "2026-12-31",
        "apply_link": "#apply",
        "is_active": True
    },

    # ── EMPLOYMENT SCHEMES ──
    {
        "scheme_id": "SCH014",
        "name": {
            "en": "Rural Employment Guarantee",
            "hi": "ग्रामीण रोजगार गारंटी",
            "kn": "ಗ್ರಾಮೀಣ ಉದ್ಯೋಗ ಖಾತ್ರಿ"
        },
        "description": {
            "en": "Guaranteed 100 days of wage employment per year to rural households for unskilled manual work.",
            "hi": "ग्रामीण परिवारों को अकुशल शारीरिक कार्य के लिए प्रति वर्ष 100 दिनों के वेतन रोजगार की गारंटी।",
            "kn": "ಗ್ರಾಮೀಣ ಕುಟುಂಬಗಳಿಗೆ ಅಕೌಶಲ ಕೈ ಕೆಲಸಕ್ಕೆ ವಾರ್ಷಿಕ 100 ದಿನಗಳ ವೇತನ ಉದ್ಯೋಗ ಖಾತ್ರಿ."
        },
        "category": "employment",
        "eligibility": {
            "income_limit": 250000,
            "gender": "all",
            "min_age": 18,
            "max_age": 65,
            "categories": ["SC", "ST", "OBC", "General"],
            "occupation": ["unemployed", "farmer", "labourer", "any"],
            "has_land": False,
            "bpl_required": False,
            "disability": False,
            "location": {"states": ["Karnataka", "Maharashtra", "Tamil Nadu", "Uttar Pradesh"]}
        },
        "required_documents": ["aadhaar_card", "address_proof", "bank_passbook"],
        "benefit_amount": "100 days @ ₹309/day",
        "last_date": "2026-12-31",
        "apply_link": "#apply",
        "is_active": True
    },

    # ── OBC SCHEME ──
    {
        "scheme_id": "SCH015",
        "name": {
            "en": "OBC Skill Development Fund",
            "hi": "ओबीसी कौशल विकास निधि",
            "kn": "OBC ಕೌಶಲ್ಯ ಅಭಿವೃದ್ಧಿ ನಿಧಿ"
        },
        "description": {
            "en": "Vocational training and certification courses for OBC youth with ₹15,000 stipend during training.",
            "hi": "ओबीसी युवाओं के लिए व्यावसायिक प्रशिक्षण और प्रमाणन पाठ्यक्रम, प्रशिक्षण के दौरान ₹15,000 वजीफा।",
            "kn": "OBC ಯುವಕರಿಗೆ ವೃತ್ತಿಪರ ತರಬೇತಿ ಮತ್ತು ಪ್ರಮಾಣೀಕರಣ ಕೋರ್ಸ್‌ಗಳು, ತರಬೇತಿ ಸಮಯದಲ್ಲಿ ₹15,000 ಸ್ಟೈಪೆಂಡ್."
        },
        "category": "employment",
        "eligibility": {
            "income_limit": 400000,
            "gender": "all",
            "min_age": 18,
            "max_age": 35,
            "categories": ["OBC"],
            "occupation": ["unemployed", "student", "any"],
            "has_land": False,
            "bpl_required": False,
            "disability": False,
            "location": {"states": ["Karnataka", "Maharashtra", "Tamil Nadu"]}
        },
        "required_documents": ["aadhaar_card", "caste_certificate", "income_certificate", "education_certificate"],
        "benefit_amount": "Free training + ₹15,000 stipend",
        "last_date": "2026-10-31",
        "apply_link": "#apply",
        "is_active": True
    },
]

# Dummy location hierarchy
LOCATIONS = {
    "Karnataka": {
        "Bangalore Urban": ["Yelahanka", "Whitefield", "Electronic City", "Jayanagar", "Malleshwaram"],
        "Bangalore Rural": ["Hoskote", "Devanahalli", "Nelamangala", "Doddaballapur", "Anekal"],
        "Mysore": ["Nanjangud", "T. Narasipura", "Hunsur", "K.R. Nagar", "Periyapatna"],
        "Belgaum": ["Athani", "Chikkodi", "Gokak", "Raibag", "Savadatti"],
    },
    "Maharashtra": {
        "Pune": ["Haveli", "Baramati", "Junnar", "Shirur", "Mulshi"],
        "Nagpur": ["Kamptee", "Hingna", "Saoner", "Ramtek", "Umred"],
        "Nashik": ["Igatpuri", "Trimbak", "Sinnar", "Dindori", "Kalwan"],
    },
    "Tamil Nadu": {
        "Chennai": ["Ambattur", "Tiruvottiyur", "Madhavaram", "Sholinganallur", "Perungudi"],
        "Coimbatore": ["Pollachi", "Mettupalayam", "Sulur", "Annur", "Kinathukadavu"],
        "Madurai": ["Melur", "Thirumangalam", "Usilampatti", "Vadipatti", "Peraiyur"],
    },
    "Uttar Pradesh": {
        "Lucknow": ["Mohanlalganj", "Bakshi Ka Talab", "Malihabad", "Sarojini Nagar", "Chinhat"],
        "Varanasi": ["Pindra", "Sevapuri", "Arajiline", "Kashi Vidyapeeth", "Cholapur"],
        "Agra": ["Fatehpur Sikri", "Kiraoli", "Bah", "Etmadpur", "Kheragarh"],
    },
}

# Dummy users for seeding (representing various citizen profiles)
DUMMY_USERS = [
    {"phone": "9876543210", "name": "Ramesh Kumar", "language": "hi", "village": "Hoskote", "district": "Bangalore Rural", "state": "Karnataka", "whatsapp_consent": True},
    {"phone": "9876543211", "name": "Lakshmi Devi", "language": "kn", "village": "Nanjangud", "district": "Mysore", "state": "Karnataka", "whatsapp_consent": True},
    {"phone": "9876543212", "name": "Suresh Patil", "language": "en", "village": "Baramati", "district": "Pune", "state": "Maharashtra", "whatsapp_consent": False},
    {"phone": "9876543213", "name": "Annapurna M", "language": "kn", "village": "Hunsur", "district": "Mysore", "state": "Karnataka", "whatsapp_consent": True},
    {"phone": "9876543214", "name": "Raju Gowda", "language": "kn", "village": "Devanahalli", "district": "Bangalore Rural", "state": "Karnataka", "whatsapp_consent": True},
    {"phone": "9876543215", "name": "Meena Kumari", "language": "hi", "village": "Mohanlalganj", "district": "Lucknow", "state": "Uttar Pradesh", "whatsapp_consent": True},
    {"phone": "9876543216", "name": "Selvam R", "language": "en", "village": "Pollachi", "district": "Coimbatore", "state": "Tamil Nadu", "whatsapp_consent": False},
    {"phone": "9876543217", "name": "Ganga Bai", "language": "hi", "village": "Pindra", "district": "Varanasi", "state": "Uttar Pradesh", "whatsapp_consent": True},
    {"phone": "9876543218", "name": "Manjunath S", "language": "kn", "village": "Athani", "district": "Belgaum", "state": "Karnataka", "whatsapp_consent": True},
    {"phone": "9876543219", "name": "Priya Sharma", "language": "hi", "village": "Chinhat", "district": "Lucknow", "state": "Uttar Pradesh", "whatsapp_consent": True},
]

# Dummy user responses for analytics
DUMMY_RESPONSES = [
    {"user_index": 0, "responses": {"income": 180000, "occupation": "farmer", "gender": "male", "age": 45, "category": "OBC", "has_land": True, "disability": False, "bpl_card": True, "state": "Karnataka", "district": "Bangalore Rural", "village": "Hoskote"}, "matched_schemes": ["SCH001", "SCH002", "SCH006", "SCH011", "SCH014"]},
    {"user_index": 1, "responses": {"income": 120000, "occupation": "farmer", "gender": "female", "age": 38, "category": "SC", "has_land": True, "disability": False, "bpl_card": True, "state": "Karnataka", "district": "Mysore", "village": "Nanjangud"}, "matched_schemes": ["SCH001", "SCH004", "SCH005", "SCH006", "SCH007", "SCH011"]},
    {"user_index": 2, "responses": {"income": 280000, "occupation": "labourer", "gender": "male", "age": 32, "category": "ST", "has_land": False, "disability": False, "bpl_card": False, "state": "Maharashtra", "district": "Pune", "village": "Baramati"}, "matched_schemes": ["SCH008", "SCH013", "SCH014"]},
    {"user_index": 3, "responses": {"income": 90000, "occupation": "homemaker", "gender": "female", "age": 55, "category": "SC", "has_land": False, "disability": True, "bpl_card": True, "state": "Karnataka", "district": "Mysore", "village": "Hunsur"}, "matched_schemes": ["SCH004", "SCH006", "SCH010", "SCH011"]},
    {"user_index": 4, "responses": {"income": 220000, "occupation": "farmer", "gender": "male", "age": 50, "category": "OBC", "has_land": True, "disability": False, "bpl_card": False, "state": "Karnataka", "district": "Bangalore Rural", "village": "Devanahalli"}, "matched_schemes": ["SCH001", "SCH002", "SCH013", "SCH014"]},
    {"user_index": 5, "responses": {"income": 150000, "occupation": "homemaker", "gender": "female", "age": 28, "category": "General", "has_land": False, "disability": False, "bpl_card": True, "state": "Uttar Pradesh", "district": "Lucknow", "village": "Mohanlalganj"}, "matched_schemes": ["SCH004", "SCH005", "SCH006", "SCH011", "SCH013"]},
    {"user_index": 6, "responses": {"income": 350000, "occupation": "self_employed", "gender": "male", "age": 40, "category": "OBC", "has_land": False, "disability": False, "bpl_card": False, "state": "Tamil Nadu", "district": "Coimbatore", "village": "Pollachi"}, "matched_schemes": ["SCH013", "SCH015"]},
    {"user_index": 7, "responses": {"income": 80000, "occupation": "homemaker", "gender": "female", "age": 68, "category": "SC", "has_land": False, "disability": False, "bpl_card": True, "state": "Uttar Pradesh", "district": "Varanasi", "village": "Pindra"}, "matched_schemes": ["SCH004", "SCH006", "SCH009", "SCH011"]},
    {"user_index": 8, "responses": {"income": 200000, "occupation": "farmer", "gender": "male", "age": 42, "category": "SC", "has_land": True, "disability": False, "bpl_card": True, "state": "Karnataka", "district": "Belgaum", "village": "Athani"}, "matched_schemes": ["SCH001", "SCH002", "SCH003", "SCH006", "SCH008", "SCH011", "SCH014"]},
    {"user_index": 9, "responses": {"income": 160000, "occupation": "student", "gender": "female", "age": 20, "category": "OBC", "has_land": False, "disability": False, "bpl_card": False, "state": "Uttar Pradesh", "district": "Lucknow", "village": "Chinhat"}, "matched_schemes": ["SCH004", "SCH012", "SCH013", "SCH015"]},
]

# Dummy applications (some applied, some not — to show underutilization)
DUMMY_APPLICATIONS = [
    {"user_index": 0, "scheme_id": "SCH001", "status": "applied", "doc_completeness": 100, "benefit_prob": 92},
    {"user_index": 0, "scheme_id": "SCH002", "status": "applied", "doc_completeness": 75, "benefit_prob": 70},
    {"user_index": 0, "scheme_id": "SCH006", "status": "eligible_not_applied", "doc_completeness": 50, "benefit_prob": 55},
    {"user_index": 0, "scheme_id": "SCH011", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 40},
    {"user_index": 0, "scheme_id": "SCH014", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 35},
    {"user_index": 1, "scheme_id": "SCH001", "status": "applied", "doc_completeness": 100, "benefit_prob": 95},
    {"user_index": 1, "scheme_id": "SCH004", "status": "applied", "doc_completeness": 100, "benefit_prob": 88},
    {"user_index": 1, "scheme_id": "SCH005", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 42},
    {"user_index": 1, "scheme_id": "SCH006", "status": "eligible_not_applied", "doc_completeness": 33, "benefit_prob": 45},
    {"user_index": 1, "scheme_id": "SCH007", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 38},
    {"user_index": 1, "scheme_id": "SCH011", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 35},
    {"user_index": 2, "scheme_id": "SCH008", "status": "applied", "doc_completeness": 80, "benefit_prob": 72},
    {"user_index": 2, "scheme_id": "SCH013", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 30},
    {"user_index": 2, "scheme_id": "SCH014", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 32},
    {"user_index": 3, "scheme_id": "SCH010", "status": "applied", "doc_completeness": 100, "benefit_prob": 90},
    {"user_index": 3, "scheme_id": "SCH004", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 40},
    {"user_index": 3, "scheme_id": "SCH006", "status": "eligible_not_applied", "doc_completeness": 25, "benefit_prob": 45},
    {"user_index": 3, "scheme_id": "SCH011", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 33},
    {"user_index": 4, "scheme_id": "SCH001", "status": "applied", "doc_completeness": 100, "benefit_prob": 88},
    {"user_index": 4, "scheme_id": "SCH002", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 35},
    {"user_index": 4, "scheme_id": "SCH013", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 30},
    {"user_index": 4, "scheme_id": "SCH014", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 28},
    {"user_index": 5, "scheme_id": "SCH004", "status": "applied", "doc_completeness": 100, "benefit_prob": 85},
    {"user_index": 5, "scheme_id": "SCH005", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 40},
    {"user_index": 5, "scheme_id": "SCH006", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 38},
    {"user_index": 5, "scheme_id": "SCH011", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 30},
    {"user_index": 5, "scheme_id": "SCH013", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 32},
    {"user_index": 6, "scheme_id": "SCH013", "status": "eligible_not_applied", "doc_completeness": 50, "benefit_prob": 45},
    {"user_index": 6, "scheme_id": "SCH015", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 35},
    {"user_index": 7, "scheme_id": "SCH009", "status": "applied", "doc_completeness": 100, "benefit_prob": 92},
    {"user_index": 7, "scheme_id": "SCH004", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 38},
    {"user_index": 7, "scheme_id": "SCH006", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 35},
    {"user_index": 7, "scheme_id": "SCH011", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 30},
    {"user_index": 8, "scheme_id": "SCH001", "status": "applied", "doc_completeness": 100, "benefit_prob": 95},
    {"user_index": 8, "scheme_id": "SCH003", "status": "applied", "doc_completeness": 75, "benefit_prob": 72},
    {"user_index": 8, "scheme_id": "SCH002", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 35},
    {"user_index": 8, "scheme_id": "SCH006", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 38},
    {"user_index": 8, "scheme_id": "SCH008", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 32},
    {"user_index": 8, "scheme_id": "SCH011", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 30},
    {"user_index": 8, "scheme_id": "SCH014", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 28},
    {"user_index": 9, "scheme_id": "SCH012", "status": "applied", "doc_completeness": 100, "benefit_prob": 90},
    {"user_index": 9, "scheme_id": "SCH004", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 40},
    {"user_index": 9, "scheme_id": "SCH013", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 35},
    {"user_index": 9, "scheme_id": "SCH015", "status": "eligible_not_applied", "doc_completeness": 0, "benefit_prob": 38},
]
