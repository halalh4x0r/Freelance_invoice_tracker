## Freelance Invoice Tracker
A Command-Line Application for Managing Clients, Invoices, and Payments
## Overview

The Freelance Invoice Tracker is a CLI (Command-Line Interface) Python application designed to help freelancers efficiently manage their business operations — from creating clients and generating invoices to tracking payments.

This project demonstrates mastery of Python fundamentals, object-oriented programming, database management, and software design patterns.
It was built as part of the Phase 3 Project, which emphasizes understanding how ORMs work by manually linking Python classes with an SQLite database using sqlite3.

## Key Features

 User Management – Create and manage freelance user profiles.

 Client Management – Add, view, and update client information.

 Invoice Tracking – Create invoices, assign them to clients, mark payments, and calculate totals.

 Payment History – Track when payments were made and view outstanding balances.

 Automatic Database Handling – All data is saved persistently using SQLite.

 Clean CLI Interface – Intuitive text-based menus for navigating the app.

## Technologies Used
Component	Technology
Language	Python 3
Database	SQLite (via sqlite3 module)
Interface	Command-Line (CLI)
ORM Simulation	Custom CRUD methods inside Python classes
Environment	pip / venv
Version Control	Git + GitHub

## Project Structure
Freelance_invoice_tracker/
│
├── lib/
│   ├── cli.py                # Main CLI menu logic
│   ├── database.py           # Database connection and table creation
│   └── models/
│       ├── user.py           # User model and CRUD operations
│       ├── client.py         # Client model
│       ├── invoice.py        # Invoice model
│       └── payment.py        # Payment model
│
├── db/
│   └── database.db           # SQLite database file
│
├── main.py                   # App entry point
├── README.md                 # Documentation (this file)
└── .gitignore                # Ignored files and folders

## Learning Objectives Demonstrated

This project directly aligns with the Phase 3 learning goals, showcasing proficiency in:

 1. CLI Application Development

Designed a fully functional command-line app using Python’s built-in libraries (os, sqlite3, datetime).

Implemented modular code organization with reusable components.

 2. Database Design & Management

Created multiple related tables (users, clients, invoices, payments).

Wrote SQL statements manually for CREATE, READ, UPDATE, and DELETE operations.

Demonstrated one-to-many relationships (e.g., one user → many clients, one client → many invoices).

 3. Custom ORM-Like Structure

Each model represents a table with its own methods for data persistence.

Handled validation and integrity constraints (e.g., unique emails, valid amounts).

 4. Coding Best Practices

Followed Pythonic naming conventions (PEP8).

Used exception handling for robust user experience.

Implemented DRY (Don’t Repeat Yourself) and separation of concerns.

 5. Technical Communication

Documented setup steps, functionality, and design decisions.

Wrote meaningful commit messages to reflect development stages.

## How to Run the Application
Step 1: Clone the Repository
git clone https://github.com/your-username/phase-3-project-yourname.git
cd phase-3-project-yourname

Step 2: Create a Virtual Environment
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Step 3: Install Dependencies (if any)
pip install -r requirements.txt

Step 4: Run the App
python3 main.py

## Credits

Developed by: Moha
Role: Software Developer
Project: Phase 3 Final Project — Python CLI + SQLite ORM Simulation
Institution: Moringa School