#Section A: Creating the grid for Tictactoe

#creating a dictionary to store the moves of the game
grid={"U1":" ","U2":" ", "U3":" ",
      "M1":" ","M2":" ","M3":" ",
      "L1":" ","L2":" ","L3":" "}

#using a function to create an empty board for the start of each game
def gridlines(board):
    print(board["U1"] + "|" + board["U2"] + "|" + board["U3"])
    print("-+-+-")
    print(board["M1"] + "|" + board["M2"] + "|" + board["M3"])
    print("-+-+-")
    print(board["L1"] + "|" + board["L2"] + "|" + board["L3"])

#printing the board by calling the gridlines function
gridlines(grid)


#Secion B: Function to show instructions on how to play the game

#this function will carry out the actual game itself        
def tictactoe():
    turn=1
    option = 0
    valid = 0   #setting flags which will be used during our checks
    print("\nHow to play the game:") #displaying instructions to the user on how to communicate the move they are interested in
    print("\nRow: U = Upper, M = Middle, L = Lower") 
    print("Column: 1 = Left, 2 = Centre, 3 = Right") 
    print("For example, top left corner= U1")
    while valid == 0:   #this section of the code keeps asking the user for their choice until "x" or "o" is entered
        choice=str(input("\nPlayer 1 to select between \"X\" or \"O\": "))  
        if choice.lower() == "x" or choice.lower() == "o":  #.lower allows user to use capital or lower case letters
            valid = 1
        else:
            print("Invalid input, enter again.") #this will cause the while loop to repeat until a valid input has been entered
            
    
    #Section C: Tictactoe game for Player 1 as 'X', Player 2 as 'O'


    if choice.lower()=="x": # Carrying out the game where player 1's choice is 'X' and player 2's is 'O'
        while turn<=9 and option == 0:
            if turn%2!=0:
                print("\n")
                move=str(input("Player 1, please enter your move: ")) #if the turn is an odd number, it should be player 1's turn.
                print("\n")
                if move.upper() not in grid.keys(): 
                    print("Invalid input, enter again") #checking whether the move is actually on the grid.
                elif grid[move.upper()]==" ":   #Checks if the position on grid is empty and if so, enters an 'X'
                    grid[move.upper()]="X"
                    gridlines(grid)
                    turn=turn+1     # 1 added to turn so turn variable becomes even, which is for player 2
                elif grid[move.upper()]!=" ":   # indicates to user that the space is already taken
                    print("Space already taken!")
            else:
                print("\n")
                move=str(input("Player 2, please enter your move: "))   #If the turn is even, it is player 2's turn
                print("\n")
                if move.upper() not in grid.keys():
                    print("Invalid input, enter again")
                elif grid[move.upper()]==" ":
                    grid[move.upper()]="O"
                    gridlines(grid)
                    turn=turn+1
                elif grid[move.upper()]!=" ":
                    print("Space already taken!")
            
            
            #Section D: Determines the winner of the game
            
            
            #This section of the program checks for 3 in a row, column or diagonal of either 'X' or 'O' which
            #indicates the winner of tic tac toe, with a message showing who won the game
            #if we get 3 Xs in a line, Player 1 wins, or else player 2 wins.
            if grid["U1"] == grid["U2"] and grid["U1"] == grid["U3"]:
                if grid["U1"] == "X":
                    print("\nPlayer 1 wins!")
                    option = 1 # Setting option to 1 will break the while loop
                elif grid["U1"] == "O":
                    print("\nPlayer 2 wins!")
                    option = 1
            elif grid["M1"] == grid["M2"] and grid["M1"] == grid["M3"]:
                if grid["M1"] == "X":
                    print("\nPlayer 1 wins!")
                    option = 1
                elif grid["M1"] == "O":
                    print("\nPlayer 2 wins!")
                    option = 1
            elif grid["L1"] == grid["L2"] and grid["L1"] == grid["L3"]:
                if grid["L1"] == "X":
                    print("\nPlayer 1 wins!")
                    option = 1
                elif grid["L1"] == "O":
                    print("\nPlayer 2 wins!")
                    option = 1
            elif grid["U1"] == grid["M1"] and grid["U1"] == grid["L1"]:
                if grid["U1"] == "X":
                    print("\nPlayer 1 wins!")
                    option = 1
                elif grid["U1"] == "O":
                    print("\nPlayer 2 wins!")
                    option = 1
            elif grid["U2"] == grid["M2"] and grid["U2"] == grid["L2"]:
                if grid["U2"] == "X":
                    print("\nPlayer 1 wins!")
                    option = 1
                elif grid["U2"] == "O":
                    print("\nPlayer 2 wins!")
                    option = 1
            elif grid["U3"] == grid["M3"] and grid["U3"] == grid["L3"]:
                if grid["U3"] == "X":
                    print("\nPlayer 1 wins!")
                    option = 1
                elif grid["U3"] == "O":
                    print("\nPlayer 2 wins!")
                    option = 1
            elif grid["U1"] == grid["M2"] and grid["U1"] == grid["L3"]:
                if grid["U1"] == "X":
                    print("\nPlayer 1 wins!")
                    option = 1
                elif grid["U1"] == "O":
                    print("\nPlayer 2 wins!")
                    option = 1
            elif grid["U3"] == grid["M2"] and grid["U3"] == grid["L1"]:
                if grid["U3"] == "X":
                    print("\nPlayer 1 wins!")
                    option = 1
                elif grid["U3"] == "O":
                    print("\nPlayer 2 wins!")
                    option = 1
            elif turn == 10:    # If after all 9 moves are finished and still no winner is decided, the program will print a statement saying that the game is tied
                print("Tie")

      
      
    #Section E: Tictactoe game for Player 1 as 'O', Player 2 as 'X'
      
      
    #this following part codes the game for when player 1 chooses 'O' instead of 'X'. 
    #we see that the rest of the code is the same, except that we swap 'O' and 'X'.
    elif choice.lower() == "o":
        while turn<=9 and option == 0:
            if turn%2!=0:
                print("\n")
                move=str(input("Player 1, please enter your move: "))
                print("\n")
                if move.upper() not in grid.keys():
                    print("Invalid input, enter again")
                elif grid[move.upper()]==" ":
                    grid[move.upper()]="O"
                    gridlines(grid)
                    turn=turn+1
                elif grid[move.upper()]!=" ":
                    print("Space already taken!") 
            else:
                print("\n")
                move=str(input("Player 2, please enter your move: "))
                print("\n")
                if move.upper() not in grid.keys():
                    print("Invalid input, enter again")
                elif grid[move.upper()]==" ":
                    grid[move.upper()]="X"
                    gridlines(grid)
                    turn=turn+1
                elif grid[move.upper()]!=" ":
                    print("Space already taken!")
            if grid["U1"] == grid["U2"] and grid["U1"] == grid["U3"]:
                if grid["U1"] == "O":
                    print("\nPlayer 1 wins!")
                    option = 1
                elif grid["U1"] == "X":
                    print("\nPlayer 2 wins!")
                    option = 1
            elif grid["M1"] == grid["M2"] and grid["M1"] == grid["M3"]:
                if grid["M1"] == "O":
                    print("\nPlayer 1 wins!")
                    option = 1
                elif grid["M1"] == "X":
                    print("\nPlayer 2 wins!")
                    option = 1
            elif grid["L1"] == grid["L2"] and grid["L1"] == grid["L3"]:
                if grid["L1"] == "O":
                    print("\nPlayer 1 wins!")
                    option = 1
                elif grid["L1"] == "X":
                    print("\nPlayer 2 wins!")
                    option = 1
            elif grid["U1"] == grid["M1"] and grid["U1"] == grid["L1"]:
                if grid["U1"] == "O":
                    print("\nPlayer 1 wins!")
                    option = 1
                elif grid["U1"] == "X":
                    print("\nPlayer 2 wins!")
                    option = 1
            elif grid["U2"] == grid["M2"] and grid["U2"] == grid["L2"]:
                if grid["U2"] == "O":
                    print("\nPlayer 1 wins!")
                    option = 1
                elif grid["U2"] == "X":
                    print("\nPlayer 2 wins!")
                    option = 1
            elif grid["U3"] == grid["M3"] and grid["U3"] == grid["L3"]:
                if grid["U3"] == "O":
                    print("\nPlayer 1 wins!")
                    option = 1
                elif grid["U3"] == "X":
                    print("\nPlayer 2 wins!")
                    option = 1
            elif grid["U1"] == grid["M2"] and grid["U1"] == grid["L3"]:
                if grid["U1"] == "O":
                    print("\nPlayer 1 wins!")
                    option = 1
                elif grid["U1"] == "X":
                    print("\nPlayer 2 wins!")
                    option = 1
            elif grid["U3"] == grid["M2"] and grid["U3"] == grid["L1"]:
                if grid["U3"] == "O":
                    print("\nPlayer 1 wins!")
                    option = 1
                elif grid["U3"] == "X":
                    print("\nPlayer 2 wins!")
                    option = 1
            elif turn == 10:
                print("Tie")

            
        
tictactoe() # runs the whole game

