#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>
using namespace std;

int dx[4] = { 1, -1, 0, 0 };
int dy[4] = { 0, 0, 1, -1 };
int visit[105][105];

int main() {
	/*
		1261 알고스팟
		- 운영진이 n-1, m-1로 이동할 때 벽을 최소로 부시려면?
	*/
	int m, n; cin >> m >> n;
	int INF = 987654321;
	vector<string> maps;
	for (int i = 0; i < n; i++) {
		string s; cin >> s;
		maps.push_back(s);
	}

	for (int i = 0; i < n +3; i++) {
		fill_n(&visit[i][0], m+3, INF);
	}

	queue <vector<int>> q;
	q.push({ 0, 0, 0 }); // x, y, 부신 벽의 갯수
	visit[0][0] = 0;
	int minima = INF;

	while (!q.empty()) {
		int x = q.front()[0];
		int y = q.front()[1];
		int wall = q.front()[2];
		q.pop();
		if (wall >= minima || visit[x][y] < wall) continue;

		if (x == n - 1 && y == m - 1) {
			minima = min(minima, wall);
			continue;
		}

		for (int k = 0; k < 4; k++) {
			int nx = x + dx[k];
			int ny = y + dy[k];
			if (0 <= nx && nx <= n - 1 && 0 <= ny && ny <= m - 1) {
				if (maps[nx][ny] == '0' && visit[nx][ny] > wall) {
					visit[nx][ny] = wall;
					q.push({ nx, ny, wall});
				}
				if (maps[nx][ny] == '1' && visit[nx][ny] >  wall + 1){
					visit[nx][ny] = wall + 1;
					q.push({ nx, ny, wall + 1});
				}
			}
		}
	}
	cout << minima;
}