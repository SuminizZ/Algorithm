formula = input().split('-')
result = sum(list(map(int, formula.pop(0).split('+'))))

for e in formula:    # if there's any '-' in formula
    e = sum(list(map(int, e.split('+'))))
    result -= e

print(result)

# regex in python
# () <- keep the separators
# [] <- match everything in between
# ^a-zA-Z0-9 <-except alphabets, upper/lower and numbers.

# import re
# formula = list(re.split('([+-])', input()))
# print(formula)