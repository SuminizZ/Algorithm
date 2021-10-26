# 조건 1. queen 은 서로 같은 일직선 상에 놓이지 않는다(하나의 행, 열에는 하나의 퀸만 배치)
# 조건 2. 서로 같은 대각선상에 놓이지 않는다(행의 차 != 열의 차, 즉 임의의 두 queen 을 연결한 선의 기울기가 -1, 1 이 아니다)

# 방법 1. 재귀 + dfs + 백트래킹

n = int(input())
qMap = [0 for _ in range(n)]
visited = [False for _ in range(n)]

def nQueen(qMap, n, row):
    cnt = 0

    if row == n:
        return 1
    for col in range(n):
        qMap[row] = col         # 각 행에 대응하는 열 넣어주기(queen 배치)
        for i in range(row):        # 존재하는 모든 queen 의 위치에 대해
            if qMap[i] == qMap[row] or abs(qMap[i] - qMap[row]) == abs(i - row):       
                break
        else :                  # for - else 문 : 가장 마지막의 if 에 대한 else, if 문을 타고 break 된 애들은 else 문을 타지 못함
            cnt += nQueen(qMap, n, row + 1)

    return cnt

print(nQueen(qMap, n, 0))


# 방법 2. 작동은 하지만, permutations 쓰면 메모리 초과 난다.

from itertools import permutations

n = int(input())

def backTrack(q):
    diagnalMap1 = [0 for _ in range(2*n)]    # nxn 배열 상의 우하향 대각선
    diagnalMap2 = [0 for _ in range(2*n)]    # nxn 배열 상의 우상향 대각선
    
    for i in range(n):    
        if diagnalMap1[q[i]-i + n] > 0 or diagnalMap2[q[i] + i] > 0 :        # 같은 우하향 대각선은 모두 같은 p[i] - i + n 값을 가짐
            return 0
        diagnalMap1[q[i]-i + n] = 1
        diagnalMap2[q[i] + i] = 1

    return 1

def nQueen(n):
    arr = list(range(n))
    combs = list(permutations(arr, n))  # 각 row 에 서로 다른 col 부여하는 모든 경우의 수 (조건 1.)
    cnt = 0
    for comb in combs:
        cnt += backTrack(comb)

    return cnt

print(nQueen(n))