📚 Library Management API

A simple Django REST API for managing books, users, and transactions using JWT authentication.

🚀 Features

User registration, login (JWT, expires in 1 hour)

Admin can manage users & books

Users can borrow & return books

Swagger UI for easy testing

⚙️ Setup

Clone repo & enter folder

Create venv → python -m venv venv

Activate venv → venv\Scripts\activate or source venv/bin/activate

Install deps → pip install -r requirements.txt

Migrate → python manage.py migrate

Create admin → python manage.py createsuperuser

Run → python manage.py runserver

🌐 Endpoints
Endpoint	Method	Description
/api/register/	POST	Register user
/api/token/	POST	Login (JWT)
/api/token/refresh/	POST	Refresh token
/api/books/	GET	List books
/api/books/	POST	Add book (Admin)
/api/transactions/	POST	Borrow book
/api/transactions/<id>/return/	PUT	Return book
/swagger/	GET	API docs
🧠 How It Works

JWT tokens expire in 1 hour

Borrowing reduces available copies

Returning increases available copies

Prevents duplicate borrowing

🧩 Tech Stack

Django · DRF · SimpleJWT · Swagger · SQLite

Author: Monim Es-Sraoui