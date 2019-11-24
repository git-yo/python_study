old_boy_age = 56
count = 0
while count < 3:
    age = int(input("please input old boy's age: "))
    if age == old_boy_age:
        print("Yes,you guess ok!")
        #exit ()
        break
    elif age > old_boy_age:
        print("No,your answer is too big!")

    else :
        print ("No,your answer is too low!")
    count +=1
    if count == 3:
        continue_play = input("Do you want to keep playing? Please input yes or no: ")
        if continue_play == "yes":
            count = 0
            #如果这里写成count == 0是错误的。
        else:
            print("Game over")