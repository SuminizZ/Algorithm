# dp : 최적부분구조 + 중복된 하위 문제
## 1. (오름차순 배열(유일) + 끝값 특정 + 합이 n)
import sys
input = sys.stdin.readline
tc = int(input())

dp = [[0, 0, 0] for _ in range(10001)]
dp[1][0] = 1
dp[2][0] = dp[2][1] = 1
dp[3][0] = dp[3][1] = dp[3][2] = 1

for i in range(4, 10001):
    dp[i][0] = dp[i-1][0]
    dp[i][1] = dp[i-2][0] + dp[i-2][1]
    dp[i][2] = dp[i-3][0] + dp[i-3][1] + dp[i-3][2]

while tc:
    tc -= 1
    n = int(input())
    print(sum(dp[n]))

## 2. (이해 x)
# import sys
# input = sys.stdin.readline
# tc = int(input())
# result = []

# for _ in range(tc):
#     n = int(input())

#     dp = [0]*(n+1)
#     dp[0] = dp[1] = 1
#     for i in range(2, n+1):
#         dp[i] += 1 + dp[i-2] 
#     for i in range(3, n+1):
#         dp[i] += dp[i-3]

#     result.append(dp[n])

# print('\n'.join(map(str, result)))
    

