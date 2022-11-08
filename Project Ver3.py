import mysql.connector
from tkinter import *
import random as r
import sys
t=Tk()
pwd=''
t.title("Start-Up Window")
t.geometry("370x270")
def destroy():
    t.destroy()
    exit()
    sys.exit()
t.resizable(0,0)
Label(t,text="Welcome to password manager!",font="arial 15 bold",fg='white',bg='cyan').place(x=10,y=0)
Label(t,text="This is the start-up screen",font="arial 15 bold",fg='white',bg='lime').place(x=10,y=40)
Label(t,text="Note- If program closes abruptly on this screen,\n that means password entered is incorrect",font="arial 10",fg='brown').place(x=10,y=170)
def getpass():
    global pwd
    pwd=x.get()
    t.destroy()
statement='Entry(t,textvariable=x,show="*").place(x=170,y=90)'
def pas():
    global statement
    if statement.find('show="*"')!=-1:
        statement='Entry(t,textvariable=x).place(x=170,y=90)'
        exec(statement)
        #print (statement)
    else:
        statement='Entry(t,textvariable=x,show="*").place(x=170,y=90)'
        exec(statement)
        #print (statement)

made_by="Made By: Devansh Arora"
Label(t,text="Enter MySQL password-").place(x=30,y=90)
x=StringVar()
Checkbutton(t,text="Show password" ,onvalue=1, offvalue=0, command=pas).place(x=200,y=110)
Entry(t,textvariable=x,show="*").place(x=170,y=90)
Button(t,text="Enter",border=5,fg="black",bg="orange",command=getpass).place(x=30,y=120)
Button(t,text="Exit",fg='black',bg='orange',command=destroy,border=5).place(x=90,y=120)
Label(t,text=made_by,fg='white',bg='Black').place(x=230,y=250)
t.mainloop()

mydb=mysql.connector.connect(host="localhost",user="root",password=pwd)
curs=mydb.cursor()
def generate():
    z=""
    l1=list("abcdefghijklmnopqrstuvwxyz")
    l2=list("1234567890")
    l3=list("?_@#$!%^&*~")
    r.shuffle(l1)        
    r.shuffle(l2)
    r.shuffle(l3)
    l=list(l1[0]+l1[1]+l1[2]+l1[3]+l1[4]+l2[0]+l2[1]+l2[2]+l3[0]+l3[1]+l3[2])
    r.shuffle(l)
    for h in range(len(l)):
            z+=str(l[h])
    return z

sql="create database if not exists project"
curs.execute(sql)
sql="use project"
curs.execute(sql)
sql="create table if not exists accounts(name varchar(30) primary key,c_pass varchar(20),s_pass varchar(20),str varchar(20))"
curs.execute(sql)

def strength(s):
    a,d,sp=0,0,0
    
    for i in s:
        if i.isalpha():
            a+=1
        elif i.isdigit():
            d+=1
        elif i.isspace():
            pass
        else:
            sp+=1

    if a>0 and d>0 and sp>0 and len(s)>=5 :
        return "Strong"
    elif a>0 and d>0 and sp==0 and len(s)>=8:
        return "Medium"
    elif len(s)<8:
        return "Very Weak"
    elif a>0 and d==0 and len(s)>=8:
        return "Ok-ish"
    elif d>0 and a==0 and len(s)>=8:
        return "Medium"
    elif a>0 and sp>0 and len(s)>=5 and d==0:
        return "Medium"
    elif d>0 and sp>0 and len(s)>=5 and a==0:
        return "Medium"

