print("_______________________________")
print("\t Bank Management System")
print("_____________________________________")
import mysql.connector
mydb=mysql.connector.connect(user="root",passwd="parth",host="localhost",auth_plugin="mysql_native_password")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists bank2")
mycursor.execute("use bank2")
mycursor.execute("create table if not exists login(admin varchar(25) not null,password varchar(25)not null)")
mycursor.execute("create table if not exists bank_master(acc_no int not null,name varchar(25) not null,city varchar(25) not null, pin int not null, balance int not null)")
mycursor.execute("create table if not exists sno(no int not full, temp int not null)")
mydb.commit()
j=0
mycursor.execute("select * form login")
for i in mycursor:
    j=1
if(j==0):
   mycursor.execute("insert into login values('admin','nd')")
   mydb.commit()
z=0
mycursor.execute("select * from sno")
for i in mycursor:
   z=1
if(z==0):
   mycursor.execute("insert into sno values(0,0)")
   mydb.commit()    
while True:
    print("1.login")
    print("2.exit")
    ch=input("enter your choice:")
    if(ch==1):
        password=input("Enter password:")
        mycursor.execute("select * form login")
        for I in mycursor:
             admin,passs=I
        if(password==passs):
              print("Successfully login...")
              print("1.create account")
              print("2.deposite money")
              print("3.withdraw money")
              print("4.Display")
              print("5.Exit")
              ch2=input("Enter your choice:")
              if(ch2==1):
                  name=input('enter name:')
                  city=input("enter your city:")
                  pin=input("enter PIN")
                  balance=0
                  mycursor.execute("select * from sno")
                  for I in mycursor:
                      no,temp=I
                  no+=1
                  mycursor.execute("insert into bank_master values('"+str(no)+"','"+name+"','"+city+"','"+pin+"','"+str(balance)+"')")
                  mydb.commit()
                  print("Successfully done...")
              elif(ch2==2):
                   account=input("enter account number:")
                   amount=int(input("enter amount:"))
                   mycursor.execute("select* from bank_master where acc_no='"+str(account)+"'")
                   for I in mycursor:
                       acc,name,city,pin,balace=I
                   balance=balance+amount
                   mycursor.execute("update bank_master set balance='"+str(balance)+"' where acc_no='"+str(account)+"'")
                   mydb.commit()
                   print("Successfully deposit....")
              elif(ch2==3):  
                   account=int(input("Enter account number:"))
                   amount=int(input("Enter amount:"))
                   mycursor.execute("select * from bank_master where acc_no='"+str(account)+"'")
                   for I in mycursor:
                       acc,name,city,pin,balance=I
                   balance=balance-amount
                   if(balance<0):
                       print("not having required amount")
                       continue
                   mycursor.execute("update bank_master set balance='"+str(balance)+"'where acc_no='"+str(account)+"'")
                   mydb.commit()
                   print("Successfully withdraws...")
              elif(ch2==4):
                   account=int(input("Enter your account number:"))
                   mycursor.execute("select * from bank_master where acc_no='"+str(account)+"'")
                   for I in mycursor:
                       acc,name,city,pin,balance=I
                   print(f"Account--> {acc}")
                   print(f"Name--> {name}")
                   print(f"City--> {city}")
                   print(f"balance--> {balance}")
              elif(ch2==5):
                   break
        elif(ch==2):
            break
        else:
            print("Wrong password..")
           
               
                   
                   
                       
                  
               



























