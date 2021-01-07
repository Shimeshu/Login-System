import os

def Register():
	print("Welcome to the Registration Portal!!\n")

	user_name = input('Enter Your Name -> ')

	cwd = os.getcwd()

	if os.path.exists(f"{cwd}/Registered Users") != True:
		os.mkdir(f"{cwd}/Registered Users")

	login_file = open("{}/Registered Users/{}.txt".format(cwd, user_name), 'w+')
	login_file.write("User Details\n")
	login_file.write("Name = " + user_name + "\n")

	user_email = input("Enter Your Email ID -> ")
	login_file.write('Email ID = ' + user_email + "\n")

	user_username = input("Enter Your Desired Username -> ")
	login_file.write("Username = " + user_username + "\n")

	user_password = input("Enter Password -> ")

	user_repassword = input("Enter Your Password Again -> ")

	if user_password == user_repassword and len(user_password) <= 20:
		login_file.write('Password = ' + user_repassword + "\n")

	print("Congratulations! You have successfully registered!")
	print("Go to the Login Portal for Logging in to your Account!")
	print("Thank You For Registering!! :)")

	login_file.close()
