k = int(input())
step = [0]

for _ in range(k):
    step.append(int(input()))
# file_name = "0609\sample.txt" 

# step = [0]

# with open(file_name, "r") as file:
#     k = int(file.readline())  
#     for _ in range(k):
#         step.append(int(file.readline())) 


dp = [[0] * len(step)] * 3
dp = [[0] * len(step) for _ in range(3)]  

for i in range(1, len(step)):
    dp[0][i] = max(dp[1][i-1], dp[2][i-1])
    dp[1][i] = dp[0][i-1] + step[i]
    dp[2][i] = dp[1][i-1] + step[i]
    
print(max(dp[1][len(step)-1], dp[2][len(step)-1]))