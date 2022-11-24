
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="rpsconsulting",database="accenture")

mycursor=mydb.cursor()

mycursor.execute("delete from accentureemps where empid=123");

mydb.commit();