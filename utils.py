import random
import chess
import game_logic
import move_selection


def random_player(board):
    move = random.choice(list(board.legal_moves))
    return move.uci()

def alpha_beta_player(board):
    return move_selection.alfa_beta_prunning(board, game_logic.MATERIAL_EVAL, game_logic.max_depth)

def stockfish_greedy(board):
    move = move_selection.stockfish_move(board, 10)
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
