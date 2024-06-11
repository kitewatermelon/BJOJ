# file_name = "0611\sample.txt" 

# case = []

# with open(file_name, "r") as file:
#     k = int(file.readline())  
#     for _ in range(k):
#         case.append(int(file.readline())) 
k = int(input())
case = []

for _ in range(k):
    case.append(int(input()))

for n in case:
    dp = [[1,0],[0,1]]
    for i in range(2,n+1):
        dp[0].append(dp[0][i-1]+dp[0][i-2])
        dp[1].append(dp[1][i-1]+dp[1][i-2])
    print(dp[0][n], dp[1][n])