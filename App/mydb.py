import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '@Morelos0103',
    )
    host='localhost',
    user='root',
    passwd='@Morelos0103',
)

# prepare cursor object (using the connector declare above)
cursorObject = dataBase.cursor()

# create data base
cursorObject.execute("CREATE DATABASE todoData")

# Message in console to see if it worked
print("Hello data base todoData")
 #checking if it works