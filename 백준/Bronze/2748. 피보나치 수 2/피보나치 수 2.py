import sys

input_value = int(sys.stdin.read())

dp = [0] * (input_value + 1)

def finb(n):
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

print(finb(input_value))