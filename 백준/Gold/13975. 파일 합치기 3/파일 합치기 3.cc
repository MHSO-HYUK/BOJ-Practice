#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>

using namespace std;

long long solution(priority_queue<long long> seq, long long n){
	/*
		11066 파일 합치기
		- 하나의 파일로 합칠 때 필요한 최소 비용을 계산

	*/
	long long answer = 0;
	while (seq.size() != 1) {
		long long a = seq.top();
		seq.pop();
		long long b = seq.top();
		seq.pop();
		answer += -(a + b);
		seq.push(a + b);
	}

	return answer;
}

int main() {
	long long t; cin >> t;
	vector <long long> a;
	vector <vector <long long>>answer;
	for (long long i = 0; i < t; i++) {
		long long n; cin >> n;
		priority_queue <long long> seq;
		for (long long j = 0; j < n; j++) {
			long long s; cin >> s;
			seq.push(-s);
		}
		a.push_back(solution(seq, n));
	}
	for (long long i : a) {
		cout << i << endl;
	}
}