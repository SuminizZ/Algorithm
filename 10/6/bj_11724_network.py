import sys
sys.setrecursionlimit(100000)
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [0 for _ in range(n+1)]
def dfs(start):
    visited[start] = 1
    if start in graph:
        for node in graph[start]:
            if not visited[node]:
                dfs(node)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        cnt += 1
        dfs(i) 

print(cnt)