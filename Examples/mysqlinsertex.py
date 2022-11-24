
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="rpsconsulting",database="accenture")

mycursor=mydb.cursor()

mycursor.execute("insert into accentureemps values(123,'suresh')");

mydb.commit();