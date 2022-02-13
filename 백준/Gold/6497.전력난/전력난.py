#6497 전력난 
#모든 집에 대하여 가는 길에 불이 켜져있어야 함 + 최소 비용 
from sys import stdin 
import heapq
from collections import deque
def power():
    queue = deque()
    ans = 0
    visit = [0 for _ in range(n+1)]
    parent = [i for i in range(n+1)]
    while(road):
        queue.append(heapq.heappop(road))
        
    while(queue):
        cost, x, y = queue.popleft()
        if parent[x] > parent[y]:
            temp = parent[x]
            for v in range(1, n+1):
                if parent[v] == temp:
                    parent[v] = parent[y]
        
        
        elif parent[x] < parent[y]:
            temp = parent[y]
            for v in range(1, n+1):
                if parent[v] == temp:
                    parent[v] = parent[x]
                        
        else:
            ans += cost
            
    return ans 

while(1):
    n, m = map(int, stdin.readline().split())
    if([n, m] == [0, 0]):
        break
    road = []
    for _ in range(m):
        x, y, z = map(int,stdin.readline().split())
        heapq.heappush(road, [z, x, y])
    print(power())
