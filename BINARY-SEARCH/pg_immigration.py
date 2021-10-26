def binary_counter(mid, n, times):   
    cnt = 0
    for t in times:
        cnt += mid//t      
    
    return cnt
    
def solution(n, times):
    times.sort()    
    start = 0               
    end = times[-1]*n       

    while start <= end:     
        mid = (start + end)//2
        cnt = binary_counter(mid, n, times)
        if cnt >= n:
            end = mid - 1  
            ans = mid
        elif cnt < n:
            start = mid + 1
    
    return ans


    