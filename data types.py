day1, day2, day3, day4, day5, day6, day7 = float(input("what was temperature on monday")), float(input("what was temperature on tuesday")), float(input("what was temperature on wednesday")),float(input("what was temperature on thursday")),float(input("what was temperature on friday")),float(input("what was temperature on saturday")),float(input("what was temperature on sunday"))
averageTemp = (day1 + day2 + day3 + day4 + day5 + day6 + day7) / 7
print(averageTemp)

PI = 3.14
x = float(input("enter a number"))
y = float(input("enter another one"))
z = float(input("enter a third one"))
print(((x ** 4) * 4) + ((y ** 3) * 3) + (z * 9) + (PI * 6))

time = int(input("enter time in seconds"))
timeMins = time // 60
timeSecs = int((time % 60))
print(timeMins,"mins", timeSecs,"secs")

hour = int(input("enter hour between 1 and 12"))
ahead = int(input("how many hours ahead"))
finalTime = hour + ahead
while finalTime > 12:
    finalTime -= 12
print(finalTime, "oclock")

digit3 = input("enter a 3 digit number")
print(digit3[::-1])

month = int(input("enter the number of the month"))
day = int(input("enter a day(1 - 30)"))
year = (month * 30) + day
print("it is day",year, "of the year")
          
