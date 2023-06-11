from matplotlib import pyplot as pp
from turtle import *
import mysql.connector as ma
def connection():
    try:
      con=ma.connect(host="localhost",user="root",password="Jeeprep5*",database="hospital_management_system")     
      if con.is_connected()==False:
          print("database not connected")
      else:
          return con
    except ma.Error as er:
      print(er)
      
#TURTLE GRAPHICS RED CROSS
t=Turtle()
t.color("red","red")
t.begin_fill()
t.pensize(26)
t.speed(1000)

t.right(90)
t.forward(100)
t.left(90)
t.backward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()
      

def a_insert_ncpatients():
    try:
        con=connection()
        cur=con.cursor()
        name=input("Enter patient's name: ")
        p_id=int(input('Enter patient id:'))
        date_in=input("Enter the date of joining the hospital:")
        date_out=input('enter the date of discharge')
        gender=input("Enter patient's gender' : ")
        age=int(input(" Enter patient's age: "))
        aadhar=int(input("Enter patient's aadhar number: "))
        insurance=int(input("Enter patient's health insurance number: "))
        phone=int(input("Enter patient's contact number ' : "))
        address=input("Enter patient's address ': ")
        disease=input("Enter patient's disease: ")
        room=input("Enter room type: " )
        room_number=int(input("Enter the room number : "))
        email=input("Enter email id of the patient : ")
        doc=int(input("Enter doctor id assigned : "))
        cur.execute("insert into patients(name,p_id,date_in,date_out,gender,age,aadhar,insurance,phone,address,disease,room,room_number,email,doc)values('%s',%d,'%s','%s','%s',%d,%d,%d,%d,'%s','%s','%s',%d,'%s',%d)"%(
name,p_id,date_in,date_out,gender,age,aadhar,insurance,phone,address,disease,room,room_number,email,doc))    
        print()
        print("Data inserted successfully")
        con.commit()
    except ma.Error as er:
        print(er)
        
def a_display_ncpatients():
    try:
        con=connection()
        cur=con.cursor() 
        cur.execute("select * from patients")
        for i in cur.fetchall():
            print(i)
    except ma.Error as er:
          print(er)
         
def a_update_ncpatients():
    try:
        con=connection()
        cur=con.cursor()
        name=input("Enter patient's name: ")
        p_id=int(input('Enter patient id:'))
        date_in=input("Enter the date of joining the hospital:")
        date_out=input('enter date of discharge')
        gender=input("Enter patient's gender' : ")
        age=int(input(" Enter patient's age: "))
        aadhar=int(input("Enter patient's aadhar number: "))
        insurance=int(input("Enter patient's health insurance number: "))
        phone=int(input("Enter patient's contact number ' : "))
        address=input("Enter patient's address ': ")
        disease=input("Enter patient's disease: ")
        room=input("Enter room type: " )
        room_number=int(input("Enter the room number : "))
        email=input("Enter email id of the patient : ")
        doc=int(input("Enter doctor id assigned : "))
        cur.execute(" update patients set  name='%s',date_in='%s',date_out='%s',gender='%s',age=%d,aadhar=%d,insurance=%d,phone=%d,address='%s',disease='%s',room='%s',room_number=%d,email='%s',doc=%d where p_id=%d"%(name,date_in,date_out,gender,age,aadhar,insurance,phone,address,disease,room,room_number,email,doc,p_id))
        print()
        con.commit()
        print("Data updated successfully")
    except ma.Error as er:
          print(er)
         
def a_delete_ncpatients():
    try:
        con=connection()
        cur=con.cursor()
        name=input("Enter patient's name to be deleted: ")
        cur.execute("delete from patients where name='%s'"%(name))
        print()
        con.commit()
        print("Data deleted successfully")
    except ma.error as er:
        print(er)
def d_insert_doctor():
    try:
        con=connection()
        cur=con.cursor()
        name=input("Enter the doctor's name: ")
        d_id=int(input("Enter the doctor's id"))
        gend=input("Enter the gender of doctor")
        time=input("Enter the time of consultation:   ")
        spec=input("Enter the specialization:  ")
        exp=int(input("Enter the experience: "))
        fee=int(input("Enter the fee of consultation:  "))
        email=input("Enter the doctor's email id:  ")
        ph_no=int(input("Enter doctor's phone number:   "))
        addr=input("Enter the doctor's address:   ")
       
        cur.execute("insert into doctors(name,d_id,gend,time,spec,exp,fee,email,ph_no,addr)values('%s',%d,'%s','%s','%s',%d,%d,'%s',%d,'%s')"%(name,d_id,gend,time,spec,exp,fee,email,ph_no,addr))
        print()
        print("Date inserted successfully!")
        con.commit()
    except ma.Error as er:
        print(er)
        
def d_display_doctor():
    try:
        con=connection()
        cur=con.cursor()
        cur.execute("select * from doctors")
        for i in cur.fetchall():
            print(i)
    except ma.Error as er:
        print(er)
        
def d_update_doctor():
    try:
        con=connection()
        cur=con.cursor()
        name=input("Enter the doctor's name: ")
        d_id=int(input("Enter the doctor's id"))
        gend=input("Enter the gender of doctor")
        time=input("Enter the time of consultation:    ")
        spec=input("Enter the specialization:  ")
        exp=int(input("Enter the experience: "))
        fee=int(input("Enter the fee for consulation"))
        email=input("Enter the doctor's email id:  ")
        ph_no=int(input("Enter doctor's phone number:   "))
        addr=input("Enter the doctor's address:   ")
       
        cur.execute("Update doctors set name='%s',gend='%s',time='%s',spec='%s',exp=%d,fee=%d,email='%s',ph_no=%d,addr='%s' where d_id=%d"%(name,gend,time,spec,exp,fee,email,ph_no,addr,d_id))
        print()
        con.commit()
        print("Data updated successfully!")
    except ma.Error as er:
        print(er)
      
def d_delete_doctor():
    try:
        con=connection()
        cur=con.cursor()
        name=input("Enter doctor's name to be deleted:  ")
        cur.execute("Delete from doctors where name='%s'"%(name))
        print()
        con.commit()
        print("Data deleted successfully!")
    except ma.Error as er:
        print(er)
                
        
def a_insert_wards():
    try:
        con=connection()
        cur=con.cursor()
        building=input('enter building:')
        room_number=int(input("enter room no:"))             
        number_of_beds=int(input("enter no. of beds:"))       
        status=input("enter room status:")       
        room_rent=int(input('enter  daily charge for room:'))
        cur.execute("insert into WARDS(building,room_number,number_of_beds,status,room_rent)values('%s',%d,%d,'%s',%d)"%(building,room_number,number_of_beds,status,room_rent))
        print("data inserted successfully")
        con.commit()
    except ma.Error as er:
        print(er)

def a_display_wards():
    try:
        con=connection()
        cur=con.cursor()
        cur.execute("select * from WARDS")
        for i in cur.fetchall():
            print(i)
    except ma.Error as er:
        print(er)
def a_update_wards():
    try:
        con=connection()
        cur=con.cursor()
        building=input('enter building:')
        room_number=int(input("enter room no:"))             
        number_of_beds=int(input("enter no. of beds:"))      
        status=input("enter room status:")       
        room_rent=int(input('enter  daily charge for room:'))
        cur.execute("update WARDS set building='%s',number_of_beds=%d,status='%s',room_rent=%d where room_number= %d"%(building,number_of_beds,status,room_rent,room_number))
        print()
        con.commit()
        print("records updated successfully")
    except ma.Error as er:
        print(er)

import numpy as np

def a_insert_covidpatients():
                       
    try:
        con=connection()
        cur=con.cursor()
        print('INSERT COVIDPATIENTS')
        p=int(input('enter number of patients:'))
        for i in range(p):
            p_name=input("enter name of covid patients:")
            p_id=int(input("enter id for covid patients:"))
            p_age=int(input("enter age of covid patients:"))
            p_gender=input("enter gender of covid patient;")
            p_room=input("enter room number of covid patient in C264 TYPE:")
            p_date=input("enter date of admission:")
            p_status=input('Enter recovered/dead/ongoing')
            p_doc=int(input("enter assigned doctor's id:  "))
            cur.execute("insert into COVID19_PATIENTS (patient_id,age,gender,room,date,name,status_patient,p_doc) values(%d,%d,'%s','%s','%s','%s','%s',%d)"%(p_id,p_age,p_gender,p_room,p_date,p_name,p_status,p_doc))
            
        print("INSERTED")
        con.commit()
    except ma.Error as er:
        print(er)

