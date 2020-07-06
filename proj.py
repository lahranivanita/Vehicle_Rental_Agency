from tkinter import *
import tkinter as tk
import sqlite3
import sys
from tkinter import messagebox
from datetime import date

print("Imported")
con = sqlite3.connect("pyproject.db", isolation_level=None)
print("Connected")

root1 = Tk()
v = IntVar()
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()

def createTable():
    createUsers = "CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(25), contact_no VARCHAR(10), address VARCHAR(100), email_id VARCHAR(25), username VARCHAR(15), password VARCHAR(10), gender VARCHAR(25))"
    con.execute(createUsers)
    
    createVehicles = "CREATE TABLE IF NOT EXISTS vehicles(vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT, vehicle_name VARCHAR(25), rent INTEGER, quantity INTEGER)"
    con.execute(createVehicles)

    createUVMap = "CREATE TABLE IF NOT EXISTS user_vehicle(user_id INTEGER, vehicle_id INTEGER, date_of_booking TEXT, no_of_days INTEGER, PRIMARY KEY (user_id, vehicle_id))"
    con.execute(createUVMap)
    
    print("CREATED SUCCESFULLY")

def vehicles():
    insert = "INSERT INTO vehicles(vehicle_name, rent, quantity) VALUES ('Bike', 300, 10)"
    con.execute(insert)

    insert = "INSERT INTO vehicles(vehicle_name, rent, quantity) VALUES ('Car', 1500, 10)"
    con.execute(insert)

    insert = "INSERT INTO vehicles(vehicle_name, rent, quantity) VALUES ('Jeep', 2000, 10)"
    con.execute(insert)

    insert = "INSERT INTO vehicles(vehicle_name, rent, quantity) VALUES ('Bus', 9000, 10)"
    con.execute(insert)

    insert = "INSERT INTO vehicles(vehicle_name, rent, quantity) VALUES ('Truck', 10000, 10)"
    con.execute(insert)

def insertVehicle(vid, uid, dob, adur):
    adob =  date.today()
    
    print(vid, uid, adob, adur)
    #print("Value is", aname)
    try:
        insert = str("INSERT INTO user_vehicle" + " VALUES(?,?,?,?)")
        con.execute(insert,(uid, vid, adob, adur))
        print("INSERTED SUCCESSFULLY")
        messagebox.showinfo("Booking", "Booking successful")
        con.execute("UPDATE vehicles SET quantity=quantity-1 WHERE vehicle_id=?;", (vid,))
        #con.commit()
    except sqlite3.Error as error:
        print("Booking failed", error)
        

def btnVehicles(w):
    #w.destroy()
    windV = tk.Toplevel(root,width=500,height=500)
    windV.title("VEHICLES")
    windV.geometry('1000x700+250+50')
    windV.resizable(0,0)
    windV.configure(bg="cornflowerblue")
    
    #print("Record of", sname, "is to be searched")
    data = con.execute('Select * from vehicles')

    Label(windV, text="VEHICLE NAME", font=('arial',10,'bold')).grid(row=0,column=2,padx=30,pady=17)
    Label(windV, text="PER DAY RENT", font=('arial',10,'bold')).grid(row=0,column=3,padx=30,pady=17)
    Label(windV, text="QUANTITY AVAILABLE", font=('arial',10,'bold')).grid(row=0,column=4,padx=30,pady=17)
    
    #root.grid_columnconfigure((0,1,2,3,4,5), weight=1)

    for i, row in enumerate(data) :
        Label(windV, text=row[1]).grid(row=i+1, column=2,padx=30,pady=17)
        Label(windV, text=row[2]).grid(row=i+1, column=3,padx=30,pady=17)
        Label(windV, text=row[3]).grid(row=i+1, column=4,padx=30,pady=17)

