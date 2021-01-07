from Portals.Login import Login
from Portals.Register import Register

print('Welcome to the Login System!!')
user_input = input('Want to [L]ogin or [R]egister? -> ')

if user_input.lower() == 'l':
	Login()

elif user_input.lower() == 'r':
	Register()
