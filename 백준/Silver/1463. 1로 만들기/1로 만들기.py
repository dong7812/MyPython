import sys

input_value = int(sys.stdin.read())

dp = [0] * (input_value+1)

for i in range(2, input_value+1):
        # 최소 연산 
        # 1을 빼는 게 최대의 값이니까 최대 비교값으로 두고 진행
    dp[i] = dp[i-1] + 1
        # dp i의 값(1 마이너스 중), dp[i//2]의 값과 비교해서 작은 값을 챙기기
        # 이게 작은거부터 큰거로 올라가는 타뷸레이션
    if i % 2 == 0: dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0: dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[input_value])