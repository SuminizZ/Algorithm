# 1. 숫자 1씩 올려가며 완전탐색? 단, min 값 이상, sum(추) 값 이하
import sys
input = sys.stdin.readline
n = int(input())
bw = list(map(int, input().split()))
bw.sort()

temp = 0       # sum
for i in range(n):
    if bw[i] > temp + 1:
        print(temp+1)
        break
    temp += bw[i]

else: print(temp + 1)   # for 문 다 돌 때까지 if 문 한 번도 못 탔으면 추의 전체 총합 + 1
