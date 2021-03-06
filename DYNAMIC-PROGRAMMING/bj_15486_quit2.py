import sys
input = sys.stdin.readline

consult = {}
n = int(input())
for i in range(n):
    consult[i] = list(map(int, input().split()))

dp = [0]*(n+1)

for i in range(0, n):
    if i + consult[i][0] <= n:
        dp[i + consult[i][0]] = max(dp[i + consult[i][0]], dp[i] + consult[i][1])       # i 번째 날의 최대 이익

    dp[i+1] = max(dp[i+1], dp[i])       # 한 번도 if 문 타지못한 끝 쪽의 날짜들을 위한 코드

print(dp[n])


### 다른 풀이
import sys
input = sys.stdin.readline

last_work = int(input())
max_reward = [0 for _ in range(last_work+1)]
max_day = 0 # 일 시작하는 날 전까지 중 최대 값
for day in range(1, last_work+1):
    work_day, reward = map(int, input().split())
    finish_day = day+work_day-1
    max_day = max(max_day, max_reward[day-1])
    if finish_day > last_work:
        continue
    max_reward[finish_day] = max(reward+max_day, max_reward[finish_day])
print(max(max_reward))