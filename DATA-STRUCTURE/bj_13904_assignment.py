import sys
input = sys.stdin.readline
from heapq import *
from collections import defaultdict

n = int(input())
tasks = []
howmany = defaultdict(int)
for _ in range(n):
    d, s = map(int, input().split())
    heappush(tasks, [-s, d])
    howmany[d] = 0              # 해당 마감일의 과제가 몇 번 count 됐는지 기록

cnt, max_d, total = 0, 0, 0
while tasks:
    cur_s, cur_d = heappop(tasks)
    if cnt >= cur_d:      # 현재까지 완료한 과제 수가 마감일보다 많을 때
        tmp_cnt = 0           
        for tmp_d in range(1, max_d + 1):       # 현재 마감일보다 마감일이 같거나 높은 모든 과제에 대해 양보 가능한지 확인
            tmp_cnt += howmany[tmp_d]
            if tmp_d >= cur_d and tmp_cnt >= tmp_d:      # 양보 불가
                break
        else:
            total += cur_s          # for-else 구문 : 현재 마감일 이전에 완료된 모든 과제가 양보 가능한 경우
            howmany[cur_d] += 1
            cnt += 1
    else:                       # 타겟 과제의 마감일이 완료한 과제수보다 클 때(아직 마감기한이 남은 경우), 그냥 넣어줌
        total += cur_s
        howmany[cur_d] += 1
        max_d = max(max_d, cur_d)
        cnt += 1

print(-total)
# print(howmany)