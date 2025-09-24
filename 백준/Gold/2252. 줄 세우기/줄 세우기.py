from collections import deque
import sys

# inpu_value = sys.stdin.read().splitlines()

# for i in inpu_value:
v, e = map(int, input().split())

# 모든 간선의 진입 차수를 0으로 초기화
indegree = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    # 정점? 이게 왜 A->B 인가?
    graph[a].append(b)
    
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    # 시작을 알기 위해 진입 차수가 0인 정점을 큐에 삽입 
    for i in range(1, v + 1):
        # 진입 차수가 0인 정점을 큐에 삽입
        # 시작점만 append로 큐에 삽입?
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    print(' '.join(map(str, result)))

topology_sort()