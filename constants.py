import chess
# Evaluation Constants
piece_value = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0}
outcome_value = {chess.Termination.CHECKMATE: 1000, chess.Termination.STALEMATE : 0, chess.Termination.FIFTY_MOVES: 0,
                chess.Termination.FIVEFOLD_REPETITION: 0, chess.Termination.INSUFFICIENT_MATERIAL: 0, chess.Termination.SEVENTYFIVE_MOVES: 0}
# 
EPSILON = 10e-3
