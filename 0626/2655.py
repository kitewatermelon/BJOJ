'''
밑면이 정사각형인 직육면체 벽돌들을 사용하여 탑을 쌓고자 한다. 
탑은 벽돌을 한 개씩 아래에서 위로 쌓으면서 만들어 간다. 
아래의 조건을 만족하면서 가장 높은 탑을 쌓을 수 있는 프로그램을 작성하시오.

벽돌은 회전시킬 수 없다. 즉, 옆면을 밑면으로 사용할 수 없다.
밑면의 넓이가 같은 벽돌은 없으며, 또한 무게가 같은 벽돌도 없다.
벽돌들의 높이는 같을 수도 있다.
탑을 쌓을 때 밑면이 좁은 벽돌 위에 밑면이 넓은 벽돌은 놓을 수 없다.
무게가 무거운 벽돌을 무게가 가벼운 벽돌 위에 놓을 수 없다.
상자쌓기
'''


import sys

# Reading input
n = int(sys.stdin.readline())
stones = []

for i in range(n):
    width, height, weight = map(int, sys.stdin.readline().split())
    stones.append((width, height, weight, i))

# Sorting stones by base area (width)
stones.sort(key=lambda x: x[0])

# DP array to store maximum height achievable for each box
dp = [0] * n

# Initialize DP with heights of each box
for i in range(n):
    dp[i] = stones[i][1]

# Compute maximum height for each box
for i in range(1, n):
    for j in range(i):
        if stones[j][2] < stones[i][2]:  # Can stack i on j only if weight is strictly greater
            dp[i] = max(dp[i], stones[i][1] + dp[j])

# Finding the maximum height
max_height = max(dp)

# Finding the sequence of boxes to achieve maximum height
result = []
for i in range(n-1, -1, -1):
    if dp[i] == max_height:
        result.append(stones[i][3])
        max_height -= stones[i][1]

result.reverse()

# Printing the results
print(len(result))
for box in result:
    print(box+1)
