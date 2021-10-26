n, m = map(int, input().split())
arr = [i+1 for i in range(n)]   
result = []

def getPermute(r, m, arr):
    if r == m:
        print (' '.join(map(str, result)))

    for i, num in enumerate(arr):  
        if num not in result:
            result.append(num)
            getPermute(r+1, m, arr[i+1:])
            result.pop()

getPermute(0, m, arr)
