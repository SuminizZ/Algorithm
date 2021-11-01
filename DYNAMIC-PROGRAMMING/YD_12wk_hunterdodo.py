import sys
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))

DP = [float('inf') for _ in range(n+1)]        # k 번째 거미까지 필요한 총알 개수 저장
DP[0] = 1
DP[1] = 1

for i in range(2, n+1):
    for j in range(1, i):
        if heights[i-1] == heights[j-1] - 1:
            DP[i] = DP[j]
            heights[j-1] = -1
            break
    else:                                   # for - else 문
        DP[i] = min(DP[i], max(DP[:i]) + 1)
    
    # print(DP[i])
        
print(max(DP))