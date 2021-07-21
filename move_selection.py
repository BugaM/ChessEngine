import random

def random_move(board):
    """
    Chooses a random legal move.

    :param board: current chess board.
    :type board: chess.Board.
    :return: selected random move.
    :rtype: chess.Move.
    """
    return random.choice(list(board.legal_moves))
