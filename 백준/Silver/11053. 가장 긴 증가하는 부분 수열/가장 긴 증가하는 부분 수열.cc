#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>

using namespace std;
int solution(vector<int> seq, int n) {
	/*
		11053 가장 긴 증가하는 부분 수열
	*/
	vector<int> dp(n, 1);
	for (int i = 0; i < n; i++) {
		for (int j = i; j >= 0; j--) {
			if (seq[i] > seq[j]) dp[i] = max(dp[i], dp[j] + 1);
		}
	}
	return *max_element(dp.begin(), dp.end());
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