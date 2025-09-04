nums = []
num = 0
print("press q to end")
while num != "q":
    num = input("enter a number")
    num = num.lower()
    if num.isdigit():
        num = int(num)
        nums.append(num)
nums = sorted(nums)
if len(nums) % 2 == 0:
    print("the median is", ((nums[len(nums)//2]) + (nums[len(nums)//2] - 1))/2)
else:
    print("the median is", nums[len(nums)//2])
    