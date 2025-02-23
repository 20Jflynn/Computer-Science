#1
lst = [];
num = input("enter numbers");
temp = ""
for a in num:
	if a == " ":
		if temp != "":
			temp = int(temp)
			lst.append(temp);
		temp = "";
	else:
		temp += a;
if temp.isdigit():
	temp = int(temp);
	lst.append(temp);
lst.reverse();
print(lst);

#2
lst = [1,2,3];
lst2 = [4,5,6];
lst3 = lst + lst2;
print(lst3);

#3
lst = [];
num = input("enter numbers");
temp = ""
for a in num:
	if a == " ":
		if temp != "":
			temp = int(temp)
			lst.append(temp);
		temp = "";
	else:
		temp += a;
if temp.isdigit():
	temp = int(temp);
	lst.append(temp);
for i in range(len(lst)):
	if lst[i] > 10:
		lst[i] = 10;
print(lst);

#4
lst = []
amount = int(input("enter amount of strings to be added"));
for i in range(amount):
	word = input("enter a string");
	word = word[1:];
	lst.append(word);
print(lst);

#5
lst = [];
for i in range(50):
    lst.append(i);
print(lst)

lst = [];
for i in range(50):
    lst.append(i ** 2);
print(lst);

lst = [];
alpha = "abcdefghijklmnopqrstuvwxyz"
for i in range(26):
    lst.append(alpha[i] * (i+1));
print(lst);

#6
lst = [];
num = input("enter numbers");
temp = ""
for a in num:
	if a == " ":
		if temp != "":
			temp = int(temp)
			lst.append(temp);
		temp = "";
	else:
		temp += a;
if temp.isdigit():
	temp = int(temp);
	lst.append(temp);

lst1 = [];
while len(lst1) != len(lst):
    lst1 = [];
    num = input("enter numbers");
    temp = ""
    for a in num:
        if a == " ":
            if temp != "":
                temp = int(temp)
                lst1.append(temp);
            temp = "";
        else:
            temp += a;
    if temp.isdigit():
        temp = int(temp);
        lst1.append(temp);

lst2 = []
for i in range(len(lst)):
    lst2.append(lst[i]+lst1[i]);
print(lst2);

#7
lst = list(input("enter elements"));
lst = [lst[-1]] + lst[:-1];
print(lst)

#8
n = int(input("enter a number"));
fib = [0,1]
for i in range(n):
    fib.append(fib[i + 1] + fib[i]);
print(fib[n]);

#9
#a
lst = []
temp = "";
amount = int(input("enter amount of strings to be added"));
while amount < 1:
    print("error: amount must be greater than 1");
    amount = int(input("enter amount of strings to be added"));
for i in range(amount):
	word = input("enter a string");
	lst.append(word);
for i in lst:
    if len(i) > len(temp):
        temp = i;
print(len(temp))
#b
lst = [];
num = input("enter numbers");
temp = ""
for a in num:
	if a == " ":
		if temp != "":
			temp = int(temp)
			lst.append(temp);
		temp = "";
	else:
		temp += a;
if temp.isdigit():
	temp = int(temp);
	lst.append(temp);
num = int(input("enter a number to add to elements"));
lst1 = [];
for i in lst:
    lst1.append(i + num);
print(lst1);