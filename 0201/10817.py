num_list = list(map(int, input().split()))

for i in range(2):
    for j in range(2):
        if num_list[j] > num_list[j+1]:
            tmp = num_list[j]
            num_list[j] = num_list[j+1]
            num_list[j+1] = tmp

print(num_list[1])