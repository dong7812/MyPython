import sys

rd = sys.stdin.buffer.readline

n = int(rd())

arr = [int(rd()) for _ in range(n)]
arr.sort()
sys.stdout.write('\n'.join(map(str, arr)))
