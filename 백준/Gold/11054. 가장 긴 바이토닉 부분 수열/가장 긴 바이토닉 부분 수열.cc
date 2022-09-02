#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>

using namespace std;
int solution(vector <int> seq, int n) {
	/*
		11054 가장 긴 바이토닉 부분 수열 
	*/
	vector<int> reverse_seq(n);
	copy(seq.begin(), seq.end(), reverse_seq.begin());
	reverse(reverse_seq.begin(), reverse_seq.end());

	vector <int> dp(n, 1);
	vector <int> reverse_dp(n, 1);

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < i; j++) {
			if (seq[i] > seq[j]) dp[i] = max(dp[i], dp[j] + 1);
			if (reverse_seq[i] > reverse_seq[j]) reverse_dp[i] = max(reverse_dp[i], reverse_dp[j] + 1);
		}
	}
	
	for (int i = 0; i < n; i++) dp[i] += reverse_dp[n - 1 - i];

	return *max_element(dp.begin(), dp.end()) - 1;
}

int main() {
	int n; cin >> n;
	vector <int> seq;
	for (int i = 0; i < n; i++) {
		int s; cin >> s;
		seq.push_back(s);
	}
		cout << solution(seq, n);
}