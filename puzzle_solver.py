import csv
import chess
import random
import game_logic
import time
import numpy as np


def play_puzzle(fen, moves):
    board = chess.Board(fen)
    move_number = 0
    moves_made = 0
    misses = 0
    player = game_logic.ChessPlayer(board.turn, game_logic.GREEDY_MOVE, game_logic.STOCKFISH_EVAL)
    while move_number < len(moves):
        next_move = chess.Move.from_uci(moves[move_number])
        board.push(next_move)
        move_number = move_number + 1
        right_move = chess.Move.from_uci(moves[move_number])
        move = player.get_player_move(board)
        if move != right_move and not board.is_checkmate():
            misses = misses + 1
        moves_made = moves_made + 1
        board.push(right_move)
        move_number = move_number + 1
    return 1 - misses/moves_made


FEN = 1
MOVES = 2

# Number of path plannings used in the Monte Carlo analysis
num_iterations = 1
# num_iterations = 10
# num_iterations = 100  # Monte Carlo

with open('puzzles/puzzles.csv', mode='r') as db:
    csv_reader = csv.reader(db, delimiter=',')
    rows = list(csv_reader)
    random.seed(10)
    score = np.zeros((num_iterations, 1))
    times = np.zeros((num_iterations, 1))
    for i in range(num_iterations):
        puzzle = rows[random.randint(0, len(rows))]
        fen = puzzle[FEN]
        moves = list(puzzle[MOVES].split(' '))
        tic = time.time()
        score[i] = play_puzzle(fen, moves)
        toc = time.time()
        times[i] = toc - tic
    db.close()

# Print statistics
print(r'Compute time: mean: {0}, std: {1}'.format(np.mean(times), np.std(times)))
print(r'Score: mean: {0}, std: {1}'.format(np.mean(score), np.std(score)))
