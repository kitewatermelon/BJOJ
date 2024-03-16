'''
https://www.acmicpc.net/problem/9063
'''
N = int(input())
x = 0
y = 0
bufferX = []
bufferY = []

if N == 1:
    a, b= map(int, input().split())
    print(0)
    
else:
    for i in range(N):
        a, b= map(int, input().split())
        bufferX.append(a)
        bufferY.append(b)
        
    print((max(bufferX) - min(bufferX)) * (max(bufferY) - min(bufferY)) )
