import sys

arr = sys.stdin.read().splitlines()
if arr: 
    int_arr = [int(s) for s in arr]
    print(max(int_arr))
    print(int_arr.index(max(int_arr))+1)