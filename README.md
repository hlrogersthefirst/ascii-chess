# ASCII Chess

ASCII Chess is a simple console-based chess game implemented in Python with ASCII art for a user-friendly interface. Version with full ascii art coming soon.

## Features

- Display the chess board with ASCII art.
- Implement basic move validation for pawns, rooks, knights, bishops, queens, and kings.
- Switch turns between White and Black players.

## How to Run

1. Clone the repository:

   git clone https://github.com/hlrogersthefirst/ascii-chess.git

2. Navigate to the project directory:

   cd ascii-chess

3. Run the chess game:

   python chess.py

## Usage

When it's your turn, enter the starting position using chess notation to tell the program the position of the piece you would like to move. Then, the ending position of where you want to move the piece to.

example:
White's turn.
Enter the starting position (e.g., e2): e2
Enter the ending position (e.g., e4): e4

  a b c d e f g h
 +----------------
8|r n b q k b n r|8
7|p p p p p p p p|7
6|               |6
5|               |5
4|        P      |4
3|               |3
2|P P P P   P P P|2
1|R N B Q K B N R|1
 +----------------
  a b c d e f g h
Black's turn
Enter the starting position (e.g., e7): e7
Enter the ending position (e.g., e5): e5

  a b c d e f g h
 +----------------
8|r n b q k b n r|8
7|p p p p p   p p|7
6|               |6
5|          p    |5
4|        P      |4
3|               |3
2|P P P P   P P P|2
1|R N B Q K B N R|1
 +----------------
  a b c d e f g h
Black's turn
Enter the starting position (e.g., e7): f7
Enter the ending position (e.g., e5): f5

Note: If the board and the pieces don't allign right, try adjusting your window.
Capitalized letters are white, lowercase are black.

Contributions are welcome! Feel free to open issues or pull requests.
Good luck!
