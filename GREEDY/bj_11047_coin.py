import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

cnt = 0
i = 0
while k != 0:
    coin = coins[i]
    i += 1
    cnt += k//coin
    k %= coin

print(cnt)