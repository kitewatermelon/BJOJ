'''
https://www.acmicpc.net/problem/3009
'''
x = 0
y = 0
bufferX = []
bufferY = []

for i in range(3):
    a, b= map(int, input().split())
    if a in bufferX:
        bufferX.remove(a)
    else:
        bufferX.append(a)

    if b in bufferY:
        bufferY.remove(b)
    else:
        bufferY.append(b)

print(bufferX[0], bufferY[0])