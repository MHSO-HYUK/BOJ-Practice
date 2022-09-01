#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>

using namespace std;
long long  solution(vector<int> card,int n) {
	/*
		11052 카드 구매하기
		- 돈을 최대한 많이 지불해서 카드 N개 구매
	*/
	vector <int> dp(n+1);

	for (int i = 1; i < n + 1; i++) { // i개를 구매했을 때 
		for (int j = 1; j < n + 1; j++) { // 카드팩 탐색
			if (i - j >= 0) dp[i] = max(dp[i - j] + card[j], dp[i]);
		}
	}
	return dp[n];
}

int main() {
	int n; cin >> n;
	vector <int> card;
	card.push_back(0);
	for (int i = 1; i < n+1; i++) {
		int c; cin >> c;
		card.push_back(c);
	}
	cout << solution(card, n);
}