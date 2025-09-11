import sys

input_value = sys.stdin.read().splitlines()

# N 나무 갯수 M 필요 나무 높이
N, M = map(int,input_value[0].split())

trees = [int(x) for x in input_value[1].split()]

# c는 중간보다 얼마나 더 자를지
def cut_tree(arr, M, lo=0, hi=None):
    # 초기 상한: 가장 높은 나무
    if hi is None:
        hi = max(arr)
    
    # 조건을 만족하는 최대 높이   
    if lo > hi:
        return hi

    mid = (lo + hi) // 2
    got = sum(h - mid for h in arr if h > mid)

    # 더 높게 잘라도 M을 만족 → 높이 ↑
    if got >= M:                          
        return cut_tree(arr, M, mid + 1, hi)
    else:                                  
        # 부족 → 높이 ↓
        return cut_tree(arr, M, lo, mid - 1)
    

print(cut_tree(trees, M, 0))