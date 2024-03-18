def mid(a,b,c):
    li = [a, b, c]
    li.sort()
    return li[1]

a = b = c = 0


while 1:
    a, b, c = map(int,input().split())
    
    if a == b == c == 0:
        break
    if a == b == c:
        print('Equilateral')
    elif max(a,b,c) < min(a,b,c) + mid(a,b,c):
        if (a == b) or (b == c) or (a == c):
            print('Isosceles')
        else:
            print('Scalene')
    else: 
        print('Invalid')