#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>

using namespace std;

int solution(priority_queue <int> pos, priority_queue <int> neg, int n) {
	/*
		1744 수 묶기
		길이가 N인 수열 - 수열의 두 수를 위치와 상관없이 묶어서 합을 구함 
		-> 이때 그 합이 최대가 되게 하는 프로그램을 작성하라

		- 양수 따로 힙에 쌓음 - 1인 경우, 그냥 종료
		- 음수, 0 따로 힙에 쌓음
	*/
	int answer = 0;
	while (!pos.empty() && pos.size() != 1 && pos.top() != 1) {
		int a = pos.top(); 
		pos.pop();
		int b = pos.top();
		if (b == 1) {
			pos.push(a);
			break;
		}
		pos.pop();
		answer += a * b;
	}
	if (!pos.empty()) {
		while (!pos.empty()) {
			answer += pos.top();
			pos.pop();
		}
	}

	while (!neg.empty() && neg.size() != 1) {
		int a = neg.top();
		neg.pop();
		int b = neg.top();
		neg.pop();
		answer += a * b;
	}
	if (!neg.empty()) answer -= neg.top();

	return answer;
}

int main() {
	int n; cin >> n;
	priority_queue <int> pos, neg;
	for (int i = 0; i < n; i++) {
		int num; cin >> num;
		if (num > 0) pos.push(num);
		else  neg.push(-num);
	}
	cout << solution(pos, neg, n);
}