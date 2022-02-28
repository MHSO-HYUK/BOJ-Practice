# 5721 사탕 줍기 대회 
from sys import stdin 
import sys
sys.setrecursionlimit(10**5)
def candy(i):
    if dp[i][0] != -1 :
        return dp[i]

    elif i == n:
        return [0, 0]
    
    else:
        dp[i][1] = candy(i+1)[0] + grab(i) 
        dp[i][0] = max(candy(i+1)[1], candy(i+1)[0])
        return dp[i]
    

def grab(i):
    temp = [0 for _ in range(m)]
    
    if m >= 2:
        for j in range(m):
            temp[j] = max(temp[j], temp[j-2] + maps[i][j], temp[j-3] + maps[i][j] if m > 3 else 0)
        return max(temp)
    
    else:
        return maps[i][0]
    
while(1):
    n, m = map(int, stdin.readline().split())
    if n == 0 and m == 0:
        break
    maps = []
    for _ in range(n):
        maps.append(list(map(int, stdin.readline().split())))
   
    dp =[[-1, -1] for _ in range(n+1)]
    
    print(max(candy(0)))
