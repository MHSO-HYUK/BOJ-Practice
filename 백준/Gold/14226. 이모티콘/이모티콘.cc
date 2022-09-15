#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>
using namespace std;
int s;
int visit[2000][2000];


int main() {
	/*
		14226 이모티콘
		-> 클립보드가 비어있을 때 2번 불가
		-> S개의 이모티콘을 화면에 띄우는 데 걸리는 시간의 최솟값
	*/
	cin >> s;
	for (int i = 0; i < 2000; i++) {
		memset(&visit[i][0], 0, sizeof(visit[i]));
	}

	queue <vector<int>> q; // 화면, 클립보드, 시간
	q.push({ 1, 0, 0 });
	visit[1][0] = 1;
	while (!q.empty()) {
		int scr = q.front()[0];
		int clip = q.front()[1];
		int time = q.front()[2];
		q.pop();

		if (scr == s) { // 화면에 S개의 이모티콘 올라오면 끝
			cout << time;
			break;
		}
		//  1. 화면에 있는 이모티콘 전체 복사
		if (scr <= 2001 && visit[scr][scr] == 0) {
			visit[scr][scr] = 1;
			q.push({ scr, scr, time + 1 });
		}
		// 2. 클립보드 내 이모티콘 붙혀넣기
		if (scr+clip <= 2001 && clip != 0 && visit[scr + clip][clip] == 0) {
			visit[scr + clip][clip] = 1;
			q.push({ scr + clip, clip, time + 1 });
		}
		// 3. 화면에 있는 이모티콘 중 하나 삭제
		if (scr != 0 && visit[scr - 1][clip] == 0) {
			visit[scr - 1][clip] = 1;
			q.push({ scr - 1, clip, time + 1 });
		}
	}
}