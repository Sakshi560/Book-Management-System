import pymysql as cntr , datetime as __dt , matplotlib.pyplot as plt
from random import shuffle
from tempfile import mktemp
from os import system , startfile

__db = cntr.connect(host = 'localhost' , user = 'root' , passwd = 'manager' , database = 'book_shop')
__cur = __db.cursor()
__db.autocommit(True)
#Function to check is it leap year
is_leapyear = lambda year : year % 4 == 0
#Function to get last date of month

def last_month(month , year):
    if month in (1,3,5,7,8,10,12) : return 31
    elif month == 2 and is_leapyear(year) : return 29
    elif month == 2 : return 28
    else : return 30

    clrscreen = lambda : system("cls")

def view_stock() :

    __cur.execute("select Book_No , Book_Name , Available_Stock from stock")

    data = __cur.fetchall()

print("Book Number\tBook Name\tStock")

for row in data : print(row[0] , '\t\t' , row[1] , '\t' , row[2])       


            

def add_stock() :            

   print('Add Stock'.center(89 , '='))

bno = unique_book_no()
if bno :

       print("Book Number : " , bno)

else : bno = int(input("Enter book number : "))

bname = input("Enter the Book\'s Name : ")
auth = input("Enter the Author of the Book : ")
publ = input("Enter the Publisher of the Book : ")
cost = eval(input("Enter the Cost per Book : "))
stock = int(input("Enter the Quantity purchased : "))
__cur.execute("insert into stock values ({} , '{}' , '{}' , '{}' , {} , {} , {} , '{}')".format(bno , bname , auth , publ , cost , stock , 0, __dt.date.today()))

print("Inserted Sucessfully !!!")

    
def add_user() :

    user = input("Enter the user name : ")

    passwd = input("Enter a Password : ")

    passwd2 = input("Enter Password to confirm : ")

    if passwd == passwd2 :

       __cur.execute("insert into users values('{}' , '{}')".format(user , passwd))

       print("Created Successfully!!!")

    elif passwd != passwd2 : print("You've entered different passwords")

    


        

def sell_book() :

   print('Purchase')

cname = input("Enter the Customer Name : ")
phno = int(input("Enter the phone number : "))
bno = int(input("Enter book number : "))
bname = input("Enter the name of the book : ")
cost = eval(input("Enter the cost of the book : "))
__cur.execute("insert into purchased values({} , '{}')".format(bno , __dt.date.today()))
__cur.execute("update stock set qty_purchased = qty_purchased + 1 where Book_No = {}".format(bno))
__cur.execute("update stock set Available_Stock = Available_Stock - 1 where Book_No = {}".format(bno))

print("Bought Successfully")

q = '''Book Shop\nName : {}\nPhone No : {}\nBook Number : {}\nBook Name : {}\nCost : {}\nDate Of Purchase : {}'''.format(cname , phno , bno , bname , cost , __dt.date.today())

filename = mktemp('.txt')

open(filename , 'w').write(q)

startfile(filename , 'print')
__cur.execute('select Book_Name , Book_No , Author from stock where Available_Stock = 0')

if __cur.rowcount == 1 :

       print("STOCK OF ")

       print("Book Name : " , __cur.fetchall()[0][0])

       print("Book Number : " , __cur.fetchall()[0][1])

       print("Author : " , __cur.fetchall()[0][2])

       print("EXHAUSTED")

       __cur.execute('delete from stock where Available_Stock = 0')

    

def unique_book_no () :

   __cur.execute("select max(Book_No) from stock")

data = __cur.fetchall()
if bool(data[0][0]) :

        L1 = [x for x in range((data[0][0] + 1) , (data[0][0] + 10000))]

shuffle(L1)
     



def view_sales () :

   print('Overall Sales This Month')        

   __cur.execute("select distinct(s.Book_Name) , s.qty_purchased from stock s , purchased p where s.Book_No = p.Book_No and p.purchased_on between '{year}-{month}-01' and '{year}-{month}-{date}'".format(year = __dt.date.today().year , month = __dt.date.today().month , date = last_month(__dt.date.today().month , __dt.date.today().year)))

