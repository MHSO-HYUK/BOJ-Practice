# 16288 Passport Control
from sys import stdin
import sys

n, k =map(int, stdin.readline().split())
seq = list(map(int, stdin.readline().split()))
count = [[] for _ in range(k)]

for i in range(1, n+1):
    for j in range(n):
        if seq[j] == i:
            flag = False
            for z in range(k):
                if count[z] and seq.index(count[z][-1]) < j:
                    flag= True
                    count[z].append(i)
                    break
                    
            if not flag:
                for z in range(k):
                    if not count[z]:
                        flag = True
                        count[z].append(i)
                        break
                        
            if not flag:
                print('NO')
                sys.exit()

print('YES')