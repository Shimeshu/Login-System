import os

def Login():
	print("Welcome to the Login Portal!")

	name = input("Enter Your Name -> ")

	cwd = os.getcwd()

	if os.path.exists(f"{cwd}/Registered Users") != True:
		os.mkdir(f"{cwd}/Registered Users")
	try:
		login_file = open("{}/Registered Users/{}.txt".format(cwd, name), 'r')

	except FileNotFoundError:
		print("You are not a Registered User!\nRegister and Try Again!")

	else:
		user_password = login_file.read()
		password = input("Enter Your Password -> ")
		if password in user_password:
			print("Welcome, %s!" % name)
			print(user_password)
			login_file.close()
