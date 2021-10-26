  # Stack 을 이용한 풀이
  
from collections import defaultdict
def solution(tickets):
    graph = defaultdict(list)      
    for start, end in tickets:    
        graph[start].append(end)
        graph[start].sort(reverse = True)    
    
    stack = ['ICN']
    route = []
    print(graph)
    
    while stack:
        cur = stack[-1] 
        if cur in graph and graph[cur]:        
            stack.append(graph[cur].pop())   
        else:
            route.append(stack.pop())       
    
    route.reverse()     
    
    return route