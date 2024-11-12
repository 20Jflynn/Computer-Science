number = input("enter 9  digit number");
numbers = int(number);
numChange = numbers;
numSmall = numbers;
firstNum = numbers;
numPos = 2;
length = 0;
total = 0;
numSum = 0;
numLength = numbers
while numLength > 0:
    numLength = numLength // 10;
    length += 1;
while numPos <= length + 2:
    numChange = numSmall % 10;
    total += (numChange * numPos)
    numChange = numSmall // 10;
    numSmall = numSmall // 10;
    numPos += 1;
while total % 11 > 0:
    total += 1;
    numSum += 1;
print(number,numSum)

    
