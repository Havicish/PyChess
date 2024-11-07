class ChessBoard:
    def __init__(self):
        self.Board = [[[] for i in range(8)] for i in range(8)]
        self.SetUp()

    def SetUp(self):
        # Placing pawns
        for i in range(self.Board.__len__()):
            self.Board[6][i] = "♟"  # White pawn
            self.Board[1][i] = "♙"  # Black pawn

        # Placing other pieces
        Pieces = ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
        for i in range(8):
            self.Board[7][i] = Pieces[i]  # White pieces
            self.Board[0][i] = Pieces[i].replace("♜", "♖").replace("♞", "♘").replace("♝", "♗").replace("♛", "♕").replace("♚", "♔")  # Black pieces

    def PrintBoard(self):
        for Row in self.Board:
            for i, Peice in enumerate(Row):
                print(Peice if Peice else "·", end="")
                if i != Row.__len__() - 1:
                    print(" | ", end="")
            print()

# Create an instance of the ChessBoard class and display it
Board = ChessBoard()
Board.Board[7][1] = None
Board.Board[5][2] = "♞"
Board.PrintBoard()
