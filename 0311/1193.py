# '''
# https://www.acmicpc.net/problem/1193
# '''
# n = int(input())

# FLAG = 0
# a = 0
# b = 0

# for i in range(n):
#     if FLAG == 0:
#         a += 1
#         b -= 1

#     elif FLAG == 1:
#         a -= 1
#         b += 1

#     if a <= 0:
#         a = 1
#         FLAG = 0

#     if b <= 0:
#         b = 1
#         FLAG = 1


# print(f"{a}/{b}")

num = int(input())
line = 1

while num > line:
    num -= line
    line += 1
    
if line % 2 == 0:
    a = num
    b = line - num + 1

elif line % 2 == 1:
    a = line - num + 1
    b = num

print(f'{a}/{b}')