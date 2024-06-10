a0, a1 = map(int, input().split())
c = int(input())
n0 = int(input())

state = False

for i in range(n0, 101):
    if a0*i + a1 > c*i:
        state = False
        break
    else:
        state = True


print(1) if state == True else print(0)