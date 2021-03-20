from tkinter import *
import mysql.connector
import tk as tk

root = Tk()
root.geometry("500x300")


# define function
def getvals():
    mydb = mysql.connector.connect(host='localhost', user='root', passwd='123456', database='pythonprojects')
    mycursor = mydb.cursor()
    s = "insert into registration_form values('%s','%s','%s','%s','%s')"
    mycursor.execute(s % (namevalue.get(), contactvalue.get(), gendervalue.get(), emergencyvalue.get(), paymentvalue.get()))
    mycursor.close()
    mydb.commit()
    mydb.close()


# creating Heading
Label(root, text="New Patient Registration", font="ar 15 bold").grid(row=0, column=3)

# creating tabs
name = Label(root, text="Name", font="ar 13").grid(row=1, column=2)
contact = Label(root, text="Contact Number", font="ar 13").grid(row=2, column=2)
Gender = Label(root, text="Gender", font="ar 13").grid(row=3, column=2)
emergency = Label(root, text="Emergency", font="ar 13").grid(row=4, column=2)
Paymentmode = Label(root, text="Payment Mode", font="ar 13").grid(row=5, column=2)

namevalue = StringVar()
contactvalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentvalue = StringVar()
checkvalue = IntVar()

# Creating Entry fields
nameentry = Entry(root, textvariable=namevalue)
contactentry = Entry(root, textvariable=contactvalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymententry = Entry(root, textvariable=paymentvalue)

# Packing fields
nameentry.grid(row=1, column=3)
contactentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymententry.grid(row=5, column=3)

# creating check button

checkbtn = Checkbutton(text="remember me?", variable=checkvalue)
checkbtn.grid(row=6, column=3)

# submit button
btn = Button(text="SUBMIT", command=getvals).grid(row=7, column=3)

root.mainloop()
