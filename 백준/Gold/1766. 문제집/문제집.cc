#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>
using namespace std;
int n, m; 
int degree[32001];
vector<vector<int>> graph(32001);

int main() {
	/*
		1766 문제집
		- N개의 문제는 모두 풀어야 함
		- 먼저푸는 것이 좋은 문제가 있는 문제는 순서를 지켜야 한다.
		- 가능하면 쉬운문제 먼저 풀어야 한다. 
	*/
	cin >> n >> m;
	memset(degree, 0, sizeof(degree));
	for (int i = 0; i < m; i++) {
		int a, b; cin >> a >> b;
		degree[b] += 1;
		graph[a].push_back(b);
	}

	priority_queue <int> pq;
	for (int i = 1; i <= n; i++) {
		if (degree[i] == 0) pq.push(-i);
	}

	vector<int> answer;
	while (!pq.empty()) {
		int now = pq.top();
		now = -now;
		answer.push_back(now);
		pq.pop();
		for (int parent : graph[now]) {
			degree[parent] -= 1;
			if (degree[parent] == 0) pq.push(-parent);
		}
	}

	for (int i = 0; i < n; i++) cout << answer[i] << " ";

}