# 🚀 Online Feedback Collector with Admin Dashboard

## 📘 Project Overview
The **Online Feedback Collector** is a full-stack web application built using **Flask (Python)** and **SQLite**.  
It allows users to submit feedback through a responsive web interface, while administrators can securely log in to view all feedback in a structured dashboard.

This project demonstrates **frontend–backend integration**, **database handling**, **authentication**, and **responsive UI design**, making it suitable for academic submission and beginner industry exposure.

---

## 🎯 Objectives
- Collect feedback from users through a web form
- Store feedback securely in a database
- Provide an admin-only dashboard to view feedback
- Implement basic authentication (static admin login)
- Design a clean, responsive user interface
- Prepare the project for deployment on **Render**

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3 (Responsive Design using Flexbox)
- JavaScript (Client-side validation)

### Backend
- Python
- Flask Framework

### Database
- SQLite

### Deployment
- Render (Python Web Service)
- Gunicorn (Production server)

---

---

## ✨ Features

### 👤 User Features
- Submit feedback with:
  - Name
  - Email
  - Rating (1–5)
  - Comments
- Responsive layout (works on mobile & desktop)
- Client-side validation using JavaScript

### 🔐 Admin Features
- Static login authentication  
  - **Username:** `admin`  
  - **Password:** `admin`
- Secure admin dashboard
- View all feedback in tabular format
- Total feedback count
- Average rating calculation
- Logout functionality

---

## ▶️ How to Run the Project Locally

# 1️⃣ Clone the Repository
bash

git clone https://github.com/your-username/OnlineFeedbackCollector.git
cd OnlineFeedbackCollector

Create Virtual Environment
python -m venv venv

# 2️⃣ Activate it:

 Windows
venv\Scripts\activate

# 3️⃣ Install Dependencies
pip install -r requirements.txt

# 4️⃣ Run the Application
python app.py

# 5️⃣ Open in Browser

Home Page:
👉 http://127.0.0.1:5000

Admin Login:
👉 http://127.0.0.1:5000/admin-login

Admin Dashboard (after login):
👉 http://127.0.0.1:5000/admin-dashboard


## 📂 Project Structure

```
OnlineFeedbackCollector/
│
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── database.db # SQLite database
│
├── static/
│ ├── css/
│ │ └── style.css # Responsive styling
│ └── js/
│ └── script.js # JavaScript validation
│
├── templates/
│ ├── layout.html # Base template
│ ├── index.html # Home page (Admin + Feedback)
│ ├── admin_login.html # Admin login page
│ └── admin.html # Admin dashboard
│
└── README.md # Project documentation
