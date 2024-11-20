#question 5
string = input("enter a sentence/series of words");
final = "";
length = len(string);
pos = 0;
while pos < length:
	if string[pos] == " " and string[pos + 1] != " ":
		final += string[pos];
		final += string[pos + 1].upper();
		pos += 1;
	elif pos == 0:
		final += string[pos].upper();
		pos += 1;
	elif pos != 0 and string[pos] != " " and string[pos - 1] != " ":
		final += string[pos];
		pos += 1
	else:
		pos += 1;
print(final)

#question 6
name = input("ENTER A WORD");
length = len(name);
word = "";
backWord = "";
for f in range(0, length, 1):
	word += name[f];
for b in range(-1, -length - 1, -1):
	backWord += name[b];
if word == backWord:
	print("it is a palindrome")
else:
	print("it is not a palindrome")

#question 7
substring = input("enter a string")
lengthStr = len(substring)
temp = ""
longest = ""
maxSub = 0
tempSub = 0
count = 0;
for q in range(lengthStr):
	if substring[q].upper() in ["A","O","U","I","E"]:
		if tempSub > maxSub:
			maxSub = tempSub;
			longest = temp;
			temp = "";
			tempSub = 0;
	else:
		temp += substring[q];
		tempSub += 1;
print(longest)

#question 8
wordStr = input("enter a string");
lengthWord = len(wordStr);
position = -lengthWord;
finalWord = "";
for w in range(0, lengthWord, 2):
	if w != 0:
		finalWord += wordStr[w - 1].upper()
	finalWord += wordStr[w];
print(finalWord);

#question 9
email = input("enter your email");
validity = ""
domain = "@edupillar.com";
domainLen = len(domain);
for sub in range(-1,-domainLen - 1, -1):
	validity += email[sub];
if validity[::-1] == domain:
	print("email is valid");
else:
	print("email not valid");