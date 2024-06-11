n = int(input())

arr = [0] * 5001
arr[0] = 1
arr[3] = 1
arr[5] = 1

for i in range(6,5001):
    if arr[i-5] != 0:
        arr[i] = arr[i-5] + 1
    elif arr[i-3] != 0:
        arr[i] = arr[i-3] + 1 
print(-1) if arr[n] == 0 else print(arr[n])