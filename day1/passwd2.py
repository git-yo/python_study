import getpass
_username = "mike"
_password = "driver"
username = input("name: ")
password = getpass.getpass("password: ")

if _username == username and _password == password:
    print("Welcom user {name} login".format(name=username))
else:
    print("Invalid username or password!")