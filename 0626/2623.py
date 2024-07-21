from collections import deque
'''
입력 처리:

n, m = map(int, input().split()): 정점의 수 n과 간선의 수 m을 입력으로 받습니다.
indegree: 각 정점의 진입 차수를 저장하기 위한 리스트입니다.
graph: 각 정점에서 진출하는 간선의 목록을 저장하기 위한 인접 리스트입니다.
'''
n, m = map(int, input().split())
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]

'''
그래프 구성:

각 정점의 진입 차수(indegree)를 초기화하고, 각 정점의 인접 리스트(graph)에 해당하는 정점으로 나가는 간선을 추가합니다.

'''
for _ in range(m):
    x, *order = map(int, input().split())
    for i in range(len(order)-1):
        indegree[order[i+1]] += 1
        graph[order[i]].append(order[i+1])
'''
위상 정렬 알고리즘:

진입 차수가 0인 모든 정점을 큐에 넣습니다(que).
큐에서 정점을 꺼내면서 해당 정점을 방문하고, 이 정점에서 진출하는 간선을 탐색합니다.
간선을 탐색할 때마다 진입 차수를 감소시키고, 만약 감소된 진입 차수가 0이 되면 그 정점을 큐에 추가합니다.
이 과정을 모든 정점을 방문할 때까지 반복합니다.

'''
que = deque()
for i in range(1,n+1):
    if indegree[i] ==0:
        que.append(i)
answer = []
while que:
    now = que.popleft()
    answer.append(now)
    for next in graph[now]:
        indegree[next] -= 1
        if indegree[next]==0:
            que.append(next)

'''
결과 출력:

모든 정점을 방문한 경우, 위상 정렬의 결과인 answer 리스트를 출력합니다.
사이클이 존재하면 모든 정점을 방문할 수 없으므로 0을 출력합니다.

'''
if len(answer) != n:
    print(0)
else:
    for i in range(n):
        print(answer[i])