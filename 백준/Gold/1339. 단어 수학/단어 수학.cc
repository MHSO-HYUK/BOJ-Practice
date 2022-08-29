#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>

using namespace std;

int solution(vector <int> alpha) {
	/*
		1339 단어 수학
		N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램 작성
		- 서로 다른 알파벳은 서로 다른 수
	*/
	sort(alpha.begin(), alpha.end(), greater<>()); // 내림차순 정렬
	int idx = 0;
	int num = 9;
	int answer = 0;
	while (alpha[idx] != 0) {
		answer += num * alpha[idx];
		num -= 1;
		idx += 1;
	}
	return answer;
}

int main() {
	int n; cin >> n;
	vector <int> alpha(27);
	for (int i = 0; i < n; i++) {
		string s; cin >> s;
		for (int j = s.length() - 1; j >= 0; j--) {
			alpha[s[j] - 'A'] += pow(10, s.length() - 1 - j);
		}
	}
	cout << solution(alpha);
}