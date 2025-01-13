#1 - for
for i in range(0,11):
    print(i);

#1 - while
x = 0;
while x <= 10:
    print(x);
    x+=1;

#2 - for
for i in range(10,-1,-1):
    print(i);

#2 - while
x = 10;
while x >= 0:
    print(x);
    x -= 1;

#3 - for
for i in range(1, 8):
    print("#" * i);
    
#3 - while
x = 1;
while x <= 7:
    print("#" * x);
    x += 1;

#4 - for
x = int(input("enter no. of rows"));
y = int(input("enter no. of columns"));
for i in range(1, x+1):
    print("#" * y);

#5 - for
for i  in range(0,11):
    print(i * i);#or i ** 2

#6 - for
for i in range(0,101):
    if i % 2 == 0:
        print(i);

#6 - while
x = 0;
while x <= 100:
    x += 1;
    if x % 2 == 0:
        print(x);

#7 - for
for i in range(0,101):
    if i & 2 != 0:
        print(i);

#8 - for
total = 0;
for i in range(0,101):
    total += i;
print(total);

#9 - for
eTotal = 0;
oTotal = 0;
for i in range(0, 101):
    if i % 2 == 0:
        eTotal += i;
    else:
        oTotal += i;
print("eTotal =",eTotal);
print("oTotal =", oTotal);
    

