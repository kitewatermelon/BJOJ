# 알고리즘 코딩테스트 3-1 숫자의 합 구하기
n = int(input())
l = list(input())
sum = 0

for i in l:
    sum += int(i)

print(sum)