#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>

using namespace std;
int n, k;
vector <int> coin;

int solution() {
	/*
		2294 동전 2
		- n 가지 종류 동전
		- 가치가 k가 되고 동전의 갯수가 최소가 되도록 
		- 불가능한 경우 -1 출력
	*/
	int s; s = coin.size(); // 동전의 갯수

	vector<vector <int > > dp;
	vector <int> d(k+1, 1e+6);
	for (int i = 0; i < s; i++) dp.push_back(d);

	for (int i = 0; i < s; i++) { // 동전 순회
		dp[i][0] = 0;
		if (i != 0 ) dp[i] = dp[i - 1];
		for (int j = 0; j < k + 1; j++) {
			if (j - coin[i] >= 0) dp[i][j] = min(dp[i][j], dp[i][j-coin[i]] + 1);
		}
	}
	if (dp[s - 1][k] >= 1e+6) return -1;
	return dp[s - 1][k];
}

int main() {
	cin >> n >> k;
	for (int i = 0; i < n; i++) {
		int c; cin >> c;
		if (c <= k)  coin.push_back(c);
	}
	cout << solution();
}