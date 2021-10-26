## 1. 
import sys
n, total = map(int, input().split())
graph = []
dist = [i for i in range(total+1)]
for _ in range(n):
    s, e, d = map(int, sys.stdin.readline().split())
    graph.append((s, e, d))


for i in dist:
    if i != 0:
        for s, e, d in graph:
            if i == e:     
                dist[i] = min(dist[i], dist[s] + d)
        dist[i] = min(dist[i], dist[i-1]+1)

print(dist[-1])

## 2. 실패
# from collections import defaultdict
# from heapq import *
# import sys

# n, total = map(int, input().split())
# graph = defaultdict(list)
# mincost = defaultdict(int)
# for _ in range(n):
#     start, end, dist = map(int, sys.stdin.readline().split())
#     graph[start].append((end, min(dist, end-start)))                # 지름길 사용 vs 그냥 고속도로 사용 중 최소거리
#     if not graph[end]:
#         graph[end].append((total, total-end))
#     mincost[start] = float('inf')
#     mincost[end] = float('inf')
# graph[0].append((total, total))    
# mincost[total] = float('inf')
# mincost[0] = 0

# def getShortest(n, total):
#     hq = [(mincost[0], 0)]
#     heapify(hq)
#     while hq:
#         cur_dist, cur_node = heappop(hq)  
#         for nxt_node, nxt_dist in graph[cur_node]:
#             if nxt_dist < 0 or mincost[nxt_node] <= cur_dist:
#                  continue     # 역주행 방지, 중복 방문 x
#             distance = cur_dist + nxt_dist
#             if mincost[nxt_node] > distance:
#                 mincost[nxt_node] = distance
#             heappush(hq, (mincost[nxt_node], nxt_node))

#     return mincost[total]              

# print(getShortest(n, total))


