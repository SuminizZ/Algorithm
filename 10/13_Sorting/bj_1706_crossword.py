import sys
input = sys.stdin.readline
n, m = map(int, input().split())    # (r, c)
cw = []
for _ in range(n):
    cw.append(list(input()))

result = []
dirs = [(0, 1), (1, 0)]     
def dfs(dir, cur_loc, word):
    r, c = cur_loc
    if cw[r][c] == '#':
        rest = word[:-1]
        if rest and len(rest) > 1:
            result.append(rest)
        word = ""

    nr = r + dir[0]
    nc = c + dir[1]
    if 0 <= nr < n and 0 <= nc < m:
        word += cw[nr][nc] 
        dfs(dir, (nr, nc), word)
    else :
        if len(word) > 1: 
            result.append(word)

for j in range(m):
    dfs(dirs[1], (0, j), cw[0][j])
for i in range(n):
    dfs(dirs[0], (i, 0), cw[i][0])

result.sort()
print(result[0])

