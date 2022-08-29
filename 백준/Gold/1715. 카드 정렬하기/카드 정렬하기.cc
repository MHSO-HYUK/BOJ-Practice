#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <sstream> // 문자열 분리에 요구되는 라이브러리
#include <numeric>

using namespace std;

int solution(priority_queue <int> card, int n) {
	/*
		1715 카드 정렬하기
		N개의 숫자 카드 묶음이 주어질 때 최소한 몇번의 비교가 가장 효율적인지 구하라
		-> 최소 비교 횟수
	*/
	int answer = 0;
	while (card.size() != 1) {
		int a = card.top();
		card.pop();
		int b = card.top();
		card.pop();
		answer += -(a + b);
		card.push(a + b);
	}
	return answer;
}

int main() {
	int n; cin >> n;
	priority_queue <int> card;
	for (int i = 0; i < n; i++) {
		int num; cin >> num;
		card.push(-num);
	}
	cout << solution(card, n);
}