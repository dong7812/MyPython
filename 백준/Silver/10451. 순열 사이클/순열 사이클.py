import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 해제

input_value = sys.stdin.read().splitlines()

# Num, N, N_arr, M, M_arr = input_value
check = 0
arr = []

temp_1 = []
    
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
            
def _count(n, _edges):
    uf = union_find(n)
    stack = []
    # 집합으로 parent list 만들기
    for a, b in _edges:
        uf.union(a, b)
    
    # union 된 리스트에서 prarent 중복 제거
    for i in range(1, n + 1):
        stack.append(uf.find(i))
        stack = list(set(stack))
    return stack.__len__()

for i in input_value[1:]:
    check +=1
    arr.append(i)
    if check == 2 :
        N, N_arr = arr
        
        tmp = int(N)
        tmp_arr = list(map(int, N_arr.split()))          # 문자열 라인 → 정수 리스트
        for i in range(1, tmp + 1):
            temp_1.append((i, tmp_arr[i-1]))             # 리스트 말고 정수 하나로
            
        print(_count(tmp, temp_1))
        temp_1 = []
        arr = []
        check = 0

