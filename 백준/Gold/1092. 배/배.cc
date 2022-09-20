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
int crain[51];
int m;
int box[10001];
int visit[10001];
priority_queue < pair<int, int>> pq[51];

int main() {
	/*
	1092 배
	- 1분에 박스를 하나씩 배에
	- 크레인에는 무게 제한이 있다. 
	- 걸리는 시간의 최솟값
	*/
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n;
	for (int i = 0; i < n; i++) cin >> crain[i];
	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> box[i];
		for (int j = 0; j < n; j++) {
			if (crain[j] >= box[i]) {
				pq[j].push({ box[i], i });
			}
		}
	}
	sort(box, box + m, greater<>());
	
	if (*max_element(crain, crain+n) < box[0]) {
		cout << -1;
		exit(0);
	}
	else { // 매순간 각 크레인이 들 수 있는 가장 무거운 물건을 들어야 
		memset(visit, 0, sizeof(visit));
		int time = 0;
		int cnt = 0;
		while (true) {
			time++;
			for (int i = 0; i < n; i++) {
				while (true) {
					if (!pq[i].empty()) {
						int val = pq[i].top().first;
						int idx = pq[i].top().second;
						pq[i].pop();
						if (visit[idx] == 0) {
							visit[idx] = 1;
							cnt++;
							break;
						}
						else continue;
					}
					break;
				}
			}
			if (cnt == m) break;
		}
		
		cout << time;
	}
}