import sys

sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 해제

input_value = sys.stdin.read().splitlines()
N = int(input_value[0])

_edges = [tuple(map(int, line.split()))for line in input_value[1:]]
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
parent = [0]*(N+1)
 
for i in _edges:
    a, b  = i    
    graph[a].append(b)
    graph[b].append(a)

# i를 부모로 가지는 노드들을 재귀적으로 방문
# 해당 i를 parent 리스트에 기록
def find(v):
    visited[1] = True
    for i in sorted(graph[v]):
        if not visited[i]:
            visited[i] = True
            parent[i] = v 
            find(i)
    return parent

print('\n'.join(map(str, find(1)[2:])))  # 2번 노드부터 출력