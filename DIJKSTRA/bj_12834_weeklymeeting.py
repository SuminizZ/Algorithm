import sys
from heapq import *
input = sys.stdin.readline

n, v, e = map(int, input().split())
kst, cf = map(int, input().split())
memb_loc = list(map(int, input().split()))

conn = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, l = map(int, input().split())
    conn[a].append([b, l])
    conn[b].append([a, l])

def dist(s, d):
    if s == d:
        return 0
    cost_map = [float('inf') for _ in range(v+1)]
    hq = []
    heappush(hq, [0, s])        # [cur_cummulated_cost, start]
    while hq:
        cur_w, cur_n = heappop(hq)
        for nxt_n, nxt_w in conn[cur_n]:
            if cost_map[nxt_n] <= cur_w: continue
            dist = nxt_w + cur_w 
            if cost_map[nxt_n] > dist:
                cost_map[nxt_n] = dist
                heappush(hq, [dist, nxt_n])
    
    if cost_map[d] == float('inf'):
        return -1
    else: 
        return cost_map[d] 

ans = 0
for m_loc in memb_loc:
    ans += dist(m_loc, kst) + dist(m_loc, cf)

print(ans)