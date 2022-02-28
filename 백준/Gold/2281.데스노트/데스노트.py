# 2281 데스노트
from sys import stdin
def death(i, temp, col):
    if dp[i][temp] != -1:
        return dp[i][temp]
    elif i == n-1:
        return 0      
    elif i < n-1:
        if temp - nums[i+1] >= 0: # 남은 칸에 충분히 이름을 쓸 수 있을 경우
            dp[i][temp] = min(death(i+1, temp-nums[i+1]-1, col), death(i+1, m-nums[i+1]-1, col+1)+ (temp+1)**2) # 그 줄에 또 씀
    
        else: # 남은 칸에 이름을 못쓰는 경우
            dp[i][temp] = death(i+1, m-nums[i+1]-1, col+1) + (temp+1)**2
        
        return dp[i][temp]
    
n, m = map(int, stdin.readline().split())
nums =list(int(stdin.readline()) for _ in range(n))
dp = [[-1 for _ in range(m)]for _ in range(n)]

print(death(0, m-nums[0]-1, 0))