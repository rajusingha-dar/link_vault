LinkVault: A Personal Link Saving Application
LinkVault is a sleek, fast, and modern web application built with Python, FastAPI, and MySQL for saving and organizing your important links. It features a professional dark-gradient theme and allows you to categorize and filter your links for easy access.

This project serves as a practical example of building a full-stack application using modern Python tools and object-oriented principles.

(Suggestion: Take a screenshot of your running app and replace the URL above to showcase your project!)

Features
Save & Organize: Easily save links with a title, description, and type.

CRUD Operations: Full Create, Read, Update, and Delete functionality for your links.

Dynamic Filtering: Filter your saved links by type (YouTube, GitHub, PDF, etc.) with a single click.

Modern UI: A professional and responsive dark-gradient theme built with HTML, CSS, and a touch of JavaScript.

Robust Backend: Powered by the high-performance FastAPI framework.

Reliable Database: Uses MySQL with SQLAlchemy for robust data storage and ORM capabilities.

Secure Configuration: Uses a .env file to keep database credentials safe and separate from code.

Project Structure
The application is organized into a clean, modular structure to promote separation of concerns.

/link-saver-app
|
|-- app/
|   |-- main.py         # API and HTML endpoints
|   |-- crud.py         # Database logic (CRUD)
|   |-- models.py       # Database table models
|   |-- schemas.py      # Pydantic data validation
|   |-- database.py     # DB connection setup
|   |-- templates/      # HTML files
|   |-- static/         # CSS/JS files
|
|-- requirements.txt
|-- .gitignore
|-- README.md
|-- .env

Getting Started
Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Python 3.8+

A running MySQL server instance

Installation & Setup
Clone the repository:

git clone https://github.com/rajusingha-dar/link_vault.git
cd link-saver-app

Create and activate a virtual environment:

# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Configure your database:

Create a database in MySQL (e.g., link_saver_db).

Rename the .env.example file to .env (if you have one) or create a new .env file.

Update the .env file with your MySQL credentials:

DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=link_saver_db

Run the application:

uvicorn app.main:app --reload

The application will be live at http://127.0.0.1:8000.