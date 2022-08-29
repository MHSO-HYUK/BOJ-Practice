#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <sstream> // 문자열 분리에 요구되는 라이브러리
#include <numeric>

using namespace std;

int solution(vector<pair<int, int>> score,int n) {
	/*
		1946 신입 사원
		A의 두 점수가 모두 B의 두 점수에 비해 떨어진다면 A 선발 불가
		-> 이러한 조건을 만족 시키며 선발 가능한 최대 인원 수를 구하라
	*/
	sort(score.begin(), score.end()); // 서류 점수 순위로 정렬

	int answer0 = 1; // 서류 점수 최상위 1인
	int max_meet_score0 = score[0].second;
	for (int i = 0; i < n; i++) {
		if (score[i].second < max_meet_score0) {
			max_meet_score0 = score[i].second;
			answer0 += 1;
		}
	}

	return answer0;
}

int main() {
	int t; cin >> t;
	for (int i = 0; i < t; i++) {
		int n; cin >> n;
		vector <pair<int, int>> score;
		for (int j = 0; j < n; j++) {
			int a, b;
			cin >> a >> b;
			score.push_back(make_pair(a, b));
		}
		cout << solution(score, n) << endl;
	}
}