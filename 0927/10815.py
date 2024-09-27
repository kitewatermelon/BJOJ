# 계속 풀어야 함
N = int(input())
target_arr = list(map(int, input().split()))

M = int(input())

input_arr = list(map(int, input().split()))
answer_arr = [0] * M
for i in target_arr:
    for idx, j  in enumerate(input_arr):
        if i == j:
            answer_arr[idx] = 1
            break
print(*answer_arr)