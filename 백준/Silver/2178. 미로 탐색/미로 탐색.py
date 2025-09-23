import sys
from collections import deque

input_value = sys.stdin.read().splitlines()

N, M = map(int , input_value[0].split())
arr = []

# 거리 기록용 배열 (-1은 아직 방문하지 않음을 의미)
dist = [[-1] * M for _ in range(N)]

for i in input_value[1:]:
    arr.append(list(i))

# 첫 줄이 0이면 어디든 못가니 -1 나오도록
if arr[0][0] == 0:
    print(-1)
    
q = deque([(0,0)])

# 시작점까지의 거리를 1로 초기화 (자기 자신 포함)
dist[0][0] = 1

# 4방향 탐색
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while q:
     # 현재 위치 꺼내기
    x, y = q.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and int(arr[nx][ny]) == 1 and int(dist[nx][ny]) == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))
            
print(dist[N-1][M-1])