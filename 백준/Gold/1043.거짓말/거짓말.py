from sys import stdin
from collections import deque
def lie():
    global cnt
    queue = deque()
    for v in avoid:
        queue.append(v)
        visit[v] = 1
    while(queue):
        v = queue.popleft()
        for k in party:
            if(v in k): #avoid가 파티에 포함된 경우
                for a in k:
                    if(visit[a] == 0):
                        visit[a] = 1
                        queue.append(a)

n, m = map(int, stdin.readline().split())
avoid = list(map(int, stdin.readline().split()))[1:]
party = []
for _ in range(m):
    party.append(list(map(int, stdin.readline().split()))[1:]) 
    
visit = [0 for _ in range(n+1)]
lie()
hello = []
for i in range(n+1):
    if(visit[i] == 1):
        hello.append(i)
cnt = 0
for v in party:
    for i in hello:
        if(i in v):
            cnt += 1
            break
print(m-cnt)