def btnUsers(w):
    #w.destroy()
    windU = tk.Toplevel(root,width=500,height=500)
    windU.title("USERS")
    windU.geometry('1000x700+250+50')
    windU.resizable(0,0)
    windU.configure(bg="cornflowerblue")
    
    #print("Record of", sname, "is to be searched")
    data = con.execute('Select user_id,name,contact_no,email_id,gender from users')

    Label(windU, text="USER_ID", font=('arial',10,'bold')).grid(row=0,column=3,padx=30,pady=17)
    Label(windU, text="NAME", font=('arial',10,'bold')).grid(row=0,column=4,padx=30,pady=17)
    Label(windU, text="CONTACT_NO", font=('arial',10,'bold')).grid(row=0,column=5,padx=30,pady=17)
    Label(windU, text="EMAIL_ID", font=('arial',10,'bold')).grid(row=0,column=6,padx=30,pady=17)
    Label(windU, text="GENDER", font=('arial',10,'bold')).grid(row=0,column=7,padx=30,pady=17)
    
    #root.grid_columnconfigure((0,1,2,3,4,5), weight=1)

    for i, row in enumerate(data) :
        Label(windU, text=row[0]).grid(row=i+1, column=3,padx=30,pady=17)
        Label(windU, text=row[1]).grid(row=i+1, column=4,padx=30,pady=17)
        Label(windU, text=row[2]).grid(row=i+1, column=5,padx=30,pady=17)
        Label(windU, text=row[3]).grid(row=i+1, column=6,padx=30,pady=17)
        Label(windU, text=row[4]).grid(row=i+1, column=7,padx=30,pady=17)

def btnCustomer():
    root.withdraw()
    windowCustomer = tk.Toplevel(root)
    windowCustomer.geometry('1000x700+250+50')
    windowCustomer.title("LOGIN OR REGISTER")
    windowCustomer.configure(bg="cornflowerblue")

    Label(windowCustomer, text="LOGIN OR REGISTER:", font=('Verdana',15,'bold')).pack(pady=50)
    Button(windowCustomer, text="LOGIN", width=40, height=3, command=lambda : btnLogin(windowCustomer), bg="powder blue", bd=7, relief="raise", font=(40)).pack(pady=25)
    Button(windowCustomer, text="REGISTER", width=40, height=3, command=lambda : btnRegister(windowCustomer), bg="powder blue", bd=7, relief="raise", font=(40)).pack(pady=25)
    
def btnAdmin(window, un, pw):
    if un == 'vani1234' and pw == 'vani1234':
        window.destroy()
        windowAdmin = Toplevel(root, width=500, height=500)
        windowAdmin.geometry('1000x700+250+50')
        windowAdmin.title("I'M ADMIN")
        windowAdmin.configure(bg="cornflowerblue")
        
        Label(windowAdmin, text="CHOOSE YOUR OPTION :", font=('Verdana',15,'bold')).pack(pady=25)
        Button(windowAdmin, text="VIEW THE BOOKINGS!", width=40, height=3, command=lambda : btnViewBookings(windowAdmin), bg="powder blue", bd=7, relief="raise", font=(40)).pack(pady=20)
        Button(windowAdmin, text="SEARCH A RECORD!", width=40, height=3, command=lambda : btnSearchRecord(windowAdmin), bg="powder blue", bd=7, relief="raise", font=(40)).pack(pady=20)
        Button(windowAdmin, text="DELETE A RECORD!", width=40, height=3, command=lambda : btnDeleteRecord(windowAdmin), bg="powder blue", bd=7, relief="raise", font=(40)).pack(pady=20)
        Button(windowAdmin, text="VIEW ALL USERS!", width=40, height=3, command=lambda : btnUsers(windowAdmin), bg="powder blue", bd=7, relief="raise", font=(40)).pack(pady=20)
        Button(windowAdmin, text="VIEW AVAILABLE VEHICLES!", width=40, height=3, command=lambda : btnVehicles(windowAdmin), bg="powder blue", bd=7, relief="raise", font=(40)).pack(pady=20)
    else:
        messagebox.showerror("Error", "Login failed")

    #return windowAdmin

