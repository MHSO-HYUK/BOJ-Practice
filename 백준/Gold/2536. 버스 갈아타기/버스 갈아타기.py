import sys, collections

# 입력부
n, m = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

# arr : 버스의 시점과 종점을 저장하는 리스트
arr = [0] * (k + 1)

# adj : 인접 리스트
adj = [[] for _ in range(k + 1)]

# 버스 정보 입력
for _ in range(k):
    a,b,c,d,e = map(int, sys.stdin.readline().split())
    arr[a] = (min(b,d), min(c,e), max(b,d), max(c,e))
    
# check : 더 큰 버스에 의해 포함되는 버스 확인용 리스트
check = [False] * (k + 1)
for i in range(1, k + 1):
    temp = False
    x1, y1, x2, y2 = arr[i]
    for j in range(1, k + 1):
        if i == j:
            continue
        x3, y3, x4, y4 = arr[j]
        # 수직 버스인 경우
        if x1 == x2 == x3 == x4:
            if y3 <= y1 <= y2 <= y4:
                temp = True
        # 수평 버스인 경우
        if y1 == y2 == y3 == y4:
            if x3 <= x1 <= x2 <= x4:
                temp = True
    check[i] = temp

for i in range(1, k + 1):
    # 이미 포함되는 버스면 continue
    if check[i]:
        continue
    x1, y1, x2, y2 = arr[i]
    for j in range(1, k + 1):
        # 이미 포함되는 버스면 continue
        if check[j]:
            continue
        if i == j:
            continue
        x3, y3, x4, y4 = arr[j]
        # 한 점에서 만나는 경우 (방향이 서로 다른 경우)
        if x1 <= x3 <= x2 and x1 <= x3 <= x2:
            if y3 <= y1 <= y4 and y3 <= y2 <= y4:
                adj[i].append(j)
                adj[j].append(i)
        # 한 점 혹은 겹치는 경우 (수평 방향)
        if y1 == y2 == y3 == y4:
            if not (x1 > x4 or x2 < x3):
                adj[i].append(j)
                adj[j].append(i)
        # 한 점 혹은 겹치는 경우 (수직 방향)
        if x1 == x2 == x3 == x4:
            if not (y1 > y4 or y2 < y3):
                adj[i].append(j)
                adj[j].append(i)

# 시작점, 도착점 입력부
sx, sy, ex, ey = map(int, sys.stdin.readline().split())

# start : 시작점이 속하는 버스 번호 리스트
start = []

# end : 도착점이 속하는 버스 번호 리스트
end = []
for i in range(1, k + 1):
    if check[i]:
        continue
    x1, y1, x2, y2 = arr[i]
    if x1 <= sx <= x2 and y1 <= sy <= y2:
        start.append(i)
    if x1 <= ex <= x2 and y1 <= ey <= y2:
        end.append(i)

# BFS
q = collections.deque()
vis = [-1] * (k + 1)
for i in start:
    q.append(i)
    vis[i] = 0
while q:
    now = q.popleft()
    for next in adj[now]:
        if vis[next] == -1:
            vis[next] = vis[now] + 1
            q.append(next)
            
# 정답 출력
ans = 10**10
for i in end:
    ans = min(ans, vis[i])
print(ans + 1)