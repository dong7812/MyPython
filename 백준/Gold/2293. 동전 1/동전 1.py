import sys

input_value = sys.stdin.read().splitlines()

N, M = list(map(int, input_value[0].split()))

arr = list(map(int, input_value[1:]))

dp = [0] * (M+1)

dp[0] = 1

for coin in arr:
    for i in range(coin, M+1):
        dp[i] += dp[i-coin]

print(dp[M])
