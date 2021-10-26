### DP(백준 11053번) : O(n^2) ###  
import sys

l = int(input())
nums = list(map(int, sys.stdin.readline().split()))
longest = [0 for _ in range(l+1)]

for i in range(1, l+1):
    for j in range(1, i):
        if nums[i-1] > nums[j-1]:
            longest[i] = max(longest[i], longest[j]+1)

print(max(longest)+1)


