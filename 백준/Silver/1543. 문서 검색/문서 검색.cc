#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>

using namespace std;

int solution(string s, string t) {
	/*
		1543 문서 검색
		단어가 최대 몇번 중복되지 않게 등작하는 지 구하는 프로그램 
	*/
	int answer = 0;
	int i = 0;
	while(i < s.length()){
		bool flag = true;
		for (int j = 0; j < t.length(); j++) {
			if (s[i + j] != t[j]) {
				flag = false;
				break;
			}
		}
		if (flag) {
			i += t.length();
			answer += 1;
		}
		else i += 1;
	}
	return answer;
}

int main() {
	string s; getline(cin, s);
	string t; getline(cin, t);
	cout << solution(s, t);
}