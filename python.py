from tkinter import *
import tkinter as tk
import sqlite3
import sys

print("Imported")
con = sqlite3.connect("project.db")
print("Connected")

root = tk.Tk()
v = tk.IntVar()
v1 = tk.IntVar()
v2 = tk.IntVar()
v3 = tk.IntVar()

def createtable():
    create = ("CREATE TABLE IF NOT EXISTS vehicle(NAME VARCHAR(200),"+
               "CONTACT VARCHAR(200),"+
               "VEHICLE VARCHAR(100),"+
               "DATEOFBOOKING VARCHAR(100),"+
               "DURATION VARCHAR(100),"+
               "RENT VARCHAR(100))")
    con.execute(create)
    print("CREATED SUCCESSFULLY")

def insertt(aname, acon, aveh, adob, adur, arent):
    aname = aname.get()
    acon = acon.get()
    aveh = aveh.get()
    adob = adob.get()
    adur = adur.get()
    arent = arent.get()
    print(aname, acon, aveh, adob, adur, arent)
    print("Value is", aname)
    insert = str("INSERT INTO vehicle(NAME,CONTACT,VEHICLE,DATEOFBOOKING,DURATION,RENT)"+" VALUES(?,?,?,?,?,?)")
    con.execute(insert,(aname, acon, aveh, adob, adur, arent))
    con.commit()
    print("INSERTED SUCCESSFULLY")

def btnClickdis():
    winddis = tk.Toplevel(root)
    winddis.geometry('500x500+50+50')
    winddis.title("BOOKING RECORD")
    curs = con.cursor()
    query = 'SELECT * FROM vehicle' 
    curs.execute(query)

    Label(winddis, text="NAME", font=('arial',10,'bold')).grid(row=0, column=0)
    Label(winddis, text="CONTACT", font=('arial',10,'bold')).grid(row=0, column=1)
    Label(winddis, text="VEHICLE", font=('arial',10,'bold')).grid(row=0, column=2)
    Label(winddis, text="DATE OF BOOKING", font=('arial',10,'bold')).grid(row=0, column=3)
    Label(winddis, text="DURATION", font=('arial',10,'bold')).grid(row=0, column=4)
    Label(winddis, text="RENT", font=('arial',10,'bold')).grid(row=0, column=5)
    data=curs.fetchall()
    
    for i, row in enumerate(data) :
        Label(winddis, text=row[0]).grid(row=i+1, column=0)
        Label(winddis, text=row[1]).grid(row=i+1, column=1)
        Label(winddis, text=row[2]).grid(row=i+1, column=2)
        Label(winddis, text=row[3]).grid(row=i+1, column=3)
        Label(winddis, text=row[4]).grid(row=i+1, column=4)
        Label(winddis, text=row[5]).grid(row=i+1, column=5)

def searching(e):
    windsearch = tk.Toplevel(root,width=500,height=500)
    windsearch.title("SEARCH")
    windsearch.geometry('500x500+50+50')
    sname = e.get()
    
    print("Record of", sname, "is to be deleted")
    data = con.execute('SELECT NAME,CONTACT,VEHICLE,DATEOFBOOKING,DURATION,RENT FROM vehicle where NAME=?;', (sname,))

    for row in data:
        Label(windsearch, text=row[0], font=('Verdana',12,'bold')).grid(row=1, column=4)
        Label(windsearch, text=row[1], font=('Verdana',12,'bold')).grid(row=2, column=4)
        Label(windsearch, text=row[2], font=('Verdana',12,'bold')).grid(row=3, column=4)
        Label(windsearch, text=row[3], font=('Verdana',12,'bold')).grid(row=4, column=4)
        Label(windsearch, text=row[4], font=('Verdana',12,'bold')).grid(row=5, column=4)
        Label(windsearch, text=row[5], font=('Verdana',12,'bold')).grid(row=6, column=4)

    Label(windsearch, text="NAME", font=('Verdana',15,'bold')).grid(row=1, column=1)
    Label(windsearch, text="CONTACT", font=('Verdana',15,'bold')).grid(row=2, column=1)
    Label(windsearch, text="VEHICLE", font=('Verdana',15,'bold')).grid(row=3, column=1)
    Label(windsearch, text="DATE OF BOOKING", font=('Verdana',15,'bold')).grid(row=4, column=1)
    Label(windsearch, text="DURATION", font=('Verdana',15,'bold')).grid(row=5, column=1)
    Label(windsearch, text="RENT", font=('Verdana',15,'bold')).grid(row=6, column=1)

