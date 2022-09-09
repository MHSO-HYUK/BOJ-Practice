#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>
using namespace std;

vector<vector<vector<int>>> graph(801);
queue<int> q;
int INF = 987654321;
int visit[1001];
int n, e;

vector<long long> bfs(int s) {
	vector<long long> dist(1001);
	for (int i = 1; i < n + 1; i++) dist[i] = INF;
	memset(visit, 0, sizeof(visit));
	q.push(s);
	visit[s] = 1; dist[s] = 0;
	while (!q.empty()) {
		int now = q.front();
		visit[now] = 1;
		q.pop();
		for (vector<int> v : graph[now]) {
			int nxt = v[0];
			long long cost = v[1];
			dist[nxt] = min(dist[nxt], dist[now] + cost);
		}
		long long minima = INF-1;
		int idx;
		for (int i = 1; i < n + 1; i++) {
			if (visit[i] == 0) {
				minima = min(minima, dist[i]);
				if (minima == dist[i]) {
					idx = i;
				}
			}
		}
		if (minima != INF -1)	 q.push(idx);
	}
	return dist;
}

int main() {
	/*
		1504 특정한 최단 경로
		무방향 그래프 - 1 -> n으로 최단 거리 이동
		+ 임의로 주어진 두 정점은 반드시 통과
		1 -> a -> b - > n
		1 -> b -> a -> n
	*/
	cin >> n >> e;
	for (int i = 0; i < e; i++) {
		int a, b, c; cin >> a >> b >> c;
		graph[a].push_back({ b, c });
		graph[b].push_back({ a, c });
	}
	int a, b; cin >>a >> b;

	vector <long long> dist1 = bfs(1); // 1에서부터 시작하는 거리
	vector <long long> dista = bfs(a); // a에서부터 시작하는 거리
	vector <long long> distb = bfs(b); // b에서부터 시작하는 거리

	long long routeA, routeB;
	if (dist1[a] >= INF || dista[b] >= INF || distb[n] >= INF) routeA = INF;
	else  routeA = dist1[a] + dista[b] + distb[n];
	
	if (dist1[b] >= INF || distb[a] >= INF || dista[n] >= INF) routeB = INF;
	else  routeB = dist1[b] + distb[a] + dista[n];
	
	long long answer = min(routeA, routeB);
	
	if (answer >= INF) cout << -1;
	else cout << answer;
}