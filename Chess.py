from time import sleep
from os import system as sys
from random import choice
import copy

class ChessBoard:
    def __init__(self):
        self.Board = [[None for i in range(8)] for i in range(8)]
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
        for i in range(10):
            print()
        for j, Row in enumerate(self.Board):
            for i, Peice in enumerate(Row):
                print(Peice if Peice else "·", end="")
                #if Peice == None:
                #    if (j + i) % 2 == 0:
                #        print("#", end="")
                #    else:
                #        print("·", end="")
                #else:
                #    print(Peice, end="")
                if i != Row.__len__() - 1:
                    print(" ", end="")
            print()

    def MovePeice(self, X0, Y0, X1, Y1):
        self.Board[Y1][X1] = self.Board[Y0][X0]
        self.Board[Y0][X0] = None

    def FindKing(self, Color):
        for Y, Row in enumerate(self.Board):
            for X, Peice in enumerate(Row):
                if Peice == "♔" and Color == "White":
                    return (X, Y)
                if Peice == "♚" and Color == "Black":
                    return (X, Y)

    def Color(self, X, Y):
        if self.Board[Y][X] == [] or self.Board[Y][X] == None:
            return None
        return "Black" if self.Board[Y][X] in ["♜", "♞", "♝", "♛", "♚", "♟"] else "White"
    
    def Peice(self, X, Y):
        if self.Board[Y][X] == []:
            return None
        return self.Board[Y][X]

    def IsInCheck(self, Color):
        King = self.FindKing(Color)
        for Move in self.GetValidMoves("Black" if Color == "White" else "White", True):
            if Move[2] == King[0] and Move[3] == King[1]:
                return True
            
    def PlayerInput(self, Move: str):
        FileToX = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

        StartFile = Move[0]
        StartRank = Move[1]
        EndFile = Move[2]
        EndRank = Move[3]

        X0 = FileToX[StartFile]
        Y0 = 8 - int(StartRank)
        X1 = FileToX[EndFile]
        Y1 = 8 - int(EndRank)

        return (X0, Y0, X1, Y1)

    def GetValidMoves(self, Color, FromGettingCheck = False):
        Moves = []
        
        for Y, Row in enumerate(self.Board):
            for X, Peice in enumerate(Row):

                if self.Color(X, Y) == "White" and Color == "White": # White peices

                    if Peice == "♙":
                        if Y != 0:
                            if self.Peice(X, Y - 1) == None:
                                Moves.append((X, Y, X, Y - 1))
                            if Y == 6 and self.Peice(X, Y - 2) == None and self.Peice(X, Y - 1) == None:
                                Moves.append((X, Y, X, Y - 2))
                            if X > 0 and self.Color(X - 1, Y - 1) == "Black":
                                Moves.append((X, Y, X - 1, Y - 1))
                            if X < 7 and self.Color(X + 1, Y - 1) == "Black":
                                Moves.append((X, Y, X + 1, Y - 1))
                    if Peice == "♖":
                        for i in range(1, 7):
                            if Y - i < 0:
                                break
                            if self.Color(X, Y - i) == "White":
                                break
                            Moves.append((X, Y, X, Y - i))
                            if self.Color(X, Y - i) == "Black":
                                break
                        for i in range(1, 7):
                            if Y + i > 7:
                                break
                            if self.Color(X, Y + i) == "White":
                                break
                            Moves.append((X, Y, X, Y + i))
                            if self.Color(X, Y + i) == "Black":
                                break
                        for i in range(1, 7):
                            if X - i < 0:
                                break
                            if self.Color(X - i, Y) == "White":
                                break
                            Moves.append((X, Y, X - i, Y))
                            if self.Color(X - i, Y) == "Black":
                                break
                        for i in range(1, 7):
                            if X + i > 7:
                                break
                            if self.Color(X + i, Y) == "White":
                                break
                            Moves.append((X, Y, X + i, Y))
                            if self.Color(X + i, Y) == "Black":
                                break
                    if Peice == "♘":
                        if X - 1 >= 0 and Y - 2 >= 0 and self.Color(X - 1, Y - 2) != "White":
                            Moves.append((X, Y, X - 1, Y - 2))
                        if X + 1 <= 7 and Y - 2 >= 0 and self.Color(X + 1, Y - 2) != "White":
                            Moves.append((X, Y, X + 1, Y - 2))
                        if X - 2 >= 0 and Y - 1 >= 0 and self.Color(X - 2, Y - 1) != "White":
                            Moves.append((X, Y, X - 2, Y - 1))
                        if X + 2 <= 7 and Y - 1 >= 0 and self.Color(X + 2, Y - 1) != "White":
                            Moves.append((X, Y, X + 2, Y - 1))
                        if X - 2 >= 0 and Y + 1 <= 7 and self.Color(X - 2, Y + 1) != "White":
                            Moves.append((X, Y, X - 2, Y + 1))
                        if X + 2 <= 7 and Y + 1 <= 7 and self.Color(X + 2, Y + 1) != "White":
                            Moves.append((X, Y, X + 2, Y + 1))
                        if X - 1 >= 0 and Y + 2 <= 7 and self.Color(X - 1, Y + 2) != "White":
                            Moves.append((X, Y, X - 1, Y + 2))
                        if X + 1 <= 7 and Y + 2 <= 7 and self.Color(X + 1, Y + 2) != "White":
                            Moves.append((X, Y, X + 1, Y + 2))
                    if Peice == "♗":
                        for i in range(1, 7):
                            if X - i < 0 or Y - i < 0:
                                break
                            if self.Color(X - i, Y - i) == "White":
                                break
                            Moves.append((X, Y, X - i, Y - i))
                            if self.Color(X - i, Y - i) == "Black":
                                break
                        for i in range(1, 7):
                            if X + i > 7 or Y - i < 0:
                                break
                            if self.Color(X + i, Y - i) == "White":
                                break
                            Moves.append((X, Y, X + i, Y - i))
                            if self.Color(X + i, Y - i) == "Black":
                                break
                        for i in range(1, 7):
                            if X - i < 0 or Y + i > 7:
                                break
                            if self.Color(X - i, Y + i) == "White":
                                break
                            Moves.append((X, Y, X - i, Y + i))
                            if self.Color(X - i, Y + i) == "Black":
                                break
                        for i in range(1, 7):
                            if X + i > 7 or Y + i > 7:
                                break
                            if self.Color(X + i, Y + i) == "White":
                                break
                            Moves.append((X, Y, X + i, Y + i))
                            if self.Color(X + i, Y + i) == "Black":
                                break
                    if Peice == "♕":
                        for i in range(1, 7):
                            if Y - i < 0:
                                break
                            if self.Color(X, Y - i) == "White":
                                break
                            Moves.append((X, Y, X, Y - i))
                            if self.Color(X, Y - i) == "Black":
                                break
                        for i in range(1, 7):
                            if Y + i > 7:
                                break
                            if self.Color(X, Y + i) == "White":
                                break
                            Moves.append((X, Y, X, Y + i))
                            if self.Color(X, Y + i) == "Black":
                                break
                        for i in range(1, 7):
                            if X - i < 0:
                                break
                            if self.Color(X - i, Y) == "White":
                                break
                            Moves.append((X, Y, X - i, Y))
                            if self.Color(X - i, Y) == "Black":
                                break
                        for i in range(1, 7):
                            if X + i > 7:
                                break
                            if self.Color(X + i, Y) == "White":
                                break
                            Moves.append((X, Y, X + i, Y))
                            if self.Color(X + i, Y) == "Black":
                                break
                        for i in range(1, 7):
                            if X - i < 0 or Y - i < 0:
                                break
                            if self.Color(X - i, Y - i) == "White":
                                break
                            Moves.append((X, Y, X - i, Y - i))
                            if self.Color(X - i, Y - i) == "Black":
                                break
                        for i in range(1, 7):
                            if X + i > 7 or Y - i < 0:
                                break
                            if self.Color(X + i, Y - i) == "White":
                                break
                            Moves.append((X, Y, X + i, Y - i))
                            if self.Color(X + i, Y - i) == "Black":
                                break
                        for i in range(1, 7):
                            if X - i < 0 or Y + i > 7:
                                break
                            if self.Color(X - i, Y + i) == "White":
                                break
                            Moves.append((X, Y, X - i, Y + i))
                            if self.Color(X - i, Y + i) == "Black":
                                break
                        for i in range(1, 7):
                            if X + i > 7 or Y + i > 7:
                                break
                            if self.Color(X + i, Y + i) == "White":
                                break
                            Moves.append((X, Y, X + i, Y + i))
                            if self.Color(X + i, Y + i) == "Black":
                                break
                    if Peice == "♔":
                        if X - 1 >= 0 and Y - 1 >= 0 and self.Color(X - 1, Y - 1) != "White":
                            Moves.append((X, Y, X - 1, Y - 1))
                        if X + 1 <= 7 and Y - 1 >= 0 and self.Color(X + 1, Y - 1) != "White":
                            Moves.append((X, Y, X + 1, Y - 1))
                        if X - 1 >= 0 and Y + 1 <= 7 and self.Color(X - 1, Y + 1) != "White":
                            Moves.append((X, Y, X - 1, Y + 1))
                        if X + 1 <= 7 and Y + 1 <= 7 and self.Color(X + 1, Y + 1) != "White":
                            Moves.append((X, Y, X + 1, Y + 1))
                        if X - 1 >= 0 and self.Color(X - 1, Y) != "White":
                            Moves.append((X, Y, X - 1, Y))
                        if X + 1 <= 7 and self.Color(X + 1, Y) != "White":
                            Moves.append((X, Y, X + 1, Y))
                        if Y - 1 >= 0 and self.Color(X, Y - 1) != "White":
                            Moves.append((X, Y, X, Y - 1))
                        if Y + 1 <= 7 and self.Color(X, Y + 1) != "White":
                            Moves.append((X, Y, X, Y + 1))

                if self.Color(X, Y) == "Black" and Color == "Black": # Black peices

                    if Peice == "♟":
                        if Y != 0:
                            if self.Peice(X, Y + 1) == None:
                                Moves.append((X, Y, X, Y + 1))
                            if Y == 1 and self.Peice(X, Y + 2) == None and self.Peice(X, Y + 1) == None:
                                Moves.append((X, Y, X, Y + 2))
                            if X > 0 and self.Color(X - 1, Y + 1) == "White":
                                Moves.append((X, Y, X - 1, Y + 1))
                            if X < 7 and self.Color(X + 1, Y + 1) == "White":
                                Moves.append((X, Y, X + 1, Y + 1))
                    if Peice == "♜":
                        for i in range(1, 7):
                            if Y - i < 0:
                                break
                            if self.Color(X, Y - i) == "Black":
                                break
                            Moves.append((X, Y, X, Y - i))
                            if self.Color(X, Y - i) == "White":
                                break
                        for i in range(1, 7):
                            if Y + i > 7:
                                break
                            if self.Color(X, Y + i) == "Black":
                                break
                            Moves.append((X, Y, X, Y + i))
                            if self.Color(X, Y + i) == "White":
                                break
                        for i in range(1, 7):
                            if X - i < 0:
                                break
                            if self.Color(X - i, Y) == "Black":
                                break
                            Moves.append((X, Y, X - i, Y))
                            if self.Color(X - i, Y) == "White":
                                break
                        for i in range(1, 7):
                            if X + i > 7:
                                break
                            if self.Color(X + i, Y) == "Black":
                                break
                            Moves.append((X, Y, X + i, Y))
                            if self.Color(X + i, Y) == "White":
                                break
                    if Peice == "♞":
                        if X - 1 >= 0 and Y - 2 >= 0 and self.Color(X - 1, Y - 2) != "Black":
                            Moves.append((X, Y, X - 1, Y - 2))
                        if X + 1 <= 7 and Y - 2 >= 0 and self.Color(X + 1, Y - 2) != "Black":
                            Moves.append((X, Y, X + 1, Y - 2))
                        if X - 2 >= 0 and Y - 1 >= 0 and self.Color(X - 2, Y - 1) != "Black":
                            Moves.append((X, Y, X - 2, Y - 1))
                        if X + 2 <= 7 and Y - 1 >= 0 and self.Color(X + 2, Y - 1) != "Black":
                            Moves.append((X, Y, X + 2, Y - 1))
                        if X - 2 >= 0 and Y + 1 <= 7 and self.Color(X - 2, Y + 1) != "Black":
                            Moves.append((X, Y, X - 2, Y + 1))
                        if X + 2 <= 7 and Y + 1 <= 7 and self.Color(X + 2, Y + 1) != "Black":
                            Moves.append((X, Y, X + 2, Y + 1))
                        if X - 1 >= 0 and Y + 2 <= 7 and self.Color(X - 1, Y + 2) != "Black":
                            Moves.append((X, Y, X - 1, Y + 2))
                        if X + 1 <= 7 and Y + 2 <= 7 and self.Color(X + 1, Y + 2) != "Black":
                            Moves.append((X, Y, X + 1, Y + 2))
                    if Peice == "♝":
                        for i in range(1, 7):
                            if X - i < 0 or Y - i < 0:
                                break
                            if self.Color(X - i, Y - i) == "Black":
                                break
                            Moves.append((X, Y, X - i, Y - i))
                            if self.Color(X - i, Y - i) == "White":
                                break
                        for i in range(1, 7):
                            if X + i > 7 or Y - i < 0:
                                break
                            if self.Color(X + i, Y - i) == "Black":
                                break
                            Moves.append((X, Y, X + i, Y - i))
                            if self.Color(X + i, Y - i) == "White":
                                break
                        for i in range(1, 7):
                            if X - i < 0 or Y + i > 7:
                                break
                            if self.Color(X - i, Y + i) == "Black":
                                break
                            Moves.append((X, Y, X - i, Y + i))
                            if self.Color(X - i, Y + i) == "White":
                                break
                        for i in range(1, 7):
                            if X + i > 7 or Y + i > 7:
                                break
                            if self.Color(X + i, Y + i) == "Black":
                                break
                            Moves.append((X, Y, X + i, Y + i))
                            if self.Color(X + i, Y + i) == "White":
                                break
                    if Peice == "♛":
                        for i in range(1, 7):
                            if Y - i < 0:
                                break
                            if self.Color(X, Y - i) == "Black":
                                break
                            Moves.append((X, Y, X, Y - i))
                            if self.Color(X, Y - i) == "White":
                                break
                        for i in range(1, 7):
                            if Y + i > 7:
                                break
                            if self.Color(X, Y + i) == "Black":
                                break
                            Moves.append((X, Y, X, Y + i))
                            if self.Color(X, Y + i) == "White":
                                break
                        for i in range(1, 7):
                            if X - i < 0:
                                break
                            if self.Color(X - i, Y) == "Black":
                                break
                            Moves.append((X, Y, X - i, Y))
                            if self.Color(X - i, Y) == "White":
                                break
                        for i in range(1, 7):
                            if X + i > 7:
                                break
                            if self.Color(X + i, Y) == "Black":
                                break
                            Moves.append((X, Y, X + i, Y))
                            if self.Color(X + i, Y) == "White":
                                break
                        for i in range(1, 7):
                            if X - i < 0 or Y - i < 0:
                                break
                            if self.Color(X - i, Y - i) == "Black":
                                break
                            Moves.append((X, Y, X - i, Y - i))
                            if self.Color(X - i, Y - i) == "White":
                                break
                        for i in range(1, 7):
                            if X + i > 7 or Y - i < 0:
                                break
                            if self.Color(X + i, Y - i) == "Black":
                                break
                            Moves.append((X, Y, X + i, Y - i))
                            if self.Color(X + i, Y - i) == "White":
                                break
                        for i in range(1, 7):
                            if X - i < 0 or Y + i > 7:
                                break
                            if self.Color(X - i, Y + i) == "Black":
                                break
                            Moves.append((X, Y, X - i, Y + i))
                            if self.Color(X - i, Y + i) == "White":
                                break
                        for i in range(1, 7):
                            if X + i > 7 or Y + i > 7:
                                break
                            if self.Color(X + i, Y + i) == "Black":
                                break
                            Moves.append((X, Y, X + i, Y + i))
                            if self.Color(X + i, Y + i) == "White":
                                break
                    if Peice == "♚":
                        if X - 1 >= 0 and Y - 1 >= 0 and self.Color(X - 1, Y - 1) != "Black":
                            Moves.append((X, Y, X - 1, Y - 1))
                        if X + 1 <= 7 and Y - 1 >= 0 and self.Color(X + 1, Y - 1) != "Black":
                            Moves.append((X, Y, X + 1, Y - 1))
                        if X - 1 >= 0 and Y + 1 <= 7 and self.Color(X - 1, Y + 1) != "Black":
                            Moves.append((X, Y, X - 1, Y + 1))
                        if X + 1 <= 7 and Y + 1 <= 7 and self.Color(X + 1, Y + 1) != "Black":
                            Moves.append((X, Y, X + 1, Y + 1))
                        if X - 1 >= 0 and self.Color(X - 1, Y) != "Black":
                            Moves.append((X, Y, X - 1, Y))
                        if X + 1 <= 7 and self.Color(X + 1, Y) != "Black":
                            Moves.append((X, Y, X + 1, Y))
                        if Y - 1 >= 0 and self.Color(X, Y - 1) != "Black":
                            Moves.append((X, Y, X, Y - 1))
                        if Y + 1 <= 7 and self.Color(X, Y + 1) != "Black":
                            Moves.append((X, Y, X, Y + 1))

        if FromGettingCheck == False and self.IsInCheck(Color):
            EditMoves = copy.deepcopy(Moves)
            OldBoard = copy.deepcopy(self.Board)
            for Move in Moves:
                self.MovePeice(*Move)
                if self.IsInCheck(Color):
                    EditMoves.remove(Move)
                self.MovePeice(Move[2], Move[3], Move[0], Move[1])
                self.Board = copy.deepcopy(OldBoard)
            Moves = EditMoves
            self.Board = OldBoard

        return Moves
    
    def GetValidMovesForPeice(self, X, Y):
        Moves = []
        for Move in self.GetValidMoves(self.Color(X, Y)):
            if Move[0] == X and Move[1] == Y:
                Moves.append(Move)

        return Moves

Board = ChessBoard()
Board.PrintBoard()

Sleep = 0.5
TMoves = 0
while TMoves < 1000:
    Board.MovePeice(*Board.PlayerInput(input("Move: ")))
    Board.PrintBoard()
    sleep(Sleep)
    TMoves = round(TMoves + .5, 1)

    ValidMoves = Board.GetValidMoves("Black")
    Board.MovePeice(*choice(ValidMoves))
    Board.PrintBoard()
    sleep(Sleep)
    TMoves = round(TMoves + .5, 1)