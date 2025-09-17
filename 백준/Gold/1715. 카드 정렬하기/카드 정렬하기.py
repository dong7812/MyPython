import sys
import heapq

N, *arr = sys.stdin.read().splitlines()
heap = []
temp = []
ans = 0

def sum_card(arr):
    global ans
    
    new_arr = [int(x) for x in arr]
    
    for i in new_arr:
        heapq.heappush(heap, int(i))
    
    if int(N) <= 1:
        return 0
    
    while int(N) >= 2:
        
        if len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
        
            s = a+b
        
            ans += s
            heapq.heappush(heap, s)
        else:
            break

    return ans

print(sum_card(arr))