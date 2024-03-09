'''
https://www.acmicpc.net/problem/2903
'''

n = int(input())
k = 2
for i in range(n):
    k = k + 2 ** i
    
print(k**2)