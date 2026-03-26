from fastapi import APIRouter, Depends
from utils.security import verify_token

router = APIRouter()

@router.get("/profile")
def get_profile(email: str = Depends(verify_token)):
    return {
        "message": "Access granted",
        "user": email
    }