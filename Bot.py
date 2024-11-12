from ChessBoard import ChessBoard
# ChessBoard.GetLegalMoves(Color) gets all legal moves for the given color
# ChessBoard.GetLegalMovesForPiece(X, Y) gets all legal moves for the piece at the given position
# ChessBoard.MovePiece(FromX, FromY, ToX, ToY) moves the piece at the given position to the new position
# ChessBoard.Color(X, Y) gets the color of the piece at the given position
# ChessBoard.PlayerInput(Input) converts a string input into a position tuple. eg. "a1" -> (0, 7) or "f6" -> (5, 2)
# ChessBoard.IsInCheck(Color) returns True if the given color is in check
# ChessBoard.FindKing(Color) returns the position of the king for the given color
# ChessBoard.BoardValue(Color) returns the value of the board for the given color

import random

# Reference the README.md for the function signature
def FindBestMove(Board, LegalMoves, Color = "Black"):
    BestMoves = []
    BestValue = None

    for Move in LegalMoves:
        TempBoard = Board.Copy()
        TempBoard.MovePeice(*Move)
        Value = TempBoard.BoardValue(Color)
        if BestValue == None or Value < BestValue:
            BestValue = Value
            BestMoves = [Move]
        elif Value == BestValue:
            BestMoves.append(Move)

    for Move in BestMoves:
        TempBoard = Board.Copy()
        TempBoard.MovePeice(*Move)

        for Move2 in TempBoard.GetLegalMoves(TempBoard.FlipColor(Color)):
            TempBoard2 = TempBoard.Copy()
            TempBoard2.MovePeice(*Move2)
            Value = TempBoard2.BoardValue(Color)

            if BestValue == None or Value < BestValue:
                BestValue = Value
                BestMoves = [Move]
            elif Value == BestValue:
                BestMoves.append(Move)

    print(BestMoves)
    return random.choice(BestMoves)