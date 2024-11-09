from time import sleep
from os import system as sys
import InstallLibraries
import copy

InstallLibraries.InstallColorama() # Auto install colorama if it isn't already installed
from colorama import Fore

class ChessBoard:
    def __init__(self):
        self.Board = [[None for i in range(8)] for i in range(8)]
        self.SetUp()

        # Castling
        self.WhiteKingMoved = False
        self.A1RookMoved = False
        self.H1RookMoved = False
        self.BlackKingMoved = False
        self.A8RookMoved = False
        self.H8RookMoved = False

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

    def Color(self, X, Y):
        if self.Board[Y][X] == [] or self.Board[Y][X] == None:
            return None
        return "Black" if self.Board[Y][X] in ["♜", "♞", "♝", "♛", "♚", "♟"] else "White"

    def PrintBoard(self, HighlightLegalMovesForPeice = None, MatedColor = None):
        sys("clear")

        MovesForPeice = None
        if HighlightLegalMovesForPeice:
            MovesForPeice = self.GetLegalMovesForPeice(*HighlightLegalMovesForPeice)
            NewList = []
            for Move in MovesForPeice:
                NewList.append((Move[2], Move[3]))
            MovesForPeice = copy.deepcopy(NewList)
        
        for _ in range(10):
            print()
        for Y, Row in enumerate(self.Board):
            print(8 - Y, end=" ")
            for X, Peice in enumerate(Row):
                Color0 = Fore.CYAN
                Color1 = Fore.MAGENTA
                Color2 = Fore.YELLOW # Legal moves
                Color3 = Fore.LIGHTBLACK_EX # Checkmated
                if Peice == None:
                    if MovesForPeice and (X, Y) in MovesForPeice:
                        print(Color2 + "." + Fore.RESET, end="")
                    else:
                        if (Y + X) % 2 == 0:
                            print(Color0 + "." + Fore.RESET, end="")
                        else:
                            print(Color1 + "·" + Fore.RESET, end="")
                else:
                    if MatedColor and self.Color(X, Y) == MatedColor:
                        print(Color3 + Peice + Fore.RESET, end="")
                    else:
                        if MovesForPeice and (X, Y) in MovesForPeice:
                            print(Color2 + Peice + Fore.RESET, end="")
                        else:
                            if (Y + X) % 2 == 0:
                                print(Color0 + Peice + Fore.RESET, end="")
                            else:
                                print(Color1 + Peice + Fore.RESET, end="")
                if X != Row.__len__() - 1:
                    print(" ", end="")
            print()
        print("  a b c d e f g h")

    def Peice(self, X, Y):
        if self.Board[Y][X] == []:
            return None
        return self.Board[Y][X]

    def MovePeice(self, X0, Y0, X1, Y1, CountMoveKing = True):
        if self.Peice(X0, Y0) in ["♔", "♚"] and abs(X0 - X1) >= 2:
            if X1 == 6:  # Kingside castling
                self.Board[Y0][5] = self.Board[Y0][7]
                self.Board[Y0][7] = None
            elif X1 == 2:  # Queenside castling
                self.Board[Y0][3] = self.Board[Y0][0]
                self.Board[Y0][0] = None
        self.Board[Y1][X1] = self.Board[Y0][X0]
        self.Board[Y0][X0] = None
        if (self.Peice(X1, Y1) == "♙" or self.Peice(X1, Y1) == "♟") and (Y1 == 0 or Y1 == 7):
            self.Board[Y1][X1] = "♕" if self.Color(X1, Y1) == "White" else "♛"
        if CountMoveKing == True:
            if self.Peice(0, 7) not in ["♖", "♜"]:
                self.A1RookMoved = True
            if self.Peice(7, 7) not in ["♖", "♜"]:
                self.H1RookMoved  = True
            if self.Peice(0, 0) not in ["♖", "♜"]:
                self.A8RookMoved = True
            if self.Peice(7, 0) not in ["♖", "♜"]:
                self.H8RookMoved = True
            if self.Peice(4, 7) != "♔":
                self.WhiteKingMoved = True
            if self.Peice(4, 0) != "♚":
                self.BlackKingMoved = True

    def BoardValue(self, Color):
        PeiceValues = {
            "♙": 1, "♟": 1,
            "♘": 3, "♞": 3,
            "♗": 3, "♝": 3,
            "♖": 5, "♜": 5,
            "♕": 9, "♛": 9,
        }
        Value = 0
        for Row in self.Board:
            for Peice in Row:
                if Peice and self.Color(Row.index(Peice), self.Board.index(Row)) == Color:
                    Value += PeiceValues[Peice]
        return Value

    def FindKing(self, Color):
        for Y, Row in enumerate(self.Board):
            for X, Peice in enumerate(Row):
                if Peice == "♔" and Color == "White":
                    return (X, Y)
                if Peice == "♚" and Color == "Black":
                    return (X, Y)

    def IsInCheck(self, Color):
        King = self.FindKing(Color)
        for Move in self.GetLegalMoves("Black" if Color == "White" else "White", True):
            if Move[2] == King[0] and Move[3] == King[1]:
                return True
            
    def PlayerInput(self, Move: str):
        Move = Move.lower()

        FileToX = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

        if Move.__len__() == 4:
            StartFile = Move[0]
            StartRank = Move[1]
            EndFile = Move[2]
            EndRank = Move[3]

            X0 = FileToX[StartFile]
            Y0 = 8 - int(StartRank)
            X1 = FileToX[EndFile]
            Y1 = 8 - int(EndRank)

            return (X0, Y0, X1, Y1)
        elif Move.__len__() == 2:
            StartFile = Move[0]
            StartRank = Move[1]

            X0 = FileToX[StartFile]
            Y0 = 8 - int(StartRank)

            return (X0, Y0)

    def GetLegalMoves(self, Color, FromGettingCheck = False):
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
                        for i in range(1, 8):
                            if Y - i < 0:
                                break
                            if self.Color(X, Y - i) == "White":
                                break
                            Moves.append((X, Y, X, Y - i))
                            if self.Color(X, Y - i) == "Black":
                                break
                        for i in range(1, 8):
                            if Y + i > 7:
                                break
                            if self.Color(X, Y + i) == "White":
                                break
                            Moves.append((X, Y, X, Y + i))
                            if self.Color(X, Y + i) == "Black":
                                break
                        for i in range(1, 8):
                            if X - i < 0:
                                break
                            if self.Color(X - i, Y) == "White":
                                break
                            Moves.append((X, Y, X - i, Y))
                            if self.Color(X - i, Y) == "Black":
                                break
                        for i in range(1, 8):
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
                        for i in range(1, 8):
                            if X - i < 0 or Y - i < 0:
                                break
                            if self.Color(X - i, Y - i) == "White":
                                break
                            Moves.append((X, Y, X - i, Y - i))
                            if self.Color(X - i, Y - i) == "Black":
                                break
                        for i in range(1, 8):
                            if X + i > 7 or Y - i < 0:
                                break
                            if self.Color(X + i, Y - i) == "White":
                                break
                            Moves.append((X, Y, X + i, Y - i))
                            if self.Color(X + i, Y - i) == "Black":
                                break
                        for i in range(1, 8):
                            if X - i < 0 or Y + i > 7:
                                break
                            if self.Color(X - i, Y + i) == "White":
                                break
                            Moves.append((X, Y, X - i, Y + i))
                            if self.Color(X - i, Y + i) == "Black":
                                break
                        for i in range(1, 8):
                            if X + i > 7 or Y + i > 7:
                                break
                            if self.Color(X + i, Y + i) == "White":
                                break
                            Moves.append((X, Y, X + i, Y + i))
                            if self.Color(X + i, Y + i) == "Black":
                                break
                    if Peice == "♕":
                        for i in range(1, 8):
                            if Y - i < 0:
                                break
                            if self.Color(X, Y - i) == "White":
                                break
                            Moves.append((X, Y, X, Y - i))
                            if self.Color(X, Y - i) == "Black":
                                break
                        for i in range(1, 8):
                            if Y + i > 7:
                                break
                            if self.Color(X, Y + i) == "White":
                                break
                            Moves.append((X, Y, X, Y + i))
                            if self.Color(X, Y + i) == "Black":
                                break
                        for i in range(1, 8):
                            if X - i < 0:
                                break
                            if self.Color(X - i, Y) == "White":
                                break
                            Moves.append((X, Y, X - i, Y))
                            if self.Color(X - i, Y) == "Black":
                                break
                        for i in range(1, 8):
                            if X + i > 7:
                                break
                            if self.Color(X + i, Y) == "White":
                                break
                            Moves.append((X, Y, X + i, Y))
                            if self.Color(X + i, Y) == "Black":
                                break
                        for i in range(1, 8):
                            if X - i < 0 or Y - i < 0:
                                break
                            if self.Color(X - i, Y - i) == "White":
                                break
                            Moves.append((X, Y, X - i, Y - i))
                            if self.Color(X - i, Y - i) == "Black":
                                break
                        for i in range(1, 8):
                            if X + i > 7 or Y - i < 0:
                                break
                            if self.Color(X + i, Y - i) == "White":
                                break
                            Moves.append((X, Y, X + i, Y - i))
                            if self.Color(X + i, Y - i) == "Black":
                                break
                        for i in range(1, 8):
                            if X - i < 0 or Y + i > 7:
                                break
                            if self.Color(X - i, Y + i) == "White":
                                break
                            Moves.append((X, Y, X - i, Y + i))
                            if self.Color(X - i, Y + i) == "Black":
                                break
                        for i in range(1, 8):
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
                        if self.WhiteKingMoved == False:
                            if self.A1RookMoved == False and self.Peice(X - 1, Y) == None and self.Peice(X - 2, Y) == None and self.Peice(X - 3, Y) == None:
                                Moves.append((X, Y, X - 2, Y))
                            if self.H1RookMoved == False and self.Peice(X + 1, Y) == None and self.Peice(X + 2, Y) == None:
                                Moves.append((X, Y, X + 2, Y))

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
                        for i in range(1, 8):
                            if Y - i < 0:
                                break
                            if self.Color(X, Y - i) == "Black":
                                break
                            Moves.append((X, Y, X, Y - i))
                            if self.Color(X, Y - i) == "White":
                                break
                        for i in range(1, 8):
                            if Y + i > 7:
                                break
                            if self.Color(X, Y + i) == "Black":
                                break
                            Moves.append((X, Y, X, Y + i))
                            if self.Color(X, Y + i) == "White":
                                break
                        for i in range(1, 8):
                            if X - i < 0:
                                break
                            if self.Color(X - i, Y) == "Black":
                                break
                            Moves.append((X, Y, X - i, Y))
                            if self.Color(X - i, Y) == "White":
                                break
                        for i in range(1, 8):
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
                        for i in range(1, 8):
                            if X - i < 0 or Y - i < 0:
                                break
                            if self.Color(X - i, Y - i) == "Black":
                                break
                            Moves.append((X, Y, X - i, Y - i))
                            if self.Color(X - i, Y - i) == "White":
                                break
                        for i in range(1, 8):
                            if X + i > 7 or Y - i < 0:
                                break
                            if self.Color(X + i, Y - i) == "Black":
                                break
                            Moves.append((X, Y, X + i, Y - i))
                            if self.Color(X + i, Y - i) == "White":
                                break
                        for i in range(1, 8):
                            if X - i < 0 or Y + i > 7:
                                break
                            if self.Color(X - i, Y + i) == "Black":
                                break
                            Moves.append((X, Y, X - i, Y + i))
                            if self.Color(X - i, Y + i) == "White":
                                break
                        for i in range(1, 8):
                            if X + i > 7 or Y + i > 7:
                                break
                            if self.Color(X + i, Y + i) == "Black":
                                break
                            Moves.append((X, Y, X + i, Y + i))
                            if self.Color(X + i, Y + i) == "White":
                                break
                    if Peice == "♛":
                        for i in range(1, 8):
                            if Y - i < 0:
                                break
                            if self.Color(X, Y - i) == "Black":
                                break
                            Moves.append((X, Y, X, Y - i))
                            if self.Color(X, Y - i) == "White":
                                break
                        for i in range(1, 8):
                            if Y + i > 7:
                                break
                            if self.Color(X, Y + i) == "Black":
                                break
                            Moves.append((X, Y, X, Y + i))
                            if self.Color(X, Y + i) == "White":
                                break
                        for i in range(1, 8):
                            if X - i < 0:
                                break
                            if self.Color(X - i, Y) == "Black":
                                break
                            Moves.append((X, Y, X - i, Y))
                            if self.Color(X - i, Y) == "White":
                                break
                        for i in range(1, 8):
                            if X + i > 7:
                                break
                            if self.Color(X + i, Y) == "Black":
                                break
                            Moves.append((X, Y, X + i, Y))
                            if self.Color(X + i, Y) == "White":
                                break
                        for i in range(1, 8):
                            if X - i < 0 or Y - i < 0:
                                break
                            if self.Color(X - i, Y - i) == "Black":
                                break
                            Moves.append((X, Y, X - i, Y - i))
                            if self.Color(X - i, Y - i) == "White":
                                break
                        for i in range(1, 8):
                            if X + i > 7 or Y - i < 0:
                                break
                            if self.Color(X + i, Y - i) == "Black":
                                break
                            Moves.append((X, Y, X + i, Y - i))
                            if self.Color(X + i, Y - i) == "White":
                                break
                        for i in range(1, 8):
                            if X - i < 0 or Y + i > 7:
                                break
                            if self.Color(X - i, Y + i) == "Black":
                                break
                            Moves.append((X, Y, X - i, Y + i))
                            if self.Color(X - i, Y + i) == "White":
                                break
                        for i in range(1, 8):
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
                        if self.BlackKingMoved == False:
                            if self.A8RookMoved == False and self.Peice(X - 1, Y) == None and self.Peice(X - 2, Y) == None and self.Peice(X - 3, Y) == None:
                                Moves.append((X, Y, X - 2, Y))
                            if self.H8RookMoved == False and self.Peice(X + 1, Y) == None and self.Peice(X + 2, Y) == None:
                                Moves.append((X, Y, X + 2, Y))

        if FromGettingCheck == False:
            EditMoves = copy.deepcopy(Moves)
            OldBoard = copy.deepcopy(self.Board)
            for Move in Moves:
                self.MovePeice(*Move, CountMoveKing=False)
                if self.IsInCheck(Color):
                    EditMoves.remove(Move)
                self.MovePeice(Move[2], Move[3], Move[0], Move[1], CountMoveKing=False)
                self.Board = copy.deepcopy(OldBoard)
            Moves = EditMoves
            self.Board = OldBoard

        return Moves
    
    def GetLegalMovesForPeice(self, X, Y):
        Moves = []
        for Move in self.GetLegalMoves(self.Color(X, Y)):
            if Move[0] == X and Move[1] == Y:
                Moves.append(Move)

        return Moves