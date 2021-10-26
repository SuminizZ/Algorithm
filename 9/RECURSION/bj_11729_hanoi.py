n = int(input())
cnt = 0
result = []

def hanoi(n, start, via, to):
    global cnt
    cnt += 1
    if n == 1:
        result.append("{0} {1}".format(start, to))
        return
    hanoi(n-1, start, to, via)
    result.append("{0} {1}".format(start, to))
    hanoi(n-1, via, start, to)

hanoi(n, 1, 2, 3)
print(cnt)      # 2**n - 1
print('\n'.join(result))


# 재귀는 재귀의 움직임을 하나하나 다 따라가기보단,
# 재귀 단위 별로 끊어서, 하니의 단위의 재귀가 정확히 어떤 동작을 수행해야 하는지 생각하기
# 생각보다 생각한 대로 구현된다.