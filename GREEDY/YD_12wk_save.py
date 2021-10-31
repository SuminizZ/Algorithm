import sys
input = sys.stdin.readline

n, k = map(int, input().split())

time = []
for _ in range(n):
    time.append(int(input()))
    
total = 0
gap = []
for i in range(n-1):
    cur_gap = time[i+1] - time[i]
    gap.append(cur_gap)        
    total += cur_gap

total = total + 1       # 마지막 촛불

gap.sort(key = lambda x : x, reverse=True)

off = gap[:k-1]

for i in range(len(off)):
    total -= off[i] - 1
    
print(total)