def delcnfrm(e):
    winddelcnfrm = tk.Toplevel(root)
    winddelcnfrm.geometry('250x250+50+50')
    winddelcnfrm.title("DELETE?")
    print(e)

    delname = e.get()
    print(delname)
    l = Label(winddelcnfrm,font=('timesnewroman',10,'bold'),text="CONFIRM?",fg="black").grid(columnspan=2)
    btndelete = Button(winddelcnfrm,fg="black",font=('arial',10,'bold'),text="YES",command=lambda:deleterec(delname),relief="raise",width=10,height=3,bg="cyan").grid(row=2,column=0)
    btndelete = Button(winddelcnfrm,fg="black",font=('arial',10,'bold'),text="NO",command=btnClickdel,relief="raise",width=10,height=3,bg="cyan").grid(row=2,column=1)
  
def deleterec(delname):
    con.execute("DELETE from vehicle where NAME=?;",(delname,))
    con.commit()
    print("DELETED SUCCESSFULLY")

def btnLogin():
    pass

def btnClickdel():
    winddel = tk.Toplevel(root)
    winddel.geometry('700x500+50+50')
    winddel.title("DELETE A RECORD")
    l = Label(winddel,font=('timesnewroman',10,'bold'),text="Enter the name whose vehicle booking details you want to delete.",fg="black").grid(row=0,column=0)
    e = Entry(winddel,font=(20),bd=6)
    e.place(x=75,y=75)
    Button(winddel,text="DELETE",font=(20),bg="aquamarine",relief="raise",command=lambda:delcnfrm(e),width=10,height=1).place(x=150,y=150)

def btnClickLoginRegister():
    windlgrg = tk.Toplevel(root)
    windlgrg.geometry('500x500+500+150')
    windlgrg.title("LOGIN OR REGISTER")
    Button(windlgrg, text="LOGIN", width=25, height=2, command=btnLogin, bg="gold", bd=7, relief="raise", font=(30)).place(x=110,y=100)
    Button(windlgrg, text="REGISTER", width=25, height=2, command=btnRegister, bg="gold", bd=7, relief="raise", font=(30)).place(x=110,y=230)
  
    
    
def buttonClickA():
    winda = tk.Toplevel(root, width=500, height=500)
    winda.geometry('1000x1000+50+50')
    winda.title("I'M ADMIN")
    l = tk.Label(winda, text="CHOOSE YOUR OPTION :", font=('Verdana',15,'bold')).place(x=350,y=50)
    Button(winda, text="VIEW THE BOOKINGS!", width=40, height=3, command=btnClickdis, bg="gold", bd=7, relief="raise", font=(30)).place(x=350,y=100)
    Button(winda, text="SEARCH A RECORD!", width=40, height=3, command=buttonClick, bg="gold", bd=7, relief="raise", font=(30)).place(x=350,y=230)
    Button(winda, text="DELETE A RECORD!", width=40, height=3, command=btnClickdel, bg="gold", bd=7, relief="raise", font=(30)).place(x=350,y=360)
    
def buttonClickB():
    windb = tk.Toplevel(root)
    windb.geometry('1000x1000+50+50')
    windb.title("I'M CUSTOMER")
    l = tk.Label(windb, text="CHOOSE YOUR OPTION :", font=('Verdana',15,'bold')).place(x=350,y=100)
    Button(windb, text="BOOK A VEHICLE!", width=40, height=3, command=buttonClick1, bg="maroon1", bd=7, relief="raise", font=(30)).place(x=350,y=150)
    Button(windb, text="SEARCH YOUR RECORD!", width=40, height=3, command=buttonClick, bg="maroon1", bd=7, relief="raise", font=(30)).place(x=350,y=280)
    Button(windb, text="GIVE YOUR REVIEWS!", width=40, height=3, command=buttonClick2, bg="maroon1", bd=7, relief="raise", font=(30)).place(x=350,y=410)
    
def buttonClick():
    winds = tk.Toplevel(root,width=500,height=500)
    winds.title("SEARCH WINDOW")
    winds.geometry('1000x700+50+50')
    l = tk.Label(winds, font=('timesnewroman',10,'bold'), text="Enter the name whose vehicle booking details you are looking for!", fg="black").place(x=100,y=75)
    e= Entry(winds, font=(20), bd=6)
    e.place(x=100, y=125)
    Button(winds, text="SEARCH", font=(20), bg="tomato", relief="raise", command=lambda:searching(e)).place(x=450,y=200)
    
