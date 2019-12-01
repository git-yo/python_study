#变量的引用1
#不推荐使用，开辟的内存空间较多、效率低
name = input("your name: ")
age = input("your age: ")
job = input("your job: ")

info = '''
------ info of ''' + name + ''' ------
Name: ''' + name + '''
Age: ''' + age + '''
Job: ''' + job + '''
'''

print(info)