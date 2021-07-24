# ChessEngine
This is a project done for Aeronautics Institute of Technology's (ITA) CT-213 discipline (Artificial Intelligence for mobile robots)
of authors:  
Eric Guerra Ribeiro  
Marcelo Buga Martins da Silva
## Usage:
### Main:

Run main and press ESC to choose settings. You may choose the following move selectors:  

Human: The user control the moves by clicking on the piece and the square it moves to.  
Random AI: AI that selects a random move
Alpha-Beta AI: AI that utilizes Alpha-Beta Pruning and Minimax to choose a move given an evaluation mode.  
Greedy AI: AI that takes one of the positions best moves given an evaluation mode.

The evaluation modes are:

Material: Simple evaluation that considers the traditional centipawn values for the pieces and values checkmate highly.  
Stockfish: Stockfish evaluation function. Ideally used with Greedy AI as it considers following turns by itself.  

To restart the board, press R.  

### Puzzle Solver:
Choose the number of iterations and a given player to play the puzzles. Random seed is used for reproducibility. 