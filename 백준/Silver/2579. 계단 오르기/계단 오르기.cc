#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>

using namespace std;
int solution(vector<int> stair, int n) {
	/*
		2579 계단 오르기
		- 연속 세개의 계단 불가
		- 한번에 하나 혹은 두계단 오르기 가능
		- 마지막 도착 계단은 반드시 밟아야 
		총 점수의 최댓값을 구하는 프로그램 작성
	*/
	queue <vector <int>> q;
	vector<int> v(3);
	vector <vector<int>> visit;
	for (int i = 0; i < n; i++) visit.push_back(v);
	q.push({ -1, 0, 0}); // 현 위치, 연속 밟음 상태, 점수
	int maxima = 0;
	while (!q.empty()) {
		int now = q.front()[0];
		int con = q.front()[1];
		int score = q.front()[2];
		q.pop();
		if (now == n - 1) {
			maxima = max(maxima, score);
			continue;
		}
		if (now > n - 1) continue;

		if (now >= 0) {
			if (visit[now][con] > score) continue;
			else visit[now][con] = score;
		}
		
		if (con == 2 && now+2 <= n-1) { // 연속 2 계단 밟음
			q.push({ now + 2, 1, score + stair[now + 2] });
		}
		if(con <2) {
			if(now+1 <= n-1) q.push({ now + 1, con + 1, score + stair[now + 1] });
			if (now+2 <= n-1) q.push({ now + 2, 1, score + stair[now + 2] });
		}
	}
	return maxima;
}


int main() {
	int n; cin >> n;
	vector <int> stair;
	for (int i = 0; i < n; i++) {
		int s; cin >> s;
		stair.push_back(s);
	}

	cout << solution(stair, n);
}