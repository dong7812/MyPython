import sys
from collections import deque

input_value = sys.stdin.read().splitlines()
N, M, K, start = map(int, input_value[0].split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for line in input_value[1:]:
    a, b = map(int, line.split())
    graph[a].append(b)   # 단방향만 추가

def bfs(v):
    res = []
    queue = deque([(v, 0)])   # (노드, 거리) 튜플 저장
    visited[v] = True

    while queue:
        node, dist = queue.popleft()
        if dist == K:        # 정확히 거리 K라면 결과 추가
            res.append(node)
        for nxt in sorted(graph[node]):
            if not visited[nxt]:
                visited[nxt] = True
                queue.append((nxt, dist + 1))

    if res:
        for x in sorted(res):   #오름차순 출력
            print(x)
    else:
        print(-1)

bfs(start)