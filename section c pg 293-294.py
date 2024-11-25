#question 1
phone = input("enter a phone number");
phoneLen = len(phone);
if phoneLen == 12 and phone[3] == "-" and phone[7] == "-":
	print("it is a valid number")
else:
	print("it is not valid")

#question 2
digCheck = input("enter a string");
checkLen = len(digCheck);
total = 0;
digits = "";
for x in range(0, checkLen, 1):
	if digCheck[x].isdigit() == True:
		total += int(digCheck[x]);
		digits += digCheck[x];
if total != 0 and digits != "":
	print(digCheck, total, digits);
else:
	print(digCheck,"doesnt contain digits");

#question 3
numWord = 0;
numCh = 0;
chAlpha = 0;
sentence = " ";
while sentence != "":
	sentence = input("enter a sentence");
	senLength = len(sentence);
	if sentence != "" and sentence != " ":
		numWord = 1;
	for y in range(0, senLength, 1):
		if sentence[y].isalnum():
			chAlpha += 1;
		numCh += 1;
		if sentence[y] == " ":
			numWord += 1;
print("number of words =", numWord);
print("number of characters =", numCh);
print("percentage of characters that are alpha numeric =", (chAlpha / numCh) * 100);

#question 4
s = " ";
sFinal = "";
while s != "q":
	s = input("enter a sentence or press 'q' to quit");
	sLen = len(s);
	for m in range(sLen):
		if s[m].lower() != "q":
			if s[m].isupper():
				sFinal += s[m].lower();
			elif s[m].islower():
				sFinal += s[m].upper();
			else:
				sFinal += s[m];
print(sFinal);

#question 5
num = int(input("enter a number"));
string = input("enter a string")
strLen = len(string)
total = "";
for i in range(strLen):
	if string[i].isdigit():
		total += string[i];
if total == "":
	total = 0;
else:
	total = int(total);
print(num,"+",total,"=",num + total);

#question 6
word1 = input("ENTER A STRING");
word2 = input("ENTER ANOTHER");
word1Len = len(word1);
word2Len = len(word2);
carry = 0;
if word1Len > word2Len:
	print(word2.upper());
	word1Len = word1Len / 2;
	while carry <= word1Len:
		carry += 1;
		if carry == 1:
			print(word1[carry - 1], "\t", "\t", "\t", word1[-carry])
		if carry == 2:
			print("\t",word1[carry - 1], "\t", word1[-carry])
		if carry == 3:
			print("\t","  ",word1[carry - 1], word1[-carry])
	carry = 0;
else:
	print(word1.upper());
	word2Len = word2Len / 2;
	while carry <= word2Len:
		carry += 1;
		if carry == 1:
			print(word2[carry - 1], "\t", "\t", "\t", word2[-carry])
		if carry == 2:
			print("\t",word2[carry - 1], "\t", word2[-carry])
		if carry == 3:
			print("\t","  ",word2[carry - 1], word2[-carry])