import sys
import heapq

def dijkstra(graph, start):
    # A 리스트의 크기를 (노드 개수)로 설정하고 None으로 초기화
    A = [None] * (len(graph) + 1)
    queue = [(0, start)]
    
    while queue:
        path_len, v = heapq.heappop(queue)
        
        if A[v] is None:
            A[v] = path_len
            for w, edge_len in graph[v].items():
                if A[w] is None:
                    heapq.heappush(queue, (path_len + edge_len, w))

    # None인 경우 무한대로 설정
    return ['INF' if x is None else x for x in A]

V, E = map(int, sys.stdin.readline().split())
start_node = int(sys.stdin.readline())
graph = {}
for i in range(1, V+1):
    graph[i] = {}

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u][v] = w 

# 시작 노드 'A'에서 다른 모든 노드까지의 최단 거리
shortest_distances = dijkstra(graph, start_node)
# print(shortest_distances)
for i in range(1, len(shortest_distances)):
    print(shortest_distances[i])

'''
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
'''