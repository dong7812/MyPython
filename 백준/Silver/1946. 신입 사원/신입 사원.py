import sys

lines = sys.stdin.read().splitlines()
T = int(lines[0])   # 케이스 개수
idx = 1
cases = []

for _ in range(T):
    N = int(lines[idx])   # 이번 케이스 크기
    idx += 1
    arr = []
    for _ in range(N):
        a, b = map(int, lines[idx].split())
        arr.append([a, b])
        idx += 1
    cases.append((N, arr))

_arr = []

def count(arr, n):
    # for i in sorted(arr):
    #     _arr.append(list(map(int, i.split())))
    
    arr.sort(key=lambda x: x[1])

    cnt, temp = 0, n
    for s,e in arr:
        if s <= temp:
            cnt += 1
            temp = s
            
    print(cnt)

# 확인용 출력
for N, arr in cases:
    count(arr, int(N))
    

