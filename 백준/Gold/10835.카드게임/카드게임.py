#10835 카드게임
#언제든지 왼쪽 카드만 혹은 둘다 버릴 수 있음 (점수 X)
#오른 카드가 더 작으면 오른 카드만 버릴 수 있음 (오른 카드 점수 획득)
#둘 중 한쪽의 카드가 없다면 게임 끝
from sys import stdin 
n = int(stdin.readline())  
lf =list(map(int, stdin.readline().split()))
rf =list(map(int, stdin.readline().split()))
dp = [[0 for _ in range(n + 1)] for _ in range(n+1)]

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if rf[j] < lf[i]:
            dp[i][j] = max(dp[i][j+1] + rf[j], dp[i+1][j], dp[i+1][j+1])
        else:
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])

           
print(dp[0][0])