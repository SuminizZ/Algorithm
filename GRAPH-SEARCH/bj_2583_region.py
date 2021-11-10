import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

m, n, k = map(int, input().split())
graph = [[1 for _ in range(n)] for _ in range(m)]       # m : rows / n : columns
for _ in range(k):
    c1, r1, c2, r2 = map(int, input().split())
    for i in range(r1, r2):
        for j in range(c1, c2):
            graph[i][j] = 0            # bottom to top (occupied check)

def dfs(start):
    global tmp_size
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    cur_r, cur_c = start
    graph[cur_r][cur_c] = 0
    for d in dirs:
        nxt_r = cur_r + d[0]
        nxt_c = cur_c + d[1]
        if 0 <= nxt_r < m and 0 <= nxt_c < n and graph[nxt_r][nxt_c]:
            graph[nxt_r][nxt_c] = 0
            tmp_size += 1
            dfs([nxt_r, nxt_c])
    
    return tmp_size

size = []
cnt = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            tmp_size = 1       
            size.append(dfs([i, j]))
            cnt += 1

print(cnt)
print(*sorted(size))



