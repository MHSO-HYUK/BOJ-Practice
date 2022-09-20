#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>

using namespace std;
long long n, limit, m;
vector <pair<long long, vector<long long>>> contain;
vector<long long> dp(2010);

int main() {
	/*
		8980 택배
		- 박스를 트럭에 실으면 받는 마을에서만 내린다.
		- 트럭은 지나온 마을로 되돌아 가지 않는다.
		- 박스 중 일부만 배송할 수도 있다.
	*/
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n >> limit >> m; // 마을 수 :  n, 트럭 용량 : c
	for (long long i = 0; i < m; i++) {
		long long a, b, box; cin >> a >> b >> box;
		contain.push_back({ b, {a, b , box} });
	}
	sort(contain.begin(), contain.end()); // 이동 시간이 빠른 순으로 

	long long answer = 0;
	for (long long i = 0; i < m; i++) {
		long long start = contain[i].second[0];
		long long end = contain[i].second[1];
		long long box = contain[i].second[2];
		//cout << start << " " << end << " " << box << endl;
		long long take = box;
		for (long long j = start; j < end; j++) {
			if (dp[j] + take <= limit) continue;
			else take = limit - dp[j];
		}

		for (long long j = start; j < end; j++) {
			dp[j] += take;
		}
		//cout << i << " " << take << endl;
		answer += take;
	}
	cout << answer;
}