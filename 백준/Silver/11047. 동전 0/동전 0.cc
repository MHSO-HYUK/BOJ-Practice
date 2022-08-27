#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int k, vector<int> p, int numcoin) {
	/*
		11047 동전 0
		N 종류의 동전 -> 가치의 합을 K로
		동전의 갯수는 최소로 구하는 프로그램
	*/
	int answer = 0;
	for (int i = numcoin-1; i >= 0; i --){
		answer += k / p[i];
		k = k % p[i];
	}
	return answer;
}
int main() {
	int n, k; cin >> n >> k;
	vector <int> coin;

	int numcoin = 0;
	for (int i = 0; i < n; i++) {
		int price;
		cin >> price;
		if (price > k) break;
		coin.push_back(price);
		numcoin += 1;
	}
	cout << solution(k, coin, numcoin);
	return 0;
}