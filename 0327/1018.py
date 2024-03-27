from sys import stdin, maxsize
 
input = stdin.readline
row, col = map(int, input().split())
chess_board = [[] for _ in range(row)]
for i in range(row):
    chess_board[i] = list(input().strip())
 
 
def check_board(word: str, row: int, col: int, chess_board) -> int:
    cnt = 0
    for i in range(row, row + 8):
        for j in range(col, col + 8):
            if i % 2 == 0:
                if j % 2 == 0 and chess_board[i][j] != word:
                    cnt += 1
                if j % 2 == 1 and chess_board[i][j] == word:
                    cnt += 1
            else:
                if j % 2 == 0 and chess_board[i][j] == word:
                    cnt += 1
                if j % 2 == 1 and chess_board[i][j] != word:
                    cnt += 1
    return cnt
 
 
cnt = maxsize
for i in range(0, row - 7):
    for j in range(0, col - 7):
        cnt = min(cnt, check_board("W", i, j, chess_board))
        cnt = min(cnt, check_board("B", i, j, chess_board))
print(cnt)


# def is_color_diff(board, next_color, cnt):
#     if board != next_color:
#         cnt += 1
#     if next_color == 'W':
#         next_color = 'B'
#     else:
#         next_color = 'W'
#     return next_color, cnt 

# def compute_cnt(next_color, row, col, board):
#     cnt = 0
#     for i in range(row, row+8):
#         for j in range(col, col+8):
#             next_color, cnt = is_color_diff(board[i][j], next_color, cnt)

#         if next_color == 'W':
#             next_color = 'B'
#         else:
#             next_color = 'W'

#     return cnt

# N, M = map(int, input().split())
# board = []
# for i in range(N):
#     board.append(input().rstrip())

# if board[0][0] == 'W':
#     next_color = 'W'
# else:
#     next_color = 'B'
    
# cnt = float('inf') 
# for i in range(0, N-7):
#     for j in range(0, M-7):
#         cnt = min(cnt, compute_cnt(next_color, i, j, board))
        

# print(cnt)