a, b, c = map(int,input().split())
li1 = [a, b, c]
li2 = [a, b, c]
li1.remove(max(li1))
if max(li1) + min(li1) <= max(li2):
    a = max(li1) + min(li1)
    print(2*a-1) 
else:
    print(a+b+c)