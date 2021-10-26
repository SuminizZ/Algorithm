from heapq import *
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
jewelry = []
bags = []

for _ in range(n):
    heappush(jewelry, list(map(int, input().split())))      
bags = [int(input()) for _ in range(k)]
bags.sort()

result = 0
jewelry_maxh = []
for bag in bags:
    while jewelry and bag >= jewelry[0][0]:
            heappush(jewelry_maxh, -jewelry[0][1])
            heappop(jewelry)
    
    if jewelry_maxh:
        result += heappop(jewelry_maxh)

print(-result)

