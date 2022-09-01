#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>

using namespace std;
long long  solution(int n) {
	/*
		1904 01타일
		1 / 00 타일 존재
		N이 주어졌을 때 만들수 있는 모든 가짓수
	*/
	vector <int> dp(1000000);

	dp[1] = 1;
	dp[2] = 2;
	dp[3] = 3;
	dp[4] = 5;
	if (n > 4) {
		for (int i = 5; i < n + 1; i++) {
			dp[i] = (dp[i - 1] + dp[i - 2]) % 15746;
		}
	}
	
	return dp[n];
}

int main() {
	int n; cin >> n;
	cout << solution(n);
}