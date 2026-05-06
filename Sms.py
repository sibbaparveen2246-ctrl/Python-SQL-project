# ----connect import
import mysql.connector as myconn

# connection setup -----
mydb = myconn.connect(
    host = 'localhost',
    user = 'root',
    password = 'your_password',
    database = 'School',
)

# database -------
db_cursor = mydb.cursor()
db_cursor.execute('CREATE DATABASE IF NOT EXISTS School')

db_cursor.execute('USE School')

# Table -------
db_cursor.execute("""CREATE TABLE IF NOT EXISTS classroom (
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50),
age INT,
course VARCHAR(50))
""")

# Add_Student ----

def add_student():
    name = input('Enter Name of Student: ')
    age = input('Enter Age of Student: ')
    course = input('Enter the Course: ')

    query = "INSERT INTO classroom (name,age,course) Values (%s,%s,%s)"
    values = (name,age,course)

    db_cursor.execute(query,values)
    mydb.commit()

    print('Student Added successfully!')


# View_Student ----

def view_student():
    db_cursor.execute('SELECT * FROM classroom')
    students = db_cursor.fetchall()

    print("\n Student List")

    for i in students:
        print(f"ID:{i[0]}, Name:{i[1]}, Age:{i[2]}, Course:{i[3]}")

# Update_Student----

def update_student():
    new_id = input('Enter the New Student ID:')
    new_name = input('Enter the New Student Name:')
    new_age = input('Enter the New Student Age:')
    new_course = input('Enter the New Course:')

    query = "UPDATE classroom SET name=%s, age=%s, course=%s WHERE id=%s"

    db_cursor.execute(query,(new_name,new_age,new_course,new_id))
    mydb.commit()

    print('Student Updated successfully!')

# Delete_Student ----

def delete_student():
    student_id = input('Enter Student Id:')
    query = "DELETE FROM classroom WHERE id = %s"
    db_cursor.execute(query,(student_id,))
    mydb.commit()
    print('Student Deleted Successfully')

# Reset table----
def reset_table():
    db_cursor.execute('TRUNCATE TABLE classroom')
    print('Table Reset successfully!')

# Menu------
while True:
    print("\n*****Student Management System*****")
    print("1. Add student")
    print("2. View student")
    print("3. Update student")
    print("4. Delete student")
    print("5. Reset table")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_student()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        reset_table()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print('invalid choice')

# connection close-----
mydb.close()