from collections import deque

n = int(input())
k = int(input())

apples = []
for i in range(k):
    row, col = map(int, input().split())
    apples.append((col-1, row-1))     

appleloc = [[0]*n for i in range(n)]   
for x, y in apples:
    appleloc[y][x] = 1

turn = dict()
m = int(input())
for i in range(m):
    time, change = input().split()
    turn[int(time)] = change

dq = deque([[0,0]])    
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def turnto(cur_d, change):  
    if change == 'D':
        nxt_d = (cur_d + 1)%4
    elif change == 'L':
        nxt_d = (cur_d - 1)%4
    return nxt_d

def snakeMove():
    cur_d = 0  
    sec = 0

    while True:
        cx, cy = dq[-1]  
        if sec in turn:
            cur_d = turnto(cur_d, turn[sec])
        nx = cx + dirs[cur_d][0] 
        ny = cy + dirs[cur_d][1]
        sec += 1

        if 0 <= nx < n and 0 <= ny < n:
            if [nx, ny] in dq: 
                break
            if appleloc[ny][nx] == 1:
                appleloc[ny][nx] = 0
                dq.append([nx, ny])
            else:
                dq.append([nx, ny])
                dq.popleft()
        else: 
            break

    return sec
    
print(snakeMove())




