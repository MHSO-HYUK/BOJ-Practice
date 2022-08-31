#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>

using namespace std;
int solution(int n) {
	/*
		11726 2 *n 타일링
		2*n 크기의 직사각형을 1*2 / 2* 1로 채우는 방법의 수를 구하는 프로그램
	*/
	vector <int> check(n + 1);
	check[1] = 1;
	if (n == 1) return check[1];
	check[2] = 2;
	if (n == 2) return check[2];
	for (int i = 3; i < n+1; i++) {
		check[i] = check[i - 1] + check[i - 2];
		check[i] = check[i] % 10007;
	}
	return check[n];
}


int main() {
	int n; cin >> n;
	cout << solution(n)%10007;
}