#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>

using namespace std;
int n;
vector <pair<int, int>> line;

int solution() {
	/*
		2565 전깃줄
		- 전깃줄이 교차하지 않도록 몇개의 전깃줄을 제거
		- 제거해야할 최소 전깃줄
	*/
	sort(line.begin(), line.end()); // 오름차순 정렬

	vector <int> upside_dp(n, 1);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < i; j++) {
			if (line[i].second > line[j].second ) {// 교차하는 케이스
				upside_dp[i] = max(upside_dp[i], upside_dp[j] + 1);
			}
		}
	}

	return n - *max_element(upside_dp.begin(), upside_dp.end());
}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		int a, b; cin >> a >> b;
		line.push_back({ a, b });
	}
	cout << solution();
}