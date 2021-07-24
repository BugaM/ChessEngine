from constants import WINDOW_LENGTH, WINDOW_HEIGHT, FREQUENCY
from graphics import display_screen
from input import game_input
from game_logic import make_move, running
import pygame
import chess


def start_game():
    """
    Creates and controls a pygame enviroment for playing chess.
    """
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_LENGTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Chess Engine by Eric Guerra & Marcelo Buga")
    clock = pygame.time.Clock()
    board = chess.Board()
    while running[0]:
        clock.tick(FREQUENCY)
        display_screen(board, screen)
        if not board.is_game_over():
            make_move(board, screen)
        game_input(board, screen)
    pygame.quit()


if __name__ == "__main__":
        start_game()
