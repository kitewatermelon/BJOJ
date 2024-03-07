'''
https://www.acmicpc.net/problem/28014
'''

li = []
n = int(input())
li = list(map(int, input().split()))
count = 0

for i in range(1, len(li)):
    if li[i] < li[i-1]:
        count += 1
        
print(n-count)
