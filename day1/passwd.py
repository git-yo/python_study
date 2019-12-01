import getpass
username = input("name: ")
password = getpass.getpass("password: ")

info = '''
Your name : %s
Your password : %s
''' % (username,password)

print (info)