#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>

using namespace std;
long long  solution(vector <long long> coin, int n, int k) {
	/*
		2293 동전 1
		- 가치의 합이 k가 되도록 하는 경우의 수를 구하시오
	*/
	vector <long long> dp(k + 1); // 0 ~ k원 을 만드는 경우
	dp[0] = 1;

	for (int i : coin) {
		for (int j = 1; j < k + 1; j++) {
			if(j-i >= 0)dp[j] += dp[j - i];
		}
	}
	return dp[k];
}

int main() {
	int n, k; cin >> n >> k;
	vector <long long> coin;
	for (int i = 0; i < n; i++) {
		long long c; cin >> c;
		coin.push_back(c);
	}
	cout << solution(coin, n, k);
}