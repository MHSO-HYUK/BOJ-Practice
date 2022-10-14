from collections import deque
import heapq
parent = [i for i in range(101)]

def find_parent(now):
    if parent[now] == now: return now
    else:
        parent[now] = find_parent(parent[now])
        return parent[now]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def solution(n, costs):
    for i in range(len(costs)):
        costs[i] = [costs[i][2], costs[i][0], costs[i][1]]
    answer = 0
    heapq.heapify(costs)
    
    while(len(costs)):
        now = heapq.heappop(costs)
        cost, x, y = now[0], now[1], now[2]
        if find_parent(x) == find_parent(y): continue
        else:
            union_parent(x, y)
            answer += cost
    
    return answer