def btnViewBookings(windowAdmin):
    #windowAdmin.destroy()
    windowViewBookings = tk.Toplevel(root)
    windowViewBookings.resizable(0,0)
    windowViewBookings.geometry('1000x700+250+50')
    windowViewBookings.title("VIEW BOOKINGS")
    windowViewBookings.configure(bg="cornflowerblue")

    curs = con.cursor()
    query = 'SELECT user_id, vehicle_id, name, contact_no, vehicle_name, date_of_booking, no_of_days, (no_of_days*rent) AS rent FROM users NATURAL JOIN user_vehicle NATURAL JOIN vehicles' 
    curs.execute(query)
    
    Label(windowViewBookings, text="USER_ID", font=('arial',10,'bold')).grid(row=0,column=0,padx=20,pady=17)
    Label(windowViewBookings, text="NAME", font=('arial',10,'bold')).grid(row=0,column=1,padx=20,pady=17)
    Label(windowViewBookings, text="VEHICLE_ID", font=('arial',10,'bold')).grid(row=0,column=2,padx=20,pady=17)
    Label(windowViewBookings, text="VEHICLE", font=('arial',10,'bold')).grid(row=0,column=3,padx=20,pady=17)
    Label(windowViewBookings, text="CONTACT_NO", font=('arial',10,'bold')).grid(row=0,column=4,padx=20,pady=17)
    Label(windowViewBookings, text="DATE OF BOOKING", font=('arial',10,'bold')).grid(row=0,column=5,padx=20,pady=17)
    Label(windowViewBookings, text="DURATION IN DAYS", font=('arial',10,'bold')).grid(row=0,column=6,padx=20,pady=17)
    Label(windowViewBookings, text="RENT", font=('arial',10,'bold')).grid(row=0,column=7,padx=20,pady=17)
    #root.grid_columnconfigure((0,1,2,3,4,5), weight=1)

    data = curs.fetchall()
    
    for i, row in enumerate(data) :
        Label(windowViewBookings, text=row[0]).grid(row=i+1, column=0,padx=20,pady=17)
        Label(windowViewBookings, text=row[2]).grid(row=i+1, column=1,padx=20,pady=17)
        Label(windowViewBookings, text=row[1]).grid(row=i+1, column=2,padx=20,pady=17)
        Label(windowViewBookings, text=row[4]).grid(row=i+1, column=3,padx=20,pady=17)
        Label(windowViewBookings, text=row[3]).grid(row=i+1, column=4,padx=20,pady=17)
        Label(windowViewBookings, text=row[5]).grid(row=i+1, column=5,padx=20,pady=17)
        Label(windowViewBookings, text=row[6]).grid(row=i+1, column=6,padx=20,pady=17)
        Label(windowViewBookings, text=row[7]).grid(row=i+1, column=7,padx=20,pady=17)
    
        
