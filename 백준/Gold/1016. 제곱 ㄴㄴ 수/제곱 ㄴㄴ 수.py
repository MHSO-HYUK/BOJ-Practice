from sys import stdin

a, b= map(int, stdin.readline().split())
ans = b-a+1
visit = [0 for _ in range(b-a+1)]
i = 2
while i**2 <= b:
    s = i**2
    r = 0 if a % s == 0 else 1
    j = a // s + r
    while s*j <= b:
        if not visit[s*j-a]:
            visit[s*j-a] = 1
            ans -= 1
        j+=1
    i+=1
print(ans)