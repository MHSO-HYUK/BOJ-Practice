#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

int solution(int n) {
	/* 2839 설탕 배달
		 N 만큼 배달
		3과 5 봉지가 있음
		 최대한 적은 봉지를 들고가려함
	*/
	int numfive = n/5; // 5 봉지 수
	int numthree = (n - numfive * 5) / 3; // 3 봉지 수
	while (true) {
		int total = numfive * 5 + numthree * 3;
		if (total == n) {
			return numfive + numthree;
		}
		else {
			numfive -= 1;
			if (numfive < 0) {
				return -1;
			}
			numthree = (n - numfive*5) / 3;
		}
	}
}
int main() {
	int n; cin >> n;
	cout << solution(n);
    return 0 ;
}