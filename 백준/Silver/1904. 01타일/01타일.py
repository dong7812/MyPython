import sys

input_value = int(sys.stdin.read())
dp = [0, 1, 2]
def tile(n):
    if n == 1 :
        return 1
    elif n == 2:
        return 2

    prev2 = dp[1]
    prev1 = dp[2]
    for _ in range(3, n+1):
        prev2, prev1 = prev1, (prev1 + prev2) % 15746
    
    return prev1

print(tile(input_value))