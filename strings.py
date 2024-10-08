name = input("enter your name")
print (len(name))

firstName = input("enter your first name")
secondName = input("enter second name")
fullName = firstName + " " + secondName
print (fullName)
print(len(fullName))

lowerName = (input("enter your name in lowercase")).title()
lowerSurname = (input("enter your surname in lowercase")).title()
print (lowerName + lowerSurname)

rhyme = input("enter the first line of a nursery rhyme")
print(len(rhyme))
start = int(input("starting number")) - 1
end = int(input("end number")) 
print (rhyme[start:end])

word = input("enter a word").upper()
print (word)

nameFirst = input("enter your first name")
if len(nameFirst) < 5:
    nameSecond = input("enter your surname")
    nameFull = nameFirst + nameSecond
    print (nameFull.upper())
else:
    print (nameFirst.lower())
    
pigLatinWord = input("enter a word").lower()
firstLetter = pigLatinWord[0]
if firstLetter == "a" or firstLetter == "e" or firstLetter == "i" or firstLetter == "o" or firstLetter == "u":
    finalWord = pigLatinWord + "way"
    print (finalWord)
else:
    finalWord = pigLatinWord[1:]
    finalWord1 = finalWord + firstLetter + "ay"
    print (finalWord1)
    
    
    
    