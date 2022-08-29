#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>

using namespace std;

int solution(string s) {
	/*
		1439 뒤집기
		0과 1로만 이루어진 문자열 S
		연속된 하나 이상의 숫자를 잡고 모두 뒤집을 수 있음
	*/
	int num0, num1; num0 = 0; num1 = 0;
	for (int i = 0; i < s.length(); i++) {
		if (i == 0) {
			if (s[i] == '0') num0 += 1;
			else  num1 += 1;
		}
		else {
			if (s[i] != s[i - 1]) {
				if (s[i] == '0') num0 += 1;
				else num1 += 1;
			}
		}
	}
	return min(num0, num1);
}

int main() {
	string s; cin >> s;
	cout << solution(s);
}