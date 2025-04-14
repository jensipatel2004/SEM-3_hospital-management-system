import mysql.connector 
import pandas as pd
from tabulate import tabulate
conn = mysql.connector.connect(host="localhost",user = "root",password = "",database = "hms")   
if conn.is_connected() == False : 
    print("Connection Failed")
    exit(1)


def opd_input():
            cursor = conn.cursor()
            opd_n=int(input("Enter opd No :"))
            pname = input('Enter Patient Name : ')
            dname = input("Enter Doctor Name : ")
            doa = input("Enter Date of Admission  (DD-MM-YYYY) : ")
            sympton = input("Enter Symptom : ")
            treatment  = input("Enter Treatment : ")
            query = f"INSERT INTO appoint(OPDNO,DOA,PNAME,DNAME,SYMPTON,TREATMENT) VALUES('{opd_n}','{doa}','{pname}','{dname}','{sympton}','{treatment}');"
            cursor.execute(query)
            print("Patient Added Successfully!")
            fee = input("Enter Fee : ")
            paddress=input("Enter the address of the patient :")
            pmob=input("Enter the Mobile Number of the patient :")
            query = f'INSERT INTO opd(pname,dname,fee) VALUES("{pname}","{dname}",{fee});'  
            cursor.execute(query)
            query = f'INSERT INTO patient(PNAME,PADD,PMOB) VALUES("{pname}","{paddress}","{pmob}");'  
            cursor.execute(query)
            conn.commit()
            print("Patient Added Successfully!")
def opd_edit():
        while True:
            id = int(input("Enter OPD ID for editing :"))
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM opd WHERE opdno= {id};')
            rows = cursor.fetchall()
            if len(rows)==0 :
                print("No such Patient Found.")
                continue
            else :
                    print("1. Patient's Name")
                    print("2. Doctor's Name")
                    print("3. Fee")
                    print("4. None of Them ")
                    choice = int(input("Enter the field number you want to edit : "))
                    if choice == 1 : 
                         pn = input("Enter  New Patient's Name : ")
                         cursor.execute(f"UPDATE opd SET pname='{pn}' WHERE opdno={id};")
                         conn.commit()
                    elif choice == 2 : 
                         dn = input("Enter New Doctor's Name : ")
                         cursor.execute(f"UPDATE opd SET dname='{dn}' WHERE opdno={id};")
                         conn.commit()
                    elif choice == 3 : 
                         f_input = input("Enter New FEE : ")
                         cursor.execute(f"UPDATE opd SET fee='{f_input}' WHERE opdno={id};")
                         conn.commit()
                    elif choice == 4 : 
                         break
                    else :
                         print("Please Enter a  valid option!")
                         continue
                         
        
def opd_search():
            nm = (input("Enter Patient's name to search :"))
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM opd WHERE PNAME="{nm}"; ')
            rows = cursor.fetchall()
            if len(rows)==0 :
                print("No such Patient Found.")
            else :
                qry="select * from appoint where PNAME = '{}'".format(nm)
                df=pd.read_sql(qry,conn)
                print(tabulate(df,headers='keys',tablefmt='psql',showindex=False))