
#---------------------------------------------------------------------
# Implementation of the Tic Tac Toe Gameboard using classes in Python
#---------------------------------------------------------------------

# Speciality of the code:
# ========================
# Alternates between 'X' and 'O' users, accepts only the 'square to fill' input from user.

# Commented towards the end of this file is the code generated by ChatGPT-3.5, which I generated out of curiosity after completing my coding, for the same.

# Contrast of my implementation from the ChatGPT's code:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#1. My code accepts input at the start on when to view the Gameboard- after every turn or when the game ends, and displays the Board according to the input.

#2. My code allows overwriting of values in already filled squares on promptof 'yes' or 'no',
#   if the user does not want to overwrite, the user is allowed to choose another square.

#3. On error in input, the ChatGPT's code stops execution with a error message,
#   but on my code, I return a message of all the accepted entries and allow the user to enter again!

#   FUN FACT: My code does not raise or stop execution with error message at any point in the execution.

#4. Used different functions for each of the operations, such as, alternating between players, checking the stuatus of the board and accepting input,
#   as part of modularity property of classes, there are not implemented in different functions in the ChatGPT's code.

#5. All my functions are present in the class and once the empty nested dictionary is passed into the class, all operations are performed in class,
#   as part of data abstraction.

#6. My code uses the '__str__' function in the class to print the Header message on execution.

#7. The Gameboard data-structure is implemented and displayed differently in the two implementations
#    - mine uses nested dictionary structure mimicing actual square positions for rows and columns, the board is bigger, spacious, better to view!

#8. Input is accepted as string mimicing actual square positions, which is easier to visualize on the Board,
#   rather than the integer inputs of the ChatGPT's implementation using row and column numbers of 0,1,2 in two prompts.

#9. Input accepting is implemented inside the class in my implementation, whereas, it is performed outside the class in ChatGPT's code.


# I hope you enjoy walking through the code and have fun playing with it!



import json
import pprint