def searchUser(uid):
    windsearch = tk.Toplevel(root,width=500,height=500)
    windsearch.title("SEARCH")
    windsearch.geometry('1000x700+250+50')
    windsearch.resizable(0,0)
    windsearch.configure(bg="cornflowerblue")
    
    #print("Record of", sname, "is to be searched")
    data = con.execute('SELECT name, contact_no, address, email_id, vehicle_name, date_of_booking, no_of_days, (no_of_days*rent) AS rent FROM users NATURAL JOIN user_vehicle NATURAL JOIN vehicles where user_id=?;', (uid,))


    Label(windsearch, text="NAME", font=('arial',10,'bold')).grid(row=0,column=0,padx=20,pady=17)
    Label(windsearch, text="CONTACT NO.", font=('arial',10,'bold')).grid(row=0,column=1,padx=20,pady=17)
    Label(windsearch, text="ADDRESS", font=('arial',10,'bold')).grid(row=0,column=2,padx=20,pady=17)
    Label(windsearch, text="EMAIL ID", font=('arial',10,'bold')).grid(row=0,column=3,padx=20,pady=17)
    Label(windsearch, text="VEHICLE", font=('arial',10,'bold')).grid(row=0,column=4,padx=20,pady=17)
    Label(windsearch, text="DATE OF BOOKING", font=('arial',10,'bold')).grid(row=0,column=5,padx=20,pady=17)
    Label(windsearch, text="DURATION IN DAYS", font=('arial',10,'bold')).grid(row=0,column=6,padx=20,pady=17)
    Label(windsearch, text="RENT", font=('arial',10,'bold')).grid(row=0,column=7,padx=20,pady=17)
    #root.grid_columnconfigure((0,1,2,3,4,5), weight=1)

    
    
    for i, row in enumerate(data) :
        Label(windsearch, text=row[0]).grid(row=i+1, column=0,padx=20,pady=17)
        Label(windsearch, text=row[1]).grid(row=i+1, column=1,padx=20,pady=17)
        Label(windsearch, text=row[2]).grid(row=i+1, column=2,padx=20,pady=17)
        Label(windsearch, text=row[3]).grid(row=i+1, column=3,padx=20,pady=17)
        Label(windsearch, text=row[4]).grid(row=i+1, column=4,padx=20,pady=17)
        Label(windsearch, text=row[5]).grid(row=i+1, column=5,padx=20,pady=17)
        Label(windsearch, text=row[6]).grid(row=i+1, column=6,padx=20,pady=17)
        Label(windsearch, text=row[7]).grid(row=i+1, column=7,padx=20,pady=17)

        
def btnSearchRecord(prevWindow):
    #prevWindow.destroy()
    windowSearchRecord = Toplevel(root,width=500,height=500)
    windowSearchRecord.title("SEARCH A RECORD")
    windowSearchRecord.geometry('1000x700+250+50')
    windowSearchRecord.configure(bg="cornflowerblue")

    Label(windowSearchRecord, font=('Verdana',15,'bold'), text="Enter the name of the person whose vehicle booking details you are looking for!").pack(pady=50)
    e = Entry(windowSearchRecord, font=(20), bd=7, width=50)
    e.pack(pady=10)
    Button(windowSearchRecord, text="SEARCH",width=40, height=3,  font=(40), bd=7, bg="powder blue", relief="raise", command=lambda : searching(windowSearchRecord,e.get())).pack(pady=25)
    
def searching(windowSearchRecord, cname):
    windowSearchRecord.destroy()
    windsearch = tk.Toplevel(root,width=500,height=500)
    windsearch.title("SEARCH")
    windsearch.geometry('1000x700+250+50')
    windsearch.resizable(0,0)
    windsearch.configure(bg="cornflowerblue")
    
    
    #print("Record of", sname, "is to be searched")
    data = con.execute('SELECT name, contact_no, address, email_id, vehicle_name, date_of_booking, no_of_days, (no_of_days*rent) AS rent FROM users NATURAL JOIN user_vehicle NATURAL JOIN vehicles where name=?;', (cname,))


    Label(windsearch, text="NAME", font=('arial',10,'bold')).grid(row=0,column=0,padx=20,pady=17)
    Label(windsearch, text="CONTACT NO.", font=('arial',10,'bold')).grid(row=0,column=1,padx=20,pady=17)
    Label(windsearch, text="ADDRESS", font=('arial',10,'bold')).grid(row=0,column=2,padx=20,pady=17)
    Label(windsearch, text="EMAIL ID", font=('arial',10,'bold')).grid(row=0,column=3,padx=20,pady=17)
    Label(windsearch, text="VEHICLE", font=('arial',10,'bold')).grid(row=0,column=4,padx=20,pady=17)
    Label(windsearch, text="DATE OF BOOKING", font=('arial',10,'bold')).grid(row=0,column=5,padx=20,pady=17)
    Label(windsearch, text="DURATION IN DAYS", font=('arial',10,'bold')).grid(row=0,column=6,padx=20,pady=17)
    Label(windsearch, text="RENT", font=('arial',10,'bold')).grid(row=0,column=7,padx=20,pady=17)
    #root.grid_columnconfigure((0,1,2,3,4,5), weight=1)

    
    
    for i, row in enumerate(data) :
        Label(windsearch, text=row[0]).grid(row=i+1, column=0,padx=20,pady=17)
        Label(windsearch, text=row[1]).grid(row=i+1, column=1,padx=20,pady=17)
        Label(windsearch, text=row[2]).grid(row=i+1, column=2,padx=20,pady=17)
        Label(windsearch, text=row[3]).grid(row=i+1, column=3,padx=20,pady=17)
        Label(windsearch, text=row[4]).grid(row=i+1, column=4,padx=20,pady=17)
        Label(windsearch, text=row[5]).grid(row=i+1, column=5,padx=20,pady=17)
        Label(windsearch, text=row[6]).grid(row=i+1, column=6,padx=20,pady=17)
        Label(windsearch, text=row[7]).grid(row=i+1, column=7,padx=20,pady=17)

    
