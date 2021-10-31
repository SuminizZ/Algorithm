import sys
# from collections import defaultdict
input = sys.stdin.readline

n = int(input())
coins = list(map(int, input().split()))
# coins.sort(reverse=True)
change = int(input())
 
DP = [0 for _ in range(change+1)]

DP[0] = 1

for c in coins:                 
    for i in range(1, change+1):        # 특정 동전만 사용해서 지불하는 경우
        if i - c >= 0:
            DP[i] += DP[i - c]
            
print(DP)


# for i in range(1, change+1):
#     for c in coins:           # 동일한 케이스가 누적해서 더해짐
#         if i - c >= 0:
#             DP[i] += DP[i-c]
