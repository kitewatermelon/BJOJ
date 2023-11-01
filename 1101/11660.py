import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = [[0] * (N + 1)]
S = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N):
    L = [0] + [int(x) for x in input().split()]
    A.append(L)

for i in range(1, N+1):
    for j in range(1, N+1):
        S[i][j] = S[i][j-1] + S[i-1][j] - S[i-1][j-1] + A[i][j]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    
    number = S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1]
    print(number)
