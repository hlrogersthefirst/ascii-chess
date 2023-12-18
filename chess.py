"""
Henry Rogers CS Section A

   ___| |__   ___  ___ ___ 
  / __| '_ \ / _ \/ __/ __|
 | (__| | | |  __/\__ \__ \
  \___|_| |_|\___||___/___/
"""
# import module
from tabulate import tabulate
from variables import *

# create header
HEAD = ["a", "b", "c", "d", "e", "f", "g", "h", " "]

# board
BOARD = [
    first_row + [8], 
    second_row + [7], 
    third_row + [6], 
    fourth_row + [5],
    fifth_row + [4],
    sixth_row + [3],
    seventh_row + [2],
    eighth_row + [1]
]

#compile black/white squares into list
black = [black_square_white_rook, black_square_black_rook, black_square_white_knight, black_square_black_knight, black_square_white_bishop,
         black_square_black_bishop, black_square_white_queen, black_square_black_queen, black_square_white_king, black_square_black_king,
         black_square_white_pawn, black_square_black_pawn, black_square]
white = [white_square_white_rook, white_square_black_rook, white_square_white_knight, white_square_black_knight, white_square_white_bishop,
         white_square_black_bishop, white_square_white_queen, white_square_black_queen, white_square_white_king, white_square_black_king,
         white_square_white_pawn, white_square_black_pawn, white_square]

# define class for game
class ChessGame:
    def __init__(self):
        self.board = self.initialize_board()
        self.current_player = "White"
        
    # initialize board
    def initialize_board(self):
        return BOARD

    #display board
    def display_board(self):
        print(tabulate(BOARD, headers=HEAD, tablefmt="grid"))

    # By far the most complicated method in here, takes a given start and end position and "moves" the piece two and from using indicies.
    def make_move(self, start_pos, end_pos):
        start_row, start_col = 8 - int(start_pos[1]), ord(start_pos[0]) - ord("a")
        end_row, end_col = 8 - int(end_pos[1]), ord(end_pos[0]) - ord("a")
        if self.board[end_row][end_col] in white and self.board[start_row][start_col] in white:
            self.board[end_row][end_col] = self.board[start_row][start_col]
        elif self.board[end_row][end_col] in black and self.board[start_row][start_col] in black:
            self.board[end_row][end_col] = self.board[start_row][start_col]
        else:
            if "`" in self.board[start_row][start_col]:
                self.board[end_row][end_col] = self.board[start_row][start_col].replace("`", "#")
            else:
                self.board[end_row][end_col] = self.board[start_row][start_col].replace("#", "`")
        if self.board[start_row][start_col] in black:
            self.board[start_row][start_col] = black_square
        else:
            self.board[start_row][start_col] = white_square
        return True

    # For playing (hopefully not by yourself)
    def play(self):
        while True:
            self.display_board()
            print(f"{self.current_player}'s turn")
            start_pos = input("Enter the starting position (e.g., e2): ")
            end_pos = input("Enter the ending position (e.g., e4): ")

            if self.make_move(start_pos, end_pos):
                self.current_player = "Black" if self.current_player == "White" else "White" # Switches to the other player

if __name__ == "__main__":
    chess_game = ChessGame()
    chess_game.play()
    
