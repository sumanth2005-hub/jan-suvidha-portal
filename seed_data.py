"""
Seed MongoDB with dummy data for Jan Suvidha Portal.
Run: python seed_data.py
"""
import os
import sys
import django
from datetime import datetime, timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jan_suvidha.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from core.db import get_db
from core.dummy_data import DUMMY_SCHEMES, DUMMY_USERS, DUMMY_RESPONSES, DUMMY_APPLICATIONS, LOCATIONS


def seed():
    db = get_db()
    now = datetime.now(timezone.utc)

    # Clear existing data
    for col in ['schemes', 'users', 'user_responses', 'applications']:
        db[col].drop()
    print("[*] Cleared existing collections.")

    # Seed schemes
    db['schemes'].insert_many(DUMMY_SCHEMES)
    print(f"[+] Inserted {len(DUMMY_SCHEMES)} schemes.")

    # Seed users
    for u in DUMMY_USERS:
        u['created_at'] = now
    user_results = db['users'].insert_many(DUMMY_USERS)
    user_ids = user_results.inserted_ids
    print(f"[+] Inserted {len(DUMMY_USERS)} users.")

    # Seed user responses
    responses = []
    for r in DUMMY_RESPONSES:
        responses.append({
            "user_id": user_ids[r["user_index"]],
            "responses": r["responses"],
            "matched_schemes": r["matched_schemes"],
            "created_at": now,
        })
    db['user_responses'].insert_many(responses)
    print(f"[+] Inserted {len(responses)} user responses.")

    # Seed applications
    apps = []
    for a in DUMMY_APPLICATIONS:
        apps.append({
            "user_id": user_ids[a["user_index"]],
            "scheme_id": a["scheme_id"],
            "status": a["status"],
            "document_completeness": a["doc_completeness"],
            "benefit_probability": a["benefit_prob"],
            "documents_uploaded": {},
            "reminder_sent": False,
            "created_at": now,
        })
    db['applications'].insert_many(apps)
    print(f"[+] Inserted {len(apps)} applications.")

    # Store locations as a config document
    db['config'].drop()
    db['config'].insert_one({"key": "locations", "data": LOCATIONS})
    print("[+] Inserted location hierarchy.")

    print("\n[OK] Database seeded successfully!")
    print(f"   Database: {db.name}")
    print(f"   Collections: {db.list_collection_names()}")


if __name__ == '__main__':
    seed()
