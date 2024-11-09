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
    # Return a random legal move
    return random.choice(LegalMoves)