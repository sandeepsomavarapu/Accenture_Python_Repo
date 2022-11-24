
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="rpsconsulting",database="citi")

mycursor=mydb.cursor()

eid=87

mycursor.execute(f"SELECT * FROM onlineemp1 where empid={eid}")

myresult = mycursor.fetchone()

print(type(myresult))
#for x in myresult:
#  print(x)