def write():
    l=[]
    t1=Toplevel()
    t1.title("Write Window")
    t1.geometry("250x270")
    t1.resizable(0,0)
    Label(t1,text="Username").place(x=10,y=50)
    Label(t1,text="Password").place(x=10,y=70)
    Label(t1,text=made_by,fg='white',bg='Black').place(x=110,y=250)
    user=StringVar()
    pas=StringVar()
    
    def values():
        a=user.get()
        b=pas.get()
        global l
        l = [a,b]
        #print(l)
        sql="select name from accounts"
        curs.execute(sql)
        r=curs.fetchall()
        if (l[0],) in r:
            global lab1
            lab1=Label(t1,text="Record with this Username already exists.",fg="red")
            lab1.place(x=20,y=200)
            #time.sleep(3)
            
        else :
            try:
                lab1.destroy()
            except NameError:
                pass
            d=strength(b)
            t=(l[0],l[1],c,d)
            sql="insert into accounts values{0}".format(t)
            curs.execute(sql)
            mydb.commit()
            Label(t1,text="Records Entered Succesfully",fg="blue").place(x=20,y=200)
            #t1.destroy()
    def w_again():
        values()
        t1.destroy()
        write()
    
    u_val=Entry(t1,textvariable=user)
    p_val=Entry(t1,textvariable=pas)
    u_val.place(x=90,y=50)
    p_val.place(x=90,y=70)
    Button(t1,text="Submit",bg="orange",fg="black",command=values,border=5).place(x=40,y=150)
    Button(t1,text="Exit",bg="Orange",fg="black",command=t1.destroy,border=5).place(x=100,y=150)
    Button(t1,text="Enter again",bg="Orange",fg="black",command=w_again,border=5).place(x=150,y=150)
    c=generate()
    Label(t1,text="Suggested password: ",font='comicsans 9').place(x=10,y=90)
    Label(t1,text=c,font='comicsans 9').place(x=140,y=90)
    
    
        
def disp():
    l=[]
    t1=Toplevel()
    t1.title("Display Records Window")
    t1.resizable(0,1)
    t1.geometry("500x500")
    for i in range(100):
        Label(t1).grid(row=i,column=i)
    Label(t1,text="Username",border=5,relief=SUNKEN,bg="Yellow").grid(row=0,column=0,ipadx=15)
    Label(t1,text="Current_Password",border=5,relief=SUNKEN,bg="Yellow").grid(row=0,column=1)
    Label(t1,text="Suggested_Password",border=5,relief=SUNKEN,bg="Yellow").grid(row=0,column=2)
    Label(t1,text="Strength_of_Current_Password",border=5,relief=SUNKEN,bg="Yellow").grid(row=0,column=3)
    
    
    sql="select * from accounts"
    curs.execute(sql)
    res=curs.fetchall()
    if res == []:
        print("Table is empty")
    else:
        r=1
        col=0
        for i in res:
            col=0
            for j in i:
                Label(t1,text=j,border=5).grid(row=r,column=col)
                col+=1

            r+=1
    
    x=Button(t1,text="Close Window",bg="Orange",fg="black",command=t1.destroy,border=5)
    x.grid(row=r+2,column=0)



def delete():
    a=''
    t1=Toplevel()
    t1.geometry("450x200")
    t1.resizable(False,False)
    t1.title("Delete Window")
    Label(t1,text=made_by,fg='white',bg='Black').place(x=310,y=180)
    def getval():
        global a
        a=dnamevar.get()
        sql="select name from accounts"
        curs.execute(sql)
        r=curs.fetchall()
        global lab1
        if (a,) not in r:
            lab1=Label(t1,text="No record with this Username exists.",fg="red")
            lab1.place(x=30,y=160)
        else:
            try:
                lab1.destroy()
            except NameError:
                pass
            sql="delete from accounts where name=\"{0}\"".format(a)
            curs.execute(sql)
            mydb.commit()
            Label(t1,text="Record Deleted Succesfuly!",fg="blue").place(x=30,y=160)
    
    def again():
        getval()
        t1.destroy()
        delete()
        
    Label(t1,text="Enter Username of the record to be deleted: ").place(x=10,y=50)
    dnamevar=StringVar()
    dname=Entry(t1,textvariable=dnamevar)
    dname.place(x=250,y=50)
    Button(t1,text="Submit",bg="Orange",fg="black",command=getval,border=5).place(x=50,y=100)
    Button(t1,text="Close",bg="Orange",fg="black",command=t1.destroy,border=5).place(x=110,y=100)
    Button(t1,text="Delete another record",bg="Orange",fg="black",command=again,border=5).place(x=160,y=100)
    
    
