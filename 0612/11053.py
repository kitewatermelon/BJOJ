'''
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 

A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

'''

import sys 

N = int(sys.stdin.readline())
D = [0] * (N+1)
A = [0] + list(map(int, sys.stdin.readline().split()))

D[1] = 1
for i in range(2, N+1):
    D[i] = 1
    for j in range(1, i):
        if A[i] > A[i-j]:
            D[i] = max(D[i], 1 + D[i-j])
print(max(D))