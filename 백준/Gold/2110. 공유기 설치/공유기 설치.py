import sys

input_value = sys.stdin.read().splitlines()

(first, *rest) = input_value

N, M = map(int, first.split())
_arr = sorted(list(map(int, rest)))


# N = 총 길이
# M = 공유기 숫자``
# arr = 공유기 위치

# arr에서 실제 거리가 사용될 수 있는지
def can(arr, mid):
    cnt = 1
    last = arr[0]
    for x in arr[1:]:
        if x - last >= mid:
            cnt += 1
            last = x
            if cnt >= M:
                return True
    return False


def divide(arr, mid = 0):
    left, right = 1, arr[-1] - arr[0]
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if can(arr, mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
            
    print(ans)
    
divide(_arr)