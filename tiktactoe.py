row1 = ["-","-","-"];
row2 = ["-","-","-"];
row3 = ["-","-","-"];
game = True;
valid = False;
add = "";
turn = 1;
player = ""
winnerName = "";
option = "y"
player1Check = 0;
player2Check = 0;
def game_check(add,row1,row2,row3):
	success = True
	if row1 == [add, add, add]:
		success = False;
	elif row2 == [add, add, add]:
		success = False
	elif row3 == [add, add, add]:
		success = False
	for i in range(3):
		if row1[i] == add and row1[i] == row2[i] and row2[i] == row3[i]:
			success = False
			break
	if row1[0] == add and row1[0] == row2[1] and row2[1] == row3[2] or row1[2] == add and row1[2] == row2[1] and row2[1] == row3[0]:
		success = False
	return success
while option == "y":
	row1 = ["-","-","-"];
	row2 = ["-","-","-"];
	row3 = ["-","-","-"];
	print("",*row1,"\n",*row2,"\n",*row3);
	while game == True:
		while valid == False:
			if turn % 2 == 0:
				add = "o"
				player = "player2 is o: choose the position to place your o(from 1-9)"
			else:
				add = "x"
				player = "player1 is x: choose the position to place your x(from 1-9)"
			player1 = int(input(player));
			if player1 <= 3 and player1 >= 1 and row1[player1 - 1] == "-":
				row1[player1 - 1] = add;
				valid = True;
			elif player1 >= 4 and player1 <= 6 and row2[player1 - 4] == "-":
				player1 -= 4;
				row2[player1] = add;
				valid = True;
			elif player1 >= 7 and player1 <= 9 and row3[player1 - 7] == "-":
				player1 -= 7;
				row3[player1] = add;
				valid = True;
		valid = False;
		game = game_check(add,row1,row2,row3)
		turn += 1
		print("",*row1,"\n",*row2,"\n",*row3);
	option = input("play again?(y for yes/n for no)").lower()
	if option == "y":
		game = True

