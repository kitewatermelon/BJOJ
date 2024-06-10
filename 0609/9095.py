k = int(input())

for _ in range(k):
    n = int(input())
    dp = [1, 1, 2, 4]
    for i in range(4, 12):
        dp.append(dp[i-1] +  dp[i-2] + dp[i-3])
    print(dp[n])