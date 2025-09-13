import sys

input_value = sys.stdin.read().splitlines()

(first, *rest) = input_value

N = first
_arr = sorted(list(map(int, rest[0].split())))


def find_liq(arr, mid = 0):
    
    left, right = arr[-1] + arr[0], 1
    print(left, right)
    ans = 0
    while left <= right:
        mid = (left - right) // 2
        
        print(left, right)
        if can(arr, mid):
            ans = left
            left = mid + 1
        else:
            right = mid - 1

            
def can(arr, mid):
    last = arr[0]
    for i in arr[1:]:
        if i - last >= mid:
            return True
    return False


print(find_liq(_arr))
# N = 총 길이
# M = 공유기 숫자``
# arr = 공유기 위치

# arr에서 실제 거리가 사용될 수 있는지
# def can(arr, mid):
#     cnt = 1
#     last = arr[0]
#     for x in arr[1:]:
#         if x - last >= mid:
#             cnt += 1
#             last = x
#             if cnt >= M:
#                 return True
#     return False


# def divide(arr, mid = 0):
#     left, right = 1, arr[-1] - arr[0]
#     ans = 0
#     while left <= right:
#         mid = (left + right) // 2
#         # 계속 반으로 쪼갤 수 있을지
#         if can(arr, mid):
#             ans = mid
#             left = mid + 1
#         else:
#             right = mid - 1
            
#     # print(left)
#     print(ans)

# divide(_arr)