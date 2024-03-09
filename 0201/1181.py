def swap(n1, n2):
    tmp = n1
    n1 = n2
    n2 = tmp
    return n1, n2

n = int(input())
list_n = []

for i in range(n):
    list_n.append(input())

for i in range(n-1):
    for j in range(n-1):
        if len(list_n[j]) < len(list_n[j+1]):
            continue
        
        elif len(list_n[j]) > len(list_n[j+1]):
            list_n[j], list_n[j+1] = swap(list_n[j], list_n[j+1])
        
        else:
            if list_n[j] > list_n[j+1]:
                list_n[j], list_n[j+1] = swap(list_n[j], list_n[j+1])

for i in range(len(list_n)-1):
    for j in range(len(list_n)-1):
        if list_n[j] == list_n[j+1]:
            list_n.remove(list_n[j])
            break

for i in list_n:
    print(i)