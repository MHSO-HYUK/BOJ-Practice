#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>
using namespace std;
long long n, m;
long long INF = 987654321;
long long dist[501];
vector<vector<long long>> graph(6001);

void belman(long long start) {
	dist[start] = 0;
	for (long long i = 0; i < n; i++) {
		for (long long j = 0; j < m; j++) {
			long long a = graph[j][0];
			long long b = graph[j][1];
			long long cost = graph[j][2];
			if (dist[a] != INF && dist[b] > dist[a] + cost) {
				dist[b] = dist[a] + cost;
				if (i == n - 1) {
					cout << -1;
					exit(0);
				}
			}
		}
	}
}

int main() {
	/*
		11657 타임머신
		- C = 0 이면 순간이동
		- C < 0이면 타임머신으로 되돌아가는 경우
		- C : 버스를 타고 이동하는데 걸리는 시간 
		-> 전형적인 벨만포드 
	*/
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n >> m;
	for (long long i = 0; i < m; i++) {
		long long a, b, c; cin >> a >> b >> c;
		graph[i] = { a, b, c };
	}

	fill_n(dist, n+1, INF);
	belman(1);
	for (long long i = 2; i < n+1; i++) {
		if (dist[i] >= INF) cout << -1 <<endl;
		else cout << dist[i] << endl;
	}
}