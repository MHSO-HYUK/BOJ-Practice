#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>

using namespace std;
int n;
int dp[31];

int solution() {
	/*
		2133 타일 채우기
		3*n 크기 벽을 2*1 / 1*2로 채우는 경우의 수를 구하자
	*/
	if (n % 2 == 1) return 0;
	else {
		dp[0] = 1;
		dp[2] = 3;

		for (int i = 4; i < n + 1; i += 2) {
			dp[i] = 4 * dp[i - 2] - dp[i - 4];
		}
	}
	return dp[n];
}

int main() {
	memset(dp, 0,  sizeof(dp));
	cin >> n;
	cout << solution();
}