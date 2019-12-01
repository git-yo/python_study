import getpass
_name = 'mike'
_password = 'driver'

n = 3
while n > 0:
    name = input('please enter your name:')
    password = getpass.getpass('please enter your password:')
    info = '%s welcom to here!!!'%(name)
    if name == _name and password == _password:
        print(info)
        break
    else:
        n = n - 1
