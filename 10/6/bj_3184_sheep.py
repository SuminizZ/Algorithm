import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())    # (r, c)
field = []
for _ in range(n):
    field.append(list(input()))

def bfs(start):
    dq = deque([[start[0], start[1]]])    # (r, c)
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if field[start[0]][start[1]] == 'o':
        wolf, sheep = 0, 1
    elif  field[start[0]][start[1]] == 'v':
        wolf, sheep = 1, 0
    field[start[0]][start[1]] = False
    while dq:
        r, c = dq.popleft()
        for d in dirs:
            nr = r + d[1]
            nc = c + d[0]
            if 0 <= nr < n and 0 <= nc < m and field[nr][nc] != '#':
                if field[nr][nc]:       # 여기서 visited 표시해줘야 시간초과 방지 가능
                    if field[nr][nc] == 'o':
                        sheep += 1
                    elif field[nr][nc] == 'v':
                        wolf += 1
                    field[nr][nc] = False
                    dq.append([nr, nc])

    return (wolf, sheep)

tot_wolf = 0
tot_sheep = 0
for i in range(n):
    for j in range(m):
        if field[i][j] == 'o' or field[i][j] == 'v':
            w, s = bfs([i, j])
            if w >= s:
                tot_wolf += w
            else:
                tot_sheep += s

print(*(tot_sheep, tot_wolf))
