old_boy_age = 56
age = int(input("please guess old boy's old: "))
if age == old_boy_age:
    print("Yes,you guess ok!")
elif age > old_boy_age:
    print("No,your answer is too big!")
else :
    print ("No,your answer is too low!")