def btnRegister():
    windc = tk.Toplevel(root)
    windc.geometry('1200x800+50+50')
    windc.title("PERSONAL DETAILS")

    pd = tk.Label(windc, text="PERSONAL DETAILS", font=('arial',40,'bold'), bd=6, fg="magenta2", anchor='center').grid(row=0, column=1, columnspan=4, pady=5)
    l1 = tk.Label(windc, text="NAME:", font=(20)).grid(row=1, column=0, pady=5)
    l2 = tk.Label(windc, text="CONTACT_NO:", font=(20)).grid(row=2, column=0, pady=5)
    l3 = tk.Label(windc, text="ADDRESS:", font=(20)).grid(row=3, column=0, pady=5)
    l4 = tk.Label(windc, text="EMAIL_ID:", font=(20)).grid(row=4, column=0, pady=5)
    l5 = tk.Label(windc, text="GENDER:", font=(20)).grid(row=5, column=0, pady=5)

    Button(windc, text="REGISTER", font=(20), command=btnClickLoginRegister, bg="yellow", relief="raise").grid(row=7, column=1, rowspan=2)
    aname = Entry(windc, width=80, font=(20), bd=6)
    aname.place(x=150, y=90)
    acon = Entry(windc, width=80, font=(20), bd=6)
    acon.place(x=150, y=125)
    e3 = Text(windc, font=(20), height=5, bd=6).grid(row=3, column=1, pady=5)
    e4 = Text(windc, font=(20), height=0, bd=6).grid(row=4, column=1, pady=5)

    tk.Radiobutton(windc, text="Male", variable=v, value=1, font=(20)).grid(row=5, column=1, sticky=W)
    tk.Radiobutton(windc, text="Female", variable=v, value=2, font=(20)).grid(row=6, column=1, sticky=W)
    
def buttonClick2():
    windr = tk.Toplevel(root)
    windr.geometry('1000x1000+50+50')
    windr.title("REVIEW")

    re = tk.Label(windr, text="WELCOME TO THE REVIEW SECTION", font=('arial',40,'bold'), bd=6, fg="magenta2", anchor='center').place(x=30,y=5)
    l = tk.Label(windr, text="Your Name here.", font=('System',15)).place(x=30,y=80)
    l1 = tk.Label(windr, text="Give your reviews here.", font=('System',15)).place(x=30,y=125)
    l2 = tk.Label(windr, text="If you have any complaints regarding our rental agency ,enter them here.", font=('System',15)).place(x=30,y=250)
    l3 = tk.Label(windr, text="Enter your suggestions ,if any.", font=('System',15)).place(x=30,y=375)

    e = Text(windr, height=0, width=60, font=(20), bd=6).place(x=200,y=80)
    e1 = Text(windr, height=2, font=(20), bd=6).place(x=30,y=175)
    e2 = Text(windr, height=2, font=(20), bd=6).place(x=30,y=300)
    e3 = Text(windr, height=2, font=(20), bd=6).place(x=30,y=425)
    Button(windr, text="DONE", font=(20), bg="yellow", relief="raise").place(x=425,y=500)
 
def buttonClick3(aname,acon):
    windn = tk.Toplevel(root)
    windn.geometry('1200x700+50+50')
    windn.title("VEHICLE BOOKING DETAILS")
    vd = tk.Label(windn, text="VEHICLE BOOKING DETAILS", font=('arial',40,'bold'), bd=6, fg="magenta2", anchor='center').place(x=200,y=5)
    Button(windn, text="VEHICLES FOR RENT", font=(20), command=buttonClick4, bg="orange", relief="raise").place(x=250,y=75)
    Button(windn, text="VIEW RATES", font=(20), command=buttonClick5, bg="orange", relief="raise").place(x=700,y=75)

    l6 = tk.Label(windn ,text="ENTER THE NAME OF THE VEHICLE YOU WANT ON RENT :", font=(20)).place(x=30,y=125)
    la = tk.Label(windn, text="* BIKE",font=(20)).place(x=850,y=125)
    lb = tk.Label(windn, text="* CAR",font=(20)).place(x=850,y=150)
    lc = tk.Label(windn, text="* JEEP",font=(20)).place(x=850,y=175)
    ld = tk.Label(windn, text="* BUS",font=(20)).place(x=850,y=200)
    le = tk.Label(windn, text="* TRUCK",font=(20)).place(x=850,y=225)
    l7 = tk.Label(windn, text="DATE OF BOOKING:",font=(20)).place(x=30,y=300)
    l8 = tk.Label(windn, text="DURATION:",font=(20)).place(x=30,y=350)
    l9 = tk.Label(windn, text="RENT A DRIVER?",font=(20)).place(x=30,y=400)

    Button(windn, text="NEXT", font=(20), command=lambda:buttonClick6(aname, acon, aveh, adob, adur), bg="orange", relief="raise").place(x=515,y=570)
    aveh = Entry(windn, width=80, font=(20), bd=6)
    aveh.place(x=30, y=250)
    adob = Entry(windn, width=80, font=(20), bd=6)
    adob.place(x=225, y=300)
    adur = Entry(windn, width=80, font=(20), bd=6)
    adur.place(x=225, y=350)
    tk.Radiobutton(windn, text="Yes", variable=v2, value=1, font=(20)).place(x=225,y=400)
    tk.Radiobutton(windn, text="No", variable=v2, value=2, font=(20)).place(x=225,y=450)

