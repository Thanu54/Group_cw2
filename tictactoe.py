grid={"U1":" ","U2":" ", "U3":" ",
      "M1":" ","M2":" ","M3":" ",
      "L1":" ","L2":" ","L3":" "}

def gridlines(board):
    print(board["U1"] + "|" + board["U2"] + "|" + board["U3"])
    print("-+-+-")
    print(board["M1"] + "|" + board["M2"] + "|" + board["M3"])
    print("-+-+-")
    print(board["L1"] + "|" + board["L2"] + "|" + board["L3"])

gridlines(grid)
          
def tictactoe():
    turn=1
    option = 0
    valid = 0
    print("\nHow to play the game:")
    print("\nRow: U = Upper, M = Middle, L = Lower")
    print("Column: 1 = Left, 2 = Centre, 3 = Right")
    while valid == 0:
        choice=str(input("\nPlayer 1 to select between \"X\" or \"O\": "))
        if choice == "x" or choice == "o":
            valid = 1
        else:
            print("Invalid input, enter again.")
    if choice.lower()=="x":
        while turn<=9 and option == 0:
            if turn%2!=0:
                move=str(input("Player 1, please enter your move: "))
                if move.not in grid.keys():
                    print("Invalid input, enter again")
                if grid[move.upper()]==" ":
                    grid[move.upper()]="X"
                    gridlines(grid)
                    turn=turn+1
                elif grid[move.upper()]!=" ":
                    print("Space already taken!")
            else:
                move=str(input("Player 2, please enter your move: "))
                if move not in grid.keys():
                    print("Invalid input, enter again")
                if grid[move.upper()]==" ":
                    grid[move.upper()]="O"
                    gridlines(grid)
                    turn=turn+1
                elif grid[move.upper()]!=" ":
                    print("Space already taken!")
            if grid["U1"] == grid["U2"] and grid["U1"] == grid["U3"]:
                if grid["U1"] == "X":
                    print("\nPlayer 1 wins!")
                    option = 1
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
            elif turn == 9:
                print("Tie")

    elif choice.lower() == "o":
        while turn<=9 and option == 0:
            if turn%2!=0:
                move=str(input("Player 1, please enter your move: "))
                if move not in grid.keys():
                    print("Invalid input, enter again")
                elif grid[move.upper()]==" ":
                    grid[move.upper()]="O"
                    gridlines(grid)
                    turn=turn+1
                elif grid[move.upper()]!=" ":
                    print("Space already taken!")
            else:
                move=str(input("Player 2, please enter your move: "))
                if move not in grid.keys():
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
                if grid["M1"] == "X":
                    print("\nPlayer 1 wins!")
                    option = 1
                elif grid["M1"] == "O":
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
            elif turn == 9:
                print("Tie")

            
        
tictactoe()