def btnDeleteRecord(windowAdmin):
    #windowAdmin.destroy()
    windowDeleteRecord = tk.Toplevel(root)
    windowDeleteRecord.geometry('1000x700+250+50')
    windowDeleteRecord.title("DELETE A RECORD")
    windowDeleteRecord.resizable(0,0)
    windowDeleteRecord.configure(bg="cornflowerblue")
    
    Label(windowDeleteRecord,font=('Verdana',15,'bold'),text="Enter the user_id and vehicle id of the booking record you want to delete!").grid(row=0,column=1,pady=25)

    Label(windowDeleteRecord, text="USER_ID:", font=(20)).grid(row=1,column=0,padx=5,pady=25,sticky=W)
    Label(windowDeleteRecord, text="VEHICLE_ID:", font=(20)).grid(row=2,column=0,padx=5,pady=25,sticky=W)
    uid = Entry(windowDeleteRecord,font=(20), bd=7, width=50)
    uid.grid(row=1,column=1,pady=25)

    vid = Entry(windowDeleteRecord,font=(20), bd=7, width=50)
    vid.grid(row=2,column=1,pady=25)
    Button(windowDeleteRecord, text="DELETE", width=40, height=3,  font=(40), bd=7, bg="powder blue", relief="raise", command=lambda : deleteRecord(uid,vid)).grid(row=3,column=1)

def deleteRecord(uid,vid):
    winddelcnfrm = tk.Toplevel(root)
    winddelcnfrm.geometry('1000x700+250+50')
    winddelcnfrm.title("DELETE?")
    #print(e)
    winddelcnfrm.resizable(0,0)
    winddelcnfrm.configure(bg="cornflowerblue")

    delu = uid.get()
    delv = vid.get()

    Label(winddelcnfrm,font=('Verdana',15,'bold'),text="CONFIRM?",fg="black").pack(pady=50)
    Button(winddelcnfrm,width=40, height=3,  font=(40), bd=7, bg="powder blue", relief="raise",text="YES",command=lambda : deleteQuery(delu,delv)).pack(pady=25)
    Button(winddelcnfrm,width=40, height=3,  font=(40), bd=7, bg="powder blue", relief="raise",text="NO",command=btnDeleteRecord).pack(pady=25)
    
def deleteQuery(u,v):
    try:
        con.execute("DELETE FROM user_vehicle WHERE user_id=? AND vehicle_id=?",(u,v))
        print("DELETED SUCCESSFULLY")
        messagebox.showinfo("Deletion", "Deletion successful")
        con.execute("UPDATE vehicles SET quantity=quantity+1 WHERE vehicle_id=?;",(v))
        #con.commit()
    except sqlite3.Error as error:
        print("Failed to delete record from sqlite table", error)
    

