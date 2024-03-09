'''
https://www.acmicpc.net/problem/2720
'''

n = int(input())
for i in range(n):
    change = int(input())
    print(change // 25, end=' ')
    change = change % 25
    print(change // 10, end=' ')
    change = change % 10
    print(change // 5, end=' ')
    change = change % 5
    print(change)