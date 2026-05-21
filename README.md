# 🎓 Student Management System

A Python + SQL based Student Management System to perform CRUD operations.

## ✨ Features
- **Add Student**: Insert new student records with ID, Name, Age, Course
- **View Students**: Display all student data in table format
- **Search Student**: Find student by ID or Name
- **Update Details**: Modify existing student information
- **Delete Record**: Remove student from database
- **MySQL/SQLite Support**: Works with both databases

## 🛠️ Tech Stack
| Component | Technology |
| --- | --- |
| **Language** | Python 3.x |
| **Database** | MySQL / SQLite |
| **Library** | `mysql-connector-python` or `sqlite3` |



pip install mysql-connector-python

Configure Database
For MySQL: Update db_config.py with your username & passwordpythonhost = "localhost"
user = "root"  
password = "your_password"
database = "student_db"