class TicTacToe:
    
    def __init__(self, GameBoard):

        self.Board = GameBoard
        self.entries = ["TL", "TC", "TR", "ML", "MC", "MR", "BL", "BC", "BR"]
        self.player = "X"
        
    def __str__(self):

        print("\n=============================================")
        print("Welcome to the Tic-Tac-Toe Virtual Game Board")
        print("=============================================")
        print("Select when you want to view the status of the board: \n1. After every turn \n2. Once the game ends\n")
        
        self.choice = input("Enter 1 or 2 to select your choice\n")

        return self.SelectEntry()

    def Chance(self):

        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"
        
        self.SelectEntry()

    def SelectEntry(self):
        print("\n\nEnter where you want to enter your symbol: {}".format(self.player))
        self.ent = input(
            """Enter your choice from one of the following:
                1. Top-row Left Box - TL\t 2. Top-row Center Box - TC \t 3. Top-row Right Box - TR
                4. Mid-row Left Box - ML\t 2. Mid-row Center Box - MC \t 3. Mid-row Right Box - MR
                7. Bottom-row Left Box - BL\t 2. Bottom-row Center Box - BC \t 3. Bottom-row Right Box - BR\n""")
        
        if self.ent not in self.entries:
            print("Entries should be one of {}! Enter your choice again.".format(self.entries))
            
            self.SelectEntry()
        else:
            self.Entrymap(self.ent)

    def Entrymap(self,inp):
        match inp:
            case "TL":
                if " " not in self.Board["Top"]["Left"]:
                    out = input("Box already filled! Do you want to rewrite the value in the box? Enter Y or N for yes or no:")
                    if out == 'Y':
                        self.Board["Top"]["Left"] = self.player
                        self.Check()
                    else:
                        print("Enter your choice again!")
                        self.SelectEntry()
                else:
                    self.Board["Top"]["Left"] = self.player
                    self.Check()
                    
            case "TC":
                if " " not in self.Board["Top"]["Center"]:
                    out = input("Box already filled! Do you want to rewrite the value in the box? Enter Y or N for yes or no:")
                    if out == 'Y':
                        self.Board["Top"]["Center"] = self.player
                        self.Check()
                    else:
                        print("Enter your choice again!")
                        self.SelectEntry()
                else:
                    self.Board["Top"]["Center"] = self.player
                    self.Check()

            case "TR":
                if " " not in self.Board["Top"]["Right"]:
                    out = input("Box already filled! Do you want to rewrite the value in the box? Enter Y or N for yes or no:")
                    if out == 'Y':
                        self.Board["Top"]["Right"] = self.player
                        self.Check()
                    else:
                        print("Enter your choice again!")
                        self.SelectEntry()
                else:
                    self.Board["Top"]["Right"] = self.player
                    self.Check()

            case "ML":
                if " " not in self.Board["Mid"]["Left"]:
                    out = input("Box already filled! Do you want to rewrite the value in the box? Enter Y or N for yes or no:")
                    if out == 'Y':
                        self.Board["Mid"]["Left"] = self.player
                        self.Check()
                    else:
                        print("Enter your choice again!")
                        SelectEntry()
                else:
                    self.Board["Mid"]["Left"] = self.player
                    self.Check()

            case "MC":
                if " " not in self.Board["Mid"]["Center"]:
                    out = input("Box already filled! Do you want to rewrite the value in the box? Enter Y or N for yes or no:")
                    if out == 'Y':
                        self.Board["Mid"]["Center"] = self.player
                        self.Check()
                    else:
                        print("Enter your choice again!")
                        self.SelectEntry()
                else:
                    self.Board["Mid"]["Center"] = self.player
                    self.Check()

            case "MR":
                if " " not in self.Board["Mid"]["Right"]:
                    out = input("Box already filled! Do you want to rewrite the value in the box? Enter Y or N for yes or no:")
                    if out == 'Y':
                        self.Board["Mid"]["Right"] = self.player
                        self.Check()
                    else:
                        print("Enter your choice again!")
                        self.SelectEntry()
                else:
                    self.Board["Mid"]["Right"] = self.player
                    self.Check()

            case "BL":
                if " " not in self.Board["Bottom"]["Left"]:
                    out = input("Box already filled! Do you want to rewrite the value in the box? Enter Y or N for yes or no:")
                    if out == 'Y':
                        self.Board["Bottom"]["Left"] = self.player
                        self.Check()
                    else:
                        print("Enter your choice again!")
                        self.SelectEntry()
                else:
                    self.Board["Bottom"]["Left"] = self.player
                    self.Check()

            case "BC":
                if " " not in self.Board["Bottom"]["Center"]:
                    out = input("Box already filled! Do you want to rewrite the value in the box? Enter Y or N for yes or no:")
                    if out == 'Y':
                        self.Board["Bottom"]["Center"] = self.player
                        self.Check()
                    else:
                        print("Enter your choice again!")
                        self.SelectEntry()
                else:
                    self.Board["Bottom"]["Center"] = self.player
                    self.Check()

            case "BR":
                if " " not in self.Board["Bottom"]["Right"]:
                    out = input("Box already filled! Do you want to rewrite the value in the box? Enter Y or N for yes or no:")
                    if out == 'Y':
                        self.Board["Bottom"]["Right"] = self.player
                        self.Check()
                    else:
                        print("Enter your choice again!")
                        self.SelectEntry()
                else:
                    self.Board["Bottom"]["Right"] = self.player
                    self.Check()

    def Check(self):
        
        if ((self.Board["Top"]["Left"] == self.Board["Top"]["Center"] == self.Board["Top"]["Right"] == "X") or
            (self.Board["Top"]["Left"] == self.Board["Top"]["Center"] == self.Board["Top"]["Right"] == "O") or
            (self.Board["Mid"]["Left"] == self.Board["Mid"]["Center"] == self.Board["Mid"]["Right"] == "X") or
            (self.Board["Mid"]["Left"] == self.Board["Mid"]["Center"] == self.Board["Mid"]["Right"] == "O") or
            (self.Board["Bottom"]["Left"] == self.Board["Bottom"]["Center"] == self.Board["Bottom"]["Right"] == "X") or
            (self.Board["Bottom"]["Left"] == self.Board["Bottom"]["Center"] == self.Board["Bottom"]["Right"] == "O") or
            (self.Board["Top"]["Left"] == self.Board["Mid"]["Left"] == self.Board["Bottom"]["Left"] == "X") or
            (self.Board["Top"]["Left"] == self.Board["Mid"]["Left"] == self.Board["Bottom"]["Left"] == "O") or
            (self.Board["Top"]["Center"] == self.Board["Mid"]["Center"] == self.Board["Bottom"]["Center"] == "X") or
            (self.Board["Top"]["Center"] == self.Board["Mid"]["Center"] == self.Board["Bottom"]["Center"] == "O") or
            (self.Board["Top"]["Right"] == self.Board["Mid"]["Right"] == self.Board["Bottom"]["Right"] == "X") or
            (self.Board["Top"]["Right"] == self.Board["Mid"]["Right"] == self.Board["Bottom"]["Right"] == "O") or
            (self.Board["Top"]["Left"] == self.Board["Mid"]["Center"] == self.Board["Bottom"]["Right"] == "X") or
            (self.Board["Top"]["Left"] == self.Board["Mid"]["Center"] == self.Board["Bottom"]["Right"] == "O") or
            (self.Board["Top"]["Right"] == self.Board["Mid"]["Center"] == self.Board["Bottom"]["Left"] == "X") or
            (self.Board["Top"]["Right"] == self.Board["Mid"]["Center"] == self.Board["Bottom"]["Left"] == "O")):
            self.PrintBoard(self.Board)
            print("{} won!".format(self.player))
            return

        elif (self.Board["Top"]["Left"] != " " and self.Board["Top"]["Center"] != " " and self.Board["Top"]["Right"] != " " and
              self.Board["Mid"]["Left"] != " " and self.Board["Mid"]["Center"] != " " and self.Board["Mid"]["Right"] != " " and
              self.Board["Bottom"]["Left"] != " " and self.Board["Bottom"]["Center"] != " " and self.Board["Bottom"]["Right"] != " "):
            self.PrintBoard(self.Board)
            print("it's a draw!")
            return

        elif self.choice == "1":
            self.PrintBoard(self.Board)

        else:
            print("In chance")
            print("The board:" + str(self.Board[i][j] for i in self.Board for j in self.Board[i]))
            print(type(self.choice))
            self.Chance()

            

    def PrintBoard(self,Board):
        print(" __   __   __  ")
        print("             ")
        print("| {} | {} | {} |".format(self.Board['Top']["Left"], self.Board["Top"]["Center"], self.Board["Top"]["Right"]))
        print(" __   __   __  ")
        print("             ")
        print("| {} | {} | {} |".format(self.Board['Mid']["Left"], self.Board["Mid"]["Center"], self.Board["Mid"]["Right"]))
        print(" __   __   __  ")
        print("             ")
        print("| {} | {} | {} |".format(self.Board['Bottom']["Left"], self.Board["Bottom"]["Center"], self.Board["Bottom"]["Right"]))
        print(" __   __   __  ")

        self.Chance()

