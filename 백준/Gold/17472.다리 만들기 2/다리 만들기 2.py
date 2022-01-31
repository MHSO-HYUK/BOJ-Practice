#17472 다리만들기2
#다리 방향은 일직선 + 길이 2 이상 + 연결 방향이 똑같아야
from collections import deque
from sys import stdin

def island(i, j): #섬의 갯수를 찾는 함수
    queue = deque([[i,j]])
    land = []
    visit[i][j] = 1
    while(queue):
        x, y= queue.popleft()
        for k in range(4):
            a, b = x + dx[k], y + dy[k]
            if(a<0 or b<0 or a>n-1 or b>m-1):
                continue
            if(visit[a][b] == 0 and maps[a][b] == 1):
                visit[a][b] = 1
                queue.append([a, b])
            if(maps[a][b] == 0): #해안가에 붙어있는 땅(다리가 나갈 수 있는)
                if(not [x, y] in land):
                    land.append([x, y])
    return land

def bridge(a, b): #a섬, b섬 사이 최소 다리 길이 값을 찾는 함수 
    length = []
    for i, j in lands[a]:
        for p, q in lands[b]:
            if(i==p and abs(j-q) > 2):
                flag2 = True
                if(j>q):
                    if(1 in maps[i][q+1:j]):
                        flag2 = False
                        continue
                else:
                    if(1 in maps[i][j+1:q]):
                        flag2 = False
                        continue
                if(flag2):
                    length.append(abs(j-q)-1)    
            if(j==q and abs(i-p) > 2):
                flag = True
                if(i>p):
                    for k in range(p+1, i):
                        if(maps[k][j] == 1):
                            flag = False
                            break
                    if(not flag):
                        continue
                else:
                    for k in range(i+1, p):
                        if(maps[k][j] == 1):
                            flag = False
                            break
                    if(not flag):
                        continue
                if(flag):         
                    length.append(abs(i-p)-1)   
                    
    if(len(length)):
        return min(length)
    else:
        return False
    
def cycle(): # 그래프 내에 사이클이 있는지 찾는 함수
    queue = deque()
    flag = False
    visit = [[0 for _ in range(num)] for _ in range(num)]
    for i in range(len(temp)):
        queue.append(temp[i][1])
    while(queue):
        k = queue.popleft()
        for t in graph[k]:
            if(visit[t][k] == 0 and visit[k][t] == 0):
                if(parent[t] == parent[k]):
                    flag = True
                    return False # 사이클 발생
                    break
                if(parent[t] > parent[k]):
                    visit[t][k], visit[k][t] = 1, 1
                    for c in range(len(parent)):
                        if(parent[c] == parent[t] and c != t):
                            parent[c] = parent[k]
                    parent[t] = parent[k]
                    queue.append(t)
                if(parent[t] < parent[k]):
                    visit[t][k], visit[k][t] = 1, 1
                    for c in range(len(parent)):
                        if(parent[c] == parent[k] and c != k):
                            parent[c] = parent[t]
                    parent[k] = parent[t]
                    queue.append(t)
    if(not flag):
        return True #사이클 없이 종료


n,m=map(int, stdin.readline().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, stdin.readline().split())))
    
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
num, lands =0, []
visit = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if(visit[i][j] == 0 and maps[i][j] == 1):
            lands.append(island(i, j))
            num += 1
del visit

temp = []
for i in range(num):
    for j in range(i+1, num):
        k = bridge(i, j)
        if(k):
            temp.append([k, i, j])  
temp.sort()

ans = []
graph = [[] for _ in range(num)]
for v in temp:
    a, b, c = v[0], v[1], v[2]
    graph[c].append(b)
    graph[b].append(c)
    parent = [i for i in range(num)]
    if(cycle()):
        ans.append(a)
        if(len(ans) == num -1):
            break
    else:
        graph[c].remove(b)
        graph[b].remove(c)

if(len(ans) == num-1):
    print(sum(ans))
else:
    print(-1)