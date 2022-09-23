#include <iostream>
#include <vector>
#include <queue>
#include <deque>
#include <numeric>
#include <string>
#include <algorithm>
using namespace std;
int n;
int pend[31];
int m;
int metarial[8];
bool temp[40001];
bool dp[40001];

int main(void)
{
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);
	/*
		2629 양팔 저울
		- 추를 이용하여 구슬의 무게를 확인할 수 있다면 Y / N
	*/
	cin >> n;
	for (int i = 0; i < n; i++) cin >> pend[i];
	cin >> m;
	for (int i = 0; i < m; i++) cin >> metarial[i];

	dp[0] = 1;
	for (int i = 0; i < n; i ++) {
		int now = pend[i];
		copy(dp, dp + 40000, temp);
		for (int j = 0; j < 40001; j++) {
			if (dp[j] == 1) {
				if(j+now <= 40000)temp[j + now] = 1;
				if (j - now >= 0) temp[j - now] = 1;
				else temp[now - j] = 1;
			}
		}
		copy(temp, temp + 40000, dp);
	}

	for (int i = 0; i < m; i++) {
		if (dp[metarial[i]]) cout << "Y ";
		else cout << "N ";
	}


}