from os import system as sys
from time import sleep
from ChessBoard import ChessBoard
import copy
import Bot

Board = ChessBoard()
Board.PrintBoard()

Sleep = 0
TMoves = 0
while TMoves < 99999999:
    while True:
        Input = input("Select peice to move: ")
        if Input == "Debug":
            sys("clear")
            print(Board.GetLegalMovesForPeice(*Board.PlayerInput(input("Select peice: "))))
            input("Enter to continue")
            Board.PrintBoard()
            continue
        PeiceToMove = Board.PlayerInput(Input)
        if PeiceToMove == None or Board.Color(*PeiceToMove) != "White":
            sys("clear")
            print("Illegal move")
            sleep(2)
            Board.PrintBoard()
            continue
        Board.PrintBoard(PeiceToMove)
        MovePeiceTo = Board.PlayerInput(input("Select where to move: "))
        LegalMoves = Board.GetLegalMovesForPeice(*PeiceToMove)
        if LegalMoves.__len__() <= 0:
            Board.PrintBoard(MatedColor="White")
            print("Checkmate!")
            exit()
        NewList = []
        for Move in LegalMoves:
            NewList.append((Move[2], Move[3]))
        LegalMoves = copy.deepcopy(NewList)
        if MovePeiceTo in LegalMoves:
            Board.MovePeice(PeiceToMove[0], PeiceToMove[1], MovePeiceTo[0], MovePeiceTo[1])
            break
        else:
            sys("clear")
            print("Illegal move")
            sleep(2)
        Board.PrintBoard()
    sleep(Sleep)
    TMoves = round(TMoves + .5, 1)

    LegalMoves = Board.GetLegalMoves("Black")
    if LegalMoves.__len__() <= 0:
        Board.PrintBoard(MatedColor="Black")
        print("Checkmate!")
        exit()
    try:
        BotsMove = Bot.FindBestMove(copy.deepcopy(Board), Board.GetLegalMoves("Black"), "Black")
        if BotsMove not in LegalMoves:
            raise ValueError(f"Your bot returned an illegal move: {BotsMove}")
        Board.MovePeice(*BotsMove)
    except TypeError:
        raise TypeError("Your bot returned something that isn't iterable.")
    Board.PrintBoard()
    sleep(Sleep)
    TMoves = round(TMoves + .5, 1)