#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>

using namespace std;
vector <int> seq;

int solution(int n) {
	/*
		14002 가장 긴 증가하는 부분 수열 4
	*/
	vector <int> dp(n, 1);
	vector <vector<int>> temp;
	for (int i = 0; i < n; i++) {
		vector <int > t;
		t.push_back(seq[i]);
		temp.push_back(t);
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < i; j++) {
			if (seq[i] > seq[j]) {
				dp[i] = max(dp[i], dp[j] + 1);
				if (dp[i] == dp[j] + 1) {
					temp[i] = temp[j];
					temp[i].push_back(seq[i]);
				}
			}
		}
	}
	int maxima = *max_element(dp.begin(), dp.end());
	cout << maxima << endl;
	for (int i = 0; i < n; i++) {
		if (dp[i] == maxima) {
			for (int j = 0; j < temp[i].size(); j++) {
				cout << temp[i][j]<< " ";
			}
			break;
		}
	}
	return 0;
}

int main() {
	int n; cin >> n;
	for (int i = 0; i < n; i++) {
		int s; cin >> s;
		seq.push_back(s);
	}
	solution(n);
}