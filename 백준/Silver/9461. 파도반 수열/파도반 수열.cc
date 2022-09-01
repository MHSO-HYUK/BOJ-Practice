#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>

using namespace std;
vector <long long> solution(long long n) {
	/*
		9461 파도반 수열
		1 - 1 - 1 - 2 - 2 - 3 - 4 - 5 - 7 - 9 - 12 - 16 -
	*/
	vector <long long> ans(150);
	ans[0] = 1;
	ans[1] = 1;
	ans[2] = 1;
	ans[3] = 2; // 2+ 0
	ans[4] = 2; // 3
	ans[5] = 3; // 4 + 2
	ans[6] = 4;
	ans[7] = 5;
	ans[8] = 7;
	ans[9] = 9;
	if (n > 8) {
		for (long long i = 9; i < n + 3; i++) {
			ans[i] = ans[i - 1] + ans[i - 5];
		}
	}
	return ans;
}

int main() {
	long long t; cin >> t;
	vector <long long> q;
	long long maxima = 0;
	for (long long i = 0; i < t; i++) {
		long long num;
		cin >> num;
		maxima = max(maxima, num);
		q.push_back(num);
	};
	vector<long long> ans;
	ans = solution(maxima);
	for (long long i : q) {
		cout << ans[i - 1] << endl;
	}
}