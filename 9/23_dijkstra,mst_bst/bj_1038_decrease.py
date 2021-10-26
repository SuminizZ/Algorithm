# https://jjangsungwon.tistory.com/119

n = int(input())
cnt = 9

def findNth():
    global cnt
    num = 10
    while True:
        num_str = str(num)
        for i in range(1, len(num_str)):
            if num_str[i-1] <= num_str[i]:      # check if all depth of digits are decreasing
                upper = str(int(num_str[:i]) + 1)
                target = str(0)
                lower = num_str[i+1:]
                num = int(upper + target + lower)
                break
        else :      
            cnt += 1
            if cnt == n:
                return num
            num += 1      

    return num


def solve(n):
    if n <= 9:
        return n
    if n >= 1023:       # 1022th decreasing num : 9876543210 
        return -1
    
    else:
        return findNth()

print(solve(n))