from collections import deque

def knightMove(l, start, end):
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]

    graph = [[0]*l for i in range(l)]
    cx, cy = start
    gx, gy = end
    graph[cy][cx] = 0 
    dq = deque()
    dq.append([cx, cy])

    while dq:
        cx, cy = dq.popleft()
        for j in range(8):    
            nx = cx + dx[j]
            ny = cy + dy[j]
            if 0 <= nx < l and 0 <= ny < l :
                if graph[ny][nx] == 0:  
                    graph[ny][nx] = graph[cy][cx] + 1
                    if cx == gx and cy == gy: 
                        return graph[cy][cx]
                    dq.append([nx, ny])
                      
    return graph[gy][gx]

n = int(input())
for i in range(n):
    l = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    if x0 == x1 and y0 == y1: print(0)
    else:
        print(knightMove(l, (x0, y0), (x1, y1)))

