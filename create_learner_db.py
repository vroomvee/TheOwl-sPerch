import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd = ""
)
print(mydb)
mycursor = mydb.cursor()
#mycursor.execute('CREATE DATABASE Owls_Perch_Learner_Database')
mycursor.execute('SHOW DATABASES')
for x in mycursor:
    print(x)
mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd = "",
database='Owls_Perch_Learner_Database'
)
mycursor = mydb.cursor()


#mycursor.execute('''create table learnerinfo(
 #                 ID int primary key, 
  ##               password varchar(50),
  #                email varchar(50),
     #             resume_score numeric(2,0),
    #              next_topic varchar(50))''')

mycursor.execute('''create table marks(
                  ID int,
                  topic varchar(50),
                  score int,
                  primary key(ID,topic),
                  foreign key(ID) references learnerinfo(ID))''')