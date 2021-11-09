import sys
sys.setrecursionlimit(10000000)
from collections import defaultdict
input = sys.stdin.readline

n = int(input())            
tree = defaultdict(list)     
parents = defaultdict(int)      # 자기자신의 부모 노드를 입력하는 사전
parents[1] = 1
left = []
for _ in range(n-1):
    p, c = map(int, input().split())
    tree[p].append(c)
    tree[c].append(p)

def findP(root):
    for v in tree[root]:
        if not parents[v]:       # 한 번도 상위의 노드와 연결된 적이 없으면
            parents[v] = root
            findP(v)
findP(1)

for i in range(2, n+1):
    print(parents[i])

