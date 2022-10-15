def solution(n, results):
    global visit
    answer = 0
    graph = [[[0, 0] for _ in range(n)] for _ in range(n)]
    for a, b in results:
        graph[a-1][b-1][0] = 1
        graph[b-1][a-1][1] = 1 # 관계성 성립
        
    for i in range(n):
         for j in range(n):
                for k in range(n):
                    if i != j and j != k and k != i:
                        graph[j][k][0] = (graph[j][i][0] and graph[i][k][0]) or graph[j][k][0]
                        graph[j][k][1] = (graph[j][i][1] and graph[i][k][1]) or graph[j][k][1]
    
    for i in range(n):
        temp = 0
        for j in range(n):
            temp += sum(graph[i][j])
        if temp == n-1: answer += 1
    return answer