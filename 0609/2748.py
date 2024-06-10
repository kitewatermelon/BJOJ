n = int(input())
arr = [0,1]

for i in range(n+1):
    if (i == 0) | (i == 1):
        continue
    arr.append(arr[i-1] + arr[i-2])
    
print(arr[n])