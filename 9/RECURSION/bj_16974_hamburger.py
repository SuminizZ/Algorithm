n, x = map(int, input().split())

def count_patty(lvl, x):
    if lvl == 0:
        return x
    if x <= 0:
        return 0
    cur_tot = 2**(lvl+2) - 3
    cur_patty = 2**(lvl+1) - 1
    if x == cur_tot:
        return cur_patty
    if x < cur_tot:
        mid = (1 + cur_tot)//2
        prev_patty = 2**(lvl) - 1
        if x == mid:
            return prev_patty + 1   # 1 added to prev patty_num
        else:
            return count_patty(lvl-1, x-1)    # x-1 : except the last B
    if x > cur_tot:
        x = x - (cur_tot + 1)       # 1 : mid P
        return cur_patty + 1 + count_patty(lvl, x)

result = count_patty(n, x)
print(result)


# def hamburger(lvl):
#     if lvl == 0:
#         return 'P'
    
#     left = 'B' + hamburger(lvl-1)
#     right = left[::-1]
#     result = left + 'P' + right
#     return result

# burger = hamburger(n)
# l = len(burger)
# print(burger[l-x:].count('P'))