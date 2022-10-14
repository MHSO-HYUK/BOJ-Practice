def solution(gems):
    total = len(set(gems))
    dic = dict()
    min_len = 1e9
    s, f, now = 0, 0, 0
    for idx, gem in enumerate(gems):
        while(len(dic) != total and now < len(gems)):
            if gems[now] in dic: dic[gems[now]] += 1
            else: dic[gems[now]] = 1
            now += 1
            
        if now - idx < min_len and len(dic) == total:
            min_len = now-idx
            s, f = idx, now
            
        dic[gems[idx]] -= 1
        if dic[gems[idx]] == 0: del(dic[gems[idx]])

    answer = [s+1, f]
    return answer