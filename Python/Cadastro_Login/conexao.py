import mysql.connector

conexaov = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='sgcbd',
)
cursor = conexaov.cursor()
