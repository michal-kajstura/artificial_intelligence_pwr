

def minimax(board, depth, maximizingPlayer):
    if depth == 0: # or game over
        return board.evaluate

