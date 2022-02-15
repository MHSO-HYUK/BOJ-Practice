# 1309 동물원 
# 사자는 0 ~ n마리 존재가능
n = int(input())
s = [[0] * 3 for i in range(n+1)]
for i in range(3):
    s[1][i] = 1
for i in range(2, n+1):
    s[i][0] = s[i - 1][1] + s[i - 1][2] % 9901
    s[i][1] = s[i - 1][0] + s[i - 1][2] % 9901
    s[i][2] = s[i - 1][0] + s[i - 1][1] + s[i - 1][2] % 9901
print(sum(s[n]) % 9901)