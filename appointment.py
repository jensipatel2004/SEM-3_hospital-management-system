import pandas as pd
import numpy as np
import mysql.connector as sqlt
from tabulate import tabulate
con=sqlt.connect(host="localhost", user="root", passwd="", database="hms")
cursor=con.cursor()

def appointment():
            pname = input('Enter Patient Name : ')
            dname = input("Enter Doctor Name : ")
            doa = input("Enter Date of Birth  (DD-MM-YYYY) : ")
            sympton = input("Enter Symptom : ")
            treatment  = input("Enter Treatment : ")
            query = f"INSERT INTO appoint(DOA,PNAME,DNAME,SYMPTON,TREATMENT) VALUES('{doa}','{pname}','{dname}','{sympton}','{treatment}');"
            cursor.execute(query)
            con.commit()
            print("Patient Added Successfully!")

def appointment_edit():
        while True:
            id = int(input("Enter OPD ID for editing :"))
            cursor = con.cursor()
            cursor.execute(f'SELECT * FROM appoint WHERE opdno= {id};')
            rows = cursor.fetchall()
            if len(rows)==0 :
                print("No such Patient Found.")
                continue
            else :
                    print("1. Date of Birth")
                    print("2. Patient's Name")
                    print("3. Doctor's Name")
                    print("4. Sympton")
                    print("5. Treatment")
                    print("6. Exit ")
                    choice = int(input("Enter the field number you want to edit : "))
                    if choice == 1 :
                         dob = input("New DOB (DD-MM-YYYY) : ")
                         cursor.execute(f"UPDATE appoint SET doa='{dob}' WHERE opdno={id};")
                         con.commit()
                    elif choice == 2 : 
                         pn = input("Enter  New Patient's Name : ")
                         cursor.execute(f"UPDATE appoint SET pname='{pn}' WHERE opdno={id};")
                         con.commit()
                    elif choice == 3 : 
                         dn = input("Enter New Doctor's Name : ")
                         cursor.execute(f"UPDATE appoint SET dname='{dn}' WHERE opdno={id};")
                         con.commit()
                    elif choice == 4 : 
                         smp = input("Enter New Sympton : ")
                         cursor.execute(f"UPDATE appoint SET symptoms='{smp}' WHERE opdno={id};")
                         con.commit()
                    elif choice == 5 :  
                         tmt = input("Enter New Treatment : ")
                         cursor.execute(f"UPDATE appoint SET treatments='{tmt}' WHERE opdno={id};")
                         con.commit()
                    elif choice == 6 : 
                         break
                    else :
                         print("Please Enter a  valid option!")
                         continue
                         
def appointment_search():
            nm = (input("Enter Patient's name to search :"))
            cursor = con.cursor()
            cursor.execute(f'SELECT * FROM appoint WHERE pname="{nm}"; ')
            rows = cursor.fetchall()
            if len(rows)==0 :
                print("No such Patient Found.")
            else :
                i = 1
                for row in rows:
                    print("\n\t%d."%i,end=" ")
                    print("OPD No. : ",row[0])
                    print("Date of Birth : ",row[1])
                    print("Patient's Name  : ",row[2])
                    print("Doctor's Name : ",row[3])
                    print("Symptom : ",row[4])
                    print("Treatment : ",row[5])
