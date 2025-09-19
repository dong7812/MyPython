import sys

sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 해제

input_value = sys.stdin.read().splitlines()
N, M = map(int, input_value[0].split())
edges = [tuple(map(int, line.split())) for line in input_value[1:]]

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size+1))

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            self.parent[root_v] = root_u
            
def kruskal(n, edges):
    uf = UnionFind(n)
    mst_weight = 0
    edges.sort(key=lambda x: x[2])  # 가중치 기준 오름차순 정렬

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_weight += weight

    return mst_weight

print(kruskal(N, edges))  # MST의 총 가중치 출력