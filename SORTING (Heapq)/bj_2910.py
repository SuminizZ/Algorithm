import sys
from collections import defaultdict

n, c = map(int, input().split())
nums = list(map(int, sys.stdin.readline().split()))
freq = defaultdict(int)

for num in nums:
    freq[num] += 1

freq_list = sorted(freq.items(), key=lambda x: x[1], reverse=True)
result = []
for x, f in freq_list:
    result += [x for _ in range(f)]

print(*result)


