# 16637 괄호 추가하기 
# 연산자는 +, - * 중 하나
# 괄호 안에는 연산자가 하나만 들어있어야 한다. + 중첩된 괄호를 사용할 수 없다.
# 연산자 우선순위는 모두 동일하기 때문에 괄호 제외 왼쪽에서부터 계산해야 한다. 
from sys import stdin
from itertools import combinations
from copy import deepcopy
n = int(stdin.readline())
sik = list(stdin.readline().rstrip())
for i in range(n):
    if '1' <= sik[i] <= '9' or sik[i] == '0':
        sik[i] = int(sik[i])
        
maxima = -2**31-1

for i in range(0, n):
    for seq in combinations(range(1, n, 2), i):
        flag = False
        for k in range(len(seq)-1):
            if abs(seq[k] - seq[k+1]) == 2:
                flag = True
                break
        if flag:
            continue
            
        gal = [0 for _ in range(n)]
        for k in seq:
            gal[k-1], gal[k], gal[k+1] = 1, 1, 1 # 괄호가 있는 항 체크
            
        cache = []
        for i in range(n): # 괄호 있는 항은 먼저 계산할 수 있도록
            if gal[i] and type(sik[i]) != int:
                if sik[i] == '*':
                    cache.append(sik[i-1] * sik[i+1])
                if sik[i] == '-':
                    cache.append(sik[i-1] - sik[i+1])
                if sik[i] == '+':
                    cache.append(sik[i-1] + sik[i+1])
            if not gal[i]:
                cache.append(sik[i])
        
        ans = cache[0]
        for i in range(1, len(cache)):
            if type(cache[i]) == int:
                if cache[i-1] == '-':
                    ans -= cache[i]
                if cache[i-1] == '+':
                    ans += cache[i]
                if cache[i-1] == '*':
                    ans *= cache[i]
        maxima = max(maxima, ans)
        
print(maxima)