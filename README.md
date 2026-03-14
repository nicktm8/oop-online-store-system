# 🛒 Python OOP Sales Management System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OOP](https://img.shields.io/badge/Paradigm-Object%20Oriented-green)
![Status](https://img.shields.io/badge/Project-Portfolio%20Ready-brightgreen)

A structured and modular sales management system built in Python to
demonstrate advanced Object-Oriented Programming principles.

This project models real-world sales entities such as products, users,
and employees using clean OOP architecture.

------------------------------------------------------------------------

## 🚀 Key Features

-   Abstract Base Class (`Person`)
-   Inheritance (`User`, `Employee`)
-   Polymorphism (`display_info` method)
-   Encapsulation (private & protected attributes)
-   Inventory validation
-   Shopping history tracking
-   Salary management with percentage increase
-   Randomized product assignment simulation

------------------------------------------------------------------------

## 🧠 OOP Concepts Demonstrated

### ✅ Encapsulation

-   Private attributes: `__price`, `__salary`
-   Protected attributes: `_email`, `_address`, `_description`
-   Controlled access via getters and setters

### ✅ Inheritance

-   `Employee` and `User` inherit from abstract base class `Person`

### ✅ Polymorphism

-   `display_info()` implemented differently in each subclass
-   Unified interface used in `main.py`

### ✅ Abstract Classes

-   `Person` implemented using Python's `abc` module

------------------------------------------------------------------------

## 📂 Project Structure

```
oop-online-store-system/
├── models/
│   ├── employee.py
│   ├── person.py
│   ├── product.py
│   └── user.py
├── .gitignore
├── README.md
├── main.py
└── requirements.txt
```
    
------------------------------------------------------------------------

## ▶️ How to Run

1. Clone the repository:
```bash
   git clone https://github.com/nicktm8/oop-online-store-system.git
```
2. Navigate to the project directory:
```bash
   cd oop-online-store-system
```
3. Run the program:
```bash
   python main.py
```

------------------------------------------------------------------------

## 📊 Example Functionality

-   Displays product inventory
-   Updates product prices (+10% simulation)
-   Demonstrates encapsulation via getters and setters
-   Shows polymorphic display of users and employees
-   Calculates total spending per user
-   Increases employee salaries

------------------------------------------------------------------------

## 🎯 Project Purpose

This project was developed to strengthen understanding of:

-   Clean OOP architecture
-   Writing modular Python code
-   Structuring multi-file projects
-   Applying theoretical OOP concepts in practice

It serves as a foundational backend-style system suitable for further
expansion (CLI interface, database integration, REST API version, etc.).

------------------------------------------------------------------------

## 🔮 Possible Future Improvements

-   CLI interactive menu
-   Data persistence (JSON or SQLite)
-   Logging system
-   Unit testing (pytest)
-   Flask or FastAPI API version

------------------------------------------------------------------------

## 👨‍💻 Author

**Nick Tem**\
Aspiring Python Developer

GitHub: https://github.com/nicktm8