def a_display_covidpatients():
    try:
        con=connection()
        cur=con.cursor()
        cur.execute("select * from COVID19_PATIENTS")
        for i in cur.fetchall():
            print(i)
    except ma.Error as er:
        print(er)

def a_update_covidpatients():
    try:
        con=connection()
        cur=con.cursor()
        p_name=input("enter name of covid patients:")
        p_id=int(input("enter id for covid patients:"))
        p_age=int(input("enter age of covid patients:"))
        p_gender=input("enter gender of covid patient:")
        p_room=input("enter room number of covid patient in C264 TYPE:")
        p_date=input("enter date of admission:")
        p_status=input('enter recovered/dead/ongoing')
        cur.execute("update COVID19_PATIENTS set age=%d,gender='%s', room='%s', date='%s', name='%s',status_patient='%s' where patient_id= %d"%(p_age,p_gender,p_room,p_date,p_name,p_status,p_id))
        con.commit()
        print("RECORD UPDATION COMPLETED")
    except ma.Error as er:
        print(er)
        
def a_delete_covidpatients():
    try:
        con=connection()
        cur=con.cursor()
        pid=int(input("enter id of recovered/dead covid patients whose records you want to delete:"))
        cur.execute("delete from COVID19_PATIENTS where patient_id=%d"%(pid))
        con.commit()
        print("RECORD DELETION COMPLETED or not found")
    except ma.Error as er:
        print(er)
def cov_init():
    try:
        con=connection()
        cur=con.cursor()
        #cur.execute("create table COVID_INIT(initiative varchar(340),details varchar(1999))")
        #cur.execute("insert into COVID_INIT(initiative,details) values ('CB-NAAT','REJUVENATE Hospitals takes COVID-19 testing to a whole new level with CB-NAAT By embracing the Cartridge Based Nucleic Acid Amplification Testing (CB-NAAT) method,REJUVENATE Hospitals promises overall patient satisfaction, thanks to 100% accurate test reports that are generated within just 2 hours')")
        ######################cur.execute("insert into COVID_INIT(initiative,details) values ('REJUVENATE Hospitals Separate Isolated Respiratory Block for Suspected COVID-19 Patients','REJUVENATE Hospitals Separate Isolated Respiratory Block is designed with dedicated pathways for patients & visitors to prevent cross-contamination. With 300 beds, dedicated caregivers, separate entry, exit & kitchen, the block is battle-ready in the war against COVID-19.')")
        initiative=input('you can add one initiative at a time.enter name of initiative:')
        details=input('enter details of initiative')     
        cur.execute("insert into COVID_INIT(initiative,details) values ('%s','%s')"%(initiative,details))
        con.commit()
    except ma.Error as er:
        print(er)
def cov_display_init():
    try:
        con=connection()
        cur=con.cursor()
        cur.execute('select * from COVID_INIT')
        for i in cur.fetchall():
            print(i)
    except ma.Error as er:
        print(er)
def daily_cc():
    try:
        con=connection()
        cur=con.cursor()
        date=input('enter date:')
        status_patient='ongoing'
        cur.execute("SELECT COUNT(*) from COVID19_PATIENTS where date='%s'and status_patient='%s'"%(date,status_patient))
        curry=cur.fetchone()
        print(curry[0])
    except ma.Error as er:
        print(er)
def daily_cd():
    try:
        con=connection()
        cur=con.cursor()
        date=input('enter date:')
        status_patient='dead'
        cur.execute("SELECT COUNT(*) from COVID19_PATIENTS where date='%s'and status_patient='%s'"%(date,status_patient))
        curry=cur.fetchone()
        print(curry[0])
    except ma.Error as er:
        print(er)
def daily_cr():
    try:
        con=connection()
        cur=con.cursor()
        date=input('enter date:')
        status_patient='recovered'
        cur.execute("SELECT COUNT(*) from COVID19_PATIENTS where date='%s'and status_patient='%s'"%(date,status_patient))
        curry=cur.fetchone()
        print(curry[0])
    except ma.Error as er:
        print(er)
def total_cc():
    try:
        con=connection()
        cur=con.cursor()
        cur.execute("select count(*) from COVID19_PATIENTS")
        curry=cur.fetchone()
        print(curry[0])
    except ma.Error as er:
        print(er)
def total_cd():
    try:
        con=connection()
        cur=con.cursor()
        status_patient='dead'
        cur.execute("select count(*) from COVID19_PATIENTS where status_patient='%s'"%(status_patient))
        curry=cur.fetchone()
        print(curry[0])
    except ma.Error as er:
        print(er)
def total_cr():
    try:
        con=connection()
        cur=con.cursor()
        status_patient='recovered'
        cur.execute("select count(*) from COVID19_PATIENTS where status_patient='%s'"%(status_patient))
        curry=cur.fetchone()
        print(curry[0])
    except ma.Error as er:
        print(er)

def line_chart_all_circle():
    try:
        con=connection()
        cur=con.cursor()
        ami=int(input("enter no. of dates' data' to be compiled"))
        datu=[ ]
        for i in range(ami):
            kj=input('enter date')
            datu.append(kj)
        x=datu
        y=[ ]
        for j in range(len(datu)):
            
            date=datu[j]
            cur.execute("select count(*) from COVID19_PATIENTS where date='%s'"%(date))
            curry=cur.fetchone()
            y.append(curry[0])
        z=[ ]        
        for j in range(len(datu)):
            status_patient='dead'
            
            date=datu[j]
            cur.execute("select count(*) from COVID19_PATIENTS where date='%s'and status_patient='%s'"%(date,status_patient))
            curry=cur.fetchone()
            z.append(curry[0])
        r=[ ]    
        for j in range(len(datu)):
            status_patient='recovered'
            date=datu[j]
            cur.execute("select count(*) from COVID19_PATIENTS where date='%s' and status_patient='%s'"%(date,status_patient))
            curry=cur.fetchone()
            r.append(curry[0])   
        pp.plot(x,y,'bo')
        pp.plot(x,z,'ro')
        pp.plot(x,r,'go')
        pp.title('covid cases,deaths,recoveries')
        pp.xlabel('DATES')
        pp.ylabel('CASES, DEATHS,RECOVERIES')
        pp.legend(['this is cases','this is DEATHS','this is RECOVERIES'])
        pp.show()
    except ma.Error as er:
        print(er)
def line_chart_all():
    try:
        con=connection()
        cur=con.cursor()
        ami=int(input("enter no. of dates' data' to be compiled"))
        datu=[ ]
        for i in range(ami):
            kj=input('enter date')
            datu.append(kj)
        
        y=[ ] 
        for j in range(len(datu)):
            date=datu[j]
            cur.execute("select count(*) from COVID19_PATIENTS where date='%s'"%(date))
            curry=cur.fetchone()
            y.append(curry[0])
        z=[ ]
        for j in range(len(datu)):
            status_patient='dead'
            date=datu[j]
            cur.execute("select count(*) from COVID19_PATIENTS where date='%s' and status_patient='%s'"%(date,status_patient))
            curry=cur.fetchone()
            z.append(curry[0])
        r=[ ]
        for j in range(len(datu)):
            status_patient='recovered'
            date=datu[j]
            cur.execute("select count(*) from COVID19_PATIENTS where date='%s' and status_patient='%s'"%(date,status_patient))
            curry=cur.fetchone()
            r.append(curry[0])
        x=datu
        x=np.array(x)
        y=np.array(y)
        z=np.array(z)
        r=np.array(r)
        pp.figure(figsize=(13, 3))
        pp.subplot(222)
        pp.xlabel('dates')
        pp.ylabel('cases')
        pp.plot(x,y)      #line chart
        pp.suptitle('COVID cases IN REJUVENATE HOSPITAL -ON A DAILY BASIS')
        pp.figure(figsize=(13, 3))
        pp.subplot(222)
        pp.xlabel('dates')
        pp.ylabel('deaths')
        pp.plot(x,z)      #line chart
        pp.suptitle('COVID DEATHS IN REJUVENATE HOSPITAL -ON A DAILY BASIS')
        pp.figure(figsize=(13, 3))
        pp.subplot(222)
        pp.xlabel('dates')
        pp.ylabel('recoveries')
        pp.plot(x,r)      #line chart
        pp.suptitle('COVID recoveries IN REJUVENATE HOSPITAL -ON A DAILY BASIS')
        pp.show()
    except ma.Error as er:
        print(er)    