def search():
    a=''
    t1=Toplevel()
    t1.title("Search Window")
    t1.geometry("450x200")
    t1.resizable(False,False)
    Label(t1,text=made_by,fg='white',bg='Black').place(x=310,y=180)    
    def getval():
        global a
        a=dnamevar.get()
        sql="select name from accounts"
        curs.execute(sql)
        r=curs.fetchall()
        
        global lab1
        if (a,) not in r:
            lab1=Label(t1,text="No record with this Username exists.",fg="red")
            lab1.place(x=30,y=160)
        else:
            try:
                lab1.destroy()
            except NameError:
                pass
            t2=Toplevel()
            t2.resizable(0,0)
            t2.title("Searched Record details")
            t2.geometry("500x120")
            Label(t2,text=made_by,fg='white',bg='Black').place(x=360,y=100)
            for i in range(100):
                Label(t1).grid(row=i,column=i)
            Label(t2,text="Username",border=5,relief=SUNKEN,bg="Yellow").grid(row=0,column=0,ipadx=15)
            Label(t2,text="Current_Password",border=5,relief=SUNKEN,bg="Yellow").grid(row=0,column=1)
            Label(t2,text="Suggested_Password",border=5,relief=SUNKEN,bg="Yellow").grid(row=0,column=2)
            Label(t2,text="Strength_of_Current_Password",border=5,relief=SUNKEN,bg="Yellow").grid(row=0,column=3)
            
            sql="select * from accounts where name=\"{0}\"".format(a)
            curs.execute(sql)
            res=curs.fetchall()
            r=1
            col=0
            for i in res:
                col=0
                for j in i:
                    Label(t2,text=j,border=5).grid(row=r,column=col)
                    col+=1

                r+=1
            Button(t2,text="Close",bg="Orange",fg="black",command=t2.destroy,border=5).place(x=20,y=90)
    
        
    def again():
        t1.destroy()
        search()
        
    Label(t1,text="Enter Username of the record to be searched: ").place(x=10,y=50)
    dnamevar=StringVar()
    dname=Entry(t1,textvariable=dnamevar)
    dname.place(x=250,y=50)
    Button(t1,text="Submit",bg="Orange",fg="black",command=getval,border=5).place(x=50,y=100)
    Button(t1,text="Close",bg="Orange",fg="black",command=t1.destroy,border=5).place(x=110,y=100)
    Button(t1,text="Search another record",bg="Orange",fg="black",command=again,border=5).place(x=160,y=100)

def update():
    a=''
    t1=Toplevel()
    t1.title("Update Window")
    t1.geometry("450x250")
    t1.resizable(False,False)
    Label(t1,text=made_by,fg='white',bg='Black').place(x=310,y=230)

    def getval():
        global a
        avar=dnamevar.get()
        bvar=dpassvar.get()
        a=[avar,bvar]
        sql="select name from accounts"
        curs.execute(sql)
        r=curs.fetchall()
        global lab1
        if (a[0],) not in r:
            lab1=Label(t1,text="No record with this Username exists.",fg="red")
            lab1.place(x=30,y=190)
        else:
            try:
                lab1.destroy()
            except NameError:
                pass
            b=strength(a[1])
            sql="update accounts set c_pass=\"{0}\" where name=\"{1}\"".format(a[1],a[0])
            curs.execute(sql)
            sql="update accounts set str=\"{0}\" where name=\"{1}\"".format(b,a[0])
            curs.execute(sql)
            mydb.commit()
            Label(t1,text="Record Updated Succesfuly!",fg="blue").place(x=30,y=190)
    
    def again():
        getval()
        t1.destroy()
        update()
        
    Label(t1,text="Enter Username of the record to be updated: ").place(x=10,y=50)
    Label(t1,text="Enter new Password: ").place(x=10,y=80)
    dnamevar=StringVar()
    dpassvar=StringVar()
    dpass=Entry(t1,textvariable=dpassvar)
    dname=Entry(t1,textvariable=dnamevar)
    dname.place(x=250,y=50)
    dpass.place(x=150,y=80)
    Button(t1,text="Submit",bg="Orange",fg="black",command=getval,border=5).place(x=50,y=150)
    Button(t1,text="Close",bg="Orange",fg="black",command=t1.destroy,border=5).place(x=110,y=150)
    Button(t1,text="Update another record",bg="Orange",fg="black",command=again,border=5).place(x=160,y=150)



