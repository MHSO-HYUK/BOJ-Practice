# 14238 출근기록
# A 매일 B 출근 시 하루 쉼 C 출근후 이틀 쉼 
from sys import stdin 
import sys
def commute(a, b, c, p1, p2):
    global A, B, C
    if a < 0 or b < 0 or c < 0:
        return False
    
    if a == 0 and b == 0 and c == 0:
        return True
    
    if dp[a][b][c][p1][p2]:
        return False
    dp[a][b][c][p1][p2] = True
    
    ans[n-a-b-c] = 'A'
    if commute(a-1, b, c, 0, p1):
        return True
    
    if p1 != 1:
        ans[n-a-b-c] = 'B'
        if commute(a, b-1, c, 1, p1):
            return True
        
    if p1 != 2 and p2 != 2:
        ans[n-a-b-c] = 'C'
        if commute(a, b, c-1, 2, p1):
            return True
    return False

p = list(stdin.readline().rstrip())
n = len(p)
dp = [[[[[0 for _ in range(3)] for _ in range(3)] for _ in range(51)] for _ in range(51)] for _ in range(51)]
ans = [0] * 50      

A, B, C = 0, 0, 0
for i in range(len(p)):
    if p[i] == 'A':
        A += 1
    if p[i] == 'B':
        B += 1
    if p[i] == 'C':
        C += 1

if commute(A, B, C, 0, 0):
    print(''.join(ans[:n]))
else:
    print(-1)