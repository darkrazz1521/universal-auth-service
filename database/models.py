def user_model(user):
    return {
        "id": str(user["_id"]),
        "phone": user.get("phone"),
        "email": user.get("email"),
        "created_at": user.get("created_at")
    }