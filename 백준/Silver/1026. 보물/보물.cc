#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> a, vector<int> b, int n) {
	/*
		1026 보물
		a의 순서를 재배치하여 값을 최소화하는 방법
		최소화한 S를 출력
	*/
	sort(a.begin(), a.end(), greater<>());
	sort(b.begin(), b.end(), less<>());
	int answer = 0;
	for (int i = 0; i < n; i++) {
		answer += a[i] * b[i];
	}
	return answer;
}

int main() {
	int n; cin >> n;
	vector <int> a, b;
	int c;
	for (int i = 0; i < n; i++) {
		cin >> c;
		a.push_back(c);
	}
	for (int i = 0; i < n; i++) {
		cin >> c;
		b.push_back(c);
	}
	cout << solution(a, b, n);
}