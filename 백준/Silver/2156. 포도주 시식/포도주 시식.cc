#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>

using namespace std;
int solution(vector<int> grape, int n) {
	/*
		2156 포도주 시식
		- 연속 세 잔을 마실 수는 없다
		- 가장 많은 포도주를 마실 수 있도록 하는 프로그램
	*/
	vector<int> d(3); // 스킵 /직전 잔 X + 마심 / 직전 1잔 + 마심
	vector<vector<int>> dp;
	for (int i = 0; i < n; i++) {
		dp.push_back(d);
	}

	if (n == 1) return grape[0];
	else if (n == 2) return grape[0] + grape[1];

	dp[0] = {0,  grape[0], grape[0]};
	dp[1] = {grape[0],  grape[1], dp[0][1] + grape[1]};
	for (int i = 2; i < n; i++) {
		dp[i][0] = *max_element(dp[i - 1].begin(), dp[i - 1].end());
		dp[i][1] = dp[i - 1][0] + grape[i];
		dp[i][2] = dp[i - 1][1] + grape[i];
	}


	return *max_element(dp[n-1].begin(), dp[n - 1].end());
}

int main() {
	int n; cin >> n;
	vector <int> grape;
	for (int i = 0; i < n; i++) { int g; cin >> g; grape.push_back(g); }
	cout << solution(grape, n);
}