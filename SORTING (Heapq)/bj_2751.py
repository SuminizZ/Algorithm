import sys
from heapq import *

n = int(input())
data = []
for i in range(n):
    data.append(int(sys.stdin.readline()))

heapify(data)
for i in range(len(data)):
    print(heappop(data))


def mergeSort(data):
    if len(data) <= 1:
        return data
    result = []
    med = len(data)//2

    left = mergeSort(data[med:])
    right = mergeSort(data[:med]) 
    lptr = 0
    rptr = 0

    while lptr < len(left) or rptr < len(right):
        val_l = left[lptr] if lptr < len(left) else float('inf')
        val_r = right[rptr] if rptr < len(right) else float('inf')
        if val_l <= val_r:
            result.append(val_l)
            lptr += 1
        else: 
            result.append(val_r)
            rptr += 1

    return result

print('\n'.join(map(str, mergeSort(data))))


def quickSort(data):
    if len(data) <= 1:
        return data

    pivot = data.pop()
    left = []
    right = []

    for d in data:
        if d <= pivot:
            left.append(d)
        else:
            right.append(d)
    
    return quickSort(left) + [pivot] + quickSort(right)

print('\n'.join(map(str, quickSort(data))))