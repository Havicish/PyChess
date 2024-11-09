I got the idea for this repo from Sebastian Lague's mini chess bot challenge.



How to use this repo:
    Code your bot in the Bot.py file.
    Run the RunChess.py file to test your bot.
    Run the TokenCounter.py file to count the number of tokens that your bot uses.
    You shouldn't need to manualy install any dependancies (other than python), because they will auto install.



@function FindBestMove: Called when it's your bot's turn to move
@param Board: A ChessBoard object
@param LegalMoves: List of tuples representing the legal moves
    eg. [(4, 6, 4, 5), (4, 6, 4, 4)] all the moves that e2 could play on move 0 as white
@param Color: The color that your bot is playing as
@return: Return a legal move
    eg. (4, 6, 4, 4) e2 -> e4 on move 0 as white. If your bot returns an illegal move, you will get an error.



This is what a ChessBoard.Board list looks like:
    8[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
    7 (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1),
    6 (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2),
    5 (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3),
    4 (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4),
    3 (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5),
    2 (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6),
    1 (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)]
        a       b       c       d       e       f       g       h