def btnLoginAdmin():
    root.withdraw()
    windowLogin = tk.Toplevel(root)
    windowLogin.geometry('1000x700+250+50')
    windowLogin.title("ADMIN LOGIN")
    windowLogin.resizable(0,0)
    windowLogin.configure(bg="cornflowerblue")

    Label(windowLogin, font=('Verdana',15,'bold'), text="Enter username and password: ").grid(row=0,column=1,pady=25)

    Label(windowLogin,font=(20), text="USERNAME:").grid(row=1,column=0,pady=25,padx=15,sticky=W)
    Label(windowLogin,font=(20),text="PASSWORD:").grid(row=2,column=0,pady=25,padx=15,sticky=W)
    Username = Entry(windowLogin, width=50, font=(20), bd=7)
    Username.grid(row=1,column=1,padx=10,pady=25)
    Password = Entry(windowLogin, width=50, font=(20), bd=7)
    Password.grid(row=2,column=1,pady=25,padx=25)
    Button(windowLogin, text="LOGIN", width=40, height=3,  font=(40), bd=7, bg="powder blue", relief="raise", command=lambda : btnAdmin(windowLogin, str(Username.get()),str(Password.get()))).grid(row=3,column=1, padx=200, pady=25)


def btnLogin(windowCustomer):
    windowCustomer.destroy()
    windowLogin = tk.Toplevel(root)
    windowLogin.geometry('1000x700+250+50')
    windowLogin.title("LOGIN")
    windowLogin.resizable(0,0)
    windowLogin.configure(bg="cornflowerblue")

    Label(windowLogin, font=('Verdana',15,'bold'), text="Enter username and password: ").grid(row=0,column=1,pady=25)

    Label(windowLogin,font=(20), text="USERNAME:").grid(row=1,column=0,pady=25,padx=15,sticky=W)
    Label(windowLogin,font=(20),text="PASSWORD:").grid(row=2,column=0,pady=25,padx=15,sticky=W)
    Username = Entry(windowLogin, width=50, font=(20), bd=7)
    Username.grid(row=1,column=1,padx=10,pady=25)
    Password = Entry(windowLogin, width=50, font=(20), bd=7)
    Password.grid(row=2,column=1,pady=25,padx=25)
    Button(windowLogin, text="LOGIN", width=40, height=3,  font=(40), bd=7, bg="powder blue", relief="raise", command=lambda : btnVerifyCredentials(windowCustomer,str(Username.get()),str(Password.get()))).grid(row=3,column=1, padx=200, pady=25)

    
   
    
def btnVerifyCredentials(w,un,pw):
    curs = con.cursor()
    curs.execute('SELECT * FROM users WHERE username=? AND password=? ;', (un,pw))
    data = curs.fetchall()
    for row in data:
        uid = row[0]
    #print(uid) 
    if data:
        w.destroy()
        messagebox.showinfo("Successful", "Login successful")
        windowCustOptions = tk.Toplevel(root)
        windowCustOptions.geometry('1000x700+250+50')
        windowCustOptions.title("I'M CUSTOMER")
        windowCustOptions.resizable(0,0)
        windowCustOptions.configure(bg="cornflowerblue")
        Label(windowCustOptions, text="CHOOSE YOUR OPTION :", font=('Verdana',15,'bold')).pack(pady=50)
        Button(windowCustOptions, text="BOOK A VEHICLE!", width=40, height=3, command=lambda : buttonClick3(windowCustOptions, uid), bg="powder blue", bd=7, relief="raise", font=(40)).pack(pady=30)
        Button(windowCustOptions, text="SEARCH YOUR RECORD!", width=40, height=3, command=lambda : searchUser(uid), bg="powder blue", bd=7, relief="raise", font=(40)).pack(pady=30)
    else:
        print('Login failed')
            
        messagebox.showerror("Error", "Login failed")

