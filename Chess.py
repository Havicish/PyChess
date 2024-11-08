from time import sleep
from os import system as sys
from random import choice

class ChessBoard:
    def __init__(self):
        self.Board = [[[] for i in range(8)] for i in range(8)]
        self.SetUp()

    def SetUp(self):
        # Placing pawns
        for i in range(self.Board.__len__()):
            self.Board[1][i] = "♟"  # Black pawn
            self.Board[6][i] = "♙"  # White pawn

        # Placing other pieces
        Pieces = ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
        for i in range(8):
            self.Board[0][i] = Pieces[i]  # Black pieces
            self.Board[7][i] = Pieces[i].replace("♜", "♖").replace("♞", "♘").replace("♝", "♗").replace("♛", "♕").replace("♚", "♔")  # White pieces

    def PrintBoard(self):
        sys("clear")
        for Row in self.Board:
            for i, Peice in enumerate(Row):
                print(Peice if Peice else "·", end="")
                if i != Row.__len__() - 1:
                    print(" ", end="")
            print()

    def MovePeice(self, X0, Y0, X1, Y1):
        self.Board[Y1][X1] = self.Board[Y0][X0]
        self.Board[Y0][X0] = None

    def Color(self, X, Y):
        if self.Board[Y][X] == []:
            return None
        return "Black" if self.Board[Y][X] in ["♜", "♞", "♝", "♛", "♚", "♟"] else "White"
    
    def Peice(self, X, Y):
        if self.Board[Y][X] == []:
            return None
        return self.Board[Y][X]

    def GetValidMoves(self, Color):
        Moves = []
        
        for Y, Row in enumerate(self.Board):
            for X, Peice in enumerate(Row):

                if self.Color(X, Y) == "White" and Color == "White": # White peices

                    if Peice == "♙":
                        if self.Peice(X, Y - 1) == None:
                            Moves.append((X, Y, X, Y - 1))
                        if Y == 6 and self.Peice(X, Y - 2) == None:
                            Moves.append((X, Y, X, Y - 2))
                        if X > 0 and self.Color(X - 1, Y - 1) == "Black":
                            Moves.append((X, Y, X - 1, Y - 1))
                        if X < 7 and self.Color(X + 1, Y - 1) == "Black":
                            Moves.append((X, Y, X + 1, Y - 1))
                    if Peice == "♖":
                        for i in range(1, 7):
                            if Y - i < 0:
                                continue
                            if self.Color(X, Y - i) == "White":
                                break
                            Moves.append((X, Y, X, Y - i))
                            if self.Color(X, Y - i) == "Black":
                                break
                        for i in range(1, 7):
                            if Y + i > 7:
                                continue
                            if self.Color(X, Y + i) == "White":
                                break
                            Moves.append((X, Y, X, Y + i))
                            if self.Color(X, Y + i) == "Black":
                                break

                if self.Color(X, Y) == "Black" and Color == "Black": # Black peices

                    if Peice == "♟":
                        if self.Peice(X, Y + 1) == None:
                            Moves.append((X, Y, X, Y + 1))

        return Moves
    
    def GetValidMovesForPeice(self, X, Y):
        Moves = []
        for Move in self.GetValidMoves(self.Color(X, Y)):
            if Move[0] == X and Move[1] == Y:
                Moves.append(Move)

        return Moves

Board = ChessBoard()
for i in range(8):
    Board.Board[6][i] = []
Board.PrintBoard()

TMoves = 0
while TMoves < 100:
    ValidMoves = Board.GetValidMoves("White")
    Board.MovePeice(*choice(ValidMoves))
    Board.PrintBoard()
    sleep(.1)
    TMoves = round(TMoves + .5, 1)
    ValidMoves = Board.GetValidMoves("Black")
    Board.MovePeice(*choice(ValidMoves))
    Board.PrintBoard()
    sleep(.1)
    TMoves = round(TMoves + .5, 1)

ValidMoves = Board.GetValidMovesForPeice(0, 7)

for Move in ValidMoves:
    print(Move)