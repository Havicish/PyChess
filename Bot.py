from ChessBoard import ChessBoard
# ChessBoard.GetLegalMoves(Color) gets all legal moves for the given color
# ChessBoard.GetLegalMovesForPiece(X, Y) gets all legal moves for the piece at the given position
# ChessBoard.MovePiece(FromX, FromY, ToX, ToY) moves the piece at the given position to the new position
# ChessBoard.Color(X, Y) gets the color of the piece at the given position
# ChessBoard.PlayerInput(Input) converts a string input into a position tuple. eg. "a1" -> (0, 7) or "f6" -> (5, 2)
# ChessBoard.IsInCheck(Color) returns True if the given color is in check
# ChessBoard.FindKing(Color) returns the position of the king for the given color
# ChessBoard.BoardValue(Color) returns the value of the board for the given color
# ChessBoard.PieceValue(X, Y) returns the value of the piece at given position

import random
import copy

# Reference the README.md for the function signature
def FindBestMove(Board: ChessBoard, LegalMoves, Color = "Black"):
    BestValue = Board.BoardValue(Color)
    BestMoves = []
    SafeMoves = []

    # Function to check if a position is attacked by the opponent
    def IsPositionSafe(Board, X, Y, OpponentColor):
        OpponentMoves = Board.GetLegalMoves(OpponentColor)
        for move in OpponentMoves:
            _, _, attackX, attackY = move
            if attackX == X and attackY == Y:
                return False
        return True

    OpponentColor = "White" if Color == "Black" else "Black"

    for Move in LegalMoves:
        FromX, FromY, ToX, ToY = Move
        TargetPieceValue = Board.PieceValue(ToX, ToY)
        CapturingPieceValue = Board.PieceValue(FromX, FromY)

        # Check if it's a favorable capture
        if Board.Color(ToX, ToY) != Color and TargetPieceValue >= CapturingPieceValue:
            NewBoard = Board.Copy()
            NewBoard.MovePiece(FromX, FromY, ToX, ToY)
            NewBoardValue = NewBoard.BoardValue(Color)

            if NewBoardValue > BestValue:
                BestMoves = [Move]
                BestValue = NewBoardValue
            elif NewBoardValue == BestValue:
                BestMoves.append(Move)
        else:
            # If not a capture, ensure the piece is not moving into danger
            NewBoard = Board.Copy()
            NewBoard.MovePiece(FromX, FromY, ToX, ToY)
            if IsPositionSafe(NewBoard, ToX, ToY, OpponentColor):
                SafeMoves.append(Move)

    # Prioritize favorable captures
    if BestMoves:
        return random.choice(BestMoves)
    
    # If no favorable captures, choose from safe moves
    if SafeMoves:
        return random.choice(SafeMoves)

    # If no safe moves, fallback to any legal move
    return random.choice(LegalMoves)