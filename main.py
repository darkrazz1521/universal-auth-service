from fastapi import FastAPI

app = FastAPI(title="Auth Service")

@app.get("/")
def root():
    return {"message": "Auth Service Running"}

from database.db import users_collection

@app.get("/test-db")
def test_db():
    users_collection.insert_one({"test": "working"})
    return {"message": "DB Connected"}

from routes.auth import router as auth_router

app.include_router(auth_router, prefix="/auth")

from routes.user import router as user_router

app.include_router(user_router, prefix="/user")