if __name__ == "__main__":
    Top_row = {
        "Left": " ",
        "Center": " ",
        "Right": " "
        }
    Mid_row = {
        "Left": " ",
        "Center": " ",
        "Right": " "
        }
    Bottom_row = {
        "Left": " ",
        "Center": " ",
        "Right": " "
        }
    Game = {
        "Top": Top_row,
        "Mid": Mid_row,
        "Bottom": Bottom_row
        }

    Output = TicTacToe(Game)
    print(Output)
    exit()


## ChatGPT-3.5 Code for the same:
## _______________________________

##class TicTacToe:
##    def __init__(self):
##        self.board = [[' ']*3 for _ in range(3)]
##        self.current_player = 'X'
##        
##    def print_board(self):
##        for row in self.board:
##            print('|'.join(row))
##            print('-'*5)
##
##    def place_mark(self, row, col):
##        if self.board[row][col] == ' ':
##            self.board[row][col] = self.current_player
##            self.print_board()
##            if self.check_win():
##                print(f'Player {self.current_player} wins!')
##                return True
##            elif self.check_draw():
##                print("It's a draw!")
##                return True
##            else:
##                self.current_player = 'O' if self.current_player == 'X' else 'X'
##        else:
##            print("Invalid move. Please choose an empty position.")
##
##    def check_win(self):
##        for i in range(3):
##            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':  # Check rows
##                return True
##            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':  # Check columns
##                return True
##        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':  # Check diagonals
##            return True
##        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':  # Check diagonals
##            return True
##        return False
##
##    def check_draw(self):
##        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))
##
##
##if __name__ == "__main__":
##    game = TicTacToe()
##    print(game)
##    while True:
##        row = int(input("Enter row number (0, 1, 2): "))
##        col = int(input("Enter column number (0, 1, 2): "))
##        if game.place_mark(row, col):
##            break
##