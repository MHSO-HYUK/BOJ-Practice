#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>

using namespace std;
int solution(vector <int> pend, int n) {
	/*
		2437 저울
		무게 N인 저울 추가 주어질때 측정할 수 없는 양의 정수 무게 중 
		최솟값을 구하는 프로그램
	*/
	sort(pend.begin(), pend.end()); // 무게 추 오름차순 정렬
	int answer = 0;
	for (int i = 0; i < n; i++) {
		if (answer + 1 >= pend[i]) answer += pend[i];
		else break;
	}
	return answer + 1;
}

int main() {
	int n; cin >> n;
	vector <int> pend;
	for (int i = 0; i < n; i++) {
		int p; cin >> p;
		pend.push_back(p);
	}
	cout << solution(pend, n);
}