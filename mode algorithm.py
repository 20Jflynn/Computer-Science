lst = []
tempNum = 1
mode = []
num = 0
print("press q to quit")
while num != "q":
    num = input("enter a number")
    num = num.lower()
    if num.isdigit():
        num = int(num)
        lst.append(num)
mode.append(lst[0])
for i in lst:
    if lst.count(i) > tempNum:
        tempNum = lst.count(i)
        mode = []
        mode.append(i)
    elif lst.count(i) == tempNum and i not in mode:
        mode.append(i)
if tempNum == 1:
    print("there is no mode")
else:
    print(*mode, "is/are the mode/s")
        
