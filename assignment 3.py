num = input("enter a number")
num = int(num)
if num % 5 == 0:
    print ("hello")
else:
    print("goodbye")
    
bill = int(input("how many units did you use?"))
if bill > 100 and bill <= 200:
    price1 = (bill - 100)
    price1 = int(price1)
    u_price = (price1 * 5)
    u_price = float(u_price)
elif bill > 200:
    price2 = (bill - 200)
    price2 = int(price2)
    price3 = (price2 * 10)
    price3 = int(price3)
    o_price = (price3 + 500)
    o_price = float(o_price)
while bill > 100 and bill <= 200:
    print ("€",u_price / 100)
    break
while bill > 200:
    print ("€",o_price / 100)
    break

b_price = input("bike price before tax")
b_price = int(b_price)
if b_price >= 1000:
    total_price1 = (b_price * 1.15)
    total_price1 = float(total_price1)
    tax1 = (b_price * 0.15)
    tax1 = float(tax1)
    print ("cost before tax is", b_price, " €")
    print ("tax is ", tax1, "€")#
    print ("the total is", total_price1,"€")
elif b_price >= 500 and b_price < 1000:
    total_price2 = (b_price * 1.10)
    total_price2 = float(total_price2)
    tax2 = (b_price * 0.10)
    tax2 = float(tax2)
    print ("cost before tax is", b_price, " €")
    print ("tax is ", tax2, "€")
    print ("the total is", total_price2,"€")
elif b_price < 500:
    total_price3 = (b_price * 1.05)
    total_price3 = float(total_price3)
    tax3 = (b_price * 0.05)
    tax3 = float(tax3)
    print ("cost before tax is", b_price, " €")
    print ("tax is ", tax3, "€")
    print ("the total is", total_price3,"€")
    
three = input("enter three numbers")
three = list(three)
one = three.pop(0)
one = int(one)
two = three.pop(1)
two = int(two)
three1 = three.pop(2)
three1 = int(three1)
if one > two and one > three1:
    print (one)
elif two > one and two> three1:
    print(two)
else:
    print (three1)
    
letter = input("enter a letter")
letter = letter.lower
if letter == "a" or  letter == "e" or  letter == "i" or  letter == "o" or  letter == "u": 
    print ("it is a vowel")
else:
    print("it is a constanant")

print("enter the sides to your triangle")
lefttri = input("left side:")
righttri = input("right side:")
bottomtri = input("bottom side:")
if lefttri == righttri and lefttri != bottomtri:
    print("it is an isosceles")
elif lefttri == righttri and lefttri == bottomtri:
    print("it is an equilateral")
else:
    print("it is a scalene")
    
    
print("enter your addition or subtraction equation")
let1 = input(" ")
sign = input(" ")
let2 = input(" ") 
if sign == "+":
    let1 = int(let1)
    let2 = int(let2)
    ans = let1 + let2
elif sign == "-":
    let1 = int(let1)
    let2 = int(let2)
    ans = let1 - let2
elif sign == "x" or sign == "*":
    let1 = int(let1)
    let2 = int(let2)
    ans = let1 * let2
elif sign == "/" or sign == "":
    let1 = int(let1)
    let2 = int(let2)
    ans = let1 * let2
print (ans)
    
    
i = input(" ")
j = input(" ")
k = input(" ")

if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k
print(i, j, k)