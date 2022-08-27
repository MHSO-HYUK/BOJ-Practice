#include <stdio.h>
#include <iostream>
#include <vector>
#include<algorithm>

using namespace std;

int solution(vector<int> p, int n) {
	/*
		11399 ATM
		각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력
	*/
	sort(p.begin(), p.end());
	int answer = 0;
	for (int i = 0; i < n; i++) {
		answer += (n - i) * p[i];
	}
	return answer;
}
int main() {
	vector<int> p;
	int n; cin >> n;
	for (int i = 0; i < n; i++) {
		int cache;
		cin >> cache; p.push_back(cache);
	}
	cout << solution(p, n);
    return 0;
}