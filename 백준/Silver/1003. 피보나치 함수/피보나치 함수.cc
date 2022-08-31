#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>

using namespace std;
pair<int, int> solution(int n) {
	/*
		1003 피보나치 함수
		피보나치(n) 호출 시, 0과 1이 각각 몇번 호출되는 지 구하는 프로그램
	*/
	vector <pair<int, int>> check(41);
	check[0] = { 1, 0 };
	check[1] = { 0, 1 };
	for (int i = 2; i < 41; i++) {
		check[i].first = check[i - 1].first + check[i - 2].first;
		check[i].second = check[i - 1].second + check[i - 2].second;
	}
	return check[n];
}

int main() {
	int t; cin >> t;
	vector<int> question;
	for (int i = 0; i < t; i++) {
		int n; cin >> n;
		question.push_back(n);
	}
	for (int i : question) {
		pair<int, int> ans = solution(i);
		cout << ans.first <<  ' '  <<ans.second << endl;
	}

}