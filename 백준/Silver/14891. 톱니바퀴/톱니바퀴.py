# 14891 톱니바퀴
# 8개 톱니 4 일렬 -> N / S
# 특정 톱니를 회전 + 방향 결정
# A를 회전 시 - 
# B의 맞닿은 극이 다르면 B는 반대로 회전 
# B의 맞닿은 극이 같다면 B는 회전 X 
from sys import stdin
def move(top, d):
    if d == 1:
        top = [top[-1]] + top[0:7]
        return top
    
    else:
        top = top[1:8] + [top[0]]
        return top

topp, seq = [0], []
for _ in range(4):
    topp.append(list(map(int, stdin.readline().rstrip())))
# 맞닿은 부분 
# 1 -> 2 // 2-> -2 // 3 -> 2 // 4 -> -2
k = int(stdin.readline())
for _ in range(k):
    seq.append(list(map(int, stdin.readline().split())))
seq.reverse()
con = [0, 0, 0, 0] # 1-2 2-3 3-4 접합 상태 
score = 0
while(seq):
    n, dirt = seq.pop()
    for i in range(1, 4): # 접합상태 저장
        if topp[i][2] == topp[i+1][-2]: con[i] = -1 # 같은 극이면 -> 1
        else: con[i] = 1 # 다른 극이면 -> -1
    
    if dirt == 1: # 시계방향
        topp[n] = move(topp[n], 1) # 회전시킴
        k = -1
        for i in range(n-1, 0, -1):
            if con[i] == 1:
                topp[i] = move(topp[i], k)
                k = -k
            else:
                break
        k = -1
        for i in range(n, 4):
            if con[i] == 1:
                topp[i+1] = move(topp[i+1], k)
                k = -k
            else:
                break

    else: # 반시계방향
        topp[n] = move(topp[n], -1)
        k = 1
        for i in range(n-1, 0, -1):
            if con[i] == 1:
                topp[i] = move(topp[i], k)
                k = -k
            else:
                break
                
        k = 1
        for i in range(n, 4):
            if con[i] == 1:
                topp[i+1] = move(topp[i+1], k)
                k = -k
            else:
                break
    
for i in range(1, 5):
    if topp[i][0]:
        score += 2**(i-1)        
print(score)