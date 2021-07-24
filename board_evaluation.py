import chess
from game_logic import max_depth
from chess.engine import SimpleEngine
from constants import piece_value, outcome_value, chess_pieces


def material_evaluation(board):
    """
    Evaluates the white's advantage based on material and the outcome alone,
    doesn't take into account the position of the pieces.

    :param board: current chess board.
    :type board: chess.Board.
    :return: Evaluation of the state considering material and outcome alone.
    :rtype: float.
    """
    if board.is_game_over():
        if board.outcome().winner != chess.BLACK:
            return outcome_value[board.outcome().termination]
        else:
            return -outcome_value[board.outcome().termination]
    evaluation = 0
    for piece_type in chess_pieces:
        evaluation += (piece_value[piece_type]
                       *(len(board.pieces(piece_type, chess.WHITE)) - len(board.pieces(piece_type, chess.BLACK))))
    return evaluation


def stockfish_evaluation(board, depth=max_depth - 1):
    """
    Evaluates advantage based on stockfish.

    :param board: Current chess board.
    :type board: chess.Board.
    :param side: Whoose turn it is.
    :type side: chess.Color.
    :param depth: Depth in which Stockfish analises the position.
    :type depth: int.
    :return: Evaluation of the state by stockfish.
    :rtype: float.
    """
    with chess.engine.SimpleEngine.popen_uci('stockfish/stockfish_14_x64') as sf:
        result = sf.analyse(board, chess.engine.Limit(depth=depth))
        evaluation = result['score'].white().score(mate_score=outcome_value[chess.Termination.CHECKMATE])
        return evaluation


# Evaluation Function Options
MATERIAL_EVAL = 0
STOCKFISH_EVAL = 1

evaluation_mode = {MATERIAL_EVAL: material_evaluation,
                   STOCKFISH_EVAL: stockfish_evaluation}
