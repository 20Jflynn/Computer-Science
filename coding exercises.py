#2
temp = int(input("enter temp"));
if temp < 32:
	print("ice");
elif temp < 212:
	print("water");
else:
	print("steam");

#3
x = 1;
if x > 3:
	if x > 4:
		print("A", end = " ");
	else:
		print("B", end = " ");
elif x < 2:
	if(x != 0):
		print("C", end = " ");
print("D");

#4
weather = "raining";
if weather == "sunny" :
    print ("wear sunblock");
elif weather == "snow":
    print ("going skiing");
else :
    print (weather);

#5
if int("zero") == 0 :
    print ("zero" );
elif str(0) == "zero" :
    print (0);
elif str(0) == "0 " :
    print (str(0));
else:
    print ("none of the above")

#6
if n == 0:
    print("zero");
elif n == 1:
    print("one");
elif n == 2:
    print("two");
elif n == 3:
    print("three");
    
#7
n = int (input( "Enter an integer:" ))
if n < 1:
    print ("invalid value")
else :
    for i in range(1, n +1):
        print (i* i)

#8
#(a)
n = int(input( "Enter an integer:" ))
    if n > 0 :
        for a in range(1, n + n ) :
            print (a / (n/2))
    else :
        print ("Now quiting")
#(b)
n= int (input( "Enter an integer:"))
if n >0 :
    for a in range(1, n + n) :
        print (a /(n/2))
else :
    print ("Now quiting")

#9
#(a)
for i in range(100,0,-3):
    print(i);
#(b)
num = int(input("enter num"));
temp = num;
for _ in range(num):
    if temp == 0:
        break;
    print(temp % 10);
    temp = temp / 10;
#(c)
num = int(input("enter a number"));
count = 0;
_sum = 0;
for i in range(num,0,-2):
    count += 1;
    _sum += i;
    if count == 10:
        print(_sum/float(count));
        break;

#10
#(a)
num = int(input("enter a number"))
_min = 0;
_max = num;
_sum = 0;
if num < 0:
    _min = num;
    _max = 0;
while _min != _max:
    _sum += _min;
    if _max > 0:
       _min += 1;
    else:
        _min -= 1;
#(b)
num = 1;
while num < 16:
    if num % 3 == 0:
        print(num);
    num += 1;
#(c)
i = 0;
while i < 4:
    j = 0;
    while j < 5:
        if i + 1 == j or j + i == 4:
            print("+", end=" ");
        else:
            print("o", end=" ");
        j += 1;
    i += 1;
print();

#11
#(a)
count = 0
while count < 10:
    print ("Hello")
    count += 1
#(b)
x = 10
y= 0
while x > y:
    print (x, y)
    x=x-1
    y =y + 1
#(c)
keepgoing = True
x = 100
while keepgoing :
    print (x)
    x = x - 10
    if x < 50 :
        keepgoing = False
#(d)
x = 45
while x < 50 :
    print (x)
#(e)
for x in[1,2,3,4,5]:
    print (x)
#(f)
for x in range(5):
    print (x)
#(g)
for p in range(1, 10):
    print (p)
#(h)
for q in range(100,50,-10):
    print (q)
#(i)
for z in range(-500, 500, 100):
    print (z)
#(j)
for y in range(500,100,100):
    print (" * ", y)
#(k)
x = 10
y = 5
for i in range((x-y) * 2):
    print ("% ", i)
#(l)
for x in [1,2,3]:
    for y in [4, 5, 6]:
        print (x, y)
#(m)
for x in range(3):
    for y in range(4):
        print (x, y, x + y)
#(n)
c=0
for x in range(10):
    for y in range(5):
        c += 1
print (c)

#12
for i in range(4):
    for j in range(5):
        if i + 1 == j or j+1 == 4:
            print("+", end = " ");
        else:
            print("o", end = " ");
#14
#(a)
while True :
    n = int(input("Enter an int:"))
    if n == A1 :
        continue
    elif n == A2 :
        break
    else :
        print ("what")
else:
    print ("ever")
#(b)
while True :
    n = int(input("Enter an int: "))
    if n == A1 :
        continue
    elif n == A2 :
        break
    else :
        print ("what")
print ("ever")
#(c)
while True :
    n = int(input("Enter an int: "))
    if n == A1 :
        continue
    elif n == A2 :
        break
print ("what")
print ("ever")

#15
count = 1;
a = int(input("Enter a value: ") )
while a != 0:
    count = count + 1
    a = int(input("Enter a value: "))
print("You entered", count, "values.")