def scatter_plot_all():
    try:
        con=connection()
        cur=con.cursor()
        ami=int(input("enter no. of dates' data' to be compiled"))
        datu=[ ]
        for i in range(ami):
            kj=input('enter date')
            datu.append(kj)
        x=datu
        y=[ ]
        for j in range(len(datu)):
            date=datu[j]
            cur.execute("select count(*) from COVID19_PATIENTS where date='%s'"%(date))
            curry=cur.fetchone()
            y.append(curry[0])
        z=[ ]        
        for j in range(len(datu)):
            status_patient='dead'
            
            date=datu[j]
            cur.execute("select count(*) from COVID19_PATIENTS where date='%s' and status_patient='%s'"%(date,status_patient))
            curry=cur.fetchone()
            z.append(curry[0])
        r=[ ]   
        for j in range(len(datu)):
            status_patient='recovered'
            date=datu[j]
            cur.execute("select count(*) from COVID19_PATIENTS where date='%s' and status_patient='%s'"%(date,status_patient))
            curry=cur.fetchone()
            r.append(curry[0])
        x=np.array(x)
        y=np.array(y)
        z=np.array(z)
        r=np.array(r)    
        pp.figure(figsize=(13, 3))
        pp.subplot(222)
        pp.xlabel('dates')
        pp.ylabel('cases')
        pp.scatter(x,y)      #line chart
        pp.suptitle('COVID cases IN REJUVENATE HOSPITAL -ON A DAILY BASIS')
        pp.figure(figsize=(13, 3))
        pp.subplot(222)
        pp.xlabel('dates')
        pp.ylabel('deaths')
        pp.scatter(x,z)      #line chart
        pp.suptitle('COVID DEATHS IN REJUVENATE HOSPITAL -ON A DAILY BASIS')
        pp.figure(figsize=(13, 3))
        pp.subplot(222)
        pp.xlabel('dates')
        pp.ylabel('recoveries')
        pp.scatter(x,r)      #line chart
        pp.suptitle('COVID recoveries IN REJUVENATE HOSPITAL -ON A DAILY BASIS')
        pp.show()
    except ma.Error as er:
        print(er)    
    
def bar_chart_all():
    try:
        con=connection()
        cur=con.cursor()
        ami=int(input("enter no. of dates' data' to be compiled"))
        datu=[ ]
        for i in range(ami):
            kj=input('enter date')
            datu.append(kj)
        x=datu
        y=[ ]
        for j in range(len(datu)):
            date=datu[j]
            cur.execute("select count(*) from COVID19_PATIENTS where date='%s'"%(date))
            curry=cur.fetchone()
            y.append(curry[0])
        z=[ ]     
        for j in range(len(datu)):
            status_patient='dead'
            date=datu[j]
            cur.execute("select count(*) from COVID19_PATIENTS where date='%s' and status_patient='%s'"%(date,status_patient))
            curry=cur.fetchone()
            z.append(curry[0])
        r=[ ]
        for j in range(len(datu)):
            status_patient='recovered'
            date=datu[j]
            cur.execute("select count(*) from COVID19_PATIENTS where date='%s' and status_patient='%s'"%(date,status_patient))
            curry=cur.fetchone()
            r.append(curry[0])
        x=np.array(x)
        y=np.array(y)
        z=np.array(z)
        r=np.array(r)
        pp.figure(figsize=(13, 3))
        pp.subplot(222)
        pp.xlabel('dates')
        pp.ylabel('cases')
        pp.bar(x,y)      #line chart
        pp.suptitle('COVID cases IN REJUVENATE HOSPITAL -ON A DAILY BASIS')
        pp.figure(figsize=(13, 3))
        pp.subplot(222)
        pp.xlabel('dates')
        pp.ylabel('deaths')
        pp.bar(x,z)      #line chart
        pp.suptitle('COVID DEATHS IN REJUVENATE HOSPITAL -ON A DAILY BASIS')
        pp.figure(figsize=(13, 3))
        pp.subplot(222)
        pp.xlabel('dates')
        pp.ylabel('recoveries')
        pp.bar(x,r)      #line chart
        pp.suptitle('COVID recoveries IN REJUVENATE HOSPITAL -ON A DAILY BASIS')
    except ma.Error as er:
        print(er)

def analyse_covidata():
    try:
        print()
        print("HOW'D YOU LIKE TO VIEW GRAPHICAL COVID DATA OF REJUVENATE HOSPITAL")
        print('1.d,c,r line chart \n2.d,c,r line chart with circular denotion for all three in one graph \n3.d,c,r bar graph\n4.d,c,r scatter plot\n')
        chu=int(input('enter choice:'))
                
        if chu==1:
            print()
            line_chart_all()
        elif chu==2:
            line_chart_all_circle()
        elif chu==3:
            print()
            bar_chart_all()
        elif chu==4:
            scatter_plot_all()
    except ma.Error as er:
        print(er)


def avg_case():
    try:
        con=connection()
        cur=con.cursor()
        # cur.execute("create table date_wise_covidcase(date_of varchar,cases int(34))")
        ami=int(input("enter no. of dates' data to be compiled"))
        datu=[ ]
        for i in range(ami):
            kj=input('enter date')
            datu.append(kj)
        valu=[ ]
        for i in datu:
            date=i
            cur.execute("SELECT COUNT(*) from COVID19_PATIENTS where date='%s'"%(date))
            curry=cur.fetchone()
            valu.append(curry[0])
        for m in range(len(datu)):
            date_of=datu[m]
            cases=valu[m]
            cur.execute("insert into date_wise_covidcase(date_of,cases) values ('%s',%d)"%(date_of,cases))
            con.commit()
        cur.execute('select avg(DISTINCT cases) from date_wise_covidcase')
        curry=cur.fetchone()
        print(curry[0])
    except ma.Error as er:
        print(er)
    
def avg_death():
    try:
        con=connection()
        cur=con.cursor()
        # cur.execute("create table date_wise_coviddeaths(date_of varchar,deaths int(34))")
        ami=int(input("enter no. of dates' data to be compiled"))
        datu=[ ]
        for i in range(ami):
            kj=input('enter date')
            datu.append(kj)
        valu=[ ]
        for i in datu:
            date=i
            status_patient='dead'
            cur.execute("SELECT COUNT(*) from COVID19_PATIENTS where date='%s'and status_patient='%s'"%(date,status_patient))
            curry=cur.fetchone()
            valu.append(curry[0])
        for m in range(len(datu)):
            date_of=datu[m]
            deaths=valu[m]
            cur.execute("insert into date_wise_coviddeaths(date_of,deaths) values ('%s',%d)"%(date_of,deaths))
            con.commit()
        cur.execute('select avg(DISTINCT deaths) from date_wise_coviddeaths')
        curry=cur.fetchone()
        print(curry[0])
    except ma.Error as er:
        print(er)
    
    
def avg_recoveries():
    try:
        con=connection()
        cur=con.cursor()
        # cur.execute("create table date_wise_covidrecoveries(date_of varchar,recoveries int(34))")
        ami=int(input("enter no. of dates' data to be compiled"))
        datu=[ ]
        for i in range(ami):
            kj=input('enter date')
            datu.append(kj)
        valu=[ ]
        for i in datu:
            date=i
            status_patient='recovered'
            cur.execute("SELECT COUNT(*) from COVID19_PATIENTS where date='%s'and status_patient='%s'"%(date,status_patient))
            curry=cur.fetchone()
            valu.append(curry[0])
        for m in range(len(datu)):
            date_of=datu[m]
            recoveries=valu[m]
            cur.execute("insert into date_wise_covidrecoveries(date_of,recoveries) values ('%s',%d)"%(date_of,recoveries))
            con.commit()
        cur.execute('select avg(DISTINCT recoveries) from date_wise_covidrecoveries')
        curry=cur.fetchone()
        print(curry[0])
    except ma.Error as er:
        print(er)
    
