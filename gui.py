import pygame
from constants import PYGAME_WHITE, WINDOW_HEIGHT, WINDOW_LENGTH, CHESS_BOARD_SIZE, PYGAME_BLACK
import utils
import game_logic

FONT_SIZE = 24
PIXEL_GAP = 5

pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', FONT_SIZE)


def not_color_setting(player_color_setting):
    """
    """
    if player_color_setting == game_logic.PLAYER_BLACK:
        return game_logic.PLAYER_WHITE
    elif player_color_setting == game_logic.PLAYER_WHITE:
        return game_logic.PLAYER_BLACK
    else:
        return game_logic.PLAYER_RANDOM


def color_setting_str(player_color_setting):
    """
    """
    if player_color_setting == game_logic.PLAYER_BLACK:
        return "Black"
    elif player_color_setting == game_logic.PLAYER_WHITE:
        return "White"
    elif player_color_setting == game_logic.PLAYER_RANDOM:
        return "Random"


def selec_setting_str(player_setting_selec):
    """
    """
    if player_setting_selec == game_logic.HUMAN_MOVE:
        return "Human"
    elif player_setting_selec == game_logic.RANDOM_MOVE:
        return "Random AI"
    elif player_setting_selec == game_logic.ALPHA_BETA_MOVE:
        return "Alpha-Beta AI"
    elif player_setting_selec == game_logic.GREEDY_MOVE:
        return "Greedy AI"


def eval_setting_str(player_setting_selec, eval_setting_str):
    """
    """
    if (player_setting_selec == game_logic.HUMAN_MOVE
        or player_setting_selec == game_logic.RANDOM_MOVE):
        return "---"
    else:
        if eval_setting_str == game_logic.MATERIAL_EVAL:
            return "Material"
        elif eval_setting_str == game_logic.STOCKFISH_EVAL:
            return "Stockfish"


