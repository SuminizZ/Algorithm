import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())
dirs = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]      # (c, r)

def KnightMove(n, start, end):
    sc, sr = start
    ec, er = end
    dq = deque([[sc, sr]])
    map = [[-1 for _ in range(n)] for _ in range(n)]
    map[sr][sc] = 0     # start
    
    ans = float('inf')
    while dq:
        cc, cr = dq.popleft()
        if cc == ec and cr == er :
            return map[cr][cc]
        for d in dirs:
            nc = cc + d[0]
            nr = cr + d[1]
            if 0 <= nc < n and 0 <= nr < n and map[nr][nc] == -1:
                map[nr][nc] = map[cr][cc] + 1
                dq.append([nc, nr])

    return ans

while tc:
    n = int(input())
    sc, sr = map(int, input().split())
    ec, er = map(int, input().split())
    print(KnightMove(n, [sc, sr], [ec, er]))
    tc -= 1