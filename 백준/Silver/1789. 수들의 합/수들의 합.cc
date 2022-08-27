#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <sstream> // 문자열 분리에 요구되는 라이브러리

using namespace std;

int solution(long long s) {
	/*
		1789 수들의 합
		서로 다른 N개의 자연수 합이 S 
		-> S를 알 때, 자연수 N의 최댓값
	*/
	int now = 1;
	int answer = 0;
	while (true) {
		s = s - now;
		if (s < 0) {
			break;
		}
		else if (s == 0) {
			answer += 1;
			break;
		}
		answer += 1;
		now += 1;
	}
	return answer;
}

int main() {
	long long s; cin >> s;
	cout << solution(s);
}