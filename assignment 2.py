num = input("enter a number")
num = int(num)
num2 = input("enter another")
num2 = int(num2)
if num > num2:
    print(num2, num)
else:
    print(num, num2)
    

u20 = input("enter a number under 20")
u20 = int(u20)
if u20 > 20:
    print("too high")
else:
    print("thank you")
    
b12 = input("enter a number between 10 and 20")
b12 = int(b12)
if b12 <= 10 or b12 >= 20:
    print("incorrect answer")
else:
    print("thanks")
    
col = input("what is your favourite colour")
if col == "red" or col == "Red" or col == "RED":
    print("i like red too")
else :
    print("i dont like", col, "i prefer red")
    
rain = input("is it raining")
rain = rain.lower()
if rain == ("yes"):
    windy =  input("is it windy too")
    windy = windy.lower()
    if windy == ("yes"):
     print("its too windy for an umbrella")
    else:
     print("take an umbrella")
if rain != ("yes"):
    print("have a nice day")
    
age = input("what age are you")
age = int(age)
if age >= 18:
    print("You can Vote")
elif age == 17:
    print("You can learn to drive")
elif age == 16:
    print ("You can buy a lottery ticket")
elif age <= 15:
    print ("You can go trick or treating")
    
    
user_num = input("enter a number")
user_num = int(user_num)
if user_num < 10:
    print("too low")
elif user_num > 20:
    print("too high")
else:
    print("correct")
    
o19 = input("enter 1, 2 or 3")
o19 = int(o19)
if o19 == 1:
    print("thank you")
elif o19 == 2:
    print("Correct")
elif o19 == 3:
    print("well done")
else:
    print("Error Message")