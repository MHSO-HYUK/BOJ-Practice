#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>
using namespace std;

int n, m, k;
char maps[1001][1001];
int visit[1001][1001][11];
int dx[4] = { 1, -1, 0, 0 };
int dy[4] = { 0, 0, 1, -1 };

int bfs() {
	queue<vector<int>> q;
	q.push({0, 0, 1, 0}); // 위치, 시간 , 벽부신 횟수
	for (int i = 0; i < n+1; i++) {
		for (int j = 0; j < m + 1; j++) {
			memset(&visit[i][j][0], 0, sizeof(visit[i][j]));
		}
	}

	visit[0][0][0] = 1;
	while (!q.empty()) {
		int x, y, time, wall;
		x = q.front()[0];
		y = q.front()[1];
		time = q.front()[2];
		wall = q.front()[3];
		q.pop();
		if (x == n - 1 && y == m - 1) return time;
		for (int d = 0; d < 4; d++) {
			int nx = x + dx[d];
			int ny = y + dy[d];
			if (0 <= nx && nx <= n - 1 && 0 <= ny && ny <= m - 1) {
				if (maps[nx][ny] =='1' && wall < k) {
					if (visit[nx][ny][wall + 1] == 0) {
						visit[nx][ny][wall + 1] = 1;
						q.push({ nx, ny, time + 1, wall + 1 });
					}
				}
				if (maps[nx][ny] == '0') {
					if (visit[nx][ny][wall] == 0) {
						visit[nx][ny][wall] = 1;
						q.push({ nx, ny, time + 1, wall });
					}
				}
			}
		}
	}
	return -1;
}


int main() {
	/*
		14442 벽 부수고 이동하기 2
		- K개 까지 벽을 부수고 이동할 수 있을 때 최단 경로
	*/
	cin >> n >> m >> k;
	
	for (int i = 0; i < n; i++) {
		string s;
		cin >> s;
		for (int j = 0; j < m; j++) {
			maps[i][j] = s[j];
		}
	}
	cout << bfs();
}