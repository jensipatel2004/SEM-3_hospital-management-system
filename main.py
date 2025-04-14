import doctor 
import appointment
import opd
import report 
while True:
    print("="*80)
    print("\t\t\t ------ Hospital Management System -----\n")
    print("="*80)
    print("\t\t\t\tEnter your choice")
    print("\t\t\t\t1. OPD\n\t\t\t\t2. Doctor Details\n\t\t\t\t3. Appointment\n\t\t\t\t4. Reports\n\t\t\t\t5. Exit \n")
    print("="*80)
    choice=int(input())
    if choice==1:
        while True:
            print("\t\t\t\tSelect the Action")
            print("\t\t\t\t1. New OPD\n\t\t\t\t2. Edit OPD\n\t\t\t\t3. Search OPD\n\t\t\t\t4. Back To Main Menu \n")
            print("="*80)
            choice=int(input())
            if choice==1:
                opd.opd_input()
                print("Successfully Added")
            elif choice==2:
                opd.opd_edit()
            elif choice==3:
                opd.opd_search()
                print()
            elif choice==4:
                break
    elif choice==2:
        while True:
            print("\t\t\t\tSelect the Action")
            print("\t\t\t\t1. Add New Doctor\n\t\t\t\t2. Edit Doctor Details\n\t\t\t\t3. Delete Doctor Details\n\t\t\t\t4. Search Doctor Details\n\t\t\t\t5. Back To Main Menu \n")
            print("="*80)
            choice=int(input())
            if choice==1:
                doctor.doctor_input()
            elif choice==2:
                doctor.doctor_edit()
            elif choice==3:
                doctor.doctor_delete()
            elif choice==4:
                doctor.doctor_search()
            elif choice==5:
                break
    elif choice==3:
        while True:
            print("\t\t\t\tSelect the Action")
            print("\t\t\t\t1. Appoitment\n\t\t\t\t2. Edit Appointment\n\t\t\t\t3. Search appointment\n\t\t\t\t4.Back To Main Menu \n")
            print("="*80)
            choice=int(input())
            if choice==1:
                appointment.appointment()
            elif choice==2:
                appointment.appointment_edit()
            elif choice==3:
                appointment.appointment_search()
            elif choice==4:
                break
    elif choice==4:
        while True:
            print("\t\t\t\tSelect the Action")
            print("\t\t\t\t1. Display Doctor List\n\t\t\t\t2. Display Patient list\n\t\t\t\t3. Doctor History\n\t\t\t\t4. Patient History\n\t\t\t\t5. OPD Details\n\t\t\t\t6. Max (Diagnos Chart)\n\t\t\t\t7. Back to Main Menu \n")
            print("="*80)
            choice=int(input())
            if choice==1:
                report.doctor_list()
            elif choice==2:
                report.patient_list()
            elif choice==3:
                report.doctor_treatment()
            elif choice==4:
                report.patient_history()
                print()
            elif choice==5:
                report.opd_list()
            elif choice==6:
                report.col_chart()
            elif choice==7:
                break
    elif choice==5:
        break


        