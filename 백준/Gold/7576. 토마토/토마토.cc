#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>

using namespace std;
vector<vector<int>> maps;
int dx[4] = { 0, 0, 1, -1 };
int dy[4] = { 1, -1, 0 ,0 };

long long solution(int n, int m){
	/*
		7576 토마토
		- 토마토들이 며칠이 지나면 다 익게 되나요
		- 인접한 토마토는 하루가 지나면 익은 토마토의 영향을 받아 익는다. 
	*/
	queue <vector<int>> q;

	vector<vector<int>> visit;
	vector<int> v(m);
	int day;

	for (int i = 0; i < n; i++) visit.push_back(v);


	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (maps[i][j] == 1) {
				q.push({ i, j , 0});
				visit[i][j] = 1;
			}
		}
	}
	while (!q.empty()) {
		int x = q.front()[0];
		int y = q.front()[1];
		day = q.front()[2];
		q.pop();
		for (int k = 0; k < 4; k++) {
			int nx = x + dx[k];
			int ny = y + dy[k];
			if (0 <= nx && nx <= n - 1 && 0 <= ny && ny <= m - 1) {
				if (visit[nx][ny] == 0 && maps[nx][ny] == 0) {
					q.push({ nx, ny, day + 1 });
					visit[nx][ny] = 1;
				}
			}
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (visit[i][j] == 0 && maps[i][j] == 0) {
				return -1;
			}
		}
	}
	return day;
}

int main() {
	int n, m; cin >> m >> n;
	for (int i = 0; i < n; i++) {
		vector<int>map;
		for (int j = 0; j < m; j++) {
			int v; cin >> v; 
			map.push_back(v);
		}
		maps.push_back(map);
	}
	cout << solution(n, m);
}