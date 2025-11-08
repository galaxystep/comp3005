# comp3005
for assignment 3, question 1.

VIDEO DEMONSTRATION LINK: https://youtu.be/wIQM26nYQYs

DATABASE SETUP:
INSTALLATION REQUIREMENTS: pgAdmin4

01: Within pgAdmin, create a new database called Assignment3.

02: Within the Assignment3 database, open the file called "table_creation.sql". Execute the script to create the necessary table and fill it with the necessary data.

RUNNING THE CODE
INSTALLATION REQUIREMENTS: Python 3.X, PostgreSQL, psycopg2 package

Steps to compile and run the application:

01: INSTALL POSTGRES/PYTHON CONNECTION LIBRARY

Write "pip install psycopg2" into your command line to install the necessary libraries.

02: UPDATE CONNECTION SETTINGS (within the top of the connection.py file)

Change the values to ones that concern your setup (your password, port, etc.). You can find this by clicking the "Properties" tab on the general PostgreSQL database to check the relevant settings.

03: RUN THE APPLICATION

In order to run the application, open a command line and type "python connection.py". You'll have a chance to test the functions within the application.

04: VERIFY THE RESULTS

You're able to verify the results of the application by checking the databse in pgAdmin.
