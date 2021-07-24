from constants import WINDOW_HEIGHT, WINDOW_LENGTH, CHESS_BOARD_SIZE, SQUARE_SIZE
import chess
import game_logic

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



def who(player):
    return "White" if player == chess.WHITE else "Black"



