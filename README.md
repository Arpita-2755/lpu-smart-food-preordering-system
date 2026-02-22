# 🍽 Smart Food Stall Pre-Ordering System

## 📌 Project Overview

The Smart Food Stall Pre-Ordering System is developed as part of the Smart AI-Enabled LPU Campus Management System.

This web-based application allows students to pre-order food before their break time, helping reduce congestion and waiting time at campus food stalls.

---

## 🎯 Objectives

- Enable students to pre-order meals
- Track food demand in real-time
- Display peak order time slots
- Reduce overcrowding during break hours
- Provide visual analytics using charts

---

## 🛠 Technologies Used

- Python
- Flask Framework
- SQLite Database
- Bootstrap 5 (UI Design)
- Chart.js (Data Visualization)
- HTML & CSS

---

## 🧠 System Architecture

Frontend:
- Bootstrap-based responsive UI
- Animated navbar
- Live order counter
- Bar chart visualization

Backend:
- Flask routing
- SQLite database integration
- Dynamic data rendering using Jinja templates

Database:
Table: `orders`

| Field | Type |
|-------|------|
| id | Integer (Primary Key) |
| name | Text |
| food | Text |
| slot | Text |

---

## ⚙️ How the System Works

1. Student enters:
   - Name
   - Food item
   - Preferred break time slot

2. The order is stored in SQLite database.

3. The system:
   - Counts total orders
   - Groups orders by time slot
   - Displays peak demand slots
   - Updates bar chart dynamically

---

## 🚀 How to Run the Project

### 1. Clone Repository
git clone <your_repo_link>
cd lpu-smart-food-preordering-system

### 2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run Application
python app.py


### 5. Open in Browser


http://127.0.0.1:5000


---

## 📊 Features Implemented

- Food pre-ordering system
- Real-time order storage
- Live total order counter
- Peak time slot analysis
- Data visualization using bar charts
- Modern animated UI

---

## 🔮 Future Enhancements

- AI-based demand prediction
- Admin analytics dashboard
- Order cancellation feature
- Payment integration
- Smart queue management

---

## 📚 Academic Context

Developed as part of:
Smart AI-Enabled LPU Campus Management System (Project II)

---

## 👩‍💻 Author

Arpita Mishra
B.Tech CSE | Python & Full Stack