Grid={"U1":" ","U2":" ", "U3":" ",
      "M1":" ","M2":" ","M3":" ",
      "L1":" ","L2":" ","L3":" "}

def Gridlines(board):
    print(board["U1"] + "|" + board["U2"] + "|" + board["U3"])
    print("-+-+-")
    print(board["M1"] + "|" + board["M2"] + "|" + board["M3"])
    print("-+-+-")
    print(board["L1"] + "|" + board["L2"] + "|" + board["L3"])


Gridlines(Grid)
          
def tictactoe():
    #maybe add instructions for the player here
    Choice=str(input("Player 1 to select between \"X\" or \"O\": "))
    Turn=1
    if Choice.lower()=="x":
        while Turn<=9:
            if Turn%2!=0:
                Move=str(input("Player 1, please enter your move: "))
                if Grid[Move]==" ":
                    Grid[Move]="X"
                    Gridlines(Grid)
                    Turn=Turn+1
                else:
                    print("This space is already filled")
            else:
                Move=str(input("Player 2, please enter your move: "))
                if Grid[Move]==" ":
                    Grid[Move]="O"
                    Gridlines(Grid)
                    Turn=Turn+1
                
            
            
tictactoe()
