#determines slots
choices = []
for pos in range(0,9):
    choices.append(str(pos + 1))
possible_choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
#--------------------------------------------------------------------------
Is_Current_One = True #default player is player X
won = False #default result
winner = "" #default no winner
#--------------------------------------------------------------------------
while won == False:
    #prints player's turn
    if Is_Current_One == True:
        print("\n" + "Player 1:")
    else:
        print("\n" + "Player 2:")
#--------------------------------------------------------------------------
    #prints board layout
    print('|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print("---------")
    print('|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print("---------")
    print('|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
#--------------------------------------------------------------------------
    #getting user input and filter
    choice = input(">")
    if choice.strip() in possible_choices:
        if choices[int(choice) - 1] == "X" or choices[int(choice) - 1] == "O":
            print("This square is already taken!")
        else:
            #---------------------------------------------------------------------------
            # assigns player's choice to player's symbol
            if Is_Current_One:
                choice = int(choice)
                choices[choice - 1] = "X"
                Is_Current_One = not Is_Current_One
            else:
                choice = int(choice)
                choices[choice - 1] = "O"
                Is_Current_One = not Is_Current_One
            #---------------------------------------------------------------------------
    else:
        print("Please enter only valid fields from board (1-9) ")
#---------------------------------------------------------------------------
    #logic to determine winner
    for pos_X in range(0, 3):
        pos_Y = pos_X * 3

        # horizontal win condition
        if choices[pos_Y] == choices[pos_Y + 1] == choices[pos_Y + 2] == "X":
            won = True
            winner = "Player 1"
        elif choices[pos_Y] == choices[pos_Y + 1] == choices[pos_Y + 2] == "O":
            won = True
            winner = "Player 2"

        #vertical win condition
        if choices[pos_X] == choices[pos_X + 3] == choices[pos_X + 6] == "X":
            won = True
            winner = "Player 1"
        elif choices[pos_X] == choices[pos_X + 3] == choices[pos_X + 6] == "O":
            won = True
            winner = "Player 2"

        #diagonal win condition
        if choices[0] == choices[4] == choices[8]:
            won = True
            if choices[0] == "X":
                winner = "Player 1"
            else:
                winner = "Player 2"
        elif choices[2] == choices[4] == choices[6]:
            if choices[0] == "X":
                winner = "Player 1"
            else:
                winner = "Player 2"




print("Winner: " + winner)










