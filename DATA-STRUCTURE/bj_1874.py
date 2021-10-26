import sys 

n = int(input())
data = list(map(lambda x: int(x.rstrip()), sys.stdin.readlines()))

def makeSeq(n):
    myStack = []
    result = []
    num = 1  

    for i in range(n):
        cur = data[i]

        while len(myStack) == 0 or myStack[-1] < cur: 
            myStack.append(num)
            result.append("+")
            num += 1

        if myStack[-1] > cur:
            return "NO"

        elif myStack[-1] == cur:
            myStack.pop()
            result.append("-")

    return '\n'.join(result)

print (makeSeq(n))
