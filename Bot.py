from Chess import GetLegalMoves # GetLegalMoves(Color) gets all legal moves for the given color
from Chess import GetLegalMovesForPiece # GetLegalMovesForPiece(X, Y) gets all legal moves for the piece at the given position

import random

# Reference the README.md for the function signature
def FindBestMove(Board, LegalMoves, Color):
    # Return a random legal move
    return random.choice(LegalMoves)