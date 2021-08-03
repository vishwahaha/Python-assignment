import mysql.connector  # type: ignore

mydb = mysql.connector.connect(
    host = "localhost",
    user = "first_year",
    password = "first_pass",
    database = "python"
)

mycursor = mydb.cursor()

try:
    mycursor.execute("CREATE TABLE user (username VARCHAR(255))")
except:
    pass

sql = "INSERT INTO user (username) VALUES (%s)"
val = [("radhikagarg1601",), ("ritvik.jain.52206",), ("rishi.ranjan.54966",), ("utkarsh.parkhi.1",), ("anshul.d.sharma.7",)]

mycursor.executemany(sql, val)
mydb.commit()
