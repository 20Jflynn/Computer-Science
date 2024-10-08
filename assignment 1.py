name = input("whats your name")
print ("hello", name)

name1 = input ("what is your name")
surname = input ("What is your surname")
print ("hello", name1, surname)

print("what do you call a bear with no teeth?","a gummy bear")

num1 = input("enter a number")
num1 = int(num1)
num2 = input ("enter a second number")
num2 = int(num2)
ans = num1 + num2
ans = int(ans)
print ("the total is", ans)

num3 = input("enter a number")
num3 = int(num3)
num4 = input("enter another")
num4 = int(num4)
num5 = input("one more")
num5 = int(num5)
ans1 = num3 + num4
ans1 = int(ans1)
ans2 = ans1 * num5
ans2 = int(ans2)
print("the answer is", ans2)

pizza = input("how many slices did you start with")
pizza = int(pizza)
eaten = input("how many slices of pizza have you eaten")
eaten = int(eaten)
slices = pizza - eaten
slices = int(slices)
print("you have",slices,"slices left")

user_name = input("what is your name")
user_age = input("what age are you")
user_age = int(user_age)
user_age1 = user_age + 1
print(user_name, "next birthday you will be", user_age1)

bill = input("what is the total price of the bill")
bill = float(bill)
diners = input("how many diners are there")
diners = int(diners)
each = bill / diners
each = float(each)
print("each person must pay", each)

time = input("how many days")
time = float(time)
hours = time * 24
hours = float(hours)
minutes = hours * 60
minutes = float(minutes)
sec = minutes * 60
sec = float(sec)
print("there are",hours, "hours", minutes, "minutes", sec, "seconds, in", time,"days")

weight = input("enter a weight in kg")
weight = float(weight)
lbs = weight * 2.204
lbs = float(lbs)
print (lbs)

no = input("enter a number over 100")
no = int(no)
if no < 100:
    print("that is under 100")
    no = input("enter a number over 100")
no1 = input ("enter a number over 10")
no1 = int(no1)
no2 = no / no1
no2 = int(no2)
print(no1,"goes into",no,no2, "times")

    

