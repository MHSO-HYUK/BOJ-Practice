#2437
import heapq
n = int(input())
kg = list(map(int,input().split()))
kg.sort()

res = 0

for i in range(n):
    if res + 1 >= kg[i]:
        res += kg[i]
    else:
        break
print(res + 1)