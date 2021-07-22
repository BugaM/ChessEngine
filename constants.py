import chess

# Chess Pieces and Colors
chess_pieces = [chess.PAWN, chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN, chess.KING]
chess_colors = [chess.WHITE, chess.BLACK]

# Evaluation Constants (in centipawns)
piece_value = {chess.PAWN: 100, chess.KNIGHT: 300, chess.BISHOP: 300, chess.ROOK: 500, chess.QUEEN: 900, chess.KING: 0}
outcome_value = {chess.Termination.CHECKMATE: 100000, chess.Termination.STALEMATE : 0, chess.Termination.FIFTY_MOVES: 0,
                chess.Termination.FIVEFOLD_REPETITION: 0, chess.Termination.INSUFFICIENT_MATERIAL: 0, chess.Termination.SEVENTYFIVE_MOVES: 0}

# Numerical Constants
EPSILON = 10e-3

# Pygame Constants
WINDOW_LENGTH = 854 # px
WINDOW_HEIGHT = 480 # px
CHESS_BOARD_SIZE = 376 # px, size of the image (can't be changed)
SQUARE_SIZE = CHESS_BOARD_SIZE/8
PYGAME_BLACK = 0, 0, 0
PYGAME_WHITE = 255, 255, 255
FREQUENCY = 60 # Hz
