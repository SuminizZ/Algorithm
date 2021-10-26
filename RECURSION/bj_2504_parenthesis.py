p_data = list(input())
p_stack = []
flag = False
open = ['(', '[']

for cur_p in p_data:
    if cur_p in open:      # open p
        p_stack.append(cur_p)
    else:                  # close p
        if p_stack:         
            if cur_p == ')':
                tmp = 0
                while p_stack:
                    top = p_stack.pop()     # access to prev open p
                    if top == '[':
                        flag = True
                        break
                    elif top == '(':       
                        if tmp == 0:    # p(cur) outside of p(prev)
                            p_stack.append(2)     # ends with digit
                        else:
                            p_stack.append(2*tmp)
                        break
                    else:       # type(top) is int = p(prev) in p(cur)
                        tmp += top                        
                        
            elif cur_p == ']':
                tmp = 0
                while p_stack:
                    top = p_stack.pop()     # access to prev open p
                    if top == '(':
                        flag = True
                        break
                    elif top == '[':       
                        if tmp == 0:    # p(cur) outside of p(prev)
                            p_stack.append(3)     # ends with digit
                        else:
                            p_stack.append(3*tmp)
                        break
                    else:       # type(top) is int = p(prev) in p(cur)
                        tmp += top 
        else:
            flag = True
            break

if '(' in p_stack or '[' in p_stack:
    flag = True

if flag:
    print(0)
else:
    print(sum(p_stack))



    