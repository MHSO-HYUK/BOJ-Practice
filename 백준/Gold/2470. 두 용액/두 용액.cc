#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>
using namespace std;
int liq[100001];


int main() {
	/*
		2470 두 용액
		- 특성 값이 0에 가까운 용액을 만들고자 한다.
		- 두 개의 서로 다른 용액을 혼합해 특성 값이 0에 가장 가까운 용액을 만들자
	*/
	int INF = 2000000000;
	int n; cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> liq[i];
	}
	sort(liq, liq + n); // 특성도 정렬W
	int minima = INF;
	int a = 0;
	int b = n - 1;
	int answer[2] = { 0, 0 };
	while (a < b) {
		int sum = liq[a] + liq[b];
		if (minima > abs(sum)) {
			minima = abs(sum);
			answer[0] = liq[a];
			answer[1] = liq[b];
		}
		if (sum < 0) a++;
		else b--;
	}
	cout << answer[0] << " " << answer[1];
}