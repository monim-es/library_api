# 📚 Library Management API

A simple **Library Management System** built with **Django Rest Framework (DRF)**.  
This API allows users to **register, log in, view and borrow books**, while **admins** can manage users and books.  
The project uses **JWT authentication** and includes a **Swagger UI** for easy testing.

---

## 🚀 Features

### 👥 User Management
- Users can **register**, **log in**, and view their own profile.  
- **Admins** can view, create, update, and delete all users.  
- Each user has a **profile** with phone number, address, and date of birth.

### 📘 Book Management
- **Admins** can add, update, or delete books.  
- **Users** can only view book lists and details.  
- Each book tracks:
  - `total_copies`
  - `available_copies`

### 🔁 Transactions
- **Checkout:** A user borrows a book (available copies decrease).
- **Return:** A user returns a book (available copies increase).
- Prevents borrowing the same book twice before returning it.

### 🔐 Authentication
- Uses **JWT (JSON Web Token)** for secure login.
- Tokens expire **after 1 hour**.
- Swagger allows token-based authorization directly from the browser.

---

## 🧠 Project Structure

library_project/
│
├── books/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│
├── users/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│
├── library_project/
│ ├── settings.py
│ ├── urls.py
│
└── manage.py


---

## ⚙️ Setup Instructions

1. **Clone the project**
   ```bash
   git clone <your-repo-url>
   cd library_project
Create a virtual environment

 
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
Install dependencies

 
pip install -r requirements.txt
Run migrations

 
python manage.py migrate
Create an admin user

 
python manage.py createsuperuser
Run the development server

 
python manage.py runserver
🌐 API Endpoints
Endpoint	Method	Description	Auth Required	Role
/api/register/	POST	Register a new user	No	Any
/api/token/	POST	Login (Get access & refresh tokens)	No	Any
/api/token/refresh/	POST	Refresh JWT token	No	Any
/api/users/	GET	List all users	Yes	Admin
/api/users/<id>/	GET	View user details	Yes	Admin
/api/books/	GET	List all books	Yes	Any
/api/books/<id>/	GET	Book details	Yes	Any
/api/books/	POST	Add new book	Yes	Admin
/api/transactions/	POST	Checkout a book	Yes	User
/api/transactions/<id>/return/	PUT	Return a book	Yes	User
/swagger/	GET	API documentation	No	Any

🧾 Example Requests
✅ Register
 
POST /api/register/
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "mypassword",
  "profile": {
    "phone_number": "0612345678",
    "address": "123 Main St",
    "date_of_birth": "2000-05-10"
  }
}
🔑 Login
 
POST /api/token/
{
  "username": "john_doe",
  "password": "mypassword"
}
Response:

 
{
  "access": "your-access-token",
  "refresh": "your-refresh-token"
}
Add this to Authorization Header:

 
Authorization: Bearer <your-access-token>
🧩 Technologies Used
Django – Web framework

Django REST Framework – For building the API

SimpleJWT – Authentication

drf-yasg – Swagger UI documentation

SQLite – Default database

📖 Swagger Documentation
Visit:

 
http://localhost:8000/swagger/

Authorize with your JWT access token to test endpoints directly.

⚙️ How It Works (Logic Summary)
Users register and get a JWT token to log in.

Admins can manage all users and books.

Regular users can only read book data and perform transactions (checkout/return).

Each checkout creates a transaction and decreases available book copies.

Returning a book updates the same transaction and increases available copies again.

👩‍💻 Author
monim es-sraoui