def most_cases():
    try:
        con=connection()
        cur=con.cursor()
        # cur.execute("create table date_wise_covidcase(date_of varchar,cases int(34))")
        ami=int(input("enter no. of dates' data to be compiled"))
        datu=[ ]
        for i in range(ami):
            kj=input('enter date')
            datu.append(kj)
        valu=[ ]
        for i in datu:
            date=i
            cur.execute("SELECT COUNT(*) from COVID19_PATIENTS where date='%s'"%(date))
            curry=cur.fetchone()
            valu.append(curry[0])
        for m in range(len(datu)):
            date_of=datu[m]
            cases=valu[m]
            cur.execute("insert into date_wise_covidcase(date_of,cases) values ('%s',%d)"%(date_of,cases))
            con.commit()
        cur.execute('select max(DISTINCT cases) from date_wise_covidcase')
        curry=cur.fetchone()
        print(curry[0])
    except ma.Error as er:
        print(er)
    
def most_deaths():
    try:
        con=connection()
        cur=con.cursor()
        # cur.execute("create table date_wise_coviddeaths(date_of varchar,deaths int(34))")
        ami=int(input("enter no. of dates' data to be compiled"))
        datu=[ ]
        for i in range(ami):
            kj=input('enter date')
            datu.append(kj)
        valu=[ ]
        for i in datu:
            date=i
            status_patient='dead'
            cur.execute("SELECT COUNT(*) from COVID19_PATIENTS where date='%s'and status_patient='%s'"%(date,status_patient))
            curry=cur.fetchone()
            valu.append(curry[0])
        for m in range(len(datu)):
            date_of=datu[m]
            deaths=valu[m]
            cur.execute("insert into date_wise_coviddeaths(date_of,deaths) values ('%s',%d)"%(date_of,deaths))
            con.commit()
        cur.execute('select max(DISTINCT deaths) from date_wise_coviddeaths')
        curry=cur.fetchone()
        print(curry[0])
    except ma.Error as er:
        print(er)
    
def most_recoveries():
    try:
        con=connection()
        cur=con.cursor()
        # cur.execute("create table date_wise_covidrecoveries(date_of varchar,recoveries int(34))")
        ami=int(input("enter no. of dates' data to be compiled"))
        datu=[ ]
        for i in range(ami):
            kj=input('enter date')
            datu.append(kj)
        valu=[ ]
        for i in datu:
            date=i
            status_patient='recovered'
            cur.execute("SELECT COUNT(*) from COVID19_PATIENTS where date='%s'and status_patient='%s'"%(date,status_patient))
            curry=cur.fetchone()
            valu.append(curry[0])
        for m in range(len(datu)):
            date_of=datu[m]
            recoveries=valu[m]
            cur.execute("insert into date_wise_covidrecoveries(date_of,recoveries) values ('%s',%d)"%(date_of,recoveries))
            con.commit()
        cur.execute('select max(DISTINCT recoveries) from date_wise_covidrecoveries')
        curry=cur.fetchone()
        print(curry[0])
    except ma.Error as er:
        print(er)
    
    
def least_cases():
    try:
        con=connection()
        cur=con.cursor()
        # cur.execute("create table date_wise_covidcase(date_of varchar,cases int(34))")
        ami=int(input("enter no. of dates' data to be compiled"))
        datu=[ ]
        for i in range(ami):
            kj=input('enter date')
            datu.append(kj)
        valu=[ ]
        for i in datu:
            date=i
            status_patient='ongoing'
            cur.execute("SELECT COUNT(*) from COVID19_PATIENTS where date='%s'and status_patient='%s'"%(date,status_patient))
            curry=cur.fetchone()
            valu.append(curry[0])
        for m in range(len(datu)):
            date_of=datu[m]
            cases=valu[m]
            cur.execute("insert into date_wise_covidcase(date_of,cases) values ('%s',%d)"%(date_of,cases))
            con.commit()
        cur.execute('select min(DISTINCT cases) from date_wise_covidcase')
        curry=cur.fetchone()
        print(curry[0])
    except ma.Error as er:
        print(er)
    
def least_deaths():
    try:
        con=connection()
        cur=con.cursor()
        # cur.execute("create table date_wise_coviddeaths(date_of varchar,deaths int(34))")
        ami=int(input("enter no. of dates' data to be compiled"))
        datu=[ ]
        for i in range(ami):
            kj=input('enter date')
            datu.append(kj)
        valu=[ ]
        for i in datu:
            date=i
            status_patient='dead'
            cur.execute("SELECT COUNT(*) from COVID19_PATIENTS where date='%s'and status_patient='%s'"%(date,status_patient))
            curry=cur.fetchone()
            valu.append(curry[0])
        for m in range(len(datu)):
            date_of=datu[m]
            deaths=valu[m]
            cur.execute("insert into date_wise_coviddeaths(date_of,deaths) values ('%s',%d)"%(date_of,deaths))
            con.commit()
        cur.execute('select min(DISTINCT deaths) from date_wise_coviddeaths')
        curry=cur.fetchone()
        print(curry[0])
    except ma.Error as er:
        print(er)
        
    
def least_recoveries():
    try:
        con=connection()
        cur=con.cursor()
        # cur.execute("create table date_wise_covidrecoveries(date_of varchar,recoveries int(34))")
        ami=int(input("enter no. of dates' data to be compiled"))
        datu=[ ]
        for i in range(ami):
            kj=input('enter date')
            datu.append(kj)
        valu=[ ]
        for i in datu:
            date=i
            status_patient='recovered'
            cur.execute("SELECT COUNT(*) from COVID19_PATIENTS where date='%s'and status_patient='%s'"%(date,status_patient))
            curry=cur.fetchone()
            valu.append(curry[0])
        for m in range(len(datu)):
            date_of=datu[m]
            recoveries=valu[m]
            cur.execute("insert into date_wise_covidrecoveries(date_of,recoveries) values ('%s',%d)"%(date_of,recoveries))
            con.commit()
        cur.execute('select min(DISTINCT recoveries) from date_wise_covidrecoveries')
        curry=cur.fetchone()
        print(curry[0])
    except ma.Error as er:
        print(er)
print('welcome user! COVID SPECIALITY UNIT\n JOIN US IN OUR BATTLE AGAINST THE NOVEL CORONAVIRUS')
print('1.DAILY CASES')
print('2.DAILY COVID DEATHS')
print('3.DAILY RECOVERIES')
print('4.TOTAL CASES IN OUR HOSPITAL')
print('5.TOTAL DEATHS IN OUR HOSPITAL DUE TO COVID')
print('6.TOTAL RECOVERIES IN OUR HOSPITAL')
print('7.ANALYSE COVID DATA')
print("8.SEE ALL COVID PATIENTS' DATA")
print('9.OUR COVID INITIATIVES')
print('10.AVERAGE CASES PER DAY')
print('11.AVERAGE DEATHS PER DAY')
print('12.AVERAGE RECOVERIES PER DAY')
print('13.most cases')
print('14.most deaths')
print('15.most recoveries')
print('16.least cases')
print('17.least deaths')
print('18.least recoveries')
kree=int(input('enter choice'))
if kree==1:
    print('DAILY COVID CASES')
    daily_cc()
if kree==2:
    print('DAILY COVID DEATHS')
    daily_cd()
if kree==3:
    print('DAILY COVID RECOVERIES')
    daily_cr()
if kree==4:
    print('TOTAL CASES IN OUR HOSPITAL')
    total_cc()
if kree==5:
    print('TOTAL DEATHS IN OUR HOSPITAL DUE TO COVID')
    total_cd()
if kree==6:
    print('TOTAL RECOVERIES IN OUR HOSPITAL')
    total_cr()
if kree==7:
    print('ANALYSE COVID DATA')
    analyse_covidata()
if kree==8:
    print('DISPLAY COVID PATIENTS DATA')
    a_display_covidpatients()
if kree==9:
    print('OUR COVID INITIATIVES!')
    cov_display_init()
if kree==10:
    print('10.AVERAGE CASES PER DAY')
    avg_case()
if kree==11:
    print('11.AVERAGE DEATHS PER DAY')
    avg_death()
if kree==12:
    print('12.AVERAGE RECOVERIES PER DAY')
    avg_recoveries()
if kree==13:
    most_cases()
if kree==14:
    most_deaths()
if kree==15:
    most_recoveries()
if kree==16:
    least_cases()
if kree==17:
    least_deaths()
if kree==18:
     least_recoveries()

        
def doctor_view_prof():
    try:
        con=connection()
        cur=con.cursor()
        d_id=int(input("Enter your id doctor:  "))
        cur.execute("select * from doctors where d_id=%d"%(d_id))
        for i in cur.fetchall():
            print(i)
    except ma.Error as er:
        print(er)
        
