#1
sports = ["basketball", "gaelic"]
print(sports)
choice = input("what is your favourite sport")
sports.append(choice)
sports.sort()
print(sports)
#2
sub = ["maths", "english", "irish", "biology", "physics", "chemistry"]
print(sub)
choice = input("which of these do you not like")
if choice in sub:
    sub.remove(choice)
else:
    print("choice not in list")
print(sub)
#3
col = ["red", "orange", "yellow", "green", "blue", "pink", "purple", "navy", "violet", "turquoise"]
print(col)
start = int(input("enter start number from 0-4"))
end = int(input("enter end number from 5-9"))
print(col[start:end])
#4
nums = [123,456,789,901]
for i in range(0,4):
    print(nums[i])
choice = int(input("enter a 3 digit number"))
if choice in nums:
    print(nums.index(choice))
else:
    print("not in list")
#5
people = []
for i in range(0,3):
    inv = input("enter name of friend to invite")
    people.append(inv)
opt = input("do you want to invite someone else?Y/N")
opt.lower()
while opt == "y":
    inv = input("enter name of friend to invite")
    people.append(inv)
    opt = input("do you want to invite someone else?Y/N")
    opt.lower()
print("you have invited", len(people), "people")
print(people)
name = input("enter one name on the list")
opt = input("do you still want them to come to the party?")
opt.lower()
if opt == "n" or opt == "no":
    people.remove(name)
print(people)
