from collections import deque, defaultdict

## 1. bfs

def solution(n, computers):
    visited = [0 for _ in range(n)]
    network = defaultdict(list)
    
    for i in range(n):
        for j in range(len(computers[i])):
            if computers[i][j] == 1 and i != j:
                network[i].append(j)
    
    def bfs(start):
        dq = deque([start])

        while dq:
            cur = dq.popleft()
            visited[cur] = 1
            if cur in network and network[cur]:
                for node in network[cur]:
                    if visited[node] == 0:
                        dq.append(node)
        return
    
    cnt = 0
    for i in range(n):
        if visited[i] == 0:
            cnt += 1
            bfs(i)     # i node 와 연결된 모든 자식노드를 cnt 로 세팅함

    return cnt


## 2. dfs

def solution(n, computers):
    visited = [0 for _ in range(n)]
    network = defaultdict(list)
    
    for i in range(n):
        for j in range(len(computers[i])):
            if computers[i][j] == 1 and i != j:
                network[i].append(j)
    
    def dfs(cur):
        visited[cur] = 1
        if cur in network and network[cur]:
            for node in network[cur]:
                if not visited[node]:
                    dfs(node)
        
    cnt = 0
    for i in range(n):
        if not visited[i]:
            cnt += 1
            dfs(i)     # i node 와 연결된 모든 자식노드를 cnt 로 세팅함
    
    return cnt


