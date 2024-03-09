def swap(n1, n2):
    tmp = n1
    n1 = n2
    n2 = tmp
    return n1, n2

n = int(input())
num_list = list(map(int, input().split()))

# num_list.sort()

for j in range(n-1):
    for i in range(n-1):
        if num_list[i] > num_list[i+1]:
            num_list[i], num_list[i+1] = swap(num_list[i], num_list[i+1])
        else:
            continue

sum_list = num_list

tmp = sum_list[0]
for i in range(1,n):
    sum_list[i] = sum_list[i] + sum_list[i-1] 
    tmp += sum_list[i]

print(tmp)