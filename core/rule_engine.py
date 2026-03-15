"""
Rule Engine for Jan Suvidha Portal.
Determines scheme eligibility based on user responses (rule-based, not AI).
"""


def check_eligibility(user_responses, scheme):
    eligibility = scheme.get("eligibility", {})
    reasons_met, reasons_not_met = [], []
    total_criteria, met_criteria = 0, 0

    # 1. Income check
    total_criteria += 1
    income_limit = eligibility.get("income_limit", 999999999)
    user_income = user_responses.get("income", 0)
    if user_income <= income_limit:
        met_criteria += 1
        reasons_met.append(f"Income within limit")
    else:
        reasons_not_met.append(f"Income exceeds limit of {income_limit}")

    # 2. Age check
    total_criteria += 1
    min_age = eligibility.get("min_age", 0)
    max_age = eligibility.get("max_age", 150)
    user_age = user_responses.get("age", 0)
    if min_age <= user_age <= max_age:
        met_criteria += 1
        reasons_met.append(f"Age {user_age} in range")
    else:
        reasons_not_met.append(f"Age {user_age} outside range {min_age}-{max_age}")

    # 3. Gender check
    total_criteria += 1
    gender_req = eligibility.get("gender", "all")
    user_gender = user_responses.get("gender", "").lower()
    if gender_req == "all" or user_gender == gender_req:
        met_criteria += 1
        reasons_met.append("Gender requirement met")
    else:
        reasons_not_met.append(f"Requires gender: {gender_req}")

    # 4. Category check
    total_criteria += 1
    allowed_categories = eligibility.get("categories", [])
    user_category = user_responses.get("category", "General")
    if user_category in allowed_categories:
        met_criteria += 1
        reasons_met.append(f"Category {user_category} eligible")
    else:
        reasons_not_met.append(f"Category {user_category} not eligible")

    # 5. Occupation check
    total_criteria += 1
    allowed_occ = eligibility.get("occupation", ["any"])
    user_occ = user_responses.get("occupation", "any")
    if "any" in allowed_occ or user_occ in allowed_occ:
        met_criteria += 1
        reasons_met.append("Occupation requirement met")
    else:
        reasons_not_met.append(f"Occupation '{user_occ}' not eligible")

    # 6. Location check
    total_criteria += 1
    loc_req = eligibility.get("location", {})
    allowed_states = loc_req.get("states", [])
    user_state = user_responses.get("state", "")
    if not allowed_states or user_state in allowed_states:
        met_criteria += 1
        reasons_met.append("Location eligible")
    else:
        reasons_not_met.append(f"Not available in {user_state}")

    # 7. BPL check
    if eligibility.get("bpl_required", False):
        total_criteria += 1
        if user_responses.get("bpl_card", False):
            met_criteria += 1
            reasons_met.append("BPL card confirmed")
        else:
            reasons_not_met.append("BPL card required")

    # 8. Land ownership check
    if eligibility.get("has_land", False):
        total_criteria += 1
        if user_responses.get("has_land", False):
            met_criteria += 1
            reasons_met.append("Land ownership confirmed")
        else:
            reasons_not_met.append("Land ownership required")

    # 9. Disability check
    if eligibility.get("disability", False):
        total_criteria += 1
        if user_responses.get("disability", False):
            met_criteria += 1
            reasons_met.append("Disability status confirmed")
        else:
            reasons_not_met.append("Disability certificate required")

    match_score = (met_criteria / total_criteria * 100) if total_criteria > 0 else 0
    is_eligible = met_criteria == total_criteria
    is_partial = match_score >= 70 and not is_eligible

    return {
        "eligible": is_eligible, "partial": is_partial,
        "match_score": round(match_score, 1),
        "met_criteria": met_criteria, "total_criteria": total_criteria,
        "reasons_met": reasons_met, "reasons_not_met": reasons_not_met,
    }


def calculate_benefit_probability(eligibility_result, doc_completeness):
    score = eligibility_result.get("match_score", 0)
    return round(min((score * 0.6) + (doc_completeness * 0.4), 100), 1)


def calculate_document_completeness(required_docs, uploaded_docs):
    if not required_docs:
        return 100.0
    uploaded = sum(1 for d in required_docs if uploaded_docs.get(d, {}).get("uploaded", False))
    return round((uploaded / len(required_docs)) * 100, 1)


def find_eligible_schemes(user_responses, all_schemes):
    results = []
    for scheme in all_schemes:
        if not scheme.get("is_active", True):
            continue
        result = check_eligibility(user_responses, scheme)
        if result["eligible"] or result["partial"]:
            results.append({
                "scheme": scheme,
                "eligibility": result,
                "benefit_probability": calculate_benefit_probability(result, 0),
            })
    results.sort(key=lambda x: (x["eligibility"]["eligible"], x["eligibility"]["match_score"]), reverse=True)
    return results
