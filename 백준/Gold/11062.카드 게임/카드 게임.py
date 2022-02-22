#11062 카드게임
from sys import stdin
from itertools import product
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    card = list(map(int, stdin.readline().split()))
    dp = [[0]*n for _ in range(n)]
    turn = True if n%2 else False
    for d in range(n):
        for i in range(n-d):
            j = i + d
            if d == 0:
                dp[i][j] = card[i] if turn else 0
            elif turn:
                dp[i][j] = max(dp[i+1][j] + card[i], dp[i][j-1] + card[j])
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j-1])
        turn = not turn
    print(dp[0][n-1])