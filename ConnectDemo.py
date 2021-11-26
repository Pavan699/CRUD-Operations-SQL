'''
@Author: Pavan Nakate
@Date: 2021-11-25 09:56
@Last Modified by: Pavan Nakate
@Last Modified time: 2021-11-26 09:20
@Title : CRUD-Operations  
'''
# Importing Json for the hidding the credential data
import json
with open('info.json','r') as jf:
    data = json.load(jf)

h = data['HOST']
un = data['USER']
ps = data['PASS']
db = data['DATABASE']

#importing logging 
import logging

# setting BasicConfig for the INFO
logging.basicConfig(filename='databaseinfo.log',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(funcName)s:%(message)s')
# setting BasicConfig for the ERROR
logging.basicConfig(filename='databaseinfo.log',level=logging.ERROR,format='%(asctime)s:%(levelname)s:%(funcName)s:%(message)s')

import mysql.connector
# Passing the variables holding the data from JSON file
mydb = mysql.connector.connect(
host = h,
user = un,
passwd = ps,
database= db
)
#print(mydb)
cursor = mydb.cursor()

def insert_data():
    """
    Description:
        This Function insert the new data into the table
        User Inputs : 
            id -> id of user
            name -> name of the user
            address -> address of the user
    Parameter:
        None
    Return:
        None
    """
    id = input("Enter Id : ")
    name = input("Enter the Name : ")
    address = input("Enter the Address : ")
    # sql commad to insert the data
    sql = "insert into details (id,name,address) values(%s,%s,%s)"
    val=(id,name,address)

    try:
        cursor.execute(sql,val)
        mydb.commit()
        logging.info("Data Inserted Successfully")
    except Exception as e:
        logging.error(e)

def read_data():
    """
    Description:
        This Function read(Print) the data from the table
    Parameter:
        None
    Return:
        None
    """
    sql = "Select * from details"
    try:
        cursor.execute(sql)
        data = cursor.fetchall() # Fetching all the data from the table
        for line in data:        # Printing the rows(tuple form) 
            print(line)
        logging.info("Data Printed Successfully")
    except Exception as e:
        logging.error(e)

def update_data():
    """
    Description:
        This Function updates the row data by taking user id
        User Inputs : 
            id -> id of user to update name or address
    Parameter:
        None
    Return:
        None
    """
    id = input("Enter user Id to update the data : ")
    sql = "select * from details where id=%s"
    val=(id,)
    try:
        cursor.execute(sql,val)
        user = cursor.fetchall()
        for u in user:
            name=u[1]      #getting the name of that row
            address=u[2]   #getting the address 
        print("Choose for Update : 1.Name \t 2.Address")
        choose = int(input("Enter Choice for update : "))
        if(choose==1):
            name=input("Enter Name for Updation : ")# changing the name
        elif(choose==2):
            address=input("Enter Address for Updation : ")# changing the address
        else:
            print("Wronge Choice :)")

        # Update the data
        # sql command for the update
        sql="update details set name=%s,address=%s where id=%s"
        val = (name,address,id)
        try:
            cursor.execute(sql,val)
            mydb.commit()
            logging.info("Data Updated Successfully")
        except Exception as e:
            logging.error(e)

    except Exception as e:
        logging.error(e)

def delete_data():
    """
    Description:
        This Function delete the data from the table
        id is user input to delete data
    Parameter:
        None
    Return:
        None
    """
    id = input("Enter user Id to delete the data : ")
    sql = "delete from details where id=%s"
    val=(id,)
    try:
        cursor.execute(sql,val)
        mydb.commit()
        logging.info("Data Deleted Successfully")
    except Exception as e:
        logging.error(e)


def menu():
    """
    Description:
        This Function to give choices for the user
    Parameter:
        None
    Return:
        None
    """
    flag = 1
    while(flag != 2):
        print("Select Operation : \n\t1.Insert\n\t2.Read\n\t3.Update\n\t4.Delete\n\t5.Exit\n")
        choose = int(input("Enter Choice : "))
        if(choose==1):
            insert_data()
        elif(choose==2):
            read_data()
        elif(choose==3):
            update_data()
        elif(choose==4):
            delete_data()
        else:
            flag +=1
            print("Thank You :) ")
# calling main fuction
menu()