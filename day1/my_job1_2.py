import getpass
account = {'mike':'driver','alice':'driver1','jack':'driver2','zhy':'omyga'}
n = 3
while n > 0:
    name = input('Please enter your account name: ')
    password = getpass.getpass('Please enter your password: ')
    print()
    if password == account[name]:
        print('%s welcom to our website!!!' %(name))
        break
    else:
        n -=1