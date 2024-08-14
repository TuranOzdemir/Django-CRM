import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ZaWXdE306.",
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE IF NOT EXISTS QCodeCO")
print("Database created successfully")
