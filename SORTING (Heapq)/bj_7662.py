from heapq import *
import sys

t = int(input())

for _ in range(t):
    n = int(input())
    maxh = []
    minh = []
    cnt = 0
    out = [False for _ in range(n)]

    for i in range(n):
        order, num = sys.stdin.readline().split()
        num = int(num)
        if order == 'I':
            heappush(maxh, (-num, i))
            heappush(minh, (num, i))
            cnt += 1

        if order == 'D':
            if cnt > 0:
                if num == -1:
                    while out[minh[0][1]] == True:
                        heappop(minh)
                    _, idx = heappop(minh)
                    out[idx] = True
                elif num == 1:
                    while out[maxh[0][1]] == True:
                        heappop(maxh)
                    _, idx = heappop(maxh)
                    out[idx] = True
                cnt -= 1
    
    if cnt <= 0:
        print("EMPTY")
    else:
        while out[minh[0][1]] == True:
            heappop(minh)
        while out[maxh[0][1]] == True:
            heappop(maxh)
        result = [-maxh[0][0], minh[0][0]]
        print(*result)
