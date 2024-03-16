#11659 구간합 구하기

# the number of data , query

import sys

d, q = map(int, sys.stdin.readline().split())
A = list(input().split())
S = [0]

for i in range(d):
    S.append(S[i] + int(A[i]))

for i in range(q):
    q1, q2 = map(int, sys.stdin.readline().split())
    
    print(S[q2]-S[q1-1])