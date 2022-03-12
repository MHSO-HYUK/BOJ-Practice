# 17281 야구
from sys import stdin
from itertools import permutations 
import sys
# 안타 // 타자 + 모든 주자 1루 진루 
# 2루타 // 타자 + 모든 주자 2루 진루 
# 3루타 // 타자 + 모든 주자 3루 진루 
# 홈런 // 타자 + 모든 주자 홈인 
# 아웃 // 주자 가만히 + 아웃 추가
# 1번 선수를 4번 타자로 미리 결정함 -> 각 선수가 각 이닝에서 어떤 결과를 얻는지 알고 있음
# 이때 가장 많은 득점을 하는 경우를 출력한다, 
def baseball(rnd, s, score):
    global temp, maxima
    if rnd == n:
        maxima = max(maxima, score)
        return
    if maxima == 24*n:
        print(maxima)
        sys.exit()
    out, sc, b0, b1, b2 = 0, 0, 0, 0, 0
    while(1):
        s = s % 9
        if hit[rnd][temp[s]] == 0:
            out += 1
            s += 1
            if out == 3:
                break
                
        elif hit[rnd][temp[s]] == 1:
            sc += b2
            s += 1
            b0, b1, b2 = 1, b0, b1  

        elif hit[rnd][temp[s]] == 2:
            sc += b1 + b2
            s += 1
            b0, b1, b2 = 0, 1, b0

        elif hit[rnd][temp[s]] == 3:
            sc += b0 + b1 + b2
            s += 1
            b0, b1, b2 = 0, 0, 1
        elif hit[rnd][temp[s]] == 4:
            sc += b0 + b1 + b2 + 1
            s += 1
            b0, b1, b2 = 0, 0, 0
              
    baseball(rnd+1, s, score+sc)

n = int(stdin.readline())
hit = list(list(map(int, stdin.readline().split())) for _ in range(n))

maxima = 0
for seq in permutations(range(1, 9), 8):
    temp = list(seq[:3]) + [0] + list(seq[3:])
    baseball(0, 0, 0)

print(maxima)