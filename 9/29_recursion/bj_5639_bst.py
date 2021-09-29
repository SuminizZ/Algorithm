import sys  
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
preorder = []
while True:
    try: 
        preorder.append(int(input()))
    except: break

def reorder(preorder):
    if not preorder:
        return []
    root = preorder[0]

    for i in range(len(preorder)):
        if preorder[i] > root:      # right sub_tree
            return reorder(preorder[1:i]) + reorder(preorder[i:]) + [root]  # left tree + right tree + root 

    # No right sub_tree || len(preorder) == 1 / climbing up from the final left leaf node
    return reorder(preorder[1:]) + [root]

postorder = reorder(preorder)
print('\n'.join(map(str, postorder)))