def appointment_insertion():
    try:
        con=connection()
        cur=con.cursor()        
        d_id=int(input("Enter the doctor's id:"))
        p_id=int(input("Enter the patient's id:"))
        time=input("Enter the consultation time:")
        cur.execute("insert into appointments(p_id,d_id,time)values(%d,%d,'%s')"%(d_id,p_id,time))
        print()
        print("Appointments added successfully!")
        con.commit()
    except ma.Error as er:
        print(er)
        

        
def appointment_display_admin():
    try:
        con=connection()
        cur=con.cursor()
        cur.execute("select * from appointments")
        for i in cur.fetchall():
            print(i)
    except ma.Error as er:
        print(er)

def appointment_deletion_admin():
    try:
        con=connection()
        cur=con.cursor()
        p_id=int(input("Enter the patient's id to be deleted"))
        cur.execute("delete from appointments where p_id=%d"%(p_id))
        print()
        con.commit()
        print("Appointment deleted successfully!")
    except ma.Error as er:
        print(er)

def appointment_display_doc():
    try:
        con=connection()
        cur=con.cursor()
        d_id=int(input("Enter the doctor's id: "))
        cur.execute("select * from appointments where d_id=%d"%(d_id))
        for i in cur.fetchall():
            print(i)
    except ma.Error as er:
        print(er)
        
def appointment_deletion_doc():
    try:
        con=connection()
        cur=con.cursor()
        d_id=int(input("Enter the doctor's id: "))
        p_id=int(input("Enter the patient's id to be deleted"))
        cur.execute("delete from appointments where p_id=%d and d_id=%d"%(p_id,d_id))
        print()
        con.commit()
        print("Appointment deleted successfully!")
    except ma.Error as er:
        print(er)
        

def doctor():
    try:
        idi=int(input('enter doctor id'))
        con=connection()
        cur=con.cursor()
        b=int(input("enter the doc pass:  "))
        cur.execute("select doc_pwd from doc_pwd where doc_id=%d"%(idi))
        passw=cur.fetchone()
        password=passw[0]
        ans='y'
        if b==password:
            while ans=='y':
                print("Welcome Doctor")
                print("Rejuvenate Hospitals")
                print("1.Profile")
                print("2.Appointments")
                print("3.Change password")
                print("4.Prescription")
                choice=int(input("enter your choice"))
                if choice==1:
                    doctor_view_prof()
                    
                elif choice==2:
                    print("1.Appointment display")
                    print("2.Appointment deletion")
                    opt=int(input("Enter your choice:"))
                    if opt==1:
                        print("Your appointments are below doctor:")
                        appointment_display_doc()
                    else :
                        s=input("Do you want to delete an appointment:  ")
                        if s=='y':
                            n=int(input("Number of appointments wanted to be deleted: "))
                            for i in range(n):
                                  appointment_deletion_doc()
                            print("Appointment deleted successfully!")
                        else:
                            print("you cannot delete")
                elif choice==3:
                    print('CHANGE PASSWORD')
                    m=int(input('enter old password'))
                    if m==password:
                        new=int(input('enter new password'))
                        newr=int(input('confirm new doctor password'))
                        if new==newr:
                            cur.execute("update doc_pwd set doc_pwd=%d where doc_id=%d"%(new,idi))
                            con.commit()
                            print(' password change was successful')                         
                        else:
                            print('OOPS!confirmation failure')
                    
                elif choice==4:
                    
                        #1] TAKING VOICE INPUT
                        import speech_recognition as sr
                        
                        # obtain audio from the microphone
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            print("Say patient name!")
                            r.adjust_for_ambient_noise(source)
                            audio = r.listen(source)
                        name=r.recognize_google(audio)
                        
                        with sr.Microphone() as source:
                            print("Symptoms")
                            r.adjust_for_ambient_noise(source)
                            audio = r.listen(source)
                        sympt=r.recognize_google(audio)
                            
                        with sr.Microphone() as source:
                            print("Prescription")
                            r.adjust_for_ambient_noise(source)
                            audio = r.listen(source)
                        diag=r.recognize_google(audio)
                        
                        with sr.Microphone() as source:
                            print("Advice")
                            r.adjust_for_ambient_noise(source)
                            audio = r.listen(source)
                        advice=r.recognize_google(audio)    
                        
                        # recognize speech using Google Speech Recognition
                        try:
                            # for testing purposes, we're just using the default API key
                            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                            # instead of `r.recognize_google(audio)`
                            print("Name-",name)
                            print("Symptoms-",sympt)
                            print("Prescription-",diag)
                            print("Advice-",advice)
                            pass
                            
                            
                        except sr.UnknownValueError:
                            print("Google Speech Recognition could not understand audio")
                        except sr.RequestError as e:
                            print("Could not request results from Google Speech Recognition service; {0}".format(e))
                            
                            
                            
                            
                        #2] CREATING TEXT FILE    
                        # Python code to create a file 
                        file = open('pres.txt','w') 
                        file.write(name+"\n") 
                        file.write(sympt+"\n")
                        file.write(diag+"\n")
                        file.write(advice+"\n")
                        file.close()
                        import os
                        file = "pres.txt"
                        os.system(file)
                        
                        
                        
                        #3]CREATING DIGITAL PRESCRIPTION
                        l=[['Name','Symptoms','Prescription','Advice']]
                        li=[]
                         
                        with open("pres.txt") as file:   
                            dataa = file.read()
                            li.append(dataa.split("\n"))
                        [li]=li
                        li.pop()
                        l.append(li)
                        data=l
                        fileName = 'pres.pdf'
                        
                        from reportlab.platypus import SimpleDocTemplate
                        from reportlab.lib.pagesizes import letter
                        
                        pdf = SimpleDocTemplate(
                            fileName,
                            pagesize=letter
                        )
                        
                        from reportlab.platypus import Table
                        table = Table(data)
                        
                        # add style
                        from reportlab.platypus import TableStyle
                        from reportlab.lib import colors
                        
                        style = TableStyle([
                            ('BACKGROUND', (0,0), (3,0), colors.green),
                            ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
                        
                            ('ALIGN',(0,0),(-1,-1),'CENTER'),
                        
                            ('FONTNAME', (0,0), (-1,0), 'Courier-Bold'),
                            ('FONTSIZE', (0,0), (-1,0), 14),
                        
                            ('BOTTOMPADDING', (0,0), (-1,0), 12),
                        
                            ('BACKGROUND',(0,1),(-1,-1),colors.beige),
                        ])
                        table.setStyle(style)
                        
                        #  Alternate backgroud color
                        rowNumb = len(data)
                        for i in range(1, rowNumb):
                            if i % 2 == 0:
                                bc = colors.burlywood
                            else:
                                bc = colors.beige
                            
                            ts = TableStyle(
                                [('BACKGROUND', (0,i),(-1,i), bc)]
                            )
                            table.setStyle(ts)
                        
                        #  Add borders
                        ts = TableStyle(
                            [
                            ('BOX',(0,0),(-1,-1),2,colors.black),
                        
                            ('LINEBEFORE',(2,1),(2,-1),2,colors.white),
                            ('LINEABOVE',(0,2),(-1,2),2,colors.white),
                        
                            ('GRID',(0,1),(-1,-1),2,colors.black),
                            ]
                        )
                        table.setStyle(ts)
                        
                        elems = []
                        elems.append(table)
                        
                        pdf.build(elems)
 
                ans=input('enter y to continue')
        else:
            print("password is incorrect")
    except ma.Error as er:
        print(er)
        
        
def pharm_add():
    try:
      con=connection()
      cur=con.cursor()
      mid=int(input("Enter the id of the medicine:"))
      med=input("Enter the name of the medicine:")
      pharma=input("Enter the pharma company:")
      price=int(input("Enter the price:"))
      num=int(input("Enter the number of medicines available:"))
      mfg=input("Enter the mfg date:")
      exp=input("enter the expiry date:")#create table pharma (mid int(5),med varchar(25),pharma varchar(25),price int(10),num int(20),mfg date ,exp date);
      cur.execute("insert into pharma (mid,med,pharma,price,num,mfg,exp)values(%d,'%s','%s',%d,%d,'%s','%s')"%(mid,med,pharma,price,num,mfg,exp))
      print()
      con.commit()
      print("Data inserted successfully")
    except ma.Error as er:
        print(er)
        
    
