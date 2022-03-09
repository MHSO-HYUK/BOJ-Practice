# 17825 주사위 윷놀이
from sys import stdin
def yut(i, a, b, c, d, s):
    global maxima
    ta, tb, tc, td = a, b, c, d
    if i == len(dice):
        maxima = max(maxima, s)
        return
    else:
        if maps[a] != -1: # 도착 상태가 아니면
            k = dice[i] # 주사위 숫자
            k -= 1
            ta = maps[ta][-1] # 한칸 이동
            while(k):
                if maps[ta] == -1:
                    yut(i + 1, ta, b, c, d, s)
                    break
                ta = maps[ta][0]
                k -= 1
            if ta != b and ta != c and ta != d:
                yut(i+1, ta, b, c, d, s+score[ta])

        if maps[b] != -1:
            k = dice[i]  # 주사위 숫자
            k -= 1
            tb = maps[tb][-1]
            while(k):
                if maps[tb] == -1:
                    yut(i + 1, a, tb, c, d, s)
                    break
                tb = maps[tb][0]
                k -= 1
            if tb != a and tb != c and tb != d:
                yut(i + 1, a, tb, c, d, s + score[tb])
        if maps[c] != -1:
            k = dice[i]  # 주사위 숫자
            k -= 1
            tc = maps[tc][-1]
            while(k):
                if maps[tc] == -1:
                    yut(i + 1, a, b, tc, d, s)
                    break
                tc = maps[tc][0]
                k -= 1
            if tc != a and tc != b and tc != d:
                yut(i + 1, a, b, tc, d, s + score[tc])
        if maps[d] != -1:
            k = dice[i]  # 주사위 숫자
            k -= 1
            td = maps[td][-1]
            while(k):
                if maps[td] == -1:
                    yut(i + 1, a, b, c, td, s)
                    break
                td = maps[td][0]
                k -= 1
            if td != a and td != b and td != c:
                yut(i + 1, a, b, c, td, s + score[td])

# 10 // 5    20 // 10    30 // 15    25 // 29
dice = list(map(int, stdin.readline().split()))
score = [i for i in range(0, 42, 2)] + [13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35, 0]
maps = [[1],[2],[3],[4], [5],[6, 21],[7],[8],[9],[10], [11, 24],[12], [13], [14], [15], [16, 26],[17], [18], [19], [20], [32], [22], [23], [29], [25], [29], [27], [28], [29], [30], [31], [20], -1]
maxima = 0
yut(0, 0, 0, 0, 0, 0)
print(maxima)