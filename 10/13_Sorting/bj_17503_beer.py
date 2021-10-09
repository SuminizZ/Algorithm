import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
max_c = 0
beers = []
for _ in range(k):
    beer = list(map(int, input().split()))
    beers.append(beer)
    max_c = max(max_c, beer[1])
beers.sort(key= lambda x : x[0], reverse=True)

def check(cur_c):
    cnt = 0
    pref = 0
    for p, c in beers:
        if cnt == n:
            break
        if c <= cur_c:
            pref += p
            cnt += 1
        else: continue

    return pref >= m and cnt == n
        
start = 1
end = max_c
while start <= end:
    mid = (start + end)//2
    if check(mid):
        end = mid - 1
        ans = mid
    else:
        if mid >= max_c:
            print(-1)
            sys.exit(0)
        else: 
            start = mid+1

print(ans)

