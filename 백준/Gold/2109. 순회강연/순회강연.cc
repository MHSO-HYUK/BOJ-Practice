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
vector<pair<int, int>> sche;
priority_queue<pair<int, int>> pq;

int main() {
	/*
		2109 순회강연
		- 데드라인 d / 페이 p
		- 가장 많은 돈을 벌 수 있도록 순회강연
	*/
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n;
	if (n == 0) cout << 0;
	else {
		for (int i = 0; i < n; i++) {
			int p, d; cin >> p >> d;
			sche.push_back({ d, p });
		}
		sort(sche.begin(), sche.end(), greater<>());
		int time = sche[0].first;
		int answer = 0;
		int idx = 0;
		while (true) {
			while (true) {
				if (idx <= n - 1 && sche[idx].first == time) {
					pq.push({ sche[idx].second, idx });
					idx++;
				}
				else break;
			}
			if (!pq.empty()) {
				int val = pq.top().first;
				int addr = pq.top().second;
				answer += val;
				//cout << time << " " << answer << endl;
				pq.pop();
			}
			time--;
			if (time == 0) 	break;
		}
		cout << answer;
	}
}