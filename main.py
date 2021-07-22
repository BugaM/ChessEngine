from constants import WINDOW_LENGTH, WINDOW_HEIGHT, FREQUENCY
from graphics import display_screen
from input import game_input
from game_logic import make_move
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
    font = pygame.font.Font('freesansbold.ttf', 32)
    running = True
    board = chess.Board(chess.STARTING_BOARD_FEN)
    while running:
        clock.tick(FREQUENCY)
        display_screen(board, screen)
        if not board.is_game_over():
            make_move(board)
        running = game_input(board)
    pygame.quit()

if __name__ == "__main__":
        start_game()