import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())
tomato = []
for _ in range(n):
    tomato.append(list(map(int, input().split())))

def bfs(dq):
    global cnt
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]       # (c, r)
    while dq:
        cur_r, cur_c = dq.popleft()
        for d in dirs:
            nxt_c = cur_c + d[0]
            nxt_r = cur_r + d[1]
            if 0 <= nxt_c < m and 0 <= nxt_r < n and tomato[nxt_r][nxt_c] == 0:
                tomato[nxt_r][nxt_c] = tomato[cur_r][cur_c] + 1
                dq.append((nxt_r, nxt_c))
                
dq = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            dq.append((i, j))   # 1 인 토마토 정보는 미리 다 넣고 시작해야, '최소' 소요일을 구할 수 있다

bfs(dq)     
for i in range(n):
    if 0 in tomato[i]:
        print(-1)
        sys.exit(0)

ans = max(map(max, tomato))   
if ans < 0:     # 다 비어있는 상자(-1 밖에 없는 배열)
    print(0)
else:
    print(ans-1)        


