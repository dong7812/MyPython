import sys
import heapq

input_value = sys.stdin.read().splitlines()

arr = []
# 도시 갯수
N = int(input_value[0])
# 버스 갯수
M = int(input_value[1])

start, end = map(int, list(input_value[-1:][0].split()))

graph = [[] for _ in range(N + 1)]

for i in input_value[2:-1]:
    a, b, weight = map(int, i.split())
    graph[a].append([b, weight])

def dijkstra(graph, start):
    distance = {node : float('inf') for node in range(len(graph))}
    distance[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        cur_dist, cur_node = heapq.heappop(priority_queue)
        
        if cur_dist > distance[cur_node]:
            continue
        
        for node, w in graph[cur_node]:
            dist = cur_dist + w
            if dist < distance[node]:
                distance[node] = dist
                heapq.heappush(priority_queue, (dist, node))
    return distance

print(dijkstra(graph=graph, start=start)[end])
