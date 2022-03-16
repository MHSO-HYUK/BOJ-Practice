# 16397 탈출
from sys import stdin
from collections import deque

def escape(n, cnt):
    queue = deque([[n, cnt]])
    visit.add(n)
    while(queue):
        now, cnt = queue.popleft()
        if cnt > t:
            break
        if now == g:
            return cnt
        
        if not now+1 in visit and 0 <= now+1 < 100000:
            visit.add(now+1)
            queue.append([now+1, cnt+1])
        
        if 0 <= 2*now < 100000:
            l = len(str(2*now))
            if not 2*now - 10**(l-1) in visit:
                visit.add(2*now-10**(l-1))
                queue.append([2*now-10**(l-1) , cnt+1])
    return 'ANG'
    
n, t, g = map(int, stdin.readline().split())
#A를 누르면 N이 1증가
#B를 누르면 2*N에 가장 높은 자릿수가 1 줄어듬 
#N이 99999를 넘어가는 순간 탈출 실패
visit = set()
print(escape(n, 0))