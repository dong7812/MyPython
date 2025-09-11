import sys

input = sys.stdin.readline

N = int(input())
N_set = set(map(int, input().split()))
M = int(input())
M_arr = list(map(int, input().split()))

for el in M_arr:
    if el in N_set: 
        print(1)
    else:
        print(0)