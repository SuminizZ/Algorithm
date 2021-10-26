def counter(dist, rocks, n):
    remove = 0
    cur_rock = 0 + dist
    for rock in rocks:
        if rock < cur_rock:     # cur_rock 은 그대로(걸린 바위 제거함)
            remove += 1
            if remove > n:      # 해당 dist(간격)을 유지하기 위해 제거해야 하는 바위 수가 n개 초과이면, fail
                return False
        else:
            cur_rock = rock + dist      # cur_rock 위치 조정
    
    return True
    

def solution(distance, rocks, n):
    rocks.sort()
    ans = 0
    start = 0
    end = distance
    
    while start <= end:
        mid = (start + end)//2
        
        if counter(mid, rocks, n):
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
            
    return ans