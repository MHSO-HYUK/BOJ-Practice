#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>

using namespace std;

long long solution(long long a, long long b) {
	/*
		16953 A->B
		정수 A를 B로 바꾼다
		- 2를 곱한다
		- 1을 수의 가장 오른쪽에 추가한다. 
		A를 B로 바꾸는데 필요한 연산의 최솟값을 구한다.
	*/
	queue <pair<long long, long long>> q;
	q.push(make_pair(a, 1));

	while (!q.empty()) {
		long long now = q.front().first; 
		long long cnt = q.front().second;
		if (now == b) return cnt;
		q.pop();

		if (now > b) continue;

		if (1 <= 2*now <= pow(10, 9) ) {
			q.push(make_pair(2 * now, cnt+1));
		}
		if (1 <= 10 * now + 1 <= pow(10, 9) ) {
			q.push(make_pair(now * 10 + 1, cnt+1));
		}
	}
	return -1;
}

int main() {
	long long a, b; cin >> a >> b;
	cout << solution(a, b);
}