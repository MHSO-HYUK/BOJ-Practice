#5014 스타트링크
#f 전체 - g 목표 - s 현재
#위로 u 층 - 아래로 d층  
import sys
from sys import stdin
from collections import deque
f, s, g, u, d = map(int, stdin.readline().split())
visit = [0 for _ in range(f+1)]
visit[s] = 1
queue = deque([[s, 0]])
while(queue):
    now, cnt = queue.popleft()
    if(now == g):
        print(cnt)
        sys.exit()
    if(now+u <= f and visit[now+u] == 0):
        visit[now+u] = 1
        queue.append([now+u, cnt + 1])
    
    
    if(1<=now-d and visit[now-d] == 0):
        visit[now-d] = 1
        queue.append([now-d, cnt + 1])
    

print('use the stairs')