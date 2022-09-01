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
		1912 연속합
		연속된 몇개의 수를 선택하여 구할 수 있는 가장 큰 합을 구하라
		- 수는 한개 이상 선택해야 함
	*/
	vector <int> dp(n);
	dp[0] = seq[0];
	for (int i = 1; i < n; i++) {
		dp[i] = max(dp[i - 1] + seq[i], seq[i]);
	}
	return *max_element(dp.begin(), dp.end());
}


int main() {
	int n; cin >> n;
	vector<int> seq;
	for (int i = 0; i < n; i++) { int num; cin >> num; seq.push_back(num); }
	cout << solution(seq, n);
}