def btnRegister(windowCustomer):
    windowCustomer.destroy()
    windowRegister = Toplevel(root)
    windowRegister.geometry('1000x700+250+50')
    windowRegister.title("PERSONAL DETAILS")
    windowRegister.resizable(0,0)
    windowRegister.configure(bg="cornflowerblue")

    Label(windowRegister, text="PERSONAL DETAILS", font=('Verdana',15,'bold')).grid(row=1, column=0, pady=10,padx=70)
    
    Label(windowRegister, text="NAME:",font=(20)).grid(row=2, column=0, pady=10,padx=10,sticky=W)
    Label(windowRegister, text="CONTACT_NO:",font=(20)).grid(row=3, column=0,pady=10,padx=10,sticky=W)
    Label(windowRegister, text="ADDRESS:",font=(20)).grid(row=4, column=0, pady=10,padx=10,sticky=W)
    Label(windowRegister, text="EMAIL_ID:",font=(20)).grid(row=5, column=0, pady=10,padx=10,sticky=W)
    Label(windowRegister, text="USERNAME:",font=(20)).grid(row=6, column=0,pady=10,padx=10,sticky=W)
    Label(windowRegister, text="PASSWORD:",font=(20)).grid(row=7, column=0,pady=10,padx=10,sticky=W)
    Label(windowRegister, text="GENDER:",font=(20)).grid(row=8, column=0, pady=10,padx=10,sticky=W)
    
    custName = Entry(windowRegister, width=50, font=(20), bd=7)
    custName.grid(row=2, column=1,padx=10,pady=10)
    custContact = Entry(windowRegister, width=50, font=(20), bd=7)
    custContact.grid(row=3, column=1,padx=10,pady=10)
    custAddress = Entry(windowRegister, font=(20), width=50, bd=7)
    custAddress.grid(row=4, column=1, padx=10,pady=10)
    custEmail = Entry(windowRegister, font=(20), width=50, bd=7)
    custEmail.grid(row=5, column=1, padx=10,pady=10)
    custUsername = Entry(windowRegister, width=50, font=(20), bd=7)
    custUsername.grid(row=6, column=1,padx=10,pady=10)
    custPass = Entry(windowRegister, width=50, font=(20), bd=7)
    custPass.grid(row=7, column=1,padx=10,pady=10)

    Radiobutton(windowRegister, text="Male", variable=v, value=1, font=(20), bg="cornflowerblue").grid(row=8, column=1, pady=7,sticky=W)
    Radiobutton(windowRegister, text="Female", variable=v, value=2, font=(20), bg="cornflowerblue").grid(row=9, column=1,pady=7, sticky=W)

    Button(windowRegister, text="REGISTER", width=40, height=3,  font=(40), bd=7, bg="powder blue", relief="raise", command=lambda : register(windowRegister, str(custName.get()),
        str(custContact.get()), str(custAddress.get()), str(custEmail.get()), str(custUsername.get()), str(custPass.get()), str(v.get()))).place(x=350,y=500)


def register(windowRegister, custName, custContact, custAddress, custEmail, custUsername, custPass, gender):
    windowRegister.destroy()
    g=''
    print(gender)
    if gender=='1':
        g = 'Male'
    if gender=='2':
        g = 'Female'
    insert = "INSERT INTO users(name, contact_no, address, email_id, username, password, gender) VALUES (?,?,?,?,?,?,?);"
    con.execute(insert, (custName, custContact, custAddress, custEmail, custUsername, custPass, g))
    btnCustomer()
 
