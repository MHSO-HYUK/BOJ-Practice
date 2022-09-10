#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>
using namespace std;
int parent[51];
int degree[51];
int n;
vector<vector<int>> graph(51);

int bfs(int node) {
	queue <int> q;
	degree[parent[node]] -= 1;
	q.push(node);
	while (!q.empty()) {
		int now = q.front();
		degree[now] = -1;
		q.pop();
		for (int child : graph[now]) {
			q.push(child);
		}
	}
	int answer = 0;
	for (int i = 0; i < n; i++) {
		if (degree[i] == 0) answer += 1;
	}
	return answer;
}
int main() {
	/*
		1068 트리
		- 트리에서 노드를 지웠을 때 남는 리프 노드의 수
		(리프 노드 = 자식 노드가 없는 노드)
	*/
	cin >> n;
	memset(degree, 0, sizeof(degree));
	for (int i = 0; i < n; i++) {
		int p; cin >> p; 
		parent[i] = p;
		if (p != -1) {
			degree[p] += 1;
			graph[p].push_back(i);
		}
	}
	int node; cin >> node;
	cout << bfs(node);
}