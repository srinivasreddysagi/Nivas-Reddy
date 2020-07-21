import os
import csv
import linecache

def Check_Prerequisites():
	if not os.path.isfile('./Database.csv'):
		with open('./Database.csv', 'w', newline="") as db:
			writer = csv.DictWriter(db, fieldnames=["Account Name", "Email", "Username", "Password"])
			writer.writeheader()

def PrintOptions():
	try:
		CheckEmpty()
	except:
		print("\n   Seems like there are No any Account Entries yet !! Proceed with [2] to add a New Entry...")
	print("\n   ---------------------------------\n")
	print("   Note: Select options by entering respective numbers\n")
	print("   [1] Need some account details ??")
	print("   [2] Wanna add a New Entry ??")
	print("\n   ---------------------------------\n")

def CheckEmpty():
	line = linecache.getline("./Database.csv", 2)
	if line == "":
		raise ValueError

def ShowList():
	with open('./Database.csv') as db:
		reader = csv.reader(db)
		next(reader)
		if linecache.getline('./Database.csv', 2) == None:
			raise ValueError
		Line_Num = 1
		for line in reader:
			print("   " + str([Line_Num]) + " " + str(line[0]))
			Line_Num += 1

def FetchDetails(get_line):
	line = linecache.getline('./Database.csv', get_line+1)
	line = line.split(",")
	print("   Account Name: {}\n   Email: {}\n   Username: {}\n   Password: {}".format(line[0], line[1], line[2], line[3]))

def AddNew(AccName, Email, Username, Password):
	with open('./Database.csv', mode="a+", newline="\n") as db:
		writer = csv.writer(db, delimiter=',')
		writer.writerow([AccName, Email, Username, Password])

if __name__ == "__main__":
	Check_Prerequisites()
	PrintOptions()
	choice = int(input())
	if choice == 1:
		try:
			CheckEmpty()
			ShowList()
			FetchDetails(int(input()))
		except:
			print("   No Entries Detected. Please add one...\n")
	if choice == 2:
		AccName = str(input("   Account Name: "))
		Email = str(input("   Email: "))
		Username = str(input("   Username: "))
		Password = str(input("   Password: "))
		AddNew(AccName, Email, Username, Password)
