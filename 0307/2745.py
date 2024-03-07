''' 
https://www.acmicpc.net/problem/2745 
'''

N, B = input().split()
B = int(B)
sum = 0
for i, n in enumerate(N):
    operand = ord(n)-55
    if operand < 10:
        operand = int(n)
    sum += operand * (B ** (len(N) -1 -i))

print(sum)