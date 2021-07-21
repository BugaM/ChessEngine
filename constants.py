import chess
# Evaluation Constants (in centipawns)
piece_value = {chess.PAWN: 100, chess.KNIGHT: 300, chess.BISHOP: 300, chess.ROOK: 500, chess.QUEEN: 900, chess.KING: 0}
outcome_value = {chess.Termination.CHECKMATE: 100000, chess.Termination.STALEMATE : 0, chess.Termination.FIFTY_MOVES: 0,
                chess.Termination.FIVEFOLD_REPETITION: 0, chess.Termination.INSUFFICIENT_MATERIAL: 0, chess.Termination.SEVENTYFIVE_MOVES: 0}
# 
EPSILON = 10e-3
