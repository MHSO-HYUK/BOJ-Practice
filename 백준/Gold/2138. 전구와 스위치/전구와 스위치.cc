#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
string a, b;
string temp;
int n;
int INF = 987654321;

void seq(int idx) {
	if (idx < n - 1) temp[idx + 1] = (temp[idx + 1] == '0') ? '1' :'0';
	temp[idx] = (temp[idx] == '0') ? '1' : '0';
	temp[idx - 1] = (temp[idx - 1] == '0') ? '1' : '0';
}

int light(int flag) {
	int cnt = 0;
	temp = a;
	if (flag == 0) {
		temp[0] = (temp[0] == '0') ? '1' : '0';
		temp[1] = (temp[1] == '0') ? '1' : '0';
		cnt++;
	}
	for (int i = 1; i < n; i++) {
		if (temp[i - 1] != b[i - 1]) {
			seq(i);
			cnt++;
		}
	}
	if (temp == b) return cnt;
	else return INF;
}


int main(void)
{
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);
	/*
		2138 전구와 스위치
		- i번 스위치 동작시 i -1, i, i+1 전구의 상태가 바뀜
		- 1번은 1, 2번
		- N번은 N-1, N번
	*/
	cin >> n;
	cin >> a >> b;
	int ans0 = light(0);
	int ans1 = light(1);
	if (min(ans0, ans1) == INF) cout << -1;
	else cout << min(ans0, ans1);
}