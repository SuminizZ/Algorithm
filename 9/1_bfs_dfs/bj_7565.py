from collections import deque

m, n = map(int, input().split())     
tmtMap = []
dq = deque()
for y in range(n):
    tmtMap.append([int(i) for i in input().split()])
    for x in range(m):
        if tmtMap[y][x] == 1:
            dq.append((x, y))

def ripple(tmtMap):
    dy = [-1, 0, 1, 0]      
    dx = [0, 1, 0, -1]     
    ans = -10
    while dq:
        x, y = dq.popleft()
        for i in range(4):          
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0<= ny < n and tmtMap[ny][nx] == 0:     
                dq.append((nx, ny))
                tmtMap[ny][nx] += tmtMap[y][x] + 1       
                ans = max(ans, tmtMap[ny][nx])
    return ans

ans = ripple(tmtMap)

for row in tmtMap:
    if 0 in row: 
        print(-1)
        exit(0)

print(tmtMap)
if ans == -10:
    print(0)
else:
    print(ans-1)       

            