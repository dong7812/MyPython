import sys

input_value = sys.stdin.read().splitlines()

N, M, start = map(int, input_value[0].split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
visited_2 = [False] * (N + 1)
res=[]

for i in input_value[1:]:
    a, b = map(int, i.split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(v):
    global res
    visited[v] = True
    res.append(v)
    
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(i)
    
    return ' '.join(map(str, res))

def bfs(v):
    global res
    res = []
    queue = [v]
    visited_2[v] = True

    while queue:
        v = queue.pop(0)
        res.append(v)
        
        for i in sorted(graph[v]):
            if not visited_2[i]:
                queue.append(i)
                visited_2[i] = True
                
    return ' '.join(map(str, res))

print(dfs(start))
print(bfs(start))