def ilegal_move_gui(screen):
    """
    """
    ilegal1_str = "Ilegal move."
    ilegal1_message = font.render(ilegal1_str, True, PYGAME_WHITE)
    ilegal1_size = font.size(ilegal1_str)
    ilegal1_placement = (((WINDOW_LENGTH-CHESS_BOARD_SIZE)//2 - ilegal1_size[0])//2, (WINDOW_HEIGHT - ilegal1_size[1])//2)
    screen.blit(ilegal1_message, ilegal1_placement)

    ilegal2_str = "Choose again."
    ilegal2_message = font.render(ilegal2_str, True, PYGAME_WHITE)
    ilegal2_size = font.size(ilegal2_str)
    ilegal2_placement = ((3*WINDOW_LENGTH + CHESS_BOARD_SIZE)//4 - ilegal2_size[0]//2, (WINDOW_HEIGHT - ilegal2_size[1])//2)
    screen.blit(ilegal2_message, ilegal2_placement)
    pygame.display.flip()


def options_gui(screen, selected_option, selected_player):
    """
    Shows the options and how to change them.

    :param screen: Screen in which the messages should be printed.
    :type screen: pygame.Surface.
    ::
    """
    screen.fill(PYGAME_BLACK)

    esc_str = "Esc: Back to chessboard"
    esc_message = font.render(esc_str, True, PYGAME_WHITE)
    esc_size = font.size(esc_str)
    esc_placement = ((WINDOW_LENGTH-esc_size[0])//2, WINDOW_HEIGHT - PIXEL_GAP - esc_size[1])
    screen.blit(esc_message, esc_placement)

    arr_str = "Arrow Keys: Change settings"
    arr_message = font.render(arr_str, True, PYGAME_WHITE)
    arr_size = font.size(arr_str)
    arr_placement = ((WINDOW_LENGTH-arr_size[0])//2, WINDOW_HEIGHT - 3*PIXEL_GAP - esc_size[1] - arr_size[1])
    screen.blit(arr_message, arr_placement)

    depth_str = "+/-: Change max depth ({})".format(game_logic.max_depth)
    depth_message = font.render(depth_str, True, PYGAME_WHITE)
    depth_size = font.size(depth_str)
    depth_placement = ((WINDOW_LENGTH-depth_size[0])//2, WINDOW_HEIGHT - 5*PIXEL_GAP - esc_size[1] - arr_size[1] - depth_size[1])
    screen.blit(depth_message, depth_placement)

    one_str = "Player 1: Press 1 to select."
    one_message = font.render(one_str, True, PYGAME_WHITE)
    one_size = font.size(one_str)
    one_placement = (PIXEL_GAP, PIXEL_GAP)
    screen.blit(one_message, one_placement)

    two_str = "Player 2: Press 2 to select."
    two_message = font.render(two_str, True, PYGAME_WHITE)
    two_size = font.size(two_str)
    two_placement = (PIXEL_GAP + WINDOW_LENGTH//2, PIXEL_GAP)
    screen.blit(two_message, two_placement)

    color1_str = "Color: {}".format(color_setting_str(game_logic.player1.color_setting))
    color1_message = font.render(color1_str, True, PYGAME_WHITE)
    color1_size = font.size(color1_str)
    color1_placement = (PIXEL_GAP, 3*PIXEL_GAP + one_size[1])
    screen.blit(color1_message, color1_placement)

    color2_str = "Color: {}".format(color_setting_str(not_color_setting(game_logic.player1.color_setting)))
    color2_message = font.render(color2_str, True, PYGAME_WHITE)
    color2_size = font.size(color2_str)
    color2_placement = (PIXEL_GAP + WINDOW_LENGTH//2, 3*PIXEL_GAP + two_size[1])
    screen.blit(color2_message, color2_placement)

    selec1_str = "Move Selector: {}".format(selec_setting_str(game_logic.player1.move_selec))
    selec1_message = font.render(selec1_str, True, PYGAME_WHITE)
    selec1_size = font.size(selec1_str)
    selec1_placement = (PIXEL_GAP, 5*PIXEL_GAP + one_size[1] + color1_size[1])
    screen.blit(selec1_message, selec1_placement)

    selec2_str = "Move Selector: {}".format(selec_setting_str(game_logic.player2.move_selec))
    selec2_message = font.render(selec2_str, True, PYGAME_WHITE)
    selec2_size = font.size(selec2_str)
    selec2_placement = (PIXEL_GAP + WINDOW_LENGTH//2, 5*PIXEL_GAP + two_size[1] + color2_size[1])
    screen.blit(selec2_message, selec2_placement)

    eval1_str = "Evaluation Mode: {}".format(eval_setting_str(game_logic.player1.move_selec, game_logic.player1.eval_func))
    eval1_message = font.render(eval1_str, True, PYGAME_WHITE)
    eval1_placement = (PIXEL_GAP, 7*PIXEL_GAP + one_size[1] + color1_size[1] + selec1_size[1])
    screen.blit(eval1_message, eval1_placement)

    eval2_str = "Evaluation Mode: {}".format(eval_setting_str(game_logic.player2.move_selec, game_logic.player2.eval_func))
    eval2_message = font.render(eval2_str, True, PYGAME_WHITE)
    eval2_placement = (PIXEL_GAP + WINDOW_LENGTH//2, 7*PIXEL_GAP  + two_size[1] + color2_size[1] + selec2_size[1])
    screen.blit(eval2_message, eval2_placement)

    chosen_position = (PIXEL_GAP//2 + (WINDOW_LENGTH//2)*(selected_player-1),
                       PIXEL_GAP*(2*selected_option+3) + (selected_option)*(one_size[1]) + 3*one_size[1]//2)
    pygame.draw.circle(screen, PYGAME_WHITE, chosen_position, PIXEL_GAP//2)


def game_gui(board, screen):
    """
    Shows whoose turn it is or if the game is over, the outcome and the winner.
    Also shows on screen the hotkeys to use the program.

    :param board: Board in which chess is being played.
    :type board: chess.Board.
    :param screen: Screen in which the messages should be printed.
    :type screen: pygame.Surface.
    """
    if board.is_game_over():
        if board.is_checkmate():
            top_str = "Checkmate! {} wins.".format(utils.who(not board.turn))
        else:
            top_str = "Draw!"
    else:
        top_str = "{}'s turn.".format(utils.who(board.turn))
    top_message = font.render(top_str, True, PYGAME_WHITE)
    top_size = font.size(top_str)
    top_placement = ((WINDOW_LENGTH-top_size[0])//2, ((WINDOW_HEIGHT-CHESS_BOARD_SIZE)//2 - top_size[1])//2)
    screen.blit(top_message, top_placement)

    r_str = "R: Reset Board"
    r_size = font.size(r_str)
    r_message = font.render(r_str, True, PYGAME_WHITE)
    r_placement = (WINDOW_LENGTH - PIXEL_GAP - r_size[0], WINDOW_HEIGHT - PIXEL_GAP - r_size[1])
    screen.blit(r_message, r_placement)

    esc_str = "Esc: Options Menu (Resets game)"
    esc_message = font.render(esc_str, True, PYGAME_WHITE)
    esc_size = font.size(esc_str)
    esc_placement = (PIXEL_GAP, WINDOW_HEIGHT - PIXEL_GAP - esc_size[1])
    screen.blit(esc_message, esc_placement)
