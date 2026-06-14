

# 🚀 FastAPI E-Commerce Backend

A **production-ready, scalable, and secure e-commerce backend** built using **FastAPI**, following clean architecture principles and real-world backend development practices.

This project simulates a real-world online shopping platform with features like authentication, product management, and order processing.

---

## 👨‍💻 Internship Details

* **Name:** Sakshi Sorte
* **Intern ID:** CITS1852
* **Internship Name:** Python Programming Internship

---

## ✨ Key Features

### 🔐 Authentication & Authorization

* JWT-based secure authentication system
* Role-based access control (User / Admin)

### 🛍️ Product Management

* Create, update, delete products (Admin only)
* Category-based product organization
* Pagination and filtering support

### 📦 Order System

* Place orders securely
* Track order status
* View user order history

### 🗂️ Database Integration

* SQLAlchemy ORM for database handling
* Supports MySQL / PostgreSQL
* Alembic migrations for schema updates

### ⚡ High Performance API

* Built with FastAPI (async support)
* Auto-generated Swagger UI (`/docs`)
* ReDoc documentation (`/redoc`)

### 🧩 Clean Architecture

* Modular project structure
* Separation of concerns (API, CRUD, Models, Schemas)
* Easily scalable to microservices

---

## 🏗️ Tech Stack

* **Backend Framework:** FastAPI
* **Database:** MySQL / PostgreSQL
* **ORM:** SQLAlchemy
* **Validation:** Pydantic
* **Migrations:** Alembic
* **Server:** Uvicorn

---

## 📁 Project Structure

```
app/
│── api/            # API Routes / Endpoints
│── core/           # Configuration & settings
│── models/         # Database models
│── schemas/        # Pydantic schemas
│── crud/           # Database operations
│── db/             # Database connection setup
│── middlewares/    # Custom middlewares
main.py             # Application entry point
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/fastapi-ecommerce-backend.git
cd fastapi-ecommerce-backend
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5️⃣ Run Database Migrations

```bash
alembic upgrade head
```

### 6️⃣ Start the Server

```bash
uvicorn main:app --reload
```

---

## 📌 API Documentation

Once the server is running:

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔥 Example API Endpoints

| Method | Endpoint       | Description            |
| ------ | -------------- | ---------------------- |
| POST   | /auth/register | Register a new user    |
| POST   | /auth/login    | Login user             |
| GET    | /products      | Get all products       |
| POST   | /products      | Create product (Admin) |
| POST   | /orders        | Place a new order      |

---

## 🧠 System Design Highlights

* Modular FastAPI architecture
* JWT-based authentication system
* Clean and scalable project structure
* Database migration support using Alembic
* Ready for microservices expansion

---

## 🚀 Future Improvements

* Payment gateway integration (Razorpay / Stripe)
* Redis caching for performance optimization
* Docker containerization
* CI/CD pipeline setup
* Email notifications system

---

## 📌 Conclusion

This project successfully implements a fully functional e-commerce backend with core features such as authentication, product management, and order processing. It provides a strong foundation for building scalable and production-grade backend systems.

Future enhancements like payment integration, caching, and deployment automation can further improve its real-world usability.

---

