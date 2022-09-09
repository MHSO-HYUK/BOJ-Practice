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
vector<pair<int, int>> poten_wall;
queue<vector<int>> virus;


int visit[10][10];

int dx[4] = { 0, 0, 1, -1 };
int dy[4] = { 1, -1, 0 ,0 };

long long solution(int n, int m){
	/*
		14502 연구소
		- 새로 새울 수 있는 벽은 3개 
		- 얻을 수 있는 안전 영역 크기의 최댓값
	*/
	int num = poten_wall.size();
	int minima = 100;

	for (int i = 0; i < num; i++) {
		for (int j = i; j < num; j++) {
			for (int k = j; k < num; k++) {
				if (i != j && j != k && k != i) {
					queue<vector<int>> queue;
                    queue = virus;
					int v[10][10];
					copy(&visit[0][0], &visit[0][0]+100, &v[0][0]);
                    
                    int cnt = 0;
					while (!queue.empty()) {
						if (cnt >= minima) break;
						int x = queue.front()[0];
						int y = queue.front()[1];
						queue.pop();
						for (int d = 0; d < 4; d++) {
							int nx = x + dx[d];
							int ny = y + dy[d];
							if (0 <= nx && nx <= n - 1 && 0 <= ny && ny <= m - 1) {
								if (maps[nx][ny] == 0 && poten_wall[i] != make_pair(nx, ny) && poten_wall[j] != make_pair(nx, ny) && poten_wall[k] != make_pair(nx, ny)) {
									if (v[nx][ny] == 0) {
										cnt += 1; // 감염된 빈칸 수 추가
										queue.push({ nx, ny });
										v[nx][ny] = 1;
									}
								}
							}
						}
					}
					minima = min(minima, cnt);
				}
			}
		}
	}
	return minima;
}

int main() {
	memset(visit, 0, sizeof(visit));
	int n, m; cin >> n >> m;
	
	for (int i = 0; i < n; i++) {
		vector <int> map;
		for (int j = 0; j < m; j++) {
			int val; cin >> val;
			if (val == 0) { // 빈 칸인 경우
				poten_wall.push_back({ i, j });
			}

			if (val == 2) { // 바이러스인 경우
				visit[i][j] = 1;
				virus.push({ i, j });
			}
			map.push_back(val);
		}
		maps.push_back(map);
	}
	cout << poten_wall.size() - solution(n, m) - 3;
}