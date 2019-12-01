#变量的引用2
name = input("your name: ")
age = input("your age: ")
job = input("your job: ")

info = '''
------ info of %s ------
Name: %s
Age: %s
Job: %s
''' % (name,name,age,job)

print(info)
