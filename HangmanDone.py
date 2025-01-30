import random;

wordList = { 1:"burger", 2:"electricity",3:"slot machine",4:"algorithm",5:"keyboard"}
ran = random.randrange(1,5);
word = wordList[ran];
guess = "";
blanks = "";
lives = 7;
damage = -1;
letters = "";
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

for i in word:
	num = 0;
	if i == " ":
		guess += " ";
	else:
		guess += "-";
print(guess)

while guess != word:
	userInput = input("ENTER A LETTER");
	while userInput in letters:
		print("error - letter already used");
		print("used letters =", letters);
		userInput = input("ENTER A LETTER");
	userInput = userInput.lower();
	if userInput in word:
		for i in range(len(word)):
			if userInput != word[i] and guess[i] == "-":
				blanks += "-";
			elif userInput == word[i] and guess[i] == "-":
				blanks += word[i];
				if word[i] not in letters:
					letters += word[i];
			elif userInput != word[i] and guess[i] != "-":
				blanks += guess[i];
		guess = blanks;
		blanks = "";
	else:
		lives -= 1;
		damage += 1;
		letters += userInput;
		print(HANGMANPICS[damage]);
		print(" ");
		#print("you have", lives,"lives left");
	if lives <= 0:
		print("you lose");
		print("the word was",word);
		break;
	else:
		print(guess);
else:
	print(" ");
	print("you win");