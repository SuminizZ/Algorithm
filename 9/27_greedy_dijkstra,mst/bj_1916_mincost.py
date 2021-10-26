import sys
input = sys.stdin.readline
from collections import defaultdict
from heapq import *

n = int(input())
bus = int(input())
graph = defaultdict(list)
for i in range(bus):
    s, d, cost = map(int, input().split())
    graph[s].append((d, cost))
start, end = map(int, input().split())

hq = [(0, start)]
heapify(hq)
mincost = [float('inf') for _ in range(n+1)]    # city_number = index

while hq:
    cost, city = heappop(hq)      # cost : total cost summed up to current city
    if city == end:
        print(mincost[end])
        sys.exit(0)
    if city in graph and graph[city]:
        for d_city, d_cost in graph[city]:
            if mincost[d_city] < cost : continue
            sum_cost = d_cost + cost
            if mincost[d_city] > sum_cost:  # if opposite, d_city alreay in hq with less cost
                mincost[d_city] = sum_cost
                heappush(hq, (mincost[d_city], d_city))

print(mincost[end])

