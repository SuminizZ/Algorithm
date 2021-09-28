import sys
input = sys.stdin.readline
tc = []

while True:
    temp = list(map(int, input().split()))
    if len(temp) == 1:
        break
    tc.append(temp)

comb = []
combs = []
def getCombs(s, r):
    if r == 6:
        comb.sort()
        print(*comb)
        return combs.append(comb)
    for i, num in enumerate(s):
        if num not in comb:
            comb.append(num)
            getCombs(s[i+1:], r+1)
            comb.pop()

    return combs

for case in tc:
    k = case[0]
    s = case[1:]
    getCombs(s, 0)
    print()

