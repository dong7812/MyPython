import sys
import heapq

N, *arr = sys.stdin.read().splitlines()

heap = []

for i in arr:
    if i == "0":
        if len(heap) != 0:
            print(-heapq.heappop(heap))
        else:
            print("0")
    else:
        heapq.heappush(heap, -int(i))