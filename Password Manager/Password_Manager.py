# Author : Nivas Reddy
# Title  : Password Manager

# Importing necessary libraries

import os
import csv
import linecache
from tkinter import *
from tkinter import messagebox
from plyer import notification

## Programming components or functions
# Checking Pre-requisities

def Check_Prerequisites():
	if not os.path.isfile('./Database.csv'):
		with open('./Database.csv', 'w', newline="") as db:
			writer = csv.DictWriter(db, fieldnames=["Account Name", "Email", "Username", "Password"])
			writer.writeheader()

# Checking previous entries existance

def CheckEmpty():
	line = linecache.getline("./Database.csv", 2)
	if line == "":
		raise ValueError

# Showing existing account extries

def ShowList():
	try:
		CheckEmpty()
		with open('./Database.csv') as db:
			reader = csv.reader(db)
			next(reader)
			Line_Num = 1
			show =""
			for line in reader:
				show += str([Line_Num]) + " " + str(line[0]) + "\n"
				Line_Num += 1
			messagebox.showinfo("Choose option", show)
			show = ""
	except:
		messagebox.showerror("Warning", "Database Error !\n\nNo Entries Detected")

# Clearing Entries

def ClrEntries():
	AccName = Entry_AccName.delete(0, END)
	Email = Entry_Email.delete(0, END)
	Username = Entry_Username.delete(0, END)
	Password = Entry_Password.delete(0, END)

# Fetching Details

def Fetch_Details():
	try:
		CheckEmpty()
		get_line = int(Entry_Option.get())
		line = linecache.getline('./Database.csv', get_line+1)
		line = line.split(",")
		Entry_AccName.insert(0, line[0])
		Entry_Email.insert(0, line[1])
		Entry_Username.insert(0, line[2])
		Entry_Password.insert(0, line[3])
		notification.notify(title="Account Details", message="Account Name: {}\nEmail: {}\nUsername: {}\nPassword: {}".format(line[0], line[1], line[2], line[3]), timeout=10)
	except:
		messagebox.showerror("Warning", "Database Error !\n\nEnter a valid option in the \"Enter option\" entry above")

# Adding new entries

def AddNew():
	AccName = Entry_AccName.get()
	Email = Entry_Email.get()
	Username = Entry_Username.get()
	Password = Entry_Password.get()
	if AccName != "" and Email != "" and Password != "":
		with open('./Database.csv', mode="a+", newline="\n") as db:
			writer = csv.writer(db, delimiter=',')
			writer.writerow([AccName, Email, Username, Password])
		ClrEntries()
	else:
		messagebox.showerror("Warning", "Invalid input")

# About Developer

def Dev():
	messagebox.showinfo("About", "   Project: Password Manager\n\nDeveloper: Nivas Reddy")

## Creating GUI
# Creating main window

window = Tk()
window.geometry("450x250")
window.title("Password Manager")

# Creating necessary labels

Label_AccName = Label(window, text="Account Name:", font=("Arial", 10, "bold"))
Label_Email = Label(window, text="Email:", font=("Arial", 10, "bold"))
Label_Username = Label(window, text="Username:", font=("Arial", 10, "bold"))
Label_Password = Label(window, text="Password:", font=("Arial", 10, "bold"))
Label_Option = Label(window, text="Enter option:", font=("Arial", 10, "bold"))

# Creating necessary entries

Entry_AccName = Entry(window, width=40)
Entry_Email = Entry(window, width=40)
Entry_Username = Entry(window, width=40)
Entry_Password = Entry(window, width=40)
Entry_Option = Entry(window, width=40)

# Creating necessary buttons

Button_GetDetails = Button(window, text="Get Details", command=Fetch_Details)
Button_NewEntry = Button(window, text="New Entry", command=AddNew)
Button_Show = Button(window, text="Show Entries", command=ShowList)
Button_Info = Button(window, text="About", command=Dev)

# Alligning GUI elements

Label_AccName.place(x=40, y=40)
Label_Email.place(x=40, y=60)
Label_Username.place(x=40, y=80)
Label_Password.place(x=40, y=100)
Entry_AccName.place(x=160, y=40)
Entry_Email.place(x=160, y=60)
Entry_Username.place(x=160, y=80)
Entry_Password.place(x=160, y=100)
Label_Option.place(x=40, y=130)
Entry_Option.place(x=160, y=130)
Button_GetDetails.place(x=130, y=180)
Button_NewEntry.place(x=230, y=180)
Button_Show.place(x=124, y=210)
Button_Info.place(x=240, y=210)

# Finally... Pack it up !!

window.after(2000, Check_Prerequisites)
window.mainloop()