def pharm_update():
    try:
        con=connection()
        cur=con.cursor()
        mid=int(input("Enter the id of the medicine you want to update:"))
        med=input("Enter the name of the medicine: ")
        pharma=input("Enter the name of the pharma company: ")
        price=int(input("Enter the price:"))
        num=int(input("Enter the number of medicines available:"))
        mfg=input("Enter the mfg date:")
        exp=input("enter the expiry date:")
        cur.execute("update pharma set med='%s',pharma='%s',price=%d,num=%d,mfg='%s',exp='%s' where mid=%d"%(med,pharma,price,num,mfg,exp,mid))
        con.commit()
        print("Data updated successfully")
    except ma.Error as er:
        print(er)
        
def pharm_delete():
    try:
        con=connection()
        cur=con.cursor()
        mid=int(input("Enter the id of the medicine you want to delete:"))
        cur.execute("delete from pharma where mid=%d"%(mid))
        con.commit()
        print("Record deleted")
    except ma.Error as er:
        print(er)    
    
    
    
def pharm_show():
    try:
        con=connection()
        cur=con.cursor()
        cur.execute("select * from pharma")
        for i in cur.fetchall():
            print(i)
    except ma.Error as er:
        print(er)
 
def bb_ins():
    try:
        con=connection()
        cur=con.cursor()
        Id=int(input('enter donor id'))
        fname=input("enter father's name")
        mname=input("enter mother's name")
        lname=input("enter last name")
        sex=input('enter gender of donor')
        b_type=input('enter blood group')
        bday=input('enter birthdate of donor in yy-mm-dd')
        h_address=input('enter address')
        city=input('enter city')
        don_date=input('enter date of donation(latest)')
        #### stats=imput('enter status')
        temp=input('enter body temperature at the time of donation in fahrenheit')
        pulse=input('enter pulse rate at donation')
        bp=input('enter blood pressure at donation')
        weight=int(input('enter weight'))
        haemoglobin=input('enter haemoglobin count and specifications')
        plateletcount=int(input('enter platelet count'))
        hbsag=input('enter hbsag')
        aids=input('enter HIV status')
        malaria_smear=input('enter malaria smear')
        hematocrit=input('enter hematocrit')
        phone=int(input('enter phone no.'))
        mobile=int(input('enter mobile number'))
        cur.execute("insert into tblblooddonors(Id,fname,mname,lname,sex,b_type,bday,h_address,city,don_date,temp,pulse,bp,weight,haemoglobin,plateletcount,hbsag,aids,malaria_smear,hematocrit,phone,mobile) values (%d,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',%d,'%s',%d,'%s','%s','%s','%s',%d,%d)"%(Id,fname,mname,lname,sex,b_type,bday,h_address,city,don_date,temp,pulse,bp,weight,haemoglobin,plateletcount,hbsag,aids,malaria_smear,hematocrit,phone,mobile))
        con.commit()
        print('data inserted successfully')
    except ma.Error as er:
        print(er)
def bb_upd():
    try:
        con=connection()
        cur=con.cursor()
        Id=int(input('enter donor id'))
        fname=input("enter father's name")
        mname=input("enter mother's name")
        lname=input("enter last name")
        sex=input('enter gender of donor')
        b_type=input('enter blood group')
        bday=input('enter birthdate of donor in yy-mm-dd')
        h_address=input('enter address')
        city=input('enter city')
        don_date=input('enter date of donation(latest)')
        ##### stats=imput('enter status')
        temp=input('enter body temperature at the time of donation in fahrenheit')
        pulse=input('enter pulse rate at donation')
        bp=input('enter blood pressure at donation')
        weight=int(input('enter weight'))
        haemoglobin=input('enter haemoglobin count and specifications')
        plateletcount=int(input('enter platelet count'))
        hbsag=input('enter hbsag')
        aids=input('enter HIV status')
        malaria_smear=input('enter malaria smear')
        hematocrit=input('enter hematocrit')
        phone=int(input('enter phone no.'))
        mobile=int(input('enter mobile number'))
        cur.execute("update tblblooddonors set fname='%s',mname='%s',lname='%s',sex='%s',b_type='%s',bday='%s',h_address='%s',city='%s',don_date='%s',temp='%s',pulse='%s',bp='%s',weight=%d,haemoglobin='%s',plateletcount=%d,hbsag='%s',aids='%s',malaria_smear='%s',hematocrit='%s',phone=%d,mobile=%d where Id=%d"%(fname,mname,lname,sex,b_type,bday,h_address,city,don_date,temp,pulse,bp,weight,haemoglobin,plateletcount,hbsag,aids,malaria_smear,hematocrit,phone,mobile,Id))
        con.commit()
        print('updated successfully')
    except ma.Error as er:
        print(er)
def bb_del():
    try:
        con=connection()
        cur=con.cursor()
        Id=int(input('enter donor id'))
        cur.execute('delete from tblblooddonors where Id=%d'%(Id))
        con.commit()
        print('donor data deleted successfully')
    except ma.Error as er:
        print(er)
def bb_bg_upd():
    try:
        con=connection()
        cur=con.connection()
        bg_id=int(input('enter blood group id'))
        BloodGroup=input('enter blood group')
        PostingDate=input('enter latest posting date in yy-mm-dd format')
        stock=input('enter blodd stock')
        cur.execute("update tblbloodgroup set BloodGroup='%s',PostingDate='%s',stock='%s' where bg_id=%d"%(bg_id,BloodGroup,PostingDate,stock))
        con.commit()
        print('updation success')
    except ma.Error as er:
        print(er)
        
def elli_don():
    try:
        print('1.to view the standard GENERAL POLICY FOR BLOOD DONATION \n2.COVID EXTRA RULES ON BLOOD DONATION SAFETY \n ')
        chi=int(input('enter your choice'))
        if chi==1:
            print('Must be at least 16 years old (16- and 17-year-olds must bring a signed permission form from a parent or guardian, if required by state or school')
            print('Weigh at least 110 pounds. Certain height/weight criteria may apply for donors 22 years old or younger.')
            print('Be in good general health.')
            print('For your safety and to ensure a positive donation experience, make sure you eat within two hours ahead of your donation. Drink plenty of water that day and 24 to 48 hours beforehand. Feel free to help yourself to something to eat and drink in our refreshment area.')
            print('Bring your IDsomething with your name and one of the following: date of birth, donor ID number or your photo.')
            print('You must wait eight weeks between whole blood donations. Learn more about specific intervals for other types of donation.')
            print('You should not be under the influence of alcohol or recreational drugs at the time of donation.')
            print('Additional Requirements: Component-Specific Donation include that Platelet donors should avoid aspirin and/or aspirin-containing products 48 hours prior to donation and other anti-platelet medications')
            print('Updated Donation Eligibility Criteria')
            print('Health Conditions')
            print('Medications')
            print('HIV/AIDS Risk Behaviors')
            print('Tattoos, Piercings, Permanent Make-up & Acupuncture')
            print('European Travel/Residency Criteria')
            print('Travel to Malaria Risk Areas')
            print('Source Plasma')
        elif chi==2:
            print('''Due to COVID-19 (SARS-CoV-2 Coronavirus), we are requiring that people should not donate today ,if in the PAST 4 WEEKS:
                    You had symptoms from a lab-diagnosed or suspected COVID-19 infection and have not had a subsequently-negative nasopharyngeal swab test result
                    You have lived with or been in close contact with individuals diagnosed with or suspected of having COVID-19 infection
                    You are a health care worker who has been caring for a patient diagnosed with or suspected of having COVID-19 and have not consistently been able to use recommended personal protective equipment (face mask, gown and gloves)                    
                    Masks Required
                    All staff and donors are required to wear a mask or cloth face covering. One-way valve masks are not permitted.
                    COVID-19 Convalescent Plasma
                    Learn more about convalescent plasma to see if you are eligible to give this lifesaving donation to help COVID-19 patients. We encourage healthy donors who dont qualify to give convalescent plasma to continue scheduling whole blood, platelet and other donation type appointments to help patients in need''')
        
    except ma.Error as er:
        print(er)
        


        
