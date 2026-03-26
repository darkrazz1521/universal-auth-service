import random
from datetime import datetime, timedelta
from database.db import otp_collection

OTP_EXPIRY_MINUTES = 5

def generate_otp():
    return str(random.randint(100000, 999999))


def store_otp(email: str):
    otp = generate_otp()
    expires_at = datetime.utcnow() + timedelta(minutes=5)

    otp_collection.delete_many({"email": email})

    otp_collection.insert_one({
        "email": email,
        "otp": otp,
        "expires_at": expires_at,
        "attempts": 0
    })

    return otp

def verify_otp(email: str, user_otp: str):
    record = otp_collection.find_one({"email": email})

    if not record:
        return False, "No OTP found"

    if datetime.utcnow() > record["expires_at"]:
        return False, "OTP expired"

    if record["attempts"] >= 5:
        return False, "Too many attempts"

    if record["otp"] != user_otp:
        otp_collection.update_one(
            {"email": email},
            {"$inc": {"attempts": 1}}
        )
        return False, "Invalid OTP"

    otp_collection.delete_one({"email": email})
    return True, "OTP verified"