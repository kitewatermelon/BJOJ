'''
https://www.acmicpc.net/problem/9506
'''

while 1:
    n = int(input())
    cnt = 0
    string = f'{n} = '
            
    if n == -1:
        break


    for i in range(1, n // 2 + 1):
        if n % i == 0:
            cnt += i
            string += f'{i} + '
    
    if cnt == n:
        print(string[:-2])
        
    else :
        print(f'{n} is NOT perfect.')    
        