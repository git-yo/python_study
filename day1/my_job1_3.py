import getpass
account = {'mike':'driver','alice':'driver1','jack':'driver2','zhy':'omyga'}
for i in range (3):
    name = input('Please enter your account name: ')
    password = getpass.getpass('Please enter your account password: ')
    if password == account[name]:
        print('-----------------------------------')
        print('hello %s,welcom to our website!!!' %(name))
        print('-----------------------------------')
        break