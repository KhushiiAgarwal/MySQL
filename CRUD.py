#To update go to Update.py
import mysql.connector
#import pymysql
con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="bnqhall")
if con.is_connected():
    print("Welcome to Banquet Hall Booking System")
cur=con.cursor()

def menu():
    menu_chosen=1
    while (menu_chosen==1):
        print("User specified menu \n")
        print( "1.Add Data \n", 
            "2.Show Data \n", 
            "3.Delete Data \n", 
            "4.Choose to exit \n",
        )
        choice=int(input("Enter your numerical choice:"))
        if choice not in range(1,5):
            print("INVALID CHOICE, Try Again")
        else:
            menu_chosen=0
            break
    if (choice==1):
        c_name=input("Enter your name: ")
        ph_no=int(input("Enter your 10 digit contact number:"))
        cust_key=int(input("Enter the id provided to you:"))
        Email_id=input("Enter your email:")
        city=input("Enter city: ")
        ID_Proof=input("Enter ID type:")
        Age=int(input("Enter your age:"))
        values=(c_name,ph_no,cust_key,Email_id,city,ID_Proof,Age)
        st="INSERT INTO cust(c_name,ph_no,cust_key,Email_id,city,ID_Proof,Age) VALUES( %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(st,values)
        con.commit()
        print("Thank you for the details,the data is stored")
        print(cur.rowcount, "record inserted.")
        print("Happy to serve you")
        

    elif (choice==2):
        cur.execute("Select * from bnqmain")
        data=cur.fetchall()
        count=cur.rowcount
        print("Total rows,",count)
        for row in data:
            print(row)
        con.commit()
        print("Happy to serve you, do you wish to continue ahead?")
        
    elif (choice==3):
        ck=int(input("Enter id no for deleting records:"))
        str="DELETE FROM cust WHERE cust_key=%s "
        cur.execute(str,(ck,))
        con.commit()
        print('number of rows deleted', cur.rowcount)
        print("Happy to serve you")
        
   

    elif (choice==4):
        exit

    else:
        print("INVALID CHOICE, Try Again")

choice=menu()
cur.close()
con.close()
