# 13905 세부 
# 출발 위치에서 종료위치까지 들고 갈 수 있는 최대 무게 
from sys import stdin
from collections import deque
def is_possible(limit):
    queue = deque()
    queue.append(s)
    visited = {i: False for i in range(1,n+1)}
    visited[s] = True
    while queue:
        cur_node = queue.popleft()
        if cur_node == e:
            return True
        for next_node, next_limit in graph[cur_node]:
            if not visited[next_node] and limit <= next_limit:
                visited[next_node] = True
                queue.append(next_node)
    return False

n, m = map(int, stdin.readline().split())
s, e = map(int, stdin.readline().split())
graph = [[] for _ in range(1+n)]
for _ in range(m):
    a, b, c = map(int, stdin.readline().split()) # 집1 / 집2 / 무게 제한 
    graph[a].append([b, c])
    graph[b].append([a, c])
left, right = 1, 1000000
ans = 0
while(left <= right):
    mid = (left+right)//2
    if is_possible(mid):
        left = mid + 1
        ans = mid
    else:
        right = mid - 1
        
print(ans)