# CHANGES.md

## 🔥 Issues Found
- All logic in one file (`app.py`)
- Passwords stored in plain text
- No input validation
- Poor separation of concerns
- Bad error messages and HTTP codes

## ✅ Changes Made
- Broke code into modular folders: routes, services, models, utils
- Added password hashing using `werkzeug.security`
- Used Marshmallow for input validation
- Improved error messages and response codes
- Separated config and DB initialization
- Wrote reusable business logic for users

## ⚠️ Assumptions
- Email is unique and used as login identifier
- Passwords not encrypted previously, so old users won't be compatible
- SQLAlchemy is used for simplicity (not raw SQL)

## 🕒 With More Time
- Add JWT-based login
- Use environment variables for secret configs
- Add pagination for `/users`
- Add error logging + request rate-limiting

## 🤖 AI Usage
- Used ChatGPT for code structure suggestions and generating boilerplate
- Modified all code to fit problem statement and project needs