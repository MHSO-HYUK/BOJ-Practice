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
		10844 쉬운 계단 수
		인접한 모든 자리의 차이가 1인 수
		- 길이가 N인 계단 수가 총 몇개 있는지 구해보자
		- 0으로 시작하는 수는 계단 수가 아니다.

		-> 이전 DP에서
		- 0으로 끝나는 경우 
		- 9로 끝나는 경우
		제외하고 2갈래로 나갈 수 있음
	*/
	vector <long long> numCase(10); // 0 ~ 9 끝
	vector <vector <long long>> dp;
	for (int i = 0; i < n; i++) {
		dp.push_back(numCase);
	}

	for (int i = 1; i < 10; i++) dp[0][i] = 1;

	for (int i = 1; i < n; i++) {
		for (int j = 1; j < 9; j++) {
			dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1])%1000000000;
		}
		dp[i][0] = dp[i - 1][1] % 1000000000;
		dp[i][9] = dp[i - 1][8] % 1000000000;
	}

	long long answer = 0;
	for (int i = 0; i < 10; i++) {
		answer = (answer + dp[n - 1][i]) % 1000000000;
	}
	return answer;
}

int main() {
	int n; cin >> n;
	cout << solution(n);
}