from constants import FREQUENCY
import utils
import game_logic
import pygame          


def square_input_from_mouse(board):
    """
    Gets a square from a left mouse click in the board.

    :param board: Board in which chess is being played.
    :type board: chess.Board.
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
    


def game_input(board):
    """
    Gets and controls the inputs from the keyboard and mouse while playing chess.

    :param board: Board in which chess is being played.
    :type board: chess.Board.
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
                square_input_from_mouse()
