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
pair<int, int> sche[200001];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n;
	for (int i = 0; i < n; i++) {
		int a, b; cin >> a >> b;
		sche[i] = { a, b };
	}
	sort(sche, sche + n, greater<>()); // 시간 맨 뒤부터 정렬
	
	int time = sche[0].first;
	int answer = 0;
	
	priority_queue<pair<int, int>> pq;
	int idx = 0;
	while (time > 0) {
		while (true) {
			if (sche[idx].first == time) {
				pq.push({ sche[idx].second, idx });
				idx++;
			}
			else break;
		}
		if (!pq.empty()) {
			int val = pq.top().first;
			int idx = pq.top().second;
			pq.pop();
			answer += val;
		}
		time--;
	}
	cout << answer;
}