'''
https://www.acmicpc.net/problem/2581
'''

min = int(input())
max = int(input())


cnt = 0
min_num = 0
for i in range(min, max+1):
    if i == 1:
        continue # 예외처리가 미숙했음.
    flag = 0
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            flag = 1
            break
        
    if flag == 0:
        cnt += i
        
    if cnt == i:
        min_num = i
        
if cnt == 0 :
    print(-1)
else :
    print(cnt)
    print(min_num)
    