data = __cur.fetchall()
L1 , L2 = [] , []

for row in data :

       L1.append(row[0])

       L2.append(row[1])

plt.bar(L1 , L2)
plt.xlabel('Books')
plt.ylabel('Sales')
plt.title('Sales')
plt.show()

    


    

def login():

    user = input("Enter the username : ")

    pwd = input("Enter the password : ")

__cur.execute("Select * from users where (username = '{}' and password = '{}')".format(user , pwd))

if __cur.rowcount :   returnTrue



def update_stock() :

    bno = int(input("Enter the book number : "))

__cur.execute("select Book_Name , Available_Stock from stock where Book_No = {}".format(bno))

data = __cur.fetchall()

print("Book Name : " , data[0][0])

print("Available Stock : " , data[0][1])

stock = int(input("Enter the new stock purchased : "))

__cur.execute("update stock set Available_Stock = Available_Stock + {}".format(stock))

print("Updated Successfully")



 


# PYTHON MODULE : Tables_in_mysql

 

import pymysql as cntr


db = cntr.connect(host = 'localhost' , user = 'root' , passwd = 'manager')

db.autocommit(True)

cur = db.cursor()

cur.execute("create database if not exists book_shop")

cur.execute("use book_shop")

cur.execute("create table stock\

           (Book_No bigint primary key,\

Book_Name varchar(255),\

Author varchar(255),\

Publisher varchar(255),\

Cost_per_Book float,\

Available_Stock bigint,\

qty_purchased bigint,\

purchased_on date)")

cur.execute("create table users(username varchar(255) , password varchar(255) , check (username <> 'ADMIN'))")

cur.execute("create table purchased (Book_no bigint , purchased_on date , foreign key(Book_no) references stock(Book_No))")

cur.execute("create unique index Book_Index on stock(Book_No)")

cur.execute("insert into users values('admin' , 'admin@123')")

print("Database and Tables created successfully")

c = input("Press any key to continue---->")

cur.close()

db.close()



 



# PYTHON MODULE : main

 

import Book 



c = 'y'

while c.lower() == 'y' :

   print("Book Shop Management".center(89 , '='))

print('1. Register')

print('2. Login')

print('3. Exit')

choice4 = int(input("Enter the serial number of your choice : "))

if choice4 == 1 :

       Book.clrscreen()

       Book.add_user()

elif choice4 == 2 :

       Book.clrscreen()

if Book.login() :

           Book.clrscreen

C = 'y'

while C.lower() == 'y' :

               Book.clrscreen()

               print("Book Shop Management".center(89 , '='))

               print("1. Book Stock")

               print("2. Book Selling")

               print("3. Exit")

               choice = int(input("Enter the serial number of your choice : "))

               if choice == 1 :

                    Book.clrscreen()

print("Book Book".center(89 , '='))

print("1. Add a new Stock")

print("2. View all Stock")

print("3. Update an existing Stock")

print("4. Exit")

choice2 = int(input("Enter the choice : "))

if choice2 == 1 :

                        Book.clrscreen()

                        Book.add_stock()

elif choice2 == 2 :

                        Book.clrscreen()

                        Book.view_stock()
elif choice2 == 3 :

                        Book.clrscreen()

                        Book.update_stock()

elif choice2 == 4 :

                        print("Good Bye")

                        

else : print("INVALID CHOICE")
choice == 2 
        
        
        
Book.clrscreen()

print('Book Selling'.center(89 , '='))

print('1. Sell a book')

print('2. View Sales this month')

print("3. Exit")

choice3 = int(input("Enter your choice : "))

if choice3 == 1 :

                       Book.clrscreen()
                       Book.sell_book()                   

elif choice3 == 2 :

                        Book.clrscreen()

                        Book.view_sales()

elif choice3 == 3 : 

                        print("Good Bye")
                        

else : print("INVALID CHOICE")

choice == 3 

print("Good Bye")


