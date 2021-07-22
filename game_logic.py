from move_selection import HUMAN_MOVE, RANDOM_MOVE, ALFA_BETA_MOVE, GREEDY_MOVE
from move_selection import selection_mode
from board_evaluation import MATERIAL_EVAL, STOCKFISH_EVAL
import chess
import random

# Player Color
PLAYER_BLACK = 0
PLAYER_WHITE = 1
PLAYER_RANDOM = 2

# Game Settings
white_player_human = False
black_player_human = False
max_depth = 3

class ChessPlayer:
    """
    Represents a chess player by its color, move selection policy and position evaluation function.
    """
    def __init__(self, color_setting, move_selec, eval_func):
        """
        Constructor for the player.

        :param color_setting: The chosen color setting for the player.
        :type color_setting: int.
        :param move_selec: The chosen move selection function.
        :type move_selec: int key for dictionary.
        :param eval_func: The chosen function for evaluation.
        :type eva_function: int key for dictionary.
        """
        self.color_setting = color_setting
        self.color = self.get_color()
        self.move_selec = move_selec
        self.eval_func = eval_func
    

    def get_color(self):
        """
        Sets the player color according to setting. If random, choses sets a random color.
        """
        if self.color_setting == PLAYER_RANDOM:
            return random.choice([PLAYER_BLACK, PLAYER_WHITE])
        else:
            return self.color_setting
    

    def get_oponent_color(self):
        """
        Gets its oponents color.
        """
        if self.color == PLAYER_BLACK:
            return PLAYER_WHITE
        else:
            return PLAYER_BLACK
    

    def get_player_move(self, board):
        """
        Gets the move made by the player by following the selected move policy with the selected evaluation.
        """
        return selection_mode[self.move_selec](board, self.eval_func, max_depth)

            
player1 = ChessPlayer(PLAYER_RANDOM, HUMAN_MOVE, MATERIAL_EVAL)
player2 = ChessPlayer(player1.get_oponent_color(), ALFA_BETA_MOVE, MATERIAL_EVAL)


def make_move(board):
    """
    Makes the move of the turn's player.

    :param board: Board in which the move is made.
    :type board: chess.Board.
    """
    if board.turn == player1.color:
        board.push(player1.get_player_move(board))
    else:
        board.push(player2.get_player_move(board))


def reset_board(): # TODO Not working
    """
    Resets the board to the inital positon.

    :return: Reset board.
    :type board: chess.Board.
    """
    global player1
    global player2
    player1.color = player1.get_color()
    player2.color = player1.get_oponent_color()
    return chess.Board(chess.STARTING_BOARD_FEN)
