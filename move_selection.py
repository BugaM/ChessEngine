from math import inf
from math import fabs
from game_logic import PLAYER_MOVE, RANDOM_MOVE, ALFA_BETA_MOVE
from constants import EPSILON
import random
import chess
import board_evaluation


def player_move():
    # TODO
    return


def random_move(board, eval_mode, max_depth):
    """
    Chooses a random legal move.

    :param board: current chess board.
    :type board: chess.Board.
    :return: selected random move.
    :rtype: chess.Move.
    """
    return random.choice(list(board.legal_moves))


def negamax(board, eval_mode, alpha, beta, depth_left):
    """
    Uses the Negamax algorithm with alpha-beta pruning to find the best value of the position in the worst case scenario.
    
    :param board: current chess board.
    :type board: chess.Board.
    :param alpha: which function to use for evaluation.
    :return: selected random move.
    :rtype: chess.Move.
    """
    if depth_left == 0 or board.is_game_over():
        if board.turn == chess.WHITE:
            return board_evaluation.evaluation_mode[eval_mode](board)
        else:
            return -board_evaluation.evaluation_mode[eval_mode](board)
    value = -inf
    for move in board.legal_moves:
        board.push(move)
        value = max(value, -negamax(board, eval_mode, -beta, -alpha, depth_left-1))
        board.pop()
        alpha = max(alpha, value)
        if beta >= alpha:
            break
    return value


def alfa_beta_prunning(board, eval_mode, max_depth):
    """
    Chooses a random best move according to the search tree of max_depth and evaluation function.

    :param board: current chess board.
    :type board: chess.Board.
    :param eval_mode: which function to use for evaluation.
    :type eval_mode: int
    :return: selected random move.
    :rtype: chess.Move.
    """
    best_moves = []
    best_value = -inf
    alpha = -inf
    beta = inf
    for move in board.legal_moves:
        board.push(move)
        value = negamax(board, eval_mode, alpha, beta, max_depth)
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


def stockfish_move(board, depth):
    best_move = random.choice(list(board.legal_moves))
    test_board = board.copy()
    test_board.push_uci(best_move.uci())
    best_value = board_evaluation.stockfish_evaluation(test_board, depth, board.turn)
    for move in board.legal_moves:
        test_board = board.copy()
        test_board.push_uci(move.uci())
        value = board_evaluation.stockfish_evaluation(test_board, depth, board.turn)
        if value > best_value:
            best_value = value
            best_move = move
    return best_move


selection_mode = {PLAYER_MOVE: player_move, RANDOM_MOVE: random_move, ALFA_BETA_MOVE: alfa_beta_prunning}

