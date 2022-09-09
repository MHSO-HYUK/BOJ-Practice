#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>
using namespace std;

vector<vector<pair<int, int>>> graph(1001);
int n, m;

int solution(int s, int f) {
	/*
	1916 최소비용
	- A에서 B로 가는 버스 비용을 최소화 하고자 한다. 
	*/
	queue <int> q;
	int INF = 987654321;

	int dist[1001];
	fill_n(dist, 1001, INF);
	int visit[1001];
	memset(visit, 0, sizeof(visit));
	dist[s] = 0; visit[s] = 1;
	q.push(s);
	
	while (!q.empty()) {
		int now = q.front();
		visit[now] = 1;
		q.pop();
		for (pair<int, int> p : graph[now]) {
			int node = p.first;
			int cost = p.second;
			dist[node] = min(dist[node], dist[now] + cost); // 거리 최신화
		}

		int minima = INF;
		int idx;
		for (int i = 1; i < n + 1; i++) {
			if (visit[i] == 0) {
				minima = min(dist[i], minima);
				if (minima == dist[i]) idx = i;
			}
		}
		if (minima != INF) {
			q.push(idx);
		}
	}
	return dist[f];
}

int main() {
	cin >> n >> m;

	for (int i = 0; i < m; i++) {
		int a, b, cost; cin >> a >> b >> cost;
		graph[a].push_back({ b, cost });
	}
	int s, f; cin >> s >> f;
	cout << solution(s, f);
}