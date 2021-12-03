from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
heapify(nums)

ans = 0
while len(nums) > 1:
    fst = heappop(nums)
    sec = heappop(nums)
    tmp = fst + sec
    ans += tmp 
    heappush(nums, tmp)

print(ans)