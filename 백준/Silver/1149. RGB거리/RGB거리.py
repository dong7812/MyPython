import sys

input_value = sys.stdin.read().splitlines()

case = int(input_value[0])

arr =[list(map(int, line.split())) for line in input_value[1:]]

inf = float("inf")
dp = [[inf] * 3 for _ in range(case)]

dp[0] = arr[0]

for i in range(1, case):
    dp[i][0] = arr[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = arr[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = arr[i][2] + min(dp[i-1][0], dp[i-1][1])
    
print(min(dp[case-1]))