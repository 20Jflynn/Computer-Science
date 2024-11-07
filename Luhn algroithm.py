cardNum = int(input("enter your card number"))
cardLen = int(len(str(cardNum)))
lastNum = 0;
numCount = 0;
total = 0;
while numCount <= cardLen:
	lastNum = cardNum % 10;
	numCount += 1;
	if numCount % 2 != 0:
		lastNum = (cardNum // 10) % 10;
		cardNum = cardNum // 10;
	else:
		numSqr = lastNum * 2;
		if numSqr > 9:
			total += (numSqr % 10) + (numSqr // 10);
		else:
			total += numSqr;
		lastNum = (cardNum // 10) % 10;
	cardNum = cardNum // 10;

if total % 10 == 0:
	print("this card is valid");
else:
	print("this card is invalid");
