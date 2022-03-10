# 1039 교환
from copy import deepcopy
def change(num, cnt):
    global maxima, s
    m = 0
    for i in range(len(num)):
        m += int(num[-1-i]) * 10**i 
        
    if cnt == k:
        maxima = max(maxima, m)
        return
    
    if len(num) >= 2:
        if num == target:
            if s:
                if num[0] != '0':
                    change(num, cnt+1)
            else:
                temp = deepcopy(num)
                temp[-1], temp[-2] = temp[-2], temp[-1]
                if temp[0] != '0':
                    change(temp, cnt+1)

        else:
            for i in range(len(num)):
                if num[i] == target[i]:
                    continue
                else:
                    for j in range(len(num)-1, i, -1):
                        if num[j] == target[i]:
                            temp = deepcopy(num)
                            temp[i], temp[j] = temp[j], temp[i]
                            if temp[0] != '0':
                                change(temp, cnt+1)
                    return
    

n, k = map(int, input().split())
maxima = -1
num = list(str(n))
target = sorted(num, reverse = True)
s = False
for i in range(len(target)-1):
    if target[i] == target[i+1]:
        s = True
        break
change(num, 0)
print(maxima)