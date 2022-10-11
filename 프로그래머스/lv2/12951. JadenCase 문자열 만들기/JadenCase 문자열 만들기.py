def solution(s):
    answer = ''
    flag = 1
    for now in s:
        if now == ' ':
            answer += ' '
            flag = 1
            
        else:
            if flag:
                answer += now.upper()
                flag = 0
            else:
                answer += now.lower()
    
    return answer