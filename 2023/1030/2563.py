n = int(input())
li = []
area = 100*n

for i in range(n):
    x, y = map(int,input().split())
    li.append([x,y])

for i in li:
    for j in li:
        if i[0] < j[0] < i[0]+10 or i[0] < j[0]+10 < i[0]+10:
            if  i[1] < j[1] < i[1]+10 or i[1] < j[1] + 10 < i[1]+10:
                width = min(i[0], j[0]) + 10 - max(i[0], j[0])
                height = min(i[1], j[1]) + 10 - max(i[1], j[1]) 
                area -= int(width*height/2)
print(area)
