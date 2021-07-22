from constants import FREQUENCY
import utils
import game_logic
import pygame

def square_input_from_mouse(): # TODO Find a way for it not to "freeze" pygame
    """
    Gets a square from a left mouse click in the board.

    :return: The square that was clicked.
    :rtype: chess.Square.
    """
    clock = clock = pygame.time.Clock()
    while True:
        clock.tick(FREQUENCY)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if utils.mouse_in_chessboard(mouse_position):
                    return utils.get_square_from_pos(mouse_position)
            elif event.type == pygame.QUIT: # TODO Improve this
                pygame.quit()
    


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
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                board = game_logic.reset_board()
            elif event.key == pygame.K_ESCAPE:
                square_input_from_mouse()
    return True
