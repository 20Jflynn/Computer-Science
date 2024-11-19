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


substring = input("enter a string")
lengthStr = len(substring)
temp = ""
longest = ""
maxSub = 0
tempSub = 0
for q in range(0,lengthStr,1):
	if substring[q] in "AOUIE" or substring[q] in "aoeiu":
		temp = "";
		tempSub = 0;
	else:
		temp += substring[q];
		tempSub += 1;
if tempSub > maxSub:
		maxSub = tempSub;
		longest = temp;
		temp = "";
		tempSub = 0;
else:
	temp = "";
	tempSub = 0;
print(longest)