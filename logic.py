board = [""] * 9
current_player = "X"

def make_move(pos):
    if board[pos] == "":
        board[pos] = current_player
        return True
    return False

def check_winner():
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

def switch_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"

def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
