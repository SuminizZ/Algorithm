import sys
n, c = map(int, input().split())
house = []
for i in range(n):
    house.append(int(sys.stdin.readline()))
house.sort()

def counter(dist):
    cnt = 1
    curloc = house[0] + dist
    for i in range(1, n):
        if house[i] >= curloc:
            cnt += 1    
            curloc = house[i] + dist

    return cnt

start, end = 1, house[-1] - house[0]     
ans = 0

while start <= end:
    mid = (start + end)//2

    if counter(mid) >= c:      
        start = mid + 1
        ans = mid       
    else:
        end = mid - 1

print(ans)


