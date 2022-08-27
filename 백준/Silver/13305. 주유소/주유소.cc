#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <sstream> // 문자열 분리에 요구되는 라이브러리

using namespace std;

long long solution(vector<long long> price, vector <long long> road, long long n) {
	/*
		13305 주유소
		가장 왼쪽에서 가장 오른쪽으로 이동
		이때 이동하는 최소 비용 (도시마다 기름 값 차이 O)
	*/
	long long minprice = price[0];
	long long answer = 0;
	for (long long i = 0; i < n-1; i++) {
		minprice = min(minprice, price[i]);
		answer += minprice * road[i];
	}
	return answer;
}

int main() {
	long long n; cin >> n;
	vector <long long> road, price;
	for (long long i = 0; i < n-1; i++) {
		long long c; cin >> c;
		road.push_back(c);
	}
	for (long long i = 0; i < n; i++) {
		long long c; cin >> c;
		price.push_back(c);
	}
	cout << solution(price, road, n);
}