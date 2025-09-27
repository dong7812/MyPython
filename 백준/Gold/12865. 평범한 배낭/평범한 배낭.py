import sys

input_value = sys.stdin.read().splitlines()

N, L = input_value[0].split()

weight = []
value = []

for i in input_value[1:]:
    weight.append(int(i.split()[0]))
    value.append(int(i.split()[1]))

def knapsack(weights, values, W):
    n = len(weights)
    
    # dp 선언
    dp = [0]*(W+1)
    for i in range(n):
        w, v = weights[i], values[i]
        # 용량(cap)을 W부터 w까지 역순으로 탐색
        # (정방향으로 탐색하면 같은 물건을 여러 번 사용할 수 있으므로 반드시 역순)
        for cap in range(W, w-1, -1):
            # 물건을 안 넣었을 때 vs 넣었을 때 최대 가치 비교
            dp[cap] = max(dp[cap], dp[cap-w] + v)
    return dp[W]

print(knapsack(weight, value, int(L)))