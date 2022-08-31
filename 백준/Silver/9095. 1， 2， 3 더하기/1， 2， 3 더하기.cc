#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>

using namespace std;
int solution(int n) {
	/*
		9095 1, 2, 3 더하기
		정수 n이 주어질 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하라
	*/
	vector <int> sol(12);
	sol[1] = 1;
	sol[2] = 2;
	sol[3] = 4;
	for (int i = 4; i < 12; i++) {
		sol[i] = sol[i - 1] + sol[i - 2] + sol[i - 3];
	}
	return sol[n];
}

int main() {
	int t; cin >> t;
	vector <int> q;
	for (int i = 0; i < t; i++) {
		int n; cin >> n;
		q.push_back(n);
	}
	for (int n : q) {
		cout << solution(n) << endl;
	}
}