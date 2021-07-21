import chess
import move_selection
import board_evaluation

board = chess.Board(chess.STARTING_BOARD_FEN)
i = 0
while not board.is_game_over():
    i += 1
    board.push(move_selection.selection_mode[1](board, 0, 2))
    print(board_evaluation.material_evaluation(board))
    print(board)
    print()
print(board)
print(i, "moves")