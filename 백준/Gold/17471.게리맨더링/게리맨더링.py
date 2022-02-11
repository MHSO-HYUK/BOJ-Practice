#17471 게리맨더링
from sys import stdin
from itertools import combinations 
from collections import deque
def rest(a, b):
    for k in a:
        b.remove(k)
    return b

def connect(a, b):
    flag = 0
    if(len(a) == 1 and len(b) == 1):
        flag += 2
    elif(len(a) == 1 or len(b) == 1):
        flag += 1
        
    for t in [a, b]:
        if(len(t) != 1):
            visit = [0 for _ in range(n+1)]
            queue = deque()
            queue.append(t[0])
            visit[t[0]] = 1
            while(queue):
                now = queue.popleft()
                for v in graph[now]:
                    if v in t and not visit[v]:
                        visit[v] = 1
                        queue.append(v)
            if(sum(visit) == len(t)):
                flag += 1
    
    if(flag == 2):
        return True
    else:
        return False


def number(a, b):
    global total
    numa, numb = 0, 0
    for v in a:
        numa += people[v]
    numb = total - numa
    return abs(numb- numa)
    
n = int(stdin.readline())
people = list(map(int, stdin.readline().split()))
people.insert(0, 0)
total = sum(people)
graph = [[] for _ in range(n+1)]
for i in range(n):
    num, *con = map(int,stdin.readline().split())
    for j in range(num):
        graph[i+1].append(con[j])

minima = 10**10
for i in range(1, (n//2) +1):
    for k in combinations(range(1, n+1), i):
        temp = [j for j in range(1, n+1)]
        if(connect(k, rest(k, temp))):
            minima = min(minima, number(k, temp))
if(minima == 10**10):
    print(-1)
else:
    print(minima)