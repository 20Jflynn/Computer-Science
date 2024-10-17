radius = int(input("enter the radius of the circle"))
PI = 3.14
print(PI * pow(radius, 2))

height = int(input("enter your height in cm"))
inches = (height / 2.54) - (height // 2.54)
inchesFinal = inches * 12
feet = (height / 2.54) // 12
print(feet,"ft", inchesFinal,"inches")



n = int(input("enter a number"))
print("",pow(n,2),"\n", pow(n,3),"\n", pow(n,4))

triangleHeight = int(input("enter the height"))
triangleLength = int(input("enter the length"))
print((triangleLength * triangleLength) / 2)

studentName, studentClass, studentAge = input("enter your name"), input("enter your class"), input("enter your age")
print(studentName, studentClass, studentAge, "\n", studentName, "\n", studentClass, "\n", studentAge)

number = int(input("enter a number"))
num1, num2 = str(number + 1), str(number + 2)
number = str(number)
print(number + num1 + num2)

numList = [int(input("enter a number")), int(input("enter a number")), int(input("enter a number"))]
print(numList[0:])
print((numList[0] * numList[1]), (numList[1] * numList[2]), numList[2])