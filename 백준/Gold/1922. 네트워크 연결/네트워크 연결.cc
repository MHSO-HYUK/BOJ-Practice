#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>
using namespace std;

int main() {
	/*
	1922 네트워크 연결
	컴퓨터 연결 비용을 최소로 + 모든 컴퓨터 연결
	*/
	int n, m; cin >> n >> m;
	priority_queue<pair<int, vector<int>>> pq;
	for (int i = 0; i < m; i++) {
		int a, b, c; cin >> a >> b >> c;
		pq.push({ -c, {a, b} });
	}
	int parent[1001];
	for (int i = 0; i < n + 1; i++) {
		parent[i] = i;
	}
	int answer = 0;
	while (!pq.empty()) {
		auto now = pq.top();
		int cost = -now.first;
		int x, y; x = now.second[0]; y = now.second[1];
		pq.pop();
		if (parent[x] == parent[y]) continue;
		else {
			answer += cost;
			if (parent[x] > parent[y]) {
				for (int i = 1; i < n + 1; i++) {
					if (parent[i] == parent[x] && i != x) parent[i] = parent[y];
				}
				parent[x] = parent[y];
			}
			else {
				for (int i = 1; i < n + 1; i++) {
					if (parent[i] == parent[y] && i != y) parent[i] = parent[x];
				}
				parent[y] = parent[x];
			}
		}
	}
	cout << answer;
}