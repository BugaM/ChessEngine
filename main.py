import chess
import move_selection
import board_evaluation

# Game Settings
whitePlayerHuman = False
blackPlayerHuman = False

board = chess.Board(chess.STARTING_BOARD_FEN)
while not board.is_game_over():
    board.push(move_selection.randomMove(board))
    print(board_evaluation.materialEvaluation(board))
    print(board)
    print()