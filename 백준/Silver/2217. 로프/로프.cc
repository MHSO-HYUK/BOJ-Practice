#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <sstream> // 문자열 분리에 요구되는 라이브러리

using namespace std;

int solution(vector<int> rope, int n) {
	/*
		2217 로프
		N개의 로프가 있음 -> 병렬로 연결하면 w/k만큼 중량이 걸림
		들어올릴 수 있는 물체의 최대 중량을 구하자
		-> 모든 로프를 사용할 필요는 없으며, 임의로 몇개의 로프를 골라서 사용 가능
	*/
	sort(rope.begin(), rope.end()); // 버틸 수 있는 최대 중량 오름차순 정렬

	int maxima = 0;
	for (int i = 0; i < n; i++) { // n개 사용 -> n-1개 사용 -> ...... -> 1개 사용
		maxima = max(maxima, rope[i] * (n - i));
	}
	return maxima;
}

int main() {
	int n; cin >> n;
	vector <int> rope;

	for (int i = 0; i < n; i++) {
		int c; cin >> c;
		rope.push_back(c);
	}
	cout << solution(rope, n);
}