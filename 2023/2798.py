# 재귀 풀이

# import sys

# n, score = map(int, sys.stdin.readline().split())
# card = list(map(int, sys.stdin.readline().split()))
# K = 3

# def blackjack(K, v, i, card):
#     global score, n
#     if K < 0 or v > score:
#         return 0
#     if n == i :
#         if K == 0:
#             return v 
#         else:
#             return 0
#     else:
#         return max(blackjack(K-1, v + card[i], i+1, card), blackjack(K, v, i+1, card))

# print(blackjack(K, 0, 0, card))

# for 문 풀이 

import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))

min_val = sys.maxsize
for i in range(n):
    for j in range(i+1, n):
        sum_val = 0
        for k in range(j+1, n):
            res = arr[i] + arr[j] + arr[k]
            if res <= m:
                sum_val = m - res
                min_val = min(min_val, sum_val)
print(m-min_val)
