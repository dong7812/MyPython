import sys
from collections import deque

input_value = sys.stdin.read().splitlines()

# 네 변수명 그대로 사용 (N: 열, M: 행, H: 층 으로 쓰고 있었음)
N, M, H = map(int, input_value[0].split())

# ===== [수정1] 입력 파싱: H층, 각 층 M행, 각 행 N열 =====
idx = 1
grid = []
for _ in range(H):
    layer = []
    for _ in range(M):
        row = list(map(int, input_value[idx].split()))
        # (옵션) 길이 방어: assert len(row) == N
        layer.append(row)
        idx += 1
    grid.append(layer)

# print(grid)  # 디버그 출력 제거(원하면 주석 해제)

dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

arr_today = deque()
# 시작 지점 수집
for h in range(H):
    for r in range(M):
        for c in range(N):
            if grid[h][r][c] == 1:
                arr_today.append((h, r, c))

day = 0  # ===== [수정4] day는 바깥에서 초기화 =====
arr_todo = deque()

# BFS (하루 단위 레벨 탐색)
while arr_today:
    h, r, c = arr_today.popleft()
    for i in range(6):
        n_h, n_r, n_c = h + dh[i], r + dr[i], c + dc[i]
        # ===== [수정2] 경계 체크: r<M, c<N 로 수정 =====
        if 0 <= n_h < H and 0 <= n_r < M and 0 <= n_c < N and grid[n_h][n_r][n_c] == 0:
            grid[n_h][n_r][n_c] = 1
            arr_todo.append((n_h, n_r, n_c))
    if not arr_today and arr_todo:
        day += 1
        arr_today = arr_todo.copy()
        arr_todo.clear()  # ===== [수정3] 괄호 추가 =====

# 남은 0 있으면 -1, 아니면 날짜 출력
if any(0 in grid[h][r] for r in range(M) for h in range(H)):
    print(-1)
else:
    print(day)