def buttonClick4():
    windv = tk.Toplevel(root)
    windv.geometry('700x500+50+50')
    windv.title("VEHICLES FOR RENT")

    l = tk.Label(windv, text="THE VEHICLES WHICH ARE AVAILABLE FOR RENT WITH US ARE:", font=(20)).grid()
    l1 = tk.Label(windv, text="BIKES", font=(20)).grid()
    l2 = tk.Label(windv, text="CARS ", font=(20)).grid()
    l3 = tk.Label(windv, text="JEEPS", font=(20)).grid()
    l4 = tk.Label(windv, text="BUSES", font=(20)).grid()
    l5 = tk.Label(windv, text="TRUCKS", font=(20)).grid()
    
def buttonClick5():
    windr = tk.Toplevel(root)
    windr.geometry('500x500+50+50')
    windr.title("RENTS OF VEHICLES")

    l1 = tk.Label(windr, text="RENT OF BIKE IS RS. 300/DAY", font=(20)).grid()
    l2 = tk.Label(windr, text="RENT OF CAR IS RS. 1500/DAY", font=(20)).grid()
    l3 = tk.Label(windr, text="RENT OF JEEP IS RS. 2000/DAY", font=(20)).grid()
    l4 = tk.Label(windr, text="RENT OF BUS IS RS. 9000/DAY", font=(20)).grid()
    l5 = tk.Label(windr, text="RENT OF TRUCK IS RS. 10000/DAY", font=(20)).grid()

def buttonClick6(aname, acon, aveh, adob, adur):
    windp = tk.Toplevel(root)
    windp.geometry('1200x700+50+50')
    windp.title("PAYMENT DETAILS")
    pay = tk.Label(windp, text="PAYMENT DETAILS", font=('arial',40,'bold'), bd=6, fg="magenta2", anchor='center').place(x=300,y=5)
    l1 = tk.Label(windp, text="TOTAL RENT:", font=(20)).place(x=30,y=100)
    l = tk.Label(windp, text="Enter the rent as per the vehicle chosen and the number of days for which the vehcile is rented", font=(15)).place(x=225,y=140)
    arent = Entry(windp, font=(20),bd=6)
    arent.place(x=200, y=100)

    l2 = tk.Label(windp, text="PAYMENT VIA:", font=(20)).place(x=30,y=175)
    l3 = tk.Label(windp, text="*IN CASE OF ANY DAMAGE DONE TO THE VEHICLE,DAMAGE FINE WILL BE CHARGED.", font=('Verdana',15,'bold'), fg="firebrick1").place(x=30,y=275)
    l4 = tk.Label(windp, text="Damage amount is 50% of the rent!!!", font=('Verdana',15,'bold'), fg="firebrick1").place(x=30,y=300)
    l5 = tk.Label(windp, text="*IF VEHICLE IS NOT RETURNED BACK ON TIME,LATE FINE WILL BE CHARGED.", font=('Verdana',15,'bold'), fg="firebrick1").place(x=30,y=350)
    l6 = tk.Label(windp, text="The late fine is 25% of the rent(if late by a day)!!!", font=('Verdana',15,'bold'), fg="firebrick1").place(x=30,y=375)
    tk.Radiobutton(windp, text="Credit Card", variable=v3, value=1, font=(20)).place(x=200,y=175)
    tk.Radiobutton(windp, text="Cash", variable=v3, value=2, font=(20)).place(x=200,y=225)
    ok = Button(windp, text="SUBMIT", font=('arial',20,'bold'), fg="black", bg="cyan2", relief="raise", command=lambda:insertt(aname, acon, aveh, adob, adur, arent)).place(x=525,y=500)
    
createtable()
root.title('Vehicle Rental Agency')
root.geometry('1350x700+100+50')
root.config(bg="sky blue")

backgrnd = Frame(root, width=1600, height=300, relief="raise", bg="sky blue")
backgrnd.pack(side = TOP)

backgrnd1 = Frame(root, width=1600, height=400, relief="raise", bg="sky blue")
backgrnd1.pack(side = TOP)

label1 = Label(backgrnd, font=('times',35,'bold'), text="***VEHICLE RENTAL AGENCY***", fg='black', bd=10, bg="plum1").grid()

Button(backgrnd1, text="ADMIN", width=40, height=3, command=buttonClickA, bg="blue", bd=7, relief="raise", font=(30)).place(x=450,y=150)
Button(backgrnd1, text="CUSTOMER", width=40, height=3, command=btnClickLoginRegister, bg="blue", bd=7, relief="raise", font=(30)).place(x=450,y=280)

root.mainloop()
