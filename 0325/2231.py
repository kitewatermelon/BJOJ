def position(n):
    rst = n
    n = str(n)

    for i in range(len(n)):
        rst += int(n[i])
    return int(rst)

n = int(input())
k = 0
rst = 0 
while n != rst:
    rst = position(k)
    k += 1
print(n, k-1)

n = int(input())  

for i in range(1, n+1):
    num = sum((map(int, str(i))))  
    print(num)
    num_sum = i + num  
    if num_sum == n:
        print(i)
        break
    if i == n: 
        print(0)
