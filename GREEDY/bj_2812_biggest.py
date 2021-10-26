# 내 뒷자리 수가 나보다 크면 바로 삭제(앞자리가 커지는 게 전체 수에 더 영향이 크니깐 큰 자릿수부터 바로 처리 가능)
from collections import deque

n, k = map(int, input().split())
num = input()
dq = deque([])
rmv = 0

for i in range(n):
    cur_digit = int(num[i])
    while rmv < k and dq and dq[-1] < cur_digit:
        dq.pop()
        rmv += 1
    dq.append(cur_digit)

print(int(''.join(map(str, dq))[:n-k])) 
# 모든 자리 숫자 다 돌 때까지 rmv 가 k 를 넘지 못한 경우 = dq 에 남아있는 앞자리 숫자들이 뒷자리 숫자들보다 모두 클 때 >> 앞의 k자리 숫자만 출력해준다


# string 이용 풀이 : 메모리 초과
n, k = map(int, input().split())        # 1 ≤ K < N ≤ 500,000 : string 이나 list 로 접근하면 메모리 초과난다
num = input()

def remove(num, rmv):
    if rmv >= k:
        print(int(num))
        return

    for i in range(len(num)-1):
        if int(num[i]) < int(num[i+1]):
            num = num[:i] + num[i+1:]      # 슬라이싱하면 메모리 초과?
            remove(num, rmv+1)
            break
    
remove(num, 0)

