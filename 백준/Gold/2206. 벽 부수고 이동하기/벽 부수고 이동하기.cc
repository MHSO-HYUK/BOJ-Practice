#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>

using namespace std;

int dx[4] = { 0, 0, 1, -1 };
int dy[4] = { 1, -1, 0 ,0 };

string maps[1001];
int visit[1001][1001][2];

int solution(int n, int m) {
	/*
		2206 벽 부수고 이동하기
		- (1, 1) -> (n, n) 이동
		- 이동하는 도중 한개의 벽을 부수고 이동 가능
	*/
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			visit[i][j][0] = 9000000;
			visit[i][j][1] = 9000000;
		}
	}

	queue<vector<int>> q;
	q.push({ 0, 0, 1, 0});
	while (!q.empty()) {
		auto now = q.front(); // x, y, 이동 횟수, 벽 부셧나요
		int x = now[0]; int y = now[1]; int move = now[2]; int wall = now[3];
		q.pop();
		if (x== n - 1 && y == m - 1) {
			return move;
		}
		for (int k = 0; k < 4; k++) {
			int nx = x + dx[k]; 
			int ny = y + dy[k];
			if (0 <= nx && nx <= n - 1 && 0 <= ny && ny <= m - 1) {
				if (maps[nx][ny] == '0' && visit[nx][ny][wall] > move + 1) {
					visit[nx][ny][wall] = move + 1;
					q.push({ nx, ny, move + 1, wall });
				}
				if (maps[nx][ny] == '1' && wall == 0) {
					if (visit[nx][ny][1] > move + 1) {
						visit[nx][ny][1] = move + 1;
						q.push({ nx, ny, move + 1, 1 });
					}
				}
			}
		}
	}
	return -1;
}

int main() {
	int n, m; cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> maps[i];
	}
	cout << solution(n , m);
}