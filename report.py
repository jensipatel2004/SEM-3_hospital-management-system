import pandas as pd
import mysql.connector as sqlt
import matplotlib.pyplot as plt
from tabulate import tabulate

con=sqlt.connect(host="localhost",user="root",passwd="",database="hms")
cursor=con.cursor()
def doctor_list():
    qry="select * from doctor;"
    df=pd.read_sql(qry,con)
    #cursor.execute(qry)
    #x=cursor.fetchall()
    #print(x)
    #print(df.to_string(index=False))
    print(tabulate(df,headers='keys',tablefmt='psql',showindex=False))
    print()
def patient_list():
    qry="select * from patient;"
    df=pd.read_sql(qry,con)
    #cursor.execute(qry)
    #x=cursor.fetchall()
    #print(x)
    #df=df.to_string(index=False)
    print(tabulate(df,headers='keys',tablefmt='psql',showindex=False))
    print()
def doctor_treatment():
    x=input("enter doctor name")
    qry="select * from appoint where dname='{}';".format(x)
    df=pd.read_sql(qry,con)
    print(tabulate(df,headers='keys',tablefmt='psql',showindex=False))
    print()
def opd_list():
    bdate=input("enter beginning date")
    edate=input("enter end date")
    qry="select opd.opdno ,doa,pname,dname,symptom,treatment,fee from opd where doa between '{}' and '{}';".format(bdate,edate)
    df=pd.read_sql(qry,con)
    print(tabulate(df,headers='keys',tablefmt='psql',showindex=False))
    print()
def patient_history():
    df=pd.read_sql("select * from appoint,opd where opd.opdno=appoint.opdno;",con)
    #print(df.to_string(index=False))
    #df=pd.read_sql(qry,con)
    print(tabulate(df,headers='keys',tablefmt='psql',showindex=False))
    print()
def col_chart():
    qry="select symptom,count(symptom) as total_cases from appoint group by symptom;"
    df=pd.read_sql(qry,con)
    #print(df.to_string(index=False))
    print(tabulate(df,headers='keys',tablefmt='psql',showindex=False))
    plt.bar(df.symptom,df.total_cases)
    plt.title("Bimaari")
    plt.xlabel("problems")
    plt.ylabel("total cases")
    plt.xticks(df.symptom)
    plt.show()