def solution(s):
    answer = ''
    maxima, minima = -1e9, 1e9
    flag = 0
    
    num = 0
    for temp in s:
        if temp == ' ': 
            maxima = max(maxima, num)
            minima = min(minima, num)
            num = 0
            flag = 0
            continue
        else:
            if temp == '-' : 
                flag = 1
            else:
                if flag: num = 10* num - int(temp)
                else: num = 10*num + int(temp)
            
    maxima = max(maxima, num)
    minima = min(minima, num)
    
    answer += str(minima)
    answer += ' '
    answer += str(maxima)
    
    return answer