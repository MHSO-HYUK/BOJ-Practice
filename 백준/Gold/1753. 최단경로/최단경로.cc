#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>
using namespace std;

int v, e;
int k;
vector<vector<pair<int, int>>> graph(20001);
priority_queue <pair<int, int>> pq;
int dist[20001];
int INF = 987654321;

void dijkstra(int now) {
	fill_n(dist, v+1, INF);
	dist[now] = 0;

	pq.push({ 0, now });
	while (!pq.empty()) {
		int cost = -pq.top().first;
		int now = pq.top().second;
		pq.pop();

		for (pair<int, int> next : graph[now]) {
			int node = next.first;
			int w = next.second;
			dist[node] = min(dist[node], cost + w);
			if (dist[node] == cost + w) {
				pq.push({ -dist[node], node });
			}
		}
	}
}


int main() {
	/*
		1753 최단경로
		- 
	*/
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> v >> e >> k;
	for (int i = 0; i < e; i++) {
		int a, b, c;
		cin >> a >> b >> c; // 경로 a - b  - 가중치 c
		graph[a].push_back({ b, c });
	}
	dijkstra(k);
	for (int i = 1; i < v + 1; i++) {
		if (dist[i] == INF) cout << "INF" << endl;
		else	cout << dist[i] << endl;
	}
}