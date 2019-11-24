old_boy_age = 56
for i in range(3):
    age = int(input("please input old boy's age: "))
    if age == old_boy_age:
        print("Yes,you guess ok!")
        #exit ()
        break
    elif age > old_boy_age:
        print("No,your answer is too big!")

    else :
        print ("No,your answer is too low!")
else:
    print("You tried too many times.")