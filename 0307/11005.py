'''
https://www.acmicpc.net/problem/11005
'''

N, B = map(int, input().split())
sum = ''

while N > 0:
    number = N % B
    N = N // B
    if number >= 10:
        number = chr(number+55) 
    sum = str(number) + sum

print(sum)