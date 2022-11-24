#py -m pip install oracle
#py -m pip install mysql-connector  #mysql-connector-python latest 
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="rpsconsulting",database="accenture")

mycursor=mydb.cursor()

mycursor.execute("create table accentureemps(empid  int(10),ename varchar(10))");