lst = []
tempLst = []
num = 0
print("press q to end")
while num != "q":
    num = input("enter a number")
    num = num.lower()
    if num.isdigit():
        num = int(num)
        lst.append(num)
for i in lst:
    if i not in tempLst:
        tempLst.append(i)
        print("there are:",lst.count(i),"," ,i,"s ", "in your list")

    
