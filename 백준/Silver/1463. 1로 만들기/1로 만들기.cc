#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>

using namespace std;
long long solution(long long n) {
	/*
		1462 1로 만들기
		- X가 3으로 나누어 떨어지면 3으로 나눈다.
		- X가 2로 나누어 떨어지면 2로 나눈다.
		- 1을 뺀다. 
		정수 N이 주어졌을 때, 세개 연산을 적절히 사용하여 1을 만든다. 
		연산 최솟값을 구하라
	*/
	queue <pair<int, int>> q;
	q.push({ n, 0 });
	while (!q.empty()) {
		long now = q.front().first;
		long cnt = q.front().second;
		q.pop();
		if (now == 1) return cnt;
		else {
			if (now % 3 == 0) {
				q.push({ now / 3, cnt + 1 });
			}
			if (now % 2 == 0) {
				q.push({ now / 2, cnt + 1 });
			}
			if (now - 1 > 0) {
				q.push({ now - 1, cnt + 1 });
			}
		}
	}
}

int main() {
	long long n; cin >> n;
	cout << solution(n);
}