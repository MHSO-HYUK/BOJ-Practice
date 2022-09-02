#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>

using namespace std;
long long solution(long long n) {
	/*
		11057 오르막 수
		- 인접한 수가 같아도 됌
		- N 길이 수열이 주어질때 오르막 수의 갯수를 구하는 프로그램을 작성 
	*/

	vector <long long> d(10); // 0 ~ 9로 끝나는 수열
	vector<vector<long long>> dp;
	for (long long i = 0; i < n; i++) dp.push_back(d);
	for (long long i = 0; i < 10; i++) dp[0][i] = 1;

	for (long long i = 1; i < n; i++) {
		for (long long j = 0; j < 10; j++) {
			for (long long k = 0; k <= j; k++) dp[i][j] += dp[i - 1][k];
			dp[i][j] %= 10007;
		}
	}

	long long answer = 0;
	for (long long i = 0; i < 10; i++) answer += dp[n - 1][i];
	answer %= 10007;
	return answer;
}

int main() {
	long long n; cin >> n;
	cout << solution(n);
}