#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>

using namespace std;
int solution(vector<vector<int>> maps, int n) {
	/*
		1149 RGB 거리
		- 맞닿은 집은 서로 색이 달라야 한다. 
		규칙을 만족하며 모든 집을 칠하는 비용의 최솟값
	*/
	for (int i = 1; i < n; i++) {
		maps[i][0] = min(maps[i - 1][1], maps[i - 1][2]) + maps[i][0];
		maps[i][1] = min(maps[i - 1][0], maps[i - 1][2]) + maps[i][1];
		maps[i][2] = min(maps[i - 1][0], maps[i - 1][1]) + maps[i][2];
	}
	return *min_element(maps[n - 1].begin(), maps[n - 1].end());
}


int main() {
	int n; cin >> n;
	vector <vector<int>> maps;
	for (int i = 0; i < n; i++) {
		int r, g, b; cin >> r >> g >> b;
		vector <int> col;
		col.push_back(r);
		col.push_back(g);
		col.push_back(b);
		maps.push_back(col);
	}
	cout << solution(maps, n);
}