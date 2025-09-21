import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 해제

input_value = sys.stdin.read().splitlines()
N = int(input_value[0])  # 컴퓨터의 수
M = int(input_value[1])  # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

edges = [tuple(map(int, line.split()))for line in input_value[2:]]

class union_find:
    def __init__(self, size):
        self.parent = list(range(size + 1))

    # 경로 압축 기법을 사용한 find 연산 및 같은 부모 집합인지 확인
    def find(self, u):
        # 경로 압축
        if self.parent[u] != u:
            # 재귀로 부모를 찾고, 찾은 부모로 갱신
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        # 루트 노드가 다르면 해당 루트끼리 list로 합치기
        if root_u != root_v:
            self.parent[root_v] = root_u
            
def count(n, _edges):
    uf = union_find(n)
    count = 0
    
    # 집합으로 parent list 만들기
    for a, b in _edges:
        uf.union(a, b)
    
    # union 이후 1번 컴퓨터로 parent의 값이 바뀌니 count 
    for i in range(0, n + 1):
        if uf.find(i) == uf.find(1):
            count += 1
    return count - 1  # 1번 컴퓨터 제외

print(count(N, edges))

