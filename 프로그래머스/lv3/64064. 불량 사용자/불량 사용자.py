ban = []
user = []
limit = 0
visit, cache = [], []
def dfs(idx, log):    
    if idx >= limit:
        return 1
    ret = 0
    for i in range(len(user)):
        if not visit[i] and len(ban[idx]) == len(user[i]): # 길이가 같고 아직 추가 안댐
            flag = True
            for j in range(len(user[i])):
                if ban[idx][j] == '*': 
                    continue
                else:
                    if ban[idx][j] != user[i][j]:
                        flag = False
                        break
            if flag:
                now = log + [i]
                now.sort()
                if not now in cache:
                    cache.append(now)
                    visit[i] = 1
                    ret += dfs(idx+1, now)
                    visit[i] = 0
    return ret
                
def solution(user_id, banned_id):
    global limit, ban, user, visit, cache
    ban = banned_id
    user = user_id
    limit = len(ban)
    visit = [0 for _ in range(len(user))]
    cache = []
    
    answer = dfs(0, []) #idx, log
    
    return answer