def buttonClick3(win,uid):
    win.destroy()
    windn = tk.Toplevel(root)
    windn.geometry('1000x700+250+50')
    windn.title("VEHICLE BOOKING DETAILS")
    windn.resizable(0,0)
    windn.configure(bg="cornflowerblue")
    
    Label(windn, text="Vehicle Booking Details", font=('Verdana',15,'bold')).place(x=350,y=50)
    Button(windn, text="VIEW RATES", font=(20), command=buttonClick5, bg="powder blue", relief="raise",bd=3).place(x=430,y=100)

    cur = con.cursor()
    query = "SELECT vehicle_name from vehicles WHERE quantity>0"
    data = cur.execute(query)
    arr = []

    for row in data:
        arr.append(row[0])
        
    variable = StringVar(windn)
    variable.set(arr[0]) # default value
    
    Label(windn ,text="CHOOSE THE VEHICLE YOU WANT TO RENT :", font=(20)).place(x=30,y=200)
    opt = tk.OptionMenu(windn, variable, *arr)
    opt.config(width=20, font=(12))
    opt.place(x=450,y=200)
    
    Label(windn, text="DATE OF BOOKING :",font=(20)).place(x=30,y=275)
    today = date.today()
    dob = Label(windn, text=today, width=40, font=(20), bg="cornflowerblue")
    dob.place(x=400, y=275)

    l3 = tk.Label(windn, text="DURATION IN DAYS (min 1):",font=(20)).place(x=30,y=350)
    adur = Entry(windn, width=30, font=(20), bd=6)
    adur.place(x=450, y=350)

    Button(windn, text="NEXT", width=40, height=3,  font=(40), bd=7, bg="powder blue", relief="raise",command=lambda : buttonClick6(windn, variable, uid, dob, int(adur.get()))).place(x=325,y=450)


def buttonClick5():
    windr = tk.Toplevel(root)
    windr.geometry('500x500+250+50')
    windr.title("RENTS OF VEHICLES")
    windr.resizable(0,0)
    windr.configure(bg="cornflowerblue")

    tk.Label(windr, text="RENT OF BIKE IS RS. 300/DAY", font=(20),bg="cornflowerblue").place(x=175,y=150)
    tk.Label(windr, text="RENT OF CAR IS RS. 1500/DAY", font=(20),bg="cornflowerblue").place(x=175,y=175)
    tk.Label(windr, text="RENT OF JEEP IS RS. 2000/DAY", font=(20),bg="cornflowerblue").place(x=175,y=200)
    tk.Label(windr, text="RENT OF BUS IS RS. 9000/DAY", font=(20),bg="cornflowerblue").place(x=175,y=225)
    tk.Label(windr, text="RENT OF TRUCK IS RS. 10000/DAY", font=(20),bg="cornflowerblue").place(x=175,y=250)

def buttonClick6(windn, opt, uid, dob, adur):
    windn.destroy()
    vehicle = opt.get()
    windp = tk.Toplevel(root)
    windp.geometry('500x500+250+50')
    windp.title("TOTAL RENT")
    windp.resizable(0,0)
    windp.configure(bg="cornflowerblue")

    curs = con.cursor()
    q = "SELECT vehicle_id, rent FROM vehicles WHERE vehicle_name=?"
    for row in curs.execute(q, (vehicle,)):
        id = row[0]
        rent = row[1]
    
    arent = adur * rent
    
    Label(windp, text="TOTAL RENT:", font=(20)).place(x=75,y=100)
    Label(windp, text=arent, font=(15)).place(x=275,y=100)

    Button(windp, text="SUBMIT",font=(20), bg="powder blue", relief="raise",bd=3,command=lambda : insertVehicle(id, uid, dob, adur)).place(x=225,y=200)
    
createTable()
#vehicles()

cur = con.cursor()
for row in cur.execute("SELECT * FROM vehicles"):
    print(row)

cur = con.cursor()
for row in cur.execute("SELECT * FROM users"):
    print(row)

cur = con.cursor()
for row in cur.execute("SELECT * FROM user_vehicle"):
    print(row)

root1.withdraw()
root = Toplevel(root1)

root.title('Vehicle Rental Agency')
root.geometry('1000x700+250+50')
root.config(bg="cornflowerblue")

Label(root, font=('times',35,'bold'), text="***VEHICLE RENTAL AGENCY***", bd=10).pack()

Button(root, text="ADMIN", width=40, height=3, command=btnLoginAdmin, bg="powder blue",fg="black" ,bd=7, relief="raise", font=(40)).pack(pady=125)
Button(root, text="CUSTOMER", width=40, height=3, command=btnCustomer, bg="powder blue",fg="black" , bd=7, relief="raise", font=(30)).pack(pady=25)

root.mainloop()
