import sys

a, b, c, d, e, f= map(int, sys.stdin.readline().split())

res = []

for x in range(-999,1000):
    for y in range(-999,1000):
        if a*x+b*y==c and d*x+e*y==f:
            print(x,y)
            break


# 아래는 0으로 나누는 것이 있어서 런타임 에러가 뜬 코드
# import math

# a, b, c, d, e, f= map(int, sys.stdin.readline().split())

# coef_x = math.lcm(abs(a), abs(d))
# coef_y = math.lcm(abs(b), abs(e))

# div_b = int(coef_y / b)
# div_e = int(coef_y / e)

# x_a, x_b, x_c, x_d, x_e, x_f = div_b*a, div_b*b, div_b*c ,\
#     div_e*d, div_e*e, div_e*f

# div_x = x_a-x_d
# x = int((x_c-x_f) / div_x)

# y = int((c - a*x ) / b)
# print(x, y)