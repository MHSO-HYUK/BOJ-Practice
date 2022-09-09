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

int maps[101][101];

void solution(int n, int m, int INF) {
	/*
		11404 플로이드
		n개의 도시 -> m개의 버스
		- 버스는 한번 사용할 때 필요한 비용 존재
		- 필요한 비용의 최솟값
	*/
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			for (int k = 1; k <= n; k++) {
				maps[j][k] = min(maps[j][k], maps[j][i] + maps[i][k]);
			}
		}
	}
}

int main() {
	int INF = 987654321;
	for (int i = 0; i < 101; i++) {
		fill_n(&maps[i][0], 101, INF);
	}

	int n, m; cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int x, y, cost; cin >> x >> y >> cost;
		maps[x][y] = min(maps[x][y], cost);
	}

	for (int i = 1; i <= n; i++) {
		maps[i][i] = 0;
	}

	solution(n, m, INF);

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			if (maps[i][j] == INF) cout << 0 << " ";
			else cout << maps[i][j] << " ";
		}
		cout << endl;
	}
}