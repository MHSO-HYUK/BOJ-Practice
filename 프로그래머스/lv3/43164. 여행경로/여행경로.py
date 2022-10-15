import sys
sys.setrecursionlimit(10**8)
limit = 0
answer = 0
info, visit = dict(), dict()
flag = False

def dfs(now, cnt, cache):
    global limit, answer, flag, visit, info
    if not flag:
        if cnt == limit:
            answer = cache
            flag = True
            return 0
        else:
            if now in info:
                for nxt in range(len(visit[now])):
                    if visit[now][nxt] == 0 and not flag:
                        visit[now][nxt] = 1
                        dfs(info[now][nxt], cnt+1, cache+[info[now][nxt]])
                        visit[now][nxt] = 0
    return 0

def solution(tickets):
    global limit, answer
    limit = len(tickets) + 1
    
    for a, b in tickets:
        if a in info:
            info[a].append(b)
            visit[a].append(0)
        else:
            info[a] = [b]
            visit[a] = [0]
    
    for now in info:
        info[now].sort()
    
    dfs('ICN', 1, ['ICN'])
    
    return answer