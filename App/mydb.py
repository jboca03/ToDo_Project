import mysql.connector

dataBase = mysql.connector.connect(
<<<<<<< HEAD
    host = 'localhost',
    user = 'root',
    passwd = '@Morelos0103',
    )
=======
    host='localhost',
    user='root',
    passwd='@Morelos0103',
)
>>>>>>> 704e2e811f3ea74fda7394dc839ea9f611cd9654

# prepare cursor object (using the connector declare above)
cursorObject = dataBase.cursor()

# create data base
cursorObject.execute("CREATE DATABASE todoData")

# Message in console to see if it worked
print("Hello data base todoData")
