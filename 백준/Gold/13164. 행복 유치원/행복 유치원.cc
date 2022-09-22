#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int n, k;
int child[300001];
int visit[300001];


int main(void)
{
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);
	/*
		13164 행복 유치원
		- N명의 원생을 키순으로 줄세우고 K개의 조로 나눈다.
		- 각 조에는 1명 이상 / 같은 조에 속한 원생은 인접
		- 조 마다 티셔츠를 맞추는 비용은 조에서 가장 큰 키 - 가장 작은 키
		- 최소의 비용이 들도록 진행
	*/
	cin >> n >> k;
	for (int i = 0; i < n; i++) cin >> child[i];

	int ans = child[n - 1] - child[0];
	vector<int> cost(n);
	for (int i = 1; i < n; i++)	cost[i] = child[i] - child[i-1]; // 인접한 아이들 간 키 차이 배열
	cost[0] = 0;
	sort(cost.begin(), cost.end()); // 비용이 가장 큰 것을 배제
	for (int i = n - 1; k > 1; k--, i--) {
		ans -= cost[i];
	}
	cout << ans;
}