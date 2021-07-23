import csv
import chess
import random
import game_logic


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
with open('puzzles/puzzles.csv', mode='r') as db:
    csv_reader = csv.reader(db, delimiter=',')
    rows = list(csv_reader)
    puzzle = rows[random.randint(0, len(rows))]
    fen = puzzle[FEN]
    moves = list(puzzle[MOVES].split(' '))
    percentage = play_puzzle(fen, moves)
    print(percentage)
    db.close()


