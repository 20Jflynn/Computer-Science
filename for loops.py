name = input("enter name")
num = int(input("enter a number"))
for character in range(num):
    print (name)
    
letter = input("enter name")
letter_num = int(input("enter a number"))
for number in range(letter_num):
    for namefinal in letter:
        print(namefinal)
    
p = int(input("enter a number between 1 and 12"))
for i in range(13):
        print(p , "x", i, "=", p * i)
        
b_fifty = int(input("enter a number below fifty"))
for j in range(50, b_fifty, -1):
    print(j)
print (b_fifty)

name41 = input("enter your name")
num41 = int(input("enter a number"))
if num41 <= 10:
    for name411 in range(num41):
        print(name41)
else:
    for incorrect in range(3):
        print("too high")

total = 0
for totalnum in range(5):
    input1 = int(input("enter a number"))
    input2 = input("do you want this included")
    input2.lower()
    if input2 == "yes" or input2 == "y":
        total += input1
print (total)

up_down = input("count up or down")
up_down.lower()
if up_down == "up":
    num_high = int(input("what is your highest number"))
    for count1 in range(0,num_high + 1,1):
        print(count1)
elif up_down == "down":
    num_high = int(input("what is your highest number"))
    for count2 in range(num_high,0, -1):
        print(count2)
else:
    print("i dont understand")
    
party = int(input("how many do you want at the party"))
if party < 10:
    for names in range(party):
        party_name = input("what is the name")
        print(party_name, "is invited")
else:
    print("too many people")
        