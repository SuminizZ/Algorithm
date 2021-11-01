import sys
input = sys.stdin.readline

n = int(input())
requests = list(map(int, input().split()))
total_budget = int(input())

def check(limit):
    tmp = total_budget
    for r in requests:
        if r <= limit:
            tmp -= r
        else:
            tmp -= limit
    
    return tmp >= 0
    
def bst():
    start = 0
    end = max(requests)*2
    
    while start <= end:
        mid = (start + end)//2
        
        if check(mid):
            start = mid + 1
            ans = mid
    
        else:
            end = mid - 1
            
    return ans
    
ans = bst()
if ans >= max(requests):
    ans = max(requests)
    
print(ans)

    