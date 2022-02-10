#13913 숨바꼭질 4
from sys import stdin
from collections import deque

def hide(n, k, way):
    queue = deque([[n, 0, way]])
    visit[n] = 1
    if(n > k):
        return n-k, range(n, k-1, -1)
    while(queue):
        n, cnt, way = queue.popleft()
        if(n == k):
            return cnt, way
            break
        if(2*n <= temp and visit[2*n] == 0):
            visit[2*n] = 1
            queue.append([2*n, cnt + 1, way+[2*n]])
        if(n+1 <= temp and visit[n+1] == 0):
            visit[n+1] = 1
            queue.append([n+1, cnt+1, way+[n+1]])
        if(n-1 >= 0 and visit[n-1] == 0):
            visit[n-1] = 1
            queue.append([n-1, cnt+1, way+[n-1]])


n, k  = map(int, stdin.readline().split())
temp = max(2*n, 2*k)
visit = [0 for _ in range(temp+1)]
cnt, way = hide(n, k, [n])

print(cnt)
for i in range(cnt+1):
    print(way[i], end =   ' ')