total = 0
while total < 50:
    num = int(input("enter number"))
    total = total + num
print("the total is:",total)

number = 0
while number < 5:
    number = int(input("enter a number"))
print("the last number you entered is ", number)
    
response = "y"
answer = 0
total = 0
num1 = int(input("enter a number"))
while response == "y":
    num2 = int(input("enter another one"))
    answer = num1 + num2
    total = total + answer
    response = input('do you wish to add more? enter "y" to continue')
print (total)

count = 0
yes = "yes"
while yes == "yes":
    name = input("who do you wish to invite")
    print(name,"has been invited")
    count += 1
    yes = input("is there anyone else to invite? yes to continue")
print (count , "people have been invited to the party")

compnum = 50
attempts = 0
guess = 0
while guess != compnum:
    guess = int(input("guess the number"))
    if guess < compnum:
        print("too low")
    elif guess > compnum:
        print("too high")
    attempts += 1
print("well done, you took ",attempts,"attempts")

value = 0   
while value == 0:
    number = int(input("enter a number between 10 and 20"))
    if number > 20:
        print ("too high")
    elif number < 10:
        print("too low")
    elif number >= 10 and number <= 20:
        value += 1
        print("thanks")
        
bottles = 10
question = 0
while bottles > 0:
    if bottles == 1:
        print("there is", bottles,"green bottle hanging on the wall, \n", bottles,"green bottle hanging on the wall, \n and if one green bottle should accidentally fall")
    else:
        print("there are", bottles,"green bottles hanging on the wall, \n ",bottles, " green bottles hanging on the wall, \n and if one green bottle should accidentally fall")
    bottles -= 1
    
    while question != bottles:
        question = int(input("how many bottles will be left on the wall"))
        if question != bottles:
            print("no try again")
print("there are no more green bottles hanging on the wall")

        