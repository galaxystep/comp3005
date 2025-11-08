# necessary to important the library that connects python to postgres.
import psycopg2

# the connection to the postgres. knows which server to connect through the listed information below.
connection = psycopg2.connect(
    dbname="Assignment3",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

# sets up a cursor, which allows us to execute SQL actions through the code.
cursor = connection.cursor()

# getting all students and listing them out via the database.
def getAllStudents():
    # cursor.execute() command allows for execution of an SQL command
    cursor.execute("SELECT * FROM students;")
    # taking the results of the returned query and storing into and variable called rows to print out each one here.
    rows = cursor.fetchall()
    for r in rows:
        print(r)

# adding a student to the database.
def addStudent(first_name, last_name, email, enrollment_date):
    # taking the entered values in the code as values to be entered into the database via cursor.execute()
    cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
    connection.commit()

# updating a student email.
def updateStudentEmail(student_id, new_email):
    cursor.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
    connection.commit()

# deleting a student from the database.
def deleteStudent(student_id):
    cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    connection.commit()

def main():
    print("1. Get all students in the database.")
    print("2. Add a student to the database.")
    print("3. Update a student's email.")
    print("4. Delete a student from the database.")
    choice = input("choose a number based on which option you'd like to select. ")

    if choice == "1":
        print("Simply getting all students:")
        getAllStudents()
    
    
    if choice == "2":
        student_fname = input("Enter the student's first name: ")
        student_lname = input("Enter the student's last name: ")
        student_email = input("Enter the student's email: ")
        enrolment_date = input("Enter today's date YYYY-MM-DD (including dashes): ")
        addStudent(student_fname, student_lname, student_email, enrolment_date)
        getAllStudents()

    if choice == "3":
        getAllStudents()
        student_id = input("Enter the student id of the student you want to update: ")
        new_email = input("Enter the new email: ")
        updateStudentEmail(student_id, new_email)
        getAllStudents()

    if choice == "4":
        getAllStudents()
        student_did = input("Enter a student to delete (their corresponding student_id): ")
        deleteStudent(student_did)
        getAllStudents()

if __name__ == "__main__":
    main()
# closing the connection between postgres and python.
cursor.close()
connection.close()