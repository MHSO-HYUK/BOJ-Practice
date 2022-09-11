#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>
using namespace std;

int hx[8] = {2, 1, -1, -2, -2, -1, 1, 2};
int hy[8] = {1, 2, 2, 1, -1, -2, -2, -1};
int mx[4] = {1, -1, 0, 0};
int my[4] = {0, 0, 1, -1};
int maps[201][201];
int visit[201][201][31];

int main() {
	/*
		1600 말이 되고픈 원숭이
		- K번만 말처럼 움직이기 가능 
		- 최소한의 동작으로 이동하자
	*/
	int k; cin >> k;
	int w, h; cin >> w >> h;
	for (int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			memset(&visit[i][j][0], 0, sizeof(visit[i][j]));
			int v; cin >> v;
			maps[i][j] = v;
		}
	}

	queue <vector<int>> q;
	q.push({ 0, 0, 0, 0 }); // x, y, hmove, trial
	visit[0][0][0] = 1;
	int x, y, hmove, trial;
	while (!q.empty()) {
		x = q.front()[0];
		y = q.front()[1];
		hmove = q.front()[2];
		trial = q.front()[3];
		q.pop();

		if (x == h - 1 && y == w - 1) {
			break;
		}

		if (hmove <  k) { // 말처럼 이동 가능할 경우
			for (int d = 0; d < 8; d++) {
				int nx = x + hx[d];
				int ny = y + hy[d];
				if (0 <= nx && nx <= h - 1 && 0 <= ny && ny <= w - 1) {
					if (maps[nx][ny] == 0 && visit[nx][ny][hmove + 1] == 0) {
						visit[nx][ny][hmove + 1] = 1;
						q.push({ nx, ny, hmove + 1, trial +1 });
					}
				}
			}
		}
		for (int d = 0; d < 4; d++) {
			int nx = x + mx[d];
			int ny = y + my[d];
			if (0 <= nx && nx <= h - 1 && 0 <= ny && ny <= w - 1) {
				if (maps[nx][ny] == 0 && visit[nx][ny][hmove ] == 0) {
					visit[nx][ny][hmove] = 1;
					q.push({ nx, ny, hmove, trial + 1});
				}
			}
		}
	}
	if (x == h - 1 && y == w - 1)	cout << trial;
	else cout << -1;
}