def new_suggest():
    a=generate()
    t1=Toplevel()
    t1.title("New suggestion window")
    t1.geometry("500x300")
    t1.resizable(0,0)
    Label(t1,text=made_by,fg='white',bg='Black').place(x=360,y=280)
    def yes():
        Label(t1,text="Enter Username to overwrite this password for:").place(x=20,y=140)
        x=StringVar()
        Entry(t1,textvariable=x).place(x=290,y=140)

        def getval():
            n=x.get()
            sql="select name from accounts"
            curs.execute(sql)
            r=curs.fetchall()
            global lab1
            if (n,) not in r:
                lab1=Label(t1,text="No record with this Username exists.",fg="red")
                lab1.place(x=30,y=220)
            else:
                try:
                    lab1.destroy()
                except NameError:
                    pass
                sql="update accounts set s_pass=\"{0}\" where name=\"{1}\"".format(a,n)
                curs.execute(sql)
                mydb.commit()
                Label(t1,text="Suggested password overwritten sucesfully for the given Username!",fg="blue").place(x=30,y=220)
            
        Button(t1,text="Submit",bg="Orange",fg="black",command=getval,border=5).place(x=50,y=170)
        Button(t1,text="Close",bg="Orange",fg="black",command=t1.destroy,border=5).place(x=110,y=170)
        Button(t1,text="Generate New password",bg="Orange",fg="black",command=again,border=5).place(x=160,y=170)

    def again():
        t1.destroy()
        new_suggest()
    
    Label(t1,text="A new suggested password generated randomly is: ",font="comicsans 10").place(x=30,y=50)
    Label(t1,text=a,font="comicsans 10 bold",fg="white",bg="green").place(x=330,y=50)
    Label(t1,text="Do You wish to overwrite old suggested password of a record with this one?",font="comicsans 10").place(x=30,y=80)
    Button(t1,text="Yes",bg="Orange",fg="black",command=yes,border=5).place(x=50,y=110)
    Button(t1,text="No",bg="Orange",fg="black",command=t1.destroy,border=5).place(x=90,y=110)
    Button(t1,text="Generate New password",bg="Orange",fg="black",command=again,border=5).place(x=130,y=110)


t=Tk()
t.resizable(0,0)
t.geometry("400x350")
Label(t,text=made_by,fg='white',bg='Black').place(x=260,y=330)
t.title("Password Manager Menu")
t.configure(bg="grey")
Label(t,text="Welcome to password manager!",font="arial 15 bold",fg='white',bg='cyan').place(x=30,y=0)
Label(t,text="Menu of options:-",font="arial 10 bold",fg='white',bg='orange').place(x=0,y=50)
yc=90
Button(t,text="Enter a new record.",fg='lime',bg='black',command=write).place(x=10,y=yc)
Button(t,text="Display records.",fg='lime',bg='black',command=disp).place(x=10,y=yc+30)
Button(t,text="Delete a Record.",fg='lime',bg='black',command=delete).place(x=10,y=yc+60)
Button(t,text="Search a record.",fg='lime',bg='black',command=search).place(x=10,y=yc+90)
Button(t,text="Update a record.",fg='lime',bg='black',command=update).place(x=10,y=yc+120)
Button(t,text="Suggest a new Random password.",fg='lime',bg='black',command=new_suggest).place(x=10,y=yc+150)
Button(t,text="Exit.",fg='lime',bg='black',command=destroy).place(x=10,y=yc+180)



t.mainloop()

mydb.close()
