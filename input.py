from constants import FREQUENCY
import utils
import graphics
import game_logic
import pygame          

NUMBER_OF_OPTIONS = 3

def square_input_from_mouse(board, screen):
    """
    Gets a square from a left mouse click in the board.

    :param board: Board in which chess is being played.
    :type board: chess.Board.
    :param screen: Pygame screen.
    :type screen: pygame.Surface.
    :return: The square that was clicked.
    :rtype: chess.Square.
    """
    clock = pygame.time.Clock()
    while True:
        clock.tick(FREQUENCY)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if utils.mouse_in_chessboard(mouse_position):
                    return utils.get_square_from_pos(mouse_position)
            elif event.type == pygame.QUIT:
                game_logic.running[0] = False
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_logic.reset_board(board)
                    return None
                elif event.key == pygame.K_ESCAPE:
                    graphics.display_options(board, screen)
    


def game_input(board, screen):
    """
    Gets and controls the inputs from the keyboard and mouse while playing chess.

    :param board: Board in which chess is being played.
    :type board: chess.Board.
    :param screen: Pygame screen.
    :type screen: pygame.Surface.
    :return: If the pygame window should remain opened.
    :rtype: bool.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_logic.running[0] = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_logic.reset_board(board)
            elif event.key == pygame.K_ESCAPE:
                graphics.display_options(board, screen)

def options_input(selected_option, selected_player, board):
    """
    Controls the inputs in the options screen.

    :param selected_player: Which player whose setting is selected.
    :type selected_player: int.
    :param selected_option: Which option setting is selected,
    i. e, color, move selector and evaluation function.
    :type selected_option: int.
    :param board: Board in which chess is being played.
    :type board: chess.Board.
    :return selected_player: Updated selected player.
    :rtype selected_player: int.
    :return selected_option: Updated selected option.
    :rtype selected_option: int.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_logic.running[0] = False
            graphics.options_running[0] = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_option -= 1
                if selected_option < 0:
                    selected_option = NUMBER_OF_OPTIONS - 1
            elif event.key == pygame.K_DOWN:
                selected_option += 1
                if selected_option >= NUMBER_OF_OPTIONS:
                    selected_option = 0
            elif event.key == pygame.K_LEFT:
                game_logic.decrease_option(selected_player, selected_option)
            elif event.key == pygame.K_RIGHT:
                game_logic.increase_option(selected_player, selected_option)
            elif event.key == pygame.K_1:
                selected_player = 1
            elif event.key == pygame.K_2:
                selected_player = 2
            elif event.key == pygame.K_ESCAPE:
                game_logic.reset_board(board)
                graphics.options_running[0] = False
            elif event.key == pygame.K_EQUALS:
                game_logic.increase_depth()
            elif event.key == pygame.K_MINUS:
                game_logic.decrease_depth()
    return selected_option, selected_player
