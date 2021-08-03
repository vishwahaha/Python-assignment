import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "first_year",
    password = "first_pass",
    database = "python"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM user")
usernames = mycursor.fetchall()

def decorator(func):
    def inner(username):
        available = True
        for x in usernames:
            if username == x[0]:
                available = False
        assert(available), "Username already exists"
        return func(username)
    return inner

@decorator
def func(username):
    print("Do something")




    