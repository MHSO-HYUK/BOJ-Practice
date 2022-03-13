# 14395 4연산
from sys import stdin 
import sys
from collections import deque
from collections import defaultdict

s, t= map(int, stdin.readline().split())
queue= deque([[s, 0, []]])
if s == t:
    print(0)
    sys.exit()
dic = defaultdict(int)
while(queue):
    now, cnt, comm = queue.popleft()
    if now == t:
        for k in range(len(comm)):
            print(comm[k], end = '')
        sys.exit()
    else:
        if now**2 < t+1 and not dic[now**2]:
            dic[now**2] = 1
            queue.append([now**2, cnt+1, comm+['*']])
            
        if now+now < t+1 and not dic[now*2]:
            dic[now*2] = 1
            queue.append([2*now, cnt+1, comm+['+']])
            
        if not dic[0]:
            dic[0] = 1
            queue.append([now-now, cnt+1, comm+['-']])

        if now != 0 and not dic[1]:
            dic[1] = 1
            queue.append([now//now, cnt+1, comm+['/']])
print(-1)