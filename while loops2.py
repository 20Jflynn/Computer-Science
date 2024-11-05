total = 0
amount = 0
userInt = input("enter a number")
while userInt != "":
    userInt = int(userInt)
    total += userInt
    amount += 1
    userInt = input("enter a number")
print(total / amount, "is the average")


userTotal = 0
userAmount = 0
userInt1 = int(input("enter a number"))
while userInt1 > 0:
    userTotal += userInt1
    userAmount += 1
    userInt1 = int(input("enter a number"))
print(userTotal / userAmount, "is the average")


grade = int(input("enter your grade"))
totalGrade = 0
gradeNum = 0
while grade > 0:
    totalGrade += grade
    gradeNum += 1
    grade = int(input("enter your grade"))
gradeAverage = totalGrade / gradeNum
if gradeAverage >= 90:
    letterGrade = "A"
elif gradeAverage <= 89 and gradeAverage >= 80:
    letterGrade = "B"
elif gradeAverage <= 79 and gradeAverage >= 70:
    letterGrade = "C"
elif gradeAverage <= 69 and gradeAverage >= 60:
    letterGrade = "D"
elif gradeAverage <= 59:
    letterGrade = "F"
print("your average grade is", gradeAverage, "your average letter grade is", letterGrade)


num = int(input("enter a number"))
while num > 0:
    print(num)
    num -= 1
print(num)


startValue = 0
endValue = int(input("END VAL"))
while startValue <= endValue:
    if startValue % 2 == 0:
        print(startValue)
    startValue += 1   
