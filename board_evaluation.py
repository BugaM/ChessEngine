import chess
from chess.engine import SimpleEngine
from constants import piece_value
from constants import outcome_value
from game_logic import MATERIAL_EVAL, STOCKFISH_EVAL


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
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece == None:
            continue
        if piece.color == chess.WHITE:
            evaluation += piece_value[piece.piece_type]
        else:
            evaluation -= piece_value[piece.piece_type]
    return evaluation


def stockfish_evaluation(board, side, depth=5):
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
        if side == chess.WHITE:
            evaluation = result['score'].white().score(mate_score=outcome_value[chess.Termination.CHECKMATE])
        else:
            evaluation = result['score'].black().score(mate_score=outcome_value[chess.Termination.CHECKMATE])
        return evaluation


evaluation_mode = {MATERIAL_EVAL: material_evaluation,
                   STOCKFISH_EVAL: stockfish_evaluation}



