from constants import WINDOW_HEIGHT, WINDOW_LENGTH, CHESS_BOARD_SIZE, SQUARE_SIZE
import random
import chess
import game_logic
import move_selection

board_position = ((WINDOW_LENGTH-CHESS_BOARD_SIZE)//2, (WINDOW_HEIGHT-CHESS_BOARD_SIZE)//2)

def get_square_from_pos(position):
    """
    Tells in which square the position is contained. Assumes that the position is within the board.

    :param positon: (x, y) coordinates of the position in the image .
    :type position: int tuple.
    :return: Square that contains that position.
    :rtype: chess.Square. 
    """
    return int(((position[0] - board_position[0])//SQUARE_SIZE)
            + 8*((board_position[1] + CHESS_BOARD_SIZE - position[1])//SQUARE_SIZE))

def mouse_in_chessboard(mouse_position):
    """
    Checks if the mouse is hovering over the chessboard.

    :param mouse_position: (x, y) coordinates of where the mouse is in the image 
    :type mouse_position: int tuple
    :return: If the mouse is hovering over the chessboard.
    :rtype: bool.
    """
    return (board_position[0] <= mouse_position[0] <= board_position[0] + CHESS_BOARD_SIZE 
            and board_position[1] <= mouse_position[1] <= board_position[1] + CHESS_BOARD_SIZE)


def random_player(board):
    move = random.choice(list(board.legal_moves))
    return move.uci()


def alpha_beta_player(board):
    return move_selection.alfa_beta_prunning(board, game_logic.MATERIAL_EVAL, game_logic.max_depth)


def stockfish_greedy(board):
    move = move_selection.stockfish_move(board, game_logic.MATERIAL_EVAL, game_logic.max_depth)
    return move.uci()


def who(player):
    return "White" if player == chess.WHITE else "Black"


def display_board(board, use_svg):
    if use_svg:
        return board._repr_svg_()
    else:
        return "<pre>" + str(board) + "</pre>"


def human_player(board):
    display(board)
    uci = get_move("%s's move [q to quit]> " % who(board.turn))
    legal_uci_moves = [move.uci() for move in board.legal_moves]
    while uci not in legal_uci_moves:
        print("Legal moves: " + (",".join(sorted(legal_uci_moves))))
        uci = get_move("%s's move[q to quit]> " % who(board.turn))
    return uci


def get_move(prompt):
    uci = input(prompt)
    if uci and uci[0] == "q":
        raise KeyboardInterrupt()
    try:
        chess.Move.from_uci(uci)
    except:
        uci = None
    return uci
