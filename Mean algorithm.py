mean = 0
nums = []
num = 0
print("press q to quit")
while num != "q":
    num = input("enter a number")
    num = num.lower()
    if num.isdigit():
        num = int(num)
        nums.append(num)
for i in nums:
    mean += i
mean = mean / len(nums)
print("the mean is",mean)
    