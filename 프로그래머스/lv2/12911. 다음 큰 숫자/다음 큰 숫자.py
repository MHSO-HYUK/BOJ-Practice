def solution(n):
    answer = 0
    
    cnt = 0
    bin_n = bin(n)
    for now in bin_n:
        if now == '1': cnt += 1
    
    while(True):
        n += 1
        bin_new, cnt_new = bin(n), 0
        for now in bin_new:
            if now == '1' : cnt_new += 1
    
        if cnt != cnt_new: continue        
        break
    

    return n