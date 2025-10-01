import sys

input_value = sys.stdin.read().splitlines()

case = int(input_value[0])

for i in input_value[1:]:
    dp = [0] * (int(i)+1)

    if int(i) >= 1:
        dp[1] = 1
    if int(i) >=2:
        dp[2] = 2
    if int(i) >=3: 
        dp[3] = 4

    for i in range(4, int(i)+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[int(i)])