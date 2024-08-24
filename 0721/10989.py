n = int(input())
arr = [0]*n
for i in range(n):
    k = int(input())
    arr[k] += 1

for num, i in enumerate(arr):
    for j in range(i):
        print(num)