#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>
using namespace std;

int dir[5] = { -1, 1, 3, 2, 0};
int dx[4] = {-1, 0, 1, 0}; // 상 우 하 좌 (북 동 남 서)
int dy[4] = {0, 1, 0, -1};
int maps[101][101];
int visit[101][101][5];
int m, n;

int main() {
	/*
		1726 로봇
		- 1. 현재 향하고 있는 방향으로 1, 2, 3 칸 이동 가능
		- 2. 현재 향하고 있는 방향에서 좌 / 우 측으로 회전 가능 
		1은 못가요~ 
	*/
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			int val;  cin >> val;
			maps[i][j] = val;
			memset(&visit[i][j][0], 0, sizeof(visit[i][j]));
		}
	}
	vector<int> loc[2];
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 3; j++) {
			int val;  cin >> val;
			if (j == 2) loc[i].push_back(dir[val]);
			else loc[i].push_back(val-1);
		}
	}

	queue<vector<int>> q;
	q.push(loc[0]);
	while (!q.empty()) {
		int x = q.front()[0]; 
		int y = q.front()[1];
		int d = q.front()[2]; // 방향
		q.pop();
		if (x == loc[1][0] && y == loc[1][1] && d == loc[1][2]) { // 탈출조건
			cout << visit[x][y][d];
			break;
		}

		//1. 회전
		int right = (d + 1)%4;
		int left;
		if (d == 0) left = 3;
		else left = d - 1;

		if (visit[x][y][right] == 0) {
			visit[x][y][right] = visit[x][y][d] + 1;
			q.push({ x, y, right });
		}
		if (visit[x][y][left] == 0) {
			visit[x][y][left] = visit[x][y][d] + 1;
			q.push({ x, y, left });
		}

		// 2. 직진
		for (int i = 1; i <= 3; i++) {
			int nx = x + i*dx[d];
			int ny = y + i*dy[d];
			if (0 <= nx && nx <= n - 1 && 0 <= ny && ny <= m - 1) {
				if (maps[nx][ny] == 1) break;
				if (maps[nx][ny] == 0 && visit[nx][ny][d] == 0) {
					visit[nx][ny][d] = visit[x][y][d] + 1;
					q.push({ nx, ny, d });
				}
			}
		}
		
	}
}