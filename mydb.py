import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tir1061985"
)

# prepare a cursor object using cursor() method
cursorObject = dataBase.cursor()

# Create database
cursorObject.execute("CREATE DATABASE gorilla")

print("All Done!")
