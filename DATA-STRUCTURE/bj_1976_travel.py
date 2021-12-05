import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
from collections import defaultdict

n, k = int(input()), int(input())
graph = defaultdict(list)
for i in range(n):      # row
    tmp = list(map(int, input().split()))
    for j in range(n):       # col
        if tmp[j] == 1:
            graph[i+1].append(j+1)

flag = False
def dfs(s, d, visited):       # dfs
    global flag
    if flag:
        return True
    for v in graph[s]:
        if v not in visited:
            if v == d:
                flag = True
                return True
            else:
                visited.append(v)
                dfs(v, d, visited)
    return flag  

travel = list(map(int, input().split()))

if len(travel) == 1:            # 여행할 도시가 1개뿐일 때
    if travel[0] > n:           # 주어진 도시 범위 밖의 여행지이면 NO
        print("NO")
    else:
        print("YES")
    sys.exit(0)

for k in range(len(travel)-1):
    visited = [travel[k]]
    flag = False
    res = dfs(travel[k], travel[k+1], visited)      # 매 경로마다 가능한지 여부 확인
    if not res:
        print("NO")
        break
else:
    print("YES")