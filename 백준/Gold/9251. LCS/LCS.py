import sys

input_value = sys.stdin.read().splitlines()

first = list(input_value[0])
second = list(input_value[1])

N, M = len(first), len(second)
dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N+1):
    for j in range(1, M+1):
       if first[i -1] == second[j-1]:
           dp[i][j] = dp[i-1][j-1]+1
       else:
           dp[i][j] = max(dp[i-1][j], dp[i][j-1])
  
print(dp[len(first)][len(second)])