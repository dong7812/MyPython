import sys
import heapq

input_value = sys.stdin.read().splitlines()

N, *arr = input_value

new_arr = [int(x) for x in arr]

min_heap = []
max_heap = []

def add_num(num):
    if not max_heap or num <= -max_heap[0]:
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)
        
    if len(max_heap) < len(min_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    elif len(max_heap) > len(min_heap) +1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
        
for i in new_arr:
    add_num(i)
    print(-max_heap[0])
    
    