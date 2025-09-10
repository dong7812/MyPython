import sys
import itertools

sys.setrecursionlimit(1_000_000) 

input_value = sys.stdin.read().splitlines()

N = int(input_value[0])
new_route = []

for i in range(N):
    new_route.append([int(x) for x in input_value[i+1].split()])

def main():
    result = tsp(new_route)
    print(result)

def tsp(arr):
    # 시작 도시 0 고정 → 회전 중복 제거
    perm = itertools.permutations(range(1, N))
    best = float('inf')

    for p in perm:
        find_route = (0,) + p + (0,)
        total = 0
        # 가지치기: 누적합이 best 이상이면 바로 중단
        for k in range(N):
            a = find_route[k]
            b = find_route[k+1]
            
            if arr[a][b] == 0:
                break
            
            total += arr[a][b]
            if total >= best:
                break
        else:
            # break 없이 끝났다면 total이 후보
            if total < best:
                best = total

    return best

if __name__ == "__main__":
    main()
