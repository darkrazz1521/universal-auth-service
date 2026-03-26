from fastapi import APIRouter
from services.otp_service import store_otp, verify_otp
from services.email_service import send_email   # ✅ ADD THIS
from services.token_service import create_access_token

router = APIRouter()

@router.post("/send-otp")
def send_otp(email: str):
    otp = store_otp(email)

    send_email(email, otp)

    return {"message": "OTP sent to email"}

@router.post("/verify-otp")
def verify(email: str, otp: str):
    success, message = verify_otp(email, otp)

    if not success:
        return {"status": "fail", "message": message}

    # ✅ Generate JWT
    token = create_access_token({"sub": email})

    return {
        "status": "success",
        "access_token": token,
        "token_type": "bearer"
    }