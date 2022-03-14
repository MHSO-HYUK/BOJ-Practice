# 14867 물통
from sys import stdin 
from collections import deque
from collections import defaultdict
def bfs():
    queue = deque()
    queue.append([0, 0, 0])
    visit[(0, 0)] = 1
    while(queue):
        na, nb, cnt = queue.popleft()
        if na == ta and nb == tb:
             return cnt
            
        if not visit.get((0, nb)) and na != 0:
            visit[(0, nb)] = 1
            queue.append([0, nb, cnt+1])
            
        if not visit.get((na, 0)) and nb != 0:
            visit[(na,0)] = 1
            queue.append([na, 0, cnt+1])
            
        if not visit.get((a, nb)) and na != a:
            visit[(a, nb)] = 1
            queue.append([a, nb, cnt+1])
            
        if not visit.get((na, b)) and nb != b:
            visit[(na, b)] = 1
            queue.append([na, b, cnt+1])
        
        if na+nb > a:
            if not visit.get((a, na+nb-a)) and na != a:
                visit[(a, na+nb-a)] = 1
                queue.append([a, na+nb-a, cnt+1])
            
        else:
            if not visit.get((na+nb, 0)):
                visit[(na+nb, 0)] = 1
                queue.append([na+nb, 0, cnt+1])
            
        if na+nb > b:
            if not visit.get((na+nb-b, b)) and nb != b:
                visit[(na+nb-b, b)] = 1
                queue.append([na+nb-b, b, cnt+1])
                
        else:
            if not visit.get((0, na+nb)):
                visit[(0, na+nb)] = 1
                queue.append([0, na+nb, cnt+1])
                
    return -1
        
a, b, ta, tb = map(int, stdin.readline().split())# a 용량 b 용량 목표 a b
# 1. fil x 가득
# 2. empty x 
# 3. move(x -> y) // 만약 y 용량을 초과한다면 최대로 y를 채우고 남은 x는 남김
visit = {}
print(bfs())