def admin():
    try:
        a=int(input('enter admin password:'))
        con=connection()
        cur=con.cursor()
        cur.execute("select admin_pwd from adminpwd where name_admin='administrator'")
        passw=cur.fetchone()
        password=passw[0]
        ans='y'
        if a==password:
            while ans=='y':
                print('WELCOME ADMIN')
                print('REJUVENATE HOSPITALS')
                print('1.PATIENT MODULE')
                print('2.DOCTOR MODULE')
                print('3.WARDS MODULE')
                print('4.REJUVENATE BLOOD BANK MODULE')
                print('5.COVID MODULE')
                print('6.CHANGE YOUR PASSWORD')
                print('7.REJUVENATE PHARMACY')
                print('8.GENERATE BILL')
                choice=int(input('enter your choice'))
                
                
                if choice==1:
                    print("PATIENT'S MODULE")
                    print("1.NEW PATIENT")
                    print("2.PATIENTS RECORDS")
                    print("3.UPDATE PATIENTS RECORD")
                    print("4.DISCHARGE OF PATIENT")
                    x=int(input("Enter your choice:"))
                    if x==1:
                        a_display_ncpatients()
                        n=int(input("Enter the number of records you want to add: "))
                        for i in range(n):
                            a_insert_ncpatients()
                            print()
                        print("INSERTION SUCCESSFUL")
                    
                    elif x==2:
                        print("HERE IS THE LIST OF PATIENTS RECORDS:")
                        print()
                        a_display_ncpatients()
                        print()                      
                    
                    elif x==3:
                        a_display_ncpatients()
                        m=int(input("Enter the number of records you want to update:"))
                        for i in range (m):
                            a_update_ncpatients()
                        print(" UPDATION SUCCESSFUL")
                        a_display_ncpatients()
                    
                    else:
                        a_display_ncpatients()
                        p=int(input("Enter the number of records you want to delete:"))
                        for i in range(p):
                            a_delete_ncpatients()
                        print("DELETION SUCCESSFUL")
                        a_display_ncpatients()
                
                elif choice==2:
                    print('doctor module')
                    print("submodules")
                    print("1.ADD DOCTOR")
                    print("2.LIST OF DOCTORS")
                    print("3.UPDATE DOCTOR RECORD")
                    print("4.REMOVAL OF A DOCTOR RECORD")
                    print("5.APPOINTMENTS")
                    ch=int(input("enter your choice"))
                    if ch==1:
                        d_display_doctor()
                        n=int(input("Enter the number of records you want to add "))
                        for i in range(n):
                            d_insert_doctor()
                            print()
                        print("DOCTOR'S DETAIL ADDED SUCCESSFULLY!")
                    elif ch==2:
                        print("Here is the list of doctors:")
                        print()
                        d_display_doctor()
                        print()
                    elif ch==3:
                        d_display_doctor()
                        n=int(input("Enter the number of records you want to update:"))
                        for i in range(n):
                            d_update_doctor()
                        print("UPDATED SUCCESSFULLY!")
                        d_display_doctor()
                    elif ch==4:
                        d_display_doctor()
                        n=int(input("Enter the number of records you want to delete"))
                        for i in range(n):
                            d_delete_doctor()
                        print("DELETED SUCCESSFULLY!")
                        d_display_doctor()
                    else:
                        d_display_doctor()
                        print("1.Appointment Addition")
                        print("2.Appointment Display")
                        print("3.Appointment Deletion")
                        ch=int(input("Enter your choice:  "))
                        if ch==1:
                            n=int(input("Enter number of appointments"))
                            for i in range(n):
                                appointment_insertion()
                                print()
                            print("Appointment added successfully")
                
                            
                        elif ch==2:
                            print("The appointments are: ")
                            appointment_display_admin()
                            print()
                            
                        else:
                            op=input("Do you want to delete an appointment")
                            if op=='y':
                                appointment_deletion_admin()
                                print("Appointment deleted successfully!")
                            else:
                                print("***********")
                            
                            
                elif choice==3:                                    #ADD NEW WARD: INPUT. BUILDING ,TYPE: (icu [I65]ward, covid [COR35]isolation ward,
# general[7869],VIP[VIP448]),ROOM NO.,NUMBER OF BEDS, STATUS: OCCUPIED/FREE, ROOM RENT ROOM INFORMATION. INPUT ROOM NO. DISPLAY ABOVE .
# UPDATE WARD: INPUT ROOM NO.
                    print('3.wards module')
                    print('submodules')
                    print('1.ADD NEW WARD')
                    print('2.ROOM INFORMATION and AVAILABILITY')
                    print("3.UPDATE WARD")
                    choke=int(input('enter choice'))
                    #cur.execute('create table WARDS(building varchar(10),room_number int(10),number_of_beds int(10),status varchar(10),room_rent int(55))')
                    if choke==1:
                        a_display_wards()
                        print()
                        a_insert_wards()
                        print()
                        a_display_wards()
                    elif choke==2:
                        a_display_wards()
                        print()
                        
                    elif choke==3:
                        a_display_wards()
                        print()
                        a_update_wards()
                        print("Do You Want To update More Records")
                        c=input("Enter y to update further")
                        if c=='y':
                            a_update_wards()
                        else:
                            print("^_^")
                        a_display_wards()
                    
                elif choice==4:
                    print('4.REJUVENATE BLOOD BANK MODULE')
                    print('\N{Drop of Blood}'*20)
                    print('1.insert into blood donors')
                    print('2.change donor details')
                    print('3.delete donor')
                    print('4.update blood group details')
                    print('5.see the list of elligible donors of this day')
                    chuc=int(input('enter valid choice'))
                    ascb='y'
                    while ascb=='y':
                        if chuc==1:
                            bb_ins()
                        if chuc==2:
                            bb_upd()
                        if chuc==3:
                            bb_del()
                        if chuc==4:
                            bb_bg_upd()
                        elif chuc==5:
                            elli_don()
                        ascb=input('enter y to continue in bbms')
                            
                    
                elif choice==5:
                    print('5.COVID MODULE')
                    print('SUBMODULES')
                    print()
                    print('1.COVID PATIENTS')
                    choic=int(input('enter your choice'))
                    #cur.execute('create table COVID19_PATIENTS(patient_id int(20),age int(2),gender varchar(10),room int ,date)' )
                    #cur.execute("ALTER TABLE COVID19_PATIENTS ADD COLUMN name varchar(20) ")  
                    # ive commented as it has already been created
                    if choic==1:
                        print('1.current covid patients data\n2.add new patient\n3.delete recovered patient records\n4.update patient info\n 5.insertion-OUR COVID INITIATIVES\n6. OUR COVID INITIATIVES')
                        dep=int(input('enter choice'))
                        if dep==1:
                            a_display_covidpatients()
                        if dep==2:
                                a_display_covidpatients()
                                print( )
                                a_insert_covidpatients()
                        if dep==3:
                                a_display_covidpatients()
                                print( )
                                a_delete_covidpatients()
                                print("Do You Want To Delete More Records")
                                c=input("Enter y to delete further")
                                if c=='y':
                                    a_delete_covidpatients()
                                else:
                                    print("^_^")
                        if dep==4:
                            a_display_covidpatients()
                            print( )
                            print(a_update_covidpatients())
                            print("Do You Want To update More Records")
                            c=input("Enter y to update further")
                            if c=='y':
                                a_update_covidpatients()
                            else:
                                print("^_^")
                        if dep==5:
                            print('TO ADD NEW TEXT UNDER COVID 19 INITIATIVES')
                            cov_init()
                        if dep==6:
                            print('our COVID INITIATIVES')
                            cov_display_init()
                    
                if choice==6:
                    print('change password')
                    m=int(input('enter old password'))
                    if m==password:
                        new=int(input('enter new password'))
                        newr=int(input('confirm new admin password'))
                        if new==newr:
                            cur.execute("update adminpwd set admin_pwd=%d where name_admin='administrator'"%(new))
                            con.commit()
                            print(' password change was successful')
                            
                        else:
                            print('OOPS!confirmation failure')
                if choice==7:
                        print("WELCOME TO BIOHEAL PHARMACY")
                        print("MENU")
                        print("1.Show Stock")
                        print("2.Add medicine into stock")
                        print("3.Update medicine stock")
                        print("4.Delete medicine stock")
                        
                        ansg='y'
             
                        while ansg=='y':
                            choice=int(input("Enter your choice:"))
                            if choice==1:
                                pharm_show()
                            elif choice==2:
                                pharm_add()
                            elif choice==3:
                                pharm_update()
                            elif choice==4:
                                pharm_delete()
                            ansg=input("Enter y to continue in the pharmacy module:")
                elif choice==8:
                    def patients():
                        print("PATIENT BILL")
                        n=int(input("Please enter your patient id : "))
                        try:
                            con=connection()
                            cur=con.cursor() 
                            cur.execute("select * from patients where p_id=%d"%(n))
                            for i in cur.fetchall():
                                print(i)
                       
                            print("Please verify your details")
                            print("TYPE OF TREATMENT:")
                            print("1.CONSULTATION")
                            print("2.SURGERY")
                            
                            x=int(input("Enter your type of treatment:"))
                            if x==1:
                                print("CONSULTAION FEES:₹500")
                            elif x==2:
                                surgery()
                            
                        except ma.Error as er:
                            print(er)    
                            
                            
                    def surgery():
                            room=input("ENTER YOUR ROOM TYPE (GENERAL/VIP/COVID) : ")
                            if room=="general"or "GENERAL":
                               a=200#admission rate
                               b=2500#LAB TESTS TO BE INCLUDED ?bed charge
                               s=45000#surgeon charge
                               a_s=25000#asst. surgeon charge
                               tc=6000#Theatre charges
                               af=12000#Anathetist fees
                               sc=22164#Service charges
                               e=18400#Equipment charges
                            elif room=="VIP" or "vip":
                              a=200#admission rate
                              b=2500#LAB TESTS TO BE INCLUDED ?bed charge
                              s=45000#surgeon charge
                              a_s=25000#asst. surgeon charge
                              tc=6000#Theatre charges
                              af=12000#Anathetist fees
                              sc=22164#Service charges
                              e=18400#Equipment charges
                            else :
                              a=200#admission rate
                              b=2500#LAB TESTS TO BE INCLUDED ?bed charge
                              s=45000#surgeon charge
                              a_s=25000#asst. surgeon charge
                              tc=6000#Theatre charges
                              af=12000#Anathetist fees
                              sc=22164#Service charges
                              e=18400#Equipment charges
                              
                            n=input("ENTER THE BILL NO :") 
                            
                            try:
                            
                                con=connection()
                                cur=con.cursor()
                                  
                                cur.execute("create table bill"+n+" (SLNO int (2), SERVICES varchar(50) ,QTY int (20) ,RATE int(25) , AMOUNT int(50)) ;")
                                tat=1
                                eat=2
                                wat=3
                                cat=4
                                rat=5
                                sat=6
                                fat=7
                                kat=8
                                lat=9
                                yat=0
                                dog="ADMISSION_CHARGES"
                                fog="BED_CHARGES"
                                log="SURGEON_CHARGES"
                                gog="ASST_SURGEON_CHARGES"
                                kog="THEATRE_CHARGES"
                                sog="ANAESTHETIST_FEES "
                                tog="SERVICES"
                                aog="EQUIPMENT"
                                bog="TOTAL"
                                  
                                qb=int(input("ENTER THE NUMBER OF BEDS USED:"))
                                qt=int(input("ENTER THE NUMBER OF THEATERS USED :"))
                                qa=int(input("ENTER THE NUMBER OF ANAESTHESIA WAS GIVEN TO THE PATIENT:  "))
                                qe=int(input("ENTER THE NUMBER OF EQUIPMENTS USED: "))
                                cur.execute("insert into bill"+n+"(SLNO,SERVICES,QTY,RATE,AMOUNT)values(%d,'%s',%d,%d,%d)"%(tat,dog,tat,a,a))
                                con.commit()
                                cur.execute("insert into bill"+n+"(SLNO,SERVICES,QTY,RATE,AMOUNT)values(%d,'%s',%d,%d,%d)"%(eat,fog,qb,b,b*qb))
                                con.commit()
                                cur.execute("insert into bill"+n+" (SLNO,SERVICES,QTY,RATE,AMOUNT)values(%d,'%s',%d,%d,%d)"%(wat,log,tat,s,s))
                                con.commit()
                                cur.execute("insert into bill"+n+"(SLNO,SERVICES,QTY,RATE,AMOUNT)values(%d,'%s',%d,%d,%d)"%(cat,gog,tat,a_s,a_s))
                                con.commit()
                                cur.execute("insert into bill"+n+" (SLNO,SERVICES,QTY,RATE,AMOUNT)values(%d,'%s',%d,%d,%d)"%(rat,kog,qt,tc,tc*qt))
                                con.commit()
                                cur.execute("insert into bill"+n+"(SLNO,SERVICES,QTY,RATE,AMOUNT) values(%d,'%s',%d,%d,%d)"%(sat,sog,qa,af,af*qa))
                                con.commit()
                                cur.execute("insert into bill"+n+"(SLNO,SERVICES,QTY,RATE,AMOUNT) values(%d,'%s',%d,%d,%d)"%(fat,tog,tat,sc,sc))
                                con.commit()
                                cur.execute("insert into bill"+n+"(SLNO,SERVICES,QTY,RATE,AMOUNT) values(%d,'%s',%d,%d,%d)"%(kat,aog,qe,e,qe*e))
                                con.commit()
                                cur.execute("insert into bill"+n+"(SLNO,SERVICES,QTY,RATE,AMOUNT)values(%d,'%s',%d,%d,%d)"%(lat,bog,yat,yat,a+b*qb+s+a_s+tc*qt+af*qa+sc+qe*e))
                                con.commit()                      
                                print("data inserted successfully")                             
                            except ma.Error as er:
                                print(er)                   
                    def payment():
                        print("PAYMENT MODES:")
                        print("1.CREDIT CARD")
                        print("2.CASH")                
                    def final():
                        print("REJUVENATE HOSPITAL")
                        patients()
                        payment()
                
                    final()                                                           
                ans=input('enter y to continue')
        else:
            print('password incorrect')
        t='-------------------------------------------------------------------------------'
        return t
    except ma.Error as er:
      print(er)  
               
def totale():
    print('Welcome user ! \n REJUVENATE HOSPITALS \n HOSPITAL MANAGEMENT SYSTEM \n LEADERS IN HEALTHCARE ADMINISTRATION')
    print('-------------------------------------------------------------------')
    print('1.CONTINUE AS ADMIN\n 2.CONTINUE AS DOCTOR \n 3.COVID SPECIALITY UNIT \n ')
    fun=int(input('enter choice'))
    if fun==1:
        admin() 
    elif fun==2:
        doctor()
        print()
    elif fun==3:
        print('welcome user! COVID SPECIALITY UNIT\n JOIN US IN OUR BATTLE AGAINST THE NOVEL CORONAVIRUS')
        print('1.DAILY CASES')
        print('2.DAILY COVID DEATHS')
        print('3.DAILY RECOVERIES')
        print('4.TOTAL CASES IN OUR HOSPITAL')
        print('5.TOTAL DEATHS IN OUR HOSPITAL DUE TO COVID')
        print('6.TOTAL RECOVERIES IN OUR HOSPITAL')
        print('7.ANALYSE COVID DATA')
        print("8.SEE ALL COVID PATIENTS' DATA")
        print('9.OUR COVID INITIATIVES')
        print('10.AVERAGE CASES PER DAY')
        print('11.AVERAGE DEATHS PER DAY')
        print('12.AVERAGE RECOVERIES PER DAY')
        print('13.most cases')
        print('14.most deaths')
        print('15.most recoveries')
        print('16.least cases')
        print('17.least deaths')
        print('18.least recoveries')
        kree=int(input('enter choice'))
        if kree==1:
            print('DAILY COVID CASES')
            daily_cc()
        if kree==2:
            print('DAILY COVID DEATHS')
            daily_cd()
        if kree==3:
            print('DAILY COVID RECOVERIES')
            daily_cr()
        if kree==4:
            print('TOTAL CASES IN OUR HOSPITAL')
            total_cc()
        if kree==5:
            print('TOTAL DEATHS IN OUR HOSPITAL DUE TO COVID')
            total_cd()
        if kree==6:
            print('TOTAL RECOVERIES IN OUR HOSPITAL')
            total_cr()
        if kree==7:
            print('ANALYSE COVID DATA')
            analyse_covidata()
        if kree==8:
            print('DISPLAY COVID PATIENTS DATA')
            a_display_covidpatients()
        if kree==9:
            print('OUR COVID INITIATIVES!')
            cov_display_init()
        if kree==10:
            print('10.AVERAGE CASES PER DAY')
            avg_case()
        if kree==11:
            print('11.AVERAGE DEATHS PER DAY')
            avg_death()
        if kree==12:
            print('12.AVERAGE RECOVERIES PER DAY')
            avg_recoveries()
        if kree==13:
            most_cases()
        if kree==14:
            most_deaths()
        if kree==15:
            most_recoveries()
        if kree==16:
            least_cases()
        if kree==17:
            least_deaths()
        if kree==18:
            least_recoveries()
totale()
