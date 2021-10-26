
import sys

l = int(input())
nums = list(map(int, sys.stdin.readline().split()))
num_arr = [0]

for num in nums:
    if num > num_arr[-1]:   
        num_arr.append(num)
    else:           
        start = 0
        end = len(num_arr)
        while start < end:
            mid = (start + end)//2
            if num > num_arr[mid]:
                start = mid + 1
            else:    
                end = mid       
                target = mid
        num_arr[target] = num

print(len(num_arr)-1)

