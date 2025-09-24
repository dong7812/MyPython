import sys
from collections import deque

input_value = sys.stdin.read().splitlines()

N = int(input_value[0])
arr = []

# 거리 기록용 배열 (-1은 아직 방문하지 않음을 의미)
dist = [[-1] * N for _ in range(N)]

for i in input_value[1:]:
    arr.append(list(map(int, i)))

q = deque([(0,0)])

# 시작점까지의 거리를 1로 초기화 (자기 자신 포함)
dist[0][0] = 0

# 4방향 탐색
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

cost = 0
while q:
     # 현재 위치 꺼내기
    x, y = q.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            cost = 0 if arr[nx][ny] == 1 else 1
            new_cost = dist[x][y] + cost
            if dist[nx][ny] == -1 or dist[nx][ny] > new_cost:
                dist[nx][ny] = new_cost
                if cost == 0:
                    q.appendleft((nx, ny))
                else:
                    q.append((nx, ny))
            
print(dist[N-1][N-1])