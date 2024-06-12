'''
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 

빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때,

아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

'''

import sys 
n = int(sys.stdin.readline())
li = []

for i in range(n):
    t = map(int, sys.stdin.readline().split())
    li.append(list(t))

for i in range(1,n):
    li[i][0] += min(li[i-1][1], li[i-1][2])
    li[i][1] += min(li[i-1][0], li[i-1][2])
    li[i][2] += min(li[i-1][0], li[i-1][1])

# for i in li:
#     print(i)

print(min(li[n-1]))
import tensorflow as tf

print(tf.__version__)