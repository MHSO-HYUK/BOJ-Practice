#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>
using namespace std;
int n, m;
vector<string> maps(21);
int visit[27];
int dx[4] = { 0, 0, 1, -1 };
int dy[4] = { 1, -1, 0, 0 };
int maxima;

void dfs(int x, int y, int cnt) {
	visit[maps[x][y] - 'A'] = 1;
	maxima = max(maxima, cnt);
	for (int k = 0; k < 4; k++) {
		int nx = x + dx[k];
		int ny = y + dy[k];
		if (0 <= nx && nx <= n - 1 && 0 <= ny && ny <= m - 1) {
			if (visit[maps[nx][ny] - 'A'] == 0) {
				dfs(nx, ny, cnt + 1);
				visit[maps[nx][ny] - 'A'] = 0;
			}
		}
	}
}

int main() {
	/*
		1987 알파벳
		- 새로 이동한 칸에 적혀있는 알파벳은 지금까지 지나온 모든 칸
		- 과 겹치면 안된다 
		- 최대한 이동할 수 있는 칸을 구해보세요
	*/
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> maps[i];
	}
	memset(visit, 0, sizeof(visit));
	maxima = 0;
	dfs(0, 0, 1);
	cout << maxima;
}