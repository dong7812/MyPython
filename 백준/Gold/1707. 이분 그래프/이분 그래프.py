import sys
sys.setrecursionlimit(10**6)

input_value = sys.stdin.read().splitlines()
t = int(input_value[0])
idx = 1

def dfs(v, group):
    visited[v] = group
    for nxt in graph[v]:
        if visited[nxt] == 0:
            if not dfs(nxt, -group):
                return False
        elif visited[nxt] == visited[v]:
            return False
    return True

for _ in range(t):
    n, m = map(int, input_value[idx].split())
    idx += 1

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input_value[idx].split())
        idx += 1
        graph[u].append(v)
        graph[v].append(u)  # 무방향

    visited = [0] * (n + 1)  # 0=미방문, 1/-1=그룹
    bipartite = True

    for i in range(1, n + 1):
        if visited[i] == 0:
            if not dfs(i, 1):
                bipartite = False
                break

    print('YES' if bipartite else 'NO')