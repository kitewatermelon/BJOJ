n = int(input())
arr = [[0 for j in range(100)] for i in range(100)]
li = []
area = 100*n

for i in range(n):
    x, y = map(int,input().split())
    li.append([x,y])

for x,y in li:
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1
print(sum(sum(arr,[])))