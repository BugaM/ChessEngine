import random

def randomMove(board):
    return random.choice(list(board.legal_moves))