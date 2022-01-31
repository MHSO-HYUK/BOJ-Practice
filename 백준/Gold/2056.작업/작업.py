from collections import deque
from sys import stdin
def hard():
    queue = deque([])
    temp = []
    timer = []
    for i in range(1, n+1):
        if(degree[i] == 0):
            temp.append([i, time[i]])
    temp.sort(key = lambda x : x[1])
    for i in range(len(temp)):
        queue.append([temp[i][0], temp[i][1]])
        timer.append(temp[i][1])
    while(queue):
        x, t = queue.popleft()
        for v in range(n+1):
            if(x in work[v]):
                degree[v] -= 1
                if(degree[v] == 0):
                    if(visit[v]):
                        queue.append([v,max(max(visit[v])+time[v], t+time[v])])
                        timer.append(max(max(visit[v])+time[v], t+time[v]))
                    else:
                        queue.append([v, t + time[v]])
                        timer.append(t+time[v])
                else:
                    visit[v].append(t)
    return max(timer)

n = int(stdin.readline())
work = [[] for _ in range(n+1)]
degree = [0 for _ in range(n+1)]
time = [0 for _ in range(n+1)]
visit = [[] for _ in range(n+1)]
for i in range(n):
    a, b, *c = map(int, stdin.readline().split())
    degree[i+1] += b
    time[i+1] = a
    work[i+1] = c
print(hard())