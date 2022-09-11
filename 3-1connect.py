from sqlite3 import connect
import mysql.connector
mydp = mysql.connector.connect(host='localhost',user='root',passwd = "Lucky143!")
mycursor = mydp.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)