#1
string = input("ENTER A STRING");
for i in string:
	print(i);

string = input("ENTER A STRING");
strLen = len(string);
for i in range(0,strLen):
	print(string[i]);

num = 0;
string = input("ENTER A STRING");
strLen = len(string);
while num < strLen:
	print(string[num]);
	num += 1;


#2
string = input("ENTER A STRING");
emp = "";
for i in string:
	if i.isupper():
		emp += i.lower();
	elif i.islower():
		emp+= i.upper();
print(emp);

string = input("ENTER A STRING");
strLen = len(string);
emp = "";
for i  in range(0,strLen):
	if string[i].isupper():
		emp += string[i].lower();
	elif string[i].islower():
		emp += string[i].upper();
print(emp);

string = input("ENTER A STRING");
emp = "";
strLen = len(string);
num = 0;
while num < strLen:
	if string[num].isupper():
		emp += string[num].lower();
	elif string[num].islower():
		emp += string[num].upper();
	num += 1;
print(emp);


#3
string = input("enter a string");
emp ="";
for i in string:
	emp += i*2;
print(emp);

string = input("enter a string");
emp ="";
strLen = len(string);
for i in range(0, strLen):
	emp += string[i] * 2;
print(emp);

string = input("enter a string");
emp ="";
strLen = len(string);
num = 0;
while num < strLen:
	emp += string[num] * 2;
	num += 1;
print(emp);


#4
string = input("enter a string");
string2 = input("input a second");
emp = "";
for i in string:
	if