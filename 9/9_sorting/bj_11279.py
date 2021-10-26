from heapq import *
import sys

n = int(input())
inputs = []
for i in range(n):
    inputs.append(int(sys.stdin.readline()))

hq = []
for i in inputs:
    if i != 0:
        heappush(hq, -i)
    if i == 0:
        if not hq:
            print(0)
        else: print(abs(heappop(hq)))