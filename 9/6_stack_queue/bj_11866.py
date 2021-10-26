import sys
from queue import Queue
n, k = map(int, sys.stdin.readline().split())

def josephus(n, k):
    circle = Queue()
    for i in range(1, n+1):
        circle.put(i)
    result = []

    for i in range(n):
        r = k

        while r-1 > 0:       
            circle.put(circle.get())
            r -= 1

        result.append(circle.get())

    return result

print('<'+', '.join(map(str, josephus(n, k)))+'>')

