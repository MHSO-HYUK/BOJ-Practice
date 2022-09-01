#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>

using namespace std;
long long  solution(vector<pair<int, int>> bag, int n, int k) {
	/*
		12865 평범한 배낭
		- 무게 K 만큼 넣을 수 있는 배낭 
		- 배낭에 담을 수 있으면서 가치가 가장 높게 구성하자
		- 가치 리턴
	*/
	vector <int> d(k + 2);
	vector <vector <int>> dp;
	for (int i = 0; i < n + 2; i++) {
		dp.push_back(d);
	}

	for (int i = 1; i < n+1; i++) {
		int w = bag[i].first; // 가격 
		int v = bag[i].second; // 무게
		for (int j = 1; j < k+1; j++) {
			if (j < w) dp[i][j] = dp[i - 1][j];
			else dp[i][j] = max(v + dp[i - 1][j - w], dp[i - 1][j]);
		}
	}
	return dp[n][k];
}

int main() {
	int n, k; cin >> n >> k;
	vector<pair<int, int>> bag;
	bag.push_back({ 0, 0 });
	for (int i = 0; i < n; i++){
		int weight, value; cin >> weight >> value;
		bag.push_back({weight, value});
	}
	cout << solution(bag, n, k);
}