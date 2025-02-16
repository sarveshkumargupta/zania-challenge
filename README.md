# E-Commerce REST API (Flask)

## 📌 Overview
This project is a **RESTful API for an e-commerce platform** built using **Flask, SQLAlchemy, Marshmallow**, and **SQLite**. It allows users to:
- **View products** (`GET /products`)
- **Add products** (`POST /products`)
- **Place orders** (`POST /orders`)
- **Manage stock levels automatically**

The application is containerized using **Docker** and supports **Flask-Migrate** for database migrations.

---

## 🚀 **Setup & Run the Application**

### 🔹 1. **Clone the Repository**
```bash
git clone <repo-url>
cd <repo-folder>
```

### 🔹 2. **Run Locally (Without Docker)**
#### ✅ **Install Dependencies**
```bash
pip install -r requirements.txt
```
#### ✅ **Set Environment Variables**
For Linux/macOS:
```bash
export FLASK_APP=run.py
export FLASK_ENV=development
export DATABASE_URL=sqlite:///app.db
```
For Windows (PowerShell):
```powershell
$env:FLASK_APP="run.py"
$env:FLASK_ENV="development"
$env:DATABASE_URL="sqlite:///app.db"
```

#### ✅ **Run the Flask Application**
```bash
flask run --host=0.0.0.0 --port=6161
```
The API is now accessible at: [http://127.0.0.1:6161](http://127.0.0.1:6161)

---

## 🐳 **Run Using Docker**

### 🔹 1. **Build the Docker Image**
```bash
docker build -t zania-challenge .
```
### 🔹 2. **Run the Container**
```bash
docker run -p 6161:6161 zania-challenge
```
The API is now accessible at: [http://127.0.0.1:6161](http://127.0.0.1:6161)

---

## ✅ **Testing the Application**

### 🔹 1. **Run Tests Without Docker**
```bash
pytest
```

### 🔹 2. **Run Tests Inside Docker Container**
```bash
docker run zania-challenge pytest
```

---

## 🔧 **API Endpoints**

### **📌 Products**
| Method | Endpoint      | Description         |
|--------|-------------|--------------------|
| `GET`  | `/products`  | Get all products   |
| `POST` | `/products`  | Add a new product  |

### **📌 Orders**
| Method | Endpoint    | Description         |
|--------|------------|--------------------|
| `POST` | `/orders`   | Place an order     |
