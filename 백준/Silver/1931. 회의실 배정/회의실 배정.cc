#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<pair<int, int>> time, int n) {
	/*
		1931 회의실 배정
		한개의 회의실을 사용할 N개의 회의에 대해 사용표 생성
		시작 시간 - 끝나는 시간이 주어짐
		회의가 겹치지 않게 하는 최대 회의 갯수 찾기
		-> 회의의 시작시간과 끝날 수도 있음
		-> 한 회의가 끝나면서 동시에 다음 회의 시작 가능
	*/
	sort(time.begin(), time.end()); // 시간표 pair의 오름차순 정리
	/*
		이후 탐색하는 시간표는 이미 진행한 회의보다 시작시간이 같거나 이후
	*/
	int use = time[0].second;
	int cnt = 0;
	for (int i = 0; i < n; i++) {
		if (time[i].second >= use) {
			use = time[i].first;
			cnt += 1;
		}
	}
	return cnt;
}

int main() {
	int n; cin >> n;
	vector <pair<int, int>> time;
	for (int i = 0; i < n; i++) {
		int start, end;
		cin >> start >> end;
		time.push_back(make_pair(end, start));
	}
	cout << solution(time, n);
	return 0;
}