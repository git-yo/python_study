#变量的引用4
#也不太推荐使用
name = input("your name: ")
age = input("your age: ")
job = input("your job: ")

info = '''
------ info of {_name} ------
Name: {_name}
Age: {_age}
Job: {_job}
''' .format(_name=name,
            _age=age,
            _job=job)

#print(info)

info2 = '''
------ info of {0} ------
Name: {0}
Age: {1}
Job: {2}
''' .format(name,age,job)

print (info2)