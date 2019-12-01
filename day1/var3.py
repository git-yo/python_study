#变量的引用3
name = input("your name: ")
age = int(input("your age: "))
#用int函数对输入做强转换，转换为整型
# print(tyep(age))
job = input("your job: ")

info = '''
------ info of %s ------
Name: %s
Age: %d
Job: %s
''' % (name,name,age,job)

print(info)
