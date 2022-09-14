#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>
using namespace std;

int dp[501][501];


int main() {
	/*
		2458 키 순서
		- 자신의 키가 몇번째인지 알 수 있는 학생의 수를 계산
		- 모든 이들을 상대로 나보다 큰지/ 작은지 알 수 있다면 등수를 아는 것 
	*/
	int n, m; cin >> n >> m;
	int INF = 987654321;

	for (int i = 0; i < n + 1; i++) {
		fill_n(&dp[i][0], n + 1, INF);
	}


	for (int i = 0; i < m; i++) {
		int a, b; cin >> a >> b;
		dp[a][b] = 1;
	}


	for (int i = 1; i < n + 1; i++) {
		for (int j = 1; j < n + 1; j++) {
			for (int k = 1; k < n + 1; k++) {
				if (j != k) dp[j][k] = min(dp[j][k], dp[j][i] + dp[i][k]);
			}
		}
	}
	int answer = 0;
	for (int i = 1; i < n + 1; i++) {
		bool flag = true;
		for (int j = 1; j < n + 1; j++) {
			if (i == j) continue;
			if (dp[i][j] == INF && dp[j][i] == INF) flag = false;
		}
		if (flag) answer += 1;
	}
	cout << answer;
}