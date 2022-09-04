#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>

using namespace std;
int dx[4] = {1, -1, 0, 0};
int dy[4] = { 0, 0, 1, -1 };
vector <vector<int>> maps;
int n, m;
int dp[501][501];


int dfs(int x, int y, int n , int m) {
	if (x == n - 1 && y == m - 1) {
		return 1;
	}
	if (dp[x][y] != -1) {
		return dp[x][y];
	}

	int num = 0;
	for (int k = 0; k < 4; k++) {
		int nx = x + dx[k];
		int ny = y + dy[k];
		if ((0 <= nx) && (nx<= n - 1) && (0 <= ny) &&  (ny <= m - 1)) {
			if (maps[nx][ny] < maps[x][y]) {
				num += dfs(nx, ny, n, m);
			}
		}
		else continue;
	}
	dp[x][y] = num;
	return num;
}

int solution(vector <vector<int>> maps, int n, int m) {
	/*
		1520 내리막길
		0, 0 에서 n-1, m-1로 가는데 항상 내리막길로만 이동하는 경로의 갯수
	*/
	int answer = dfs(0, 0, n, m);
	return answer;
}

int main() {
	memset(dp, -1, sizeof(dp));
	 cin >> n >> m;
	
	
	for (int i = 0; i < n; i++) {
		vector <int> map;
		for (int j = 0; j < m; j++) {
			int v; cin >> v; map.push_back(v);
		} 
		maps.push_back(map);
	}

	cout << solution(maps, n, m);
}