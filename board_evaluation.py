import chess
from constants import Piece_Value
from constants import Outcome_Value

def materialEvaluation(board):
    if board.is_game_over():
        if board.outcome().winner != chess.BLACK:
            return Outcome_Value[board.outcome().termination]
        else:
            return -Outcome_Value[board.outcome().termination]
    evaluation = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece == None:
            continue
        if piece.color == chess.WHITE:
            evaluation += Piece_Value[piece.piece_type]
        else:
            evaluation -= Piece_Value[piece.piece_type]
    return evaluation