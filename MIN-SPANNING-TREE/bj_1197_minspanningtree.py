# Prim : visited 를 구현해서 방문한 노드인지 아닌지를 확인하는 방식
import sys
from collections import defaultdict
from heapq import *

graph = defaultdict(list)
v, e = map(int, sys.stdin.readline().split())
for i in range(e):
    s, d, w = map(int, sys.stdin.readline().split())
    graph[s].append((w, d))
    graph[d].append((w, s))

visited = [False]*(v+1)     # 그냥 append 하고 계속 if v not in visited 형식으로 조회를 하게 되면 O(v**2) 만큼의 시간복잡도가 소요되니, 바로 indexing 을 할 수 있게끔 해주는 게 좋다
hq = [(0, 1)]
heapify(hq)
result = 0
cnt = 0

while hq:
    if cnt > v: break
    w, d = heappop(hq)
    if not visited[d]:
        visited[d] = True
        result += w
        cnt += 1
        for i in graph[d]:
            heappush(hq, i)

print(result)

# Kruskal : 대표 노드의 일치 여부를 확인(find)해 같으면 패스, 다르면 트리에 union 하는 방식
import sys

edges = []
v, e = map(int, sys.stdin.readline().split())
for _ in range(e):
    edges.append(list(map(int, sys.stdin.readline().split())))
edges.sort(key = lambda x : x[2])

root = [i for i in range(v+1)]   # 각 노드의 root 를 자기 자신으로 초기화
rank = [0 for _ in range(v+1)]
result = 0

def find(v):
    if v != root[v]:    # v = root[v] 를 유지할 수 있는 애는 노드 값이 가장 작은 루트노드뿐이다.
        root[v] = find(root[v])
    return root[v]

for s, d, w in edges:
    root_s = find(s)
    root_d = find(d)

    if root_s == root_d: continue       # check if cycle formed
    result += w
    if rank[root_s] > rank[root_d]:        # union by height
        root[root_d] = root_s
    else:
        root[root_s] = root_d
        if rank[root_s] == rank[root_d]:
            rank[root_d] += 1

print(result)
    











