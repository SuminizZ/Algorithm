import sys

n = int(input())
edges = []
for i in range(1, n+1):
    col = list(map(int, sys.stdin.readline().split()))
    for j in range(1, i):
        edges.append((i, j, col[j-1]))

edges.sort(key = lambda x : x[2])
root = [i for i in range(n+1)]
rank = [0 for _ in range(n+1)]

def find(v):
    if v != root[v]:
        root[v] = find(root[v])
    return root[v]

result = 0
for s, d, w in edges:
    root_s = find(s)
    root_d = find(d)

    if root_s != root_d:
        result += w
        if rank[root_s] > rank[root_d]:
            root[root_d] = root_s
        else:
            root[root_s] = root_d
            if rank[root_s] == rank[root_d]:
                rank[root_d] += 1

print(result)

