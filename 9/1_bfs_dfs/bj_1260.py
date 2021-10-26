# DFS - 재귀호출 사용
import sys
sys.setrecursionlimit(100000)

p, l, v = [int(x) for x in input().split()]
graph = {}

for _ in range(l):
    x, y = list(map(int, input().split()))    # 간선 양방향으로 연결
    if x not in graph:        
        graph[x] = [y]
    else:
        graph[x] += [y]
    if y not in graph:
        graph[y] = [x]
    else:
        graph[y] += [x]

for key in list(graph.keys()):        # 한 정점에 연결된 여러 개의 정점을 오름차순으로 정렬
    graph[key].sort()

def recur_DFS(v, visited):
    visited.append(v)
    if v not in graph:        # 시작점에 간선이 연결되어 있지 않은 경우
        return visited
    for w in graph[v]:            
        if w not in visited:
            visited = recur_DFS(w, visited)
    
    return visited
  
print(*recur_DFS(v, visited=[]))

from queue import Queue
q = Queue()

# BFS - 반복문과 queue 사용

def BFS(v, visited):
    q.put(v)
    visited.append(v)
    while q:
        cur = q.get()
        if cur not in graph:    # 시작점에 간선이 연결되어 있지 않은 경우
            return visited
        for w in graph[cur]:
            if w not in visited:
                visited.append(w)
                q.put(w)

    return visited
    
print(*BFS(v, visited=[]))