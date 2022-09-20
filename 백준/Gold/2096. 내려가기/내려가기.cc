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
int dp[3];
int mp[3];


int main() {
	/*
		2096 내려가기
		- 아래의 수와 붙어 있는 수로만 이동 가능

	*/
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	memset(dp, 0, sizeof(dp));
	memset(mp, 0, sizeof(mp));
	cin >> n;
	for (int i = 0; i < n; i++) {
		int a, b, c; cin >> a >> b >> c;
		int t0, t1, t2; t0 = dp[0]; t1 = dp[1]; t2 = dp[2];
		int m0, m1, m2; m0 = mp[0], m1 = mp[1]; m2 = mp[2];

		dp[0] = max(t0, t1) + a;
		dp[1] = max(max(t0, t1), t2) + b;
		dp[2] = max(t1, t2) + c;

		mp[0] = min(m0, m1) + a;
		mp[1] = min(min(m0, m1), m2) + b;
		mp[2] = min(m1, m2) + c;
	}
	cout << *max_element(dp, dp + 3) << " " << *min_element(mp, mp + 3);
}