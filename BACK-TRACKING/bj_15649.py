n, m = map(int, input().split())
arr = [i+1 for i in range(n)]   
result = []

def getPermute(r, m):
    if r == m:
        print (' '.join(map(str, result)))

    for num in arr:  
        if num not in result:
            result.append(num)
            getPermute(r+1, m)
            result.pop()

getPermute(0, m)

