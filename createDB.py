import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="userDb",
  password="PassDb",
  database ="nmap_report",
)

mycursor = mydb.cursor()
test = mycursor.execute("CREATE TABLE nmap (id int(6) not null primary key auto_increment, ip VARCHAR(30), port VARCHAR(30), service VARCHAR(100),product VARCHAR(100), version VARCHAR(30))")

mycursor.execute("CREATE TABLE ip (id int(6) not null primary key auto_increment, ip_address VARCHAR(30), port VARCHAR(30),product VARCHAR(100), version VARCHAR(30), title VARCHAR(30), link VARCHAR(100))")

print("done")

