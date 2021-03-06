from move_selection import HUMAN_MOVE, RANDOM_MOVE, ALPHA_BETA_MOVE, GREEDY_MOVE
from move_selection import selection_mode
from board_evaluation import MATERIAL_EVAL, STOCKFISH_EVAL
import chess
import random

# Player Color
PLAYER_BLACK = 0
PLAYER_WHITE = 1
PLAYER_RANDOM = 2

# Game Settings
running = [True]
white_player_human = False
black_player_human = False
max_depth = 4

# Help to change options
MIN_COLOR = PLAYER_BLACK
MAX_COLOR = PLAYER_RANDOM

MIN_EVAL = MATERIAL_EVAL
MAX_EVAL = STOCKFISH_EVAL

MIN_SELEC = HUMAN_MOVE
MAX_SELEC = GREEDY_MOVE


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
        Sets the player color according to setting. If random, chooses sets a random color.
        """
        if self.color_setting == PLAYER_RANDOM:
            return random.choice([PLAYER_BLACK, PLAYER_WHITE])
        else:
            return self.color_setting

    def get_oponent_color(self):
        """
        Gets its oponent's color.
        """
        if self.color == PLAYER_BLACK:
            return PLAYER_WHITE
        else:
            return PLAYER_BLACK

    def get_player_move(self, board, screen=None):
        """
        Gets the move made by the player by following the selected move policy with the selected evaluation.

        :param board: Board in which the move is made.
        :type board: chess.Board.
        :param screen: Pygame screen.
        :type screen: pygame.Surface.
        :return: Move to be made by the player.
        :rtype: chess.Move.
        """
        if self.move_selec == HUMAN_MOVE:
            return selection_mode[self.move_selec](board, self.eval_func, max_depth - 1, screen)
        return selection_mode[self.move_selec](board, self.eval_func, max_depth - 1)

            
player1 = ChessPlayer(PLAYER_RANDOM, HUMAN_MOVE, MATERIAL_EVAL)
player2 = ChessPlayer(player1.get_oponent_color(), ALPHA_BETA_MOVE, MATERIAL_EVAL)


def make_move(board, screen):
    """
    Makes the move of the turn's player.

    :param board: Board in which the move is made.
    :type board: chess.Board.
    :param screen: Pygame screen.
    :type screen: pygame.Surface.
    """
    if board.turn == player1.color:
        move = player1.get_player_move(board, screen)
    else:
        move = player2.get_player_move(board, screen)
    if move != None:
        board.push(move)


def reset_board(board):
    """
    Resets the board to the inital positon.

    :param board: Board to be reset.
    :type board: chess.Board.
    """
    global player1
    global player2
    player1.color = player1.get_color()
    player2.color = player1.get_oponent_color()
    board.reset()


def increase_option(selected_player, selected_option):
    """
    Changes the selected option setting to the right.

    :param selected_player: Which player to change the setting.
    :type selected_player: int.
    :param selected_option: Which option to change the setting,
    i. e, color, move selector and evaluation function.
    :type selected_option: int.
    """
    global player1
    global player2
    if selected_option == 0: # Color
        if selected_player == 1:
            player1.color_setting = min(player1.color_setting+1, MAX_COLOR)
        else:
            player1.color_setting = max(player1.color_setting-1, MIN_COLOR)
    elif selected_option == 1: # Selection Mode
        if selected_player == 1:
            player1.move_selec = min(player1.move_selec+1, MAX_SELEC)
        else:
            player2.move_selec = min(player2.move_selec+1, MAX_SELEC)
    else:
        if selected_player == 1:
            player1.eval_func = min(player1.eval_func+1, MAX_EVAL)
        else:
            player2.eval_func = min(player2.eval_func+1, MAX_EVAL)


def decrease_option(selected_player, selected_option):
    """
    Changes the selected option setting to the left.

    :param selected_player: Which player to change the setting.
    :type selected_player: int.
    :param selected_option: Which option to change the setting,
    i. e, color, move selector and evaluation function.
    :type selected_option: int.
    """
    global player1
    global player2
    if selected_option == 0: # Color
        if selected_player == 2:
            player1.color_setting = min(player1.color_setting+1, MAX_COLOR)
        else:
            player1.color_setting = max(player1.color_setting-1, MIN_COLOR)
    elif selected_option == 1: # Selection Mode
        if selected_player == 1:
            player1.move_selec = max(player1.move_selec-1, MIN_SELEC)
        else:
            player2.move_selec = max(player2.move_selec-1, MIN_SELEC)
    else:
        if selected_player == 1:
            player1.eval_func = max(player1.eval_func-1, MIN_EVAL)
        else:
            player2.eval_func = max(player2.eval_func-1, MIN_EVAL)


def increase_depth():
    """
    Increases max depth by one.
    """
    global max_depth
    max_depth += 1


def decrease_depth():
    """
    Decreases max depth by one.
    """
    global max_depth
    max_depth -= 1
