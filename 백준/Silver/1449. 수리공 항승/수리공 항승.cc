#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>

using namespace std;

int solution(vector <int> water, int n, int l) {
	/*
		1449 수리공 항승
		길이가 L인 테이프로 물을 막는다 - 좌우 0.5 만큼 간격을 줘야 함
		- 필요한 테이프의 최소갯수를 구하라 
	*/
	vector <int> visit(n, 0);
	sort(water.begin(), water.end()); // 물이 새는 위치 오름차순 정렬
	int answer = 0;
	for (int i = 0; i < n; i++) {
		if (visit[i] == 0) {
			visit[i] = 1;
			answer += 1;
			for (int j = i; j < n; j++) {
				if (abs(water[i] - water[j]) <= l - 1) { // 두 구멍의 차이가 l -1 인 경우
					visit[j] = 1;
				}
				else break;
			}
		}
	}
	return answer;
}

int main() {
	int n, l; cin >> n >> l;
	vector <int> water;
	for (int i = 0; i < n; i++) {
		int w; cin >> w;
		water.push_back(w);
	}
	cout << solution(water, n, l);
}