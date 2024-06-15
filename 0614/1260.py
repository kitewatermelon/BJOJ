'''
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.

단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 

더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

'''

from collections import deque, defaultdict

# 그래프를 인접 리스트로 표현
def create_graph(edges, n):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    for key in graph:
        graph[key].sort()  # 정점 번호가 작은 것을 먼저 방문하기 위해 정렬
    return graph

# DFS 구현
def dfs(graph, start, visited):
    visited.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
# BFS 구현
def bfs(graph, start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited

# 입력 처리
n, m, start = map(int, input().split())  # 정점 개수, 간선 개수, 시작 정점
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

# 그래프 생성
graph = create_graph(edges, n)

# DFS 탐색
visited_dfs = []
dfs(graph, start, visited_dfs)

# BFS 탐색
visited_bfs = bfs(graph, start)

# 결과 출력
print(' '.join(map(str, visited_dfs)))
print(' '.join(map(str, visited_bfs)))
