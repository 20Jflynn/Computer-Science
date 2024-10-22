x = int(input("enter number of days for person A to Complete alone"))
y = int(input("enter number of days for person B to Complete alone"))
z = int(input("enter number of days for person C to Complete alone"))
print((x * y * z) / ((x * y) + (y * z) + (x * z)))

num1 = int(input("enter a number"))
num2 = int(input("enter a number"))
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

number1, number2 = int(input("enter a number")), int(input("enter a number"))
swap = number2
number2 = number1
number1 = swap
print(number1, number2)

numSwap, numSwap2 = int(input("enter a number")), int(input("enter a number"))
numSwap, numSwap2 = numSwap2, numSwap
print(numSwap, numSwap2)

avg1, avg2, avg3 = int(input("number1")), int(input("number2")), int(input("number3"))
print((avg1 + avg2 + avg3) / 3)

PI = 3.14
r = 7
print((4 / 3) * PI * r ** 3)
r = 12
print((4 / 3) * PI * r ** 3)
r = 16
print((4 / 3) * PI * r ** 3)

age = int(input("enter your age"))
year = 2024
year100 = (100 - age) + 2024
print("you will be 100 in the year", year100)

m = float(input("enter the mass"))
C = 3 * 108
print(m * (C ** 2))

school = input("enter school name")
studentName = input("enter your name")
studentRoll = input("enter your Roll number")

studentClass = input("enter your class")
studentSection = input("enter your Section")

studentAddress1 = input("Address line 1")
studentAddress2 = input("Address line 1")
studentCity = input("enter your City")

studentPin = input("enter your Pin/code")
contactNum= input("enter your parent/gaurdian contact number")

print("\t \t \t   ", school)
print("\t Student Name:", studentName, "\t Roll no:", studentRoll)
print("\t Class:", studentClass, "\t \t Section:",studentSection)
print("\t Address :", studentAddress1, "\n \t", studentAddress2)
print("\n \t City:    ", studentCity, "\t \t Pin Code:", studentPin)
print("\t Parent's/ Gaurdians Contact No:", contactNum)
