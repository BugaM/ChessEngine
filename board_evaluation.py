import chess
from chess.engine import SimpleEngine
from constants import piece_value
from constants import outcome_value
from game_logic import MATERIAL_EVAL


def material_evaluation(board):
    """
    Evaluates the white's advantage based on material and the outcome alone,
    doesn't take into account the position of the pieces.

    :param board: current chess board.
    :type board: chess.Board.
    :return: float.
    :rtype: chess.Move.
    """
    if board.is_game_over():
        if board.outcome().winner != chess.BLACK:
            return outcome_value[board.outcome().termination]
        else:
            return -outcome_value[board.outcome().termination]
    evaluation = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece == None:
            continue
        if piece.color == chess.WHITE:
            evaluation += piece_value[piece.piece_type]
        else:
            evaluation -= piece_value[piece.piece_type]
    return evaluation


def stockfish_evaluation(board, depth, side):
    with chess.engine.SimpleEngine.popen_uci('stockfish/stockfish_14_x64') as sf:
        result = sf.analyse(board, chess.engine.Limit(depth=depth))
        if side == chess.WHITE:
            evaluation = result['score'].white().score(mate_score=100000)
        else:
            evaluation = result['score'].black().score(mate_score=100000)
        return evaluation


evaluation_mode = {MATERIAL_EVAL: material_evaluation}



