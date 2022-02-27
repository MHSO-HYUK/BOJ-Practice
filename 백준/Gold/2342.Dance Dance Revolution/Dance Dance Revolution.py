import sys
sys.setrecursionlimit(10**6)
def move(a, b):
    if a == b:
        return 1
    elif a == 0:
        return 2
    
    elif abs(b-a)%2 == 0:
        return 4
    
    else:
        return 3
    
def solve(n, l, r):
    global dp
    if n >= len(arr)-1:
        return 0
 
    if dp[n][l][r] != -1:
        return dp[n][l][r]
 
    dp[n][l][r] = min(solve(n+1, arr[n],r) + move(l, arr[n]), solve(n+1, l, arr[n]) + move(r, arr[n]))
    return dp[n][l][r]
 
arr = list(map(int, sys.stdin.readline().split()))
dp = [[[-1]*5 for _ in range(5)] for _ in range(len(arr) + 1)]
 
print(solve(0, 0, 0))