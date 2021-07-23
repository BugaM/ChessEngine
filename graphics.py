from constants import FREQUENCY, SQUARE_SIZE, PYGAME_BLACK, chess_pieces, chess_colors
from utils import board_position
import input
import gui
import chess
import pygame

MAX_RANK = 7

options_running = [True]

# Loading Assets
board_background = pygame.image.load("assets/board.png")

white_pawn_in_white = pygame.image.load("assets/WhiteWhitePawn.png")
white_knight_in_white = pygame.image.load("assets/WhiteWhiteKnight.png")
white_bishop_in_white = pygame.image.load("assets/WhiteWhiteBishop.png")
white_rook_in_white = pygame.image.load("assets/WhiteWhiteRook.png")
white_queen_in_white = pygame.image.load("assets/WhiteWhiteQueen.png")
white_king_in_white = pygame.image.load("assets/WhiteWhiteKing.png")

white_pieces_in_white = {chess.PAWN: white_pawn_in_white, chess.KNIGHT: white_knight_in_white,
                         chess.BISHOP: white_bishop_in_white, chess.ROOK: white_rook_in_white,
                         chess.QUEEN: white_queen_in_white, chess.KING: white_king_in_white}

white_pawn_in_black = pygame.image.load("assets/BlackWhitePawn.png")
white_knight_in_black = pygame.image.load("assets/BlackWhiteKnight.png")
white_bishop_in_black = pygame.image.load("assets/BlackWhiteBishop.png")
white_rook_in_black = pygame.image.load("assets/BlackWhiteRook.png")
white_queen_in_black = pygame.image.load("assets/BlackWhiteQueen.png")
white_king_in_black = pygame.image.load("assets/BlackWhiteKing.png")

white_pieces_in_black = {chess.PAWN: white_pawn_in_black, chess.KNIGHT: white_knight_in_black,
                         chess.BISHOP: white_bishop_in_black, chess.ROOK: white_rook_in_black,
                         chess.QUEEN: white_queen_in_black, chess.KING: white_king_in_black}

black_pawn_in_white = pygame.image.load("assets/WhiteBlackPawn.png")
black_knight_in_white = pygame.image.load("assets/WhiteBlackKnight.png")
black_bishop_in_white = pygame.image.load("assets/WhiteBlackBishop.png")
black_rook_in_white = pygame.image.load("assets/WhiteBlackRook.png")
black_queen_in_white = pygame.image.load("assets/WhiteBlackQueen.png")
black_king_in_white = pygame.image.load("assets/WhiteBlackKing.png")

black_pieces_in_white = {chess.PAWN: black_pawn_in_white, chess.KNIGHT: black_knight_in_white,
                         chess.BISHOP: black_bishop_in_white, chess.ROOK: black_rook_in_white,
                         chess.QUEEN: black_queen_in_white, chess.KING: black_king_in_white}

black_pawn_in_black = pygame.image.load("assets/BlackBlackPawn.png")
black_knight_in_black = pygame.image.load("assets/BlackBlackKnight.png")
black_bishop_in_black = pygame.image.load("assets/BlackBlackBishop.png")
black_rook_in_black = pygame.image.load("assets/BlackBlackRook.png")
black_queen_in_black = pygame.image.load("assets/BlackBlackQueen.png")
black_king_in_black = pygame.image.load("assets/BlackBlackKing.png")

black_pieces_in_black = {chess.PAWN: black_pawn_in_black, chess.KNIGHT: black_knight_in_black,
                         chess.BISHOP: black_bishop_in_black, chess.ROOK: black_rook_in_black,
                         chess.QUEEN: black_queen_in_black, chess.KING: black_king_in_black}


def is_white_square(square):
    """
    Says if the square background is white.

    :param square: The square to check.
    :type square: chess.Square.
    :return: If the square is white.
    :rtype: bool.
    """
    return chess.square_file(square)%2 != chess.square_rank(square)%2


def square_positon(square):
    """
    Calculates the position of a square in the screen.

    :param square: The square to calculate its position.
    :type square: chess.Square.
    :return: (x, y) coordinates of the top left corner of the square in the screen.
    :rtype: int tuple.
    """
    return (board_position[0] + (chess.square_file(square))*SQUARE_SIZE,
            board_position[1] + (MAX_RANK - chess.square_rank(square))*SQUARE_SIZE)


def display_piece(piece_type, piece_color, piece_square, screen):
    """
    Displays the piece in the board.

    :param piece_type: The type of piece that has to be displayed. 
    :type piece_type: chess.PieceType.
    :param piece_color: The color of the piece that has to be displayed. 
    :type piece_color: chess.Color.
    :param piece_square: The square where the piece that has to be displayed is. 
    :type piece_color: chess.Square.
    :param screen: The screen in which the piece will be displayed.
    :type screen: pygame.Surface.
    """
    if piece_color == chess.WHITE:
        if is_white_square(piece_square):
            screen.blit(white_pieces_in_white[piece_type], square_positon(piece_square))
        else:
            screen.blit(white_pieces_in_black[piece_type], square_positon(piece_square))
    else:
        if is_white_square(piece_square):
            screen.blit(black_pieces_in_white[piece_type], square_positon(piece_square))
        else:
            screen.blit(black_pieces_in_black[piece_type], square_positon(piece_square))


def display_board(board, screen):
    """
    Displays the entire board, i. e., the chessboard and its pieces.

    :param board: The chessboard in which the game is being played.
    :type board: chess.Board.
    :param screen: The screen in which the board will be displayed.
    :type screen: pygame.Surface.
    """
    screen.blit(board_background, board_position)
    for piece_type in chess_pieces:
        for piece_color in chess_colors:
            for piece in board.pieces(piece_type, piece_color):
                display_piece(piece_type, piece_color, piece, screen)


def display_screen(board, screen):
    """
    Displays everything in the screen, the board and the GUI.

    :param board: The chessboard in which the game is being played.
    :type board: chess.Board.
    :param screen: The screen in which the everything will be displayed.
    :type screen: pygame.Surface.
    :param font: Font to display GUI.
    :type font: pygame.Font
    """
    screen.fill(PYGAME_BLACK)
    display_board(board, screen)
    gui.game_gui(board, screen)
    pygame.display.flip()

def display_options(board, screen):
    """
    """
    clock = pygame.time.Clock()
    options_running[0] = True
    selected_option = 0
    selected_player = 1
    while options_running[0]:
        clock.tick(FREQUENCY)
        selected_option, selected_player = input.options_input(selected_option, selected_player, board)
        gui.options_gui(screen, selected_option, selected_player)
        pygame.display.flip()
    display_screen(board, screen)
