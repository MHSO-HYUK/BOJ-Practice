#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>
using namespace std;

priority_queue<pair<int, vector<int>>> pq;
int parent[10001];

int solution(int v, int e) {
	/*
		1197 최소 스패님 트리
		- 주어진 그래프의 모든 정점을 연결하는 부분 그래프 중 그 가중치의 합이 최소
		-> 사이클이 생기면 스패닝 트리 X
	*/

	int INF = 987654321;

	for (int i = 0; i < v + 1; i++) {
		parent[i] = i;
	}

	int answer = 0;

	while (!pq.empty()) {
		auto info = pq.top();
		pq.pop();
		int a, b, cost; 
		cost = -info.first; 
		a = info.second[0];
		b = info.second[1];

		if (parent[a] == parent[b]) continue;
		else if (parent[a] > parent[b]) {
			for (int i = 1; i < v + 1; i++) {
				if (parent[i] == parent[a] && i != a) {
					parent[i] = parent[b];
				}
			}
			parent[a] = parent[b];
		}
		else {
			for (int i = 1; i < v + 1; i++) {
				if (parent[i] == parent[b] && i != b) {
					parent[i] = parent[a];
				}
			}
			parent[b] = parent[a];
		}
		answer += cost;
	}
	return answer;
}

int main() {
	int v, e; cin >> v >> e;
	for (int i = 0; i < e; i++) {
		int a, b, c; cin >> a >> b >> c;
		vector<int> v = { a, b };
		pq.push({ -c, v });
	}
	cout << solution(v, e);
}