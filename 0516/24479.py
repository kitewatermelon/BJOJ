# graph = []
# node, edge, start = map(int, input().split())
# for i in range(edge):
#     u, v = map(int, input().split())
#     graph.append((u, v))

# graph.sort()

# visited = [0 for _ in range(node+1)]

# def dfs(E, R):
#     global visited
#     visited[R] = 1
#     for edge in E:
#         if R in edge:
#             x = edge[1]
#             if visited[x] == 0: 
#                 return dfs(E, x)
# dfs(graph, start)

# for i, e in enumerate(visited):
#     if  i== 0: pass
#     elif e == 1: print(i)
#     else: print(0)

def dfs(t):
    global cnt
    visited[t] = cnt
    line[t].sort()
    for i in line[t]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

import sys
sys.setrecursionlimit(150000)
N, M, R = map(int, sys.stdin.readline().split())
line = [[] for _ in range(N+1)]
visited = [0]*(N+1)  # 저장값
cnt = 1
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    line[a].append(b)  # 양 방향 간선
    line[b].append(a)  # 양 방향 간선
dfs(R)
for i in range(1, N+1):
    print(visited[i])