'''
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력 
6
10 20 10 30 20 50

출력
4
10 20 30 50
'''
import sys 

N = int(sys.stdin.readline())

D = [1] * N  # LIS 길이 저장
P = [-1] * N  # 이전 인덱스 저장
A = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j] and D[i] < D[j] + 1:
            D[i] = D[j] + 1
            P[i] = j

# LIS 길이와 마지막 인덱스 찾기
lis_length = max(D)
lis_index = D.index(lis_length)

# LIS 추적
lis = []
while lis_index != -1:
    lis.append(A[lis_index])
    lis_index = P[lis_index]

lis.reverse()

# 결과 출력
print(lis_length)
print(" ".join(map(str, lis)))