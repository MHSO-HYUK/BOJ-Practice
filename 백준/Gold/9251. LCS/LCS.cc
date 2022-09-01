#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>

using namespace std;
long long  solution(string a, string b) {
	/*
		9251 LCS - 최장 공통 부분 수열
	*/
	int la = a.size();
	int lb = b.size();
	vector <int> d(lb+1);
	vector<vector<int>> dp;
	for (int i = 0; i < la+1; i++) dp.push_back(d);

	for (int i = 1; i < la+1; i++) {
		for (int j = 1; j < lb+1; j++) {
			if (a[i-1] == b[j-1]) dp[i][j] = max(dp[i][j], dp[i -1][j -1] + 1);
			else {
				dp[i][j] = max(dp[i-1][j], dp[i][j - 1]);
			}
		}
	}
	return dp[la][lb];
}

int main() {
	string a, b; cin >> a >> b;
	cout << solution(a, b);
}