from math import inf
from math import fabs
from constants import EPSILON
from board_evaluation import evaluation_mode
from input import square_input_from_mouse
import gui
import random
import chess


def human_move(board, eval_mode, max_depth, screen):
    """
    Lets the human player choose a legal move.

    :param board: current chess board.
    :type board: chess.Board.
    :param eval_mode: unused value for compatibility.
    :type eval_mode: int key for dictionary.
    :param max_depth: unused value for compatibility.
    :type max_depth: int.
    :param screen: Pygame screen.
    :type screen: pygame.Surface.
    :return: selected move.
    :rtype: chess.Move.
    """
    from_square = square_input_from_mouse(board, screen)
    if from_square == None:
        return None
    to_square = square_input_from_mouse(board, screen)
    if to_square == None:
        return None
    try:
        move = board.find_move(from_square, to_square)
        move_is_legal = True
    except:
        move_is_legal = False
    while not move_is_legal:
        gui.ilegal_move_gui(screen)
        from_square = square_input_from_mouse(board, screen)
        if from_square == None:
            return None
        to_square = square_input_from_mouse(board, screen)
        if to_square == None:
            return None
        try:
            move = board.find_move(from_square, to_square)
            move_is_legal = True
        except:
            move_is_legal = False
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


def quiesce(board, eval_mode, alpha, beta):
    """
    Does Quiescence Search at the leaf node so the AI only evaluates quiet positions,
    i. e., when no captures happen. Mitigates the Horizon Effect.

    :param board: current chess board.
    :type board: chess.Board.
    :param alpha: lower bound scenario for the agent.
    :type alpha: float.
    :param beta: upper bound scenario for the agent's opponent.
    :type beta: flotat.
    :param depth_left: the depth left to reach the maximum depth.
    :type depth_left: int.
    :return: value for the state.
    :rtype: float.
    """
    if board.turn == chess.WHITE:
        current_eval = evaluation_mode[eval_mode](board)
    else:
        current_eval = -evaluation_mode[eval_mode](board)
    if current_eval >= beta :
        return beta
    alpha = max(alpha, current_eval)
    for move in board.legal_moves:
        if board.is_capture(move):
            board.push(move)
            value = -quiesce(board, eval_mode, -beta, -alpha)
            board.pop()
            if value >= beta:
                return beta
            alpha = max(alpha, value)  
    return alpha

def negamax(board, eval_mode, alpha, beta, depth_left):
    """
    Uses the Negamax algorithm with alpha-beta pruning to find the best value of the position in the worst case scenario.
    
    :param board: current chess board.
    :type board: chess.Board.
    :param alpha: lower bound scenario for the agent.
    :type alpha: float.
    :param beta: upper bound scenario for the agent's opponent.
    :type beta: flotat.
    :param depth_left: the depth left to reach the maximum depth.
    :type depth_left: int.
    :return: value for the state.
    :rtype: float.
    """
    if depth_left <= 0 or board.is_game_over():
        return quiesce(board, eval_mode, alpha, beta)
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


def minimax_move(board, eval_mode, max_depth):
    best_move = random.choice(list(board.legal_moves))
    board.push(best_move)
    best_value = minimax(board, eval_mode, max_depth, board.turn, -inf, inf)
    board.pop()
    for move in board.legal_moves:
        board.push(move)
        value = minimax(board, eval_mode, max_depth, board.turn, -inf, inf)
        board.pop()
        if (board.turn == chess.WHITE and value > best_value) or (board.turn == chess.BLACK and value < best_value):
            best_value = value
            best_move = move
    return best_move


def minimax(board, eval_mode, depth_left, side, alpha, beta):

    if depth_left == 0 or board.is_game_over():
        return evaluation_mode[eval_mode](board)

    if board.turn is not side:  # check if this is right
        max_evaluation = -inf
        for move in board.legal_moves:
            board.push(move)
            evaluation = minimax(board, eval_mode, depth_left - 1, side, alpha, beta)
            board.pop()
            max_evaluation = max(max_evaluation, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                return max_evaluation
        return max_evaluation

    else:
        min_evaluation = inf
        for move in board.legal_moves:
            board.push(move)
            evaluation = minimax(board, eval_mode, depth_left - 1, side, alpha, beta)
            board.pop()
            min_evaluation = min(min_evaluation, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:
                return min_evaluation
        return min_evaluation


def greedy_move(board, eval_mode, max_depth):
    """
    Chooses the greedy move, i. e, the one that will maximize the evaluation function next ply.

    :param board: current chess board.
    :type board: chess.Board.
    :param eval_mode: unused value for compatibility.
    :type eval_mode: int key for dictionary.
    :param max_depth: max depth for the search tree.
    :type max_depth: int.
    :return: Greedy selected move.
    :rtype: chess.Move.
    """
    best_move = random.choice(list(board.legal_moves))
    board.push(best_move)
    best_value = evaluation_mode[eval_mode](board)
    board.pop()
    for move in board.legal_moves:
        board.push(move)
        value = evaluation_mode[eval_mode](board)
        board.pop()
        if (board.turn == chess.WHITE and value > best_value) or (board.turn == chess.BLACK and value < best_value):
            best_value = value
            best_move = move
    return best_move

# Move Selector Options
HUMAN_MOVE = 0
RANDOM_MOVE = 1
ALPHA_BETA_MOVE = 2
GREEDY_MOVE = 3
MINIMAX_MOVE = 4

selection_mode = {HUMAN_MOVE: human_move, RANDOM_MOVE: random_move,
                  ALPHA_BETA_MOVE: alpha_beta_prunning,
                  GREEDY_MOVE: greedy_move,
                  MINIMAX_MOVE: minimax_move}
