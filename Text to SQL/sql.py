import sqlite3

## connect to sql
connection = sqlite3.connect("students.db")

## create the curser object to insert, cretae, retrieve
cursor = connection.cursor()

## create table
table_info = """
create table student(Name varchar(50),
Class varchar(50), Section varchar(50),
Marks int);

"""

cursor.execute(table_info)

## Insert records
cursor.execute('''insert into student values('Abi','DS','A',90)''')
cursor.execute('''insert into student values('Akila','DS','A',95)''')
cursor.execute('''insert into student values('Prakash','DE','B',70)''')
cursor.execute('''insert into student values('Banu','DS','A',89)''')
cursor.execute('''insert into student values('Kavin','DA','A',77)''')
cursor.execute('''insert into student values('Naveen','DA','C',84)''')
cursor.execute('''insert into student values('Madhu','DE','B',87)''')
cursor.execute('''insert into student values('Praba','DE','C',91)''')
cursor.execute('''insert into student values('Hema','DA','B',79)''')
cursor.execute('''insert into student values('Janu','DS','C',98)''')

## Display all recorde
print("The inserted records are")

data = cursor.execute('''select * from student''')

for row in data:
    print(row)


## close the connection
connection.commit()
connection.close()

