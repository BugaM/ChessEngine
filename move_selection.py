from math import inf
from math import fabs
from constants import EPSILON
from board_evaluation import stockfish_evaluation, evaluation_mode
from input import square_input_from_mouse
import random
import chess




def human_move(board, eval_mode, max_depth): # TODO Promotions
    """
    Lets the human player choose a legal move.

    :param board: current chess board.
    :type board: chess.Board.
    :param eval_mode: unused value for compatibility.
    :type eval_mode: int key for dictionary.
    :param max_depth: unused value for compatibility.
    :type max_depth: int.
    :return: selected move.
    :rtype: chess.Move.
    """
    promotion = None
    from_square = square_input_from_mouse()
    to_square = square_input_from_mouse()
    move = chess.Move(from_square, to_square, promotion)
    move_is_legal = board.is_legal(move)
    while not move_is_legal:
        print("Move not legal, chose another one.")
        from_square = square_input_from_mouse()
        to_square = square_input_from_mouse()
        move = chess.Move(from_square, to_square, promotion)
        move_is_legal = board.is_legal(move)
    return move


def random_move(board, eval_mode, max_depth):
    """
    Chooses a random legal move.

    :param board: current chess board.
    :type board: chess.Board.
    :param eval_mode: unused value for compatibility.
    :type eval_mode: int key for dictionary.
    :param max_depth: unused value for compatibility.
    :type max_depth: int.
    :return: selected random move.
    :rtype: chess.Move.
    """
    return random.choice(list(board.legal_moves))


def negamax(board, eval_mode, alpha, beta, depth_left):
    """
    Uses the Negamax algorithm with alpha-beta pruning to find the best value of the position in the worst case scenario.
    
    :param board: current chess board.
    :type board: chess.Board.
    :param alpha: worst case scenario for the agent.
    :type alpha: float.
    :param beta: best case scenario for the agent's opponent.
    :type beta: flotat.
    :param depth_left: the depth left to reach the maximum depth.
    :type depth_left: int.
    :return: value for the state.
    :rtype: float.
    """
    if depth_left == 0 or board.is_game_over():
        if board.turn == chess.WHITE:
            return evaluation_mode[eval_mode](board)
        else:
            return -evaluation_mode[eval_mode](board)
    value = -inf
    for move in board.legal_moves:
        board.push(move)
        value = max(value, -negamax(board, eval_mode, -beta, -alpha, depth_left-1))
        board.pop()
        alpha = max(alpha, value)
        if alpha >= beta:
            break
    return value


def alpha_beta_prunning(board, eval_mode, max_depth):
    """
    Chooses a random best move according to the search tree of max_depth and evaluation function.

    :param board: current chess board.
    :type board: chess.Board.
    :param eval_mode: which function to use for evaluation.
    :type eval_mode: int key for dictionary.
    :param max_depth: max depth for the search tree.
    :type max_depth: int.
    :return: selected random best move.
    :rtype: chess.Move.
    """
    best_moves = []
    best_value = -inf
    alpha = -inf
    beta = inf
    for move in board.legal_moves:
        board.push(move)
        value = -negamax(board, eval_mode, -beta, -alpha, max_depth-1)
        board.pop()
        if value > alpha:
            alpha = value
        if value > best_value:
            best_value = value
            best_moves.clear()
            best_moves.append(move)
        elif fabs(best_value-value) < EPSILON:
            best_moves.append(move)
    return random.choice(best_moves)


def greedy_move(board, eval_mode, max_depth):
    """
    Chooses the best move according to stockfish.

    :param board: current chess board.
    :type board: chess.Board.
    :param eval_mode: unused value for compatibility.
    :type eval_mode: int key for dictionary.
    :param max_depth: max depth for the search tree.
    :type max_depth: int.
    :return: stockfish selected move.
    :rtype: chess.Move.
    """
    best_move = random.choice(list(board.legal_moves))
    test_board = board.copy()
    test_board.push_uci(best_move.uci())
    best_value = evaluation_mode[eval_mode](test_board)
    for move in board.legal_moves:
        test_board = board.copy()
        test_board.push_uci(move.uci())
        value = evaluation_mode[eval_mode](test_board)
        if (board.turn == chess.WHITE and value > best_value) or (board.turn == chess.BLACK and value < best_value):
            best_value = value
            best_move = move
    return best_move

# Move Selector Options
HUMAN_MOVE = 0
RANDOM_MOVE = 1
ALPHA_BETA_MOVE = 2
GREEDY_MOVE = 3

selection_mode = {HUMAN_MOVE: human_move, RANDOM_MOVE: random_move,
                  ALPHA_BETA_MOVE: alpha_beta_prunning,
                  GREEDY_MOVE: greedy_move}
