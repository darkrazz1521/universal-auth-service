# 🔐 Universal Auth Service (OTP + JWT)

A production-ready authentication system built with FastAPI that provides secure login using Email OTP and JWT tokens. This service can be reused across multiple applications like Streamlit, React, and Android apps.

---

## 🚀 Features

* 🔑 Email OTP Authentication
* ⏱ OTP Expiry & Attempt Limit
* 🔐 JWT Token-Based Authentication
* 🛡 Protected Routes (Authorization Required)
* ☁ MongoDB Atlas (Cloud Database)
* 📧 Email Integration (Gmail SMTP)
* ⚡ FastAPI Backend (High Performance)

---

## 🧠 Architecture

User → Request OTP → Email
User → Verify OTP → JWT Token
User → Access Protected APIs

---

## 🛠 Tech Stack

* FastAPI
* MongoDB Atlas
* Python-JOSE (JWT)
* SMTP (Email Service)
* Uvicorn

---

## 📁 Project Structure

```
auth-service/
│
├── main.py
├── .env
│
├── routes/
│   ├── auth.py
│   └── user.py
│
├── services/
│   ├── otp_service.py
│   ├── token_service.py
│   └── email_service.py
│
├── database/
│   ├── db.py
│   └── models.py
│
├── utils/
│   ├── config.py
│   └── security.py
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/your-username/universal-auth-service.git
cd universal-auth-service
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Setup Environment Variables

Create a `.env` file:

```
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

MONGO_URI=your_mongodb_connection
DB_NAME=auth_db

EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
```

---

### 4. Run Server

```
uvicorn main:app --reload
```

---

## 🔑 API Endpoints

### 📩 Send OTP

```
POST /auth/send-otp?email=user@gmail.com
```

---

### ✅ Verify OTP (Login)

```
POST /auth/verify-otp?email=user@gmail.com&otp=123456
```

Returns:

```
{
  "access_token": "JWT_TOKEN",
  "token_type": "bearer"
}
```

---

### 🔒 Protected Route

```
GET /user/profile
Authorization: Bearer <JWT_TOKEN>
```

---

## 🌍 Deployment

This API can be deployed on:

* Render
* Railway
* AWS EC2
* Docker

---

## 🔐 Security Features

* OTP Expiry (5 minutes)
* Attempt Limiting
* JWT Expiration
* Environment Variable Protection

---

## 🚀 Future Improvements

* Refresh Tokens
* Role-Based Access (Admin/User)
* Rate Limiting
* OAuth (Google Login)
* Redis for OTP Storage

---

## 👨‍💻 Author

Built with ❤️ by Raj kumar

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
