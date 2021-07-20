import chess
import move_selection
import board_evaluation

# Game Settings
white_player_human = False
black_player_human = False

board = chess.Board(chess.STARTING_BOARD_FEN)

while not board.is_game_over():
    board.push(move_selection.random_move(board))
    print(board_evaluation.material_evaluation(board))
    print(board)
    print()
