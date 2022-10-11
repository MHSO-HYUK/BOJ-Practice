def solution(s):
    cnt = 0
    zero = 0
    while(True):
        if s == '1': break  
        new_s = 0
        for now in s:
            if now == '1': 
                new_s += 1
            else:
                zero += 1
        
        s = bin(new_s)[2:]
        cnt += 1
        
    answer = [cnt, zero]
    
    return answer