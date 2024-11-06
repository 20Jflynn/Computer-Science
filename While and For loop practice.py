n = int(input("enter a number"));
count = 0;
while count != n:
	count += 1;
	if count % 5 != 0:
		print(count);
		
		
userNum = int(input("enter a number"));
userCount = 0;
iterationCount = 0;
while userCount != userNum ** 2:
	userCount += 1;
	print(userCount);
	iterationCount += 1;
	if iterationCount >= 50:
		break;


for i in range(3, 29, 2):
	if i % 5 != 0:
		print(i);


userStart = int(input("enter a number to start at"));
userStop = int(input("enter a number to go to"));
userSkip = int(input("enter a multiple to skip"));
for i in range(userStart, userStop, 1):
	if i % userSkip != 0:
		if i % 2 != 0:
			print(i);


for x in range(50, 20, -1):
	if x % 2 == 0 and x % 3 != 0:
		print(x);


for y in range(12, -15,-1):
	if y % 2 == 0:
		print(y);

