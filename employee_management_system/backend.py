import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="123456",database="employee")
c=mydb.cursor()
login=False
emp_id=input("Enter Employee ID")
pwd=input("Enter Password")
c.execute("select * from users")
#To retrive data
for row in c:
    if (emp_id==row[0] and pwd==row[1]):
        login=True
        break
if(login):
    print("Login Successful")
else:
    print("Incorrect ID or Password")
