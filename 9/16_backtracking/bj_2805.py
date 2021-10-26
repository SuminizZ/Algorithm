import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
trees.sort()

def binary_cut(height):     
    gain = 0
    for tree in trees:
        if tree > height:
            gain += tree - height

    return gain

ans = 0
start = 1
end = trees[-1]*2      
while start <= end:
    mid = (start + end)//2
    gain = binary_cut(mid)
    if gain > m:       
        start = mid + 1
        ans = mid
    elif gain < m:
        end = mid - 1
    else:
        ans = mid   # 여기선 굳이 더 할 필요 없음
        break

print(ans)


