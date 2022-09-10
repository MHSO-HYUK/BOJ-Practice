#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>
using namespace std;

int maps[501][501];
int dp[501][501];
int dx[4] = { 1, -1, 0, 0 };
int dy[4] = { 0, 0, 1, -1 };
int n;

int dfs(int x, int y) {
	if (dp[x][y] != 0) return dp[x][y];
	else {
		dp[x][y] = 1;
		for (int k = 0; k < 4; k++) {
			int nx = x + dx[k];
			int ny = y + dy[k];
			if (0 <= nx && nx <= n - 1 && 0 <= ny && ny <= n - 1) {
				if (maps[nx][ny] > maps[x][y]) {
					dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1);
				}
			}
		}
		return dp[x][y];
	}
}
int main() {
	/*
		1937 욕심쟁이 판다
		- 더 대나무가 많은 칸으로만 이동한다. 
		- 최대한 많은 칸을 이동하려면?

	*/
	cin >> n;
	for (int i = 0; i < n; i++) {
		memset(dp, 0, sizeof(dp));
		for (int j = 0; j < n; j++) {
			int l; cin >> l;
			maps[i][j] = l;
		}
	}
	int answer = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			answer = max(answer, dfs(i, j));
		}
	}
	cout << answer;
}