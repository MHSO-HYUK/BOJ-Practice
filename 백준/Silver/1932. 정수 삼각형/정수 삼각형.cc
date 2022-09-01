#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>

using namespace std;
int solution(vector<vector<int>> tri, int n) {
	/*
		1932 정수 삼각형
		맨 위층 부터 최하층으로 갈때 
		선택한 수의 합의 최대가 되는 경로를 구하는 프로그램 작성
	*/
	for (int i = 1; i < n; i++) {
		for (int j = 0; j < i + 1; j++) {
			if (j == 0) tri[i][j] = tri[i - 1][j] + tri[i][j];
			else if (j == i) tri[i][j] = tri[i][j] + tri[i - 1][j - 1];
			else {
				tri[i][j] = max(tri[i - 1][j - 1] +tri[i][j], tri[i - 1][j] +tri[i][j]);
			}
		}
	}
	return *max_element(tri[n - 1].begin(), tri[n - 1].end());
}


int main() {
	int n; cin >> n;
	vector <vector<int>> tri;
	for (int i = 0; i < n; i++) {
		vector<int> line;
		for (int j = 0; j < i+1; j++) {
			int num; cin >> num;
			line.push_back(num);
		}
		tri.push_back(line);
	}
	cout << solution(tri, n);
}