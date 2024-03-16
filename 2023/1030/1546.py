# 1546 평균구하기 

# N개의 과목, 점수
n = int(input()) 
scores = list(map(int, input().split()))

max_val = max(scores)
sum_val = sum(scores)

print((sum_val * 100) / max_val / n )