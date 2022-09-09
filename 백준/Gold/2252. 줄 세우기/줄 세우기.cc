#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>
using namespace std;

vector<vector<int>> graph(32001);
int degree[32001];
vector<int> answer;

void solution(int n, int m) {
	/*
		일부 학생들의 키를 비교해서 줄을 세우는 프로그램
	*/
	queue <int> q;
	int visit[32001];
	memset(visit, 0, sizeof(visit));

	for (int i = 1; i < n + 1; i++) {
		if (degree[i] == 0) { // 아무 노드랑도 연결 되지 않음 or 자식 노드가 없음(나보다 큰 놈 없음) 
			answer.push_back(i); // 답에 바로 연결
			visit[i] = 1; // 방문해버림
			q.push(i);
		}
	}
	while (!q.empty()) {
		int now = q.front();
		q.pop();
		for (int next : graph[now]) { // 보다 작은 노드 탐색
			if (visit[next] == 0) {
				degree[next] -= 1;
				if (degree[next] == 0) {
					visit[next] = 1;
					answer.push_back(next);
					q.push(next);
				}
			}
		}
	}
}

int main() {
	memset(degree, 0, sizeof(degree));

	int n, m; cin >> n >> m;

	for (int i = 0; i < m; i++) {
		int a, b; cin >> a >> b;
		degree[b] += 1; // 가장 키가 큰 노드를 감별할 수 있음.
		graph[a].push_back(b); // 보다 작은 노드를 저장
	}
	solution(n, m);

	for (int i = 0; i < answer.size(); i++) {
		cout << answer[i] << " ";
	}
}