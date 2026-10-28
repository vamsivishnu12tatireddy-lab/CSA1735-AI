
N = 8
board = [-1] * N

def solve(row):
    if row == N:
        return True

    for col in range(N):
        if all(
            board[r] != col and
            abs(board[r] - col) != row - r
            for r in range(row)
        ):
            board[row] = col
            if solve(row + 1):
                return True
            board[row] = -1
    return False

if solve(0):
    for row in range(N):
        print(" ".join(
            "Q" if board[row] == col else "-"
            for col in range(N)
        ))