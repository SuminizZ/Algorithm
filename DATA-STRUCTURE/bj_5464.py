from collections import deque
from heapq import *

n, m = map(int, input().split())
price = dict()
for i in range(n):
    price[i+1] = int(input())
weight = dict()
for i in range(m):
    weight[i+1] = int(input())
order = deque()
for i in range(2*m):
    order.append(int(input()))

parked = {i+1: 0 for i in range(n)}
empty = [(i+1) for i in range(n)]
heapify(empty)
waiting = deque()
profit = 0

while order:
    while waiting and empty:
        cur = waiting.popleft()
        p = heappop(empty)
        parked[p] = cur
        profit += price[p]*weight[cur]
    cur = order.popleft()
    if cur > 0:
        if not empty:
            waiting.append(cur)
        else:
            p = heappop(empty)   
            parked[p] = cur
            profit += price[p]*weight[cur]
    elif cur < 0:
        p = [p for p, car in parked.items() if car == abs(cur)]     
        heappush(empty, p[0])

print(profit)