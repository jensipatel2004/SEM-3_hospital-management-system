import pandas as pd
import mysql.connector as sqlt
from tabulate import tabulate
con=sqlt.connect(host="localhost",user="root",passwd="",database="hms")
cursor=con.cursor()
def doctor_input():
    qry1="select max(did) from doctor;"
    cursor.execute(qry1)
    t=cursor.fetchone()
    if not t[0]:
        did=1
    else:
        did=t[0]+1
    print(did)
    dname=input("Enter the Doctor Name ")
    dept=input("Enter Department")
    qry="insert into doctor(DID,DNAME,DEPARTMENT) values ({},'{}','{}');".format(did,dname,dept)
    cursor.execute(qry)
    con.commit()
    print("Successfully Added")

def doctor_edit():
    Did=int(input("Enter Doctor ID"))
    qry="select * from doctor where did = {};".format(Did)
    cursor.execute(qry)
    r=cursor.fetchone()
    if r:
        dept=input("Enter New Deptartment")
        qry="update doctor set department='{}'".format(dept)
        cursor.execute(qry)
        print("Successfully updated")
    else:
        print("Wrong Doctor ID")
    

def doctor_delete():
    Did=int(input("Enter Doctor ID"))
    qry="select * from doctor where did = {};".format(Did)
    cursor.execute(qry)
    r=cursor.fetchone()
    if r:
        ch=input("Are you sure you want to delete y/n")
        if ch=='y':
            qry="delete from doctor where did={}".format(Did)
            cursor.execute(qry)
            con.commit()
            print("Successfully deleted ")
    else:
        print("Wrong Doctor ID")


def doctor_search():
    did=int(input("Enter the Doctor Id"))
    qry="select * from doctor where did = {}".format(did)
    df=pd.read_sql(qry,con)
    print(tabulate(df,headers='keys',tablefmt='psql',showindex=False))
