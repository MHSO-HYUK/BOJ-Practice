#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>

using namespace std;

int solution(vector <pair<int, int>> brand, vector <pair<int, int>> reverse_brand, int n) {
	/*
		1049 기타줄
		N개의 기타줄이 끊어짐 - 6개 패키지 혹은 낱개 구입 가능
		-> 적어도 N개를 사기 위해 필요한 돈의 수를 최소로 할 수 있는 프로그램
	*/
	sort(brand.begin(), brand.end()); // 패키지 가격이 가장 싼 순서대로 정렬
	sort(reverse_brand.begin(), reverse_brand.end()); // each 가격이 가장 싼 순서대로 정렬
	int answer =min( brand[0].first, reverse_brand[0].first * 6 )* (n / 6);
	answer += min(reverse_brand[0].first * (n % 6), brand[0].first); 
	return answer;
}

int main() {
	int n, m; cin >> n >> m;
	vector <pair <int, int>> brand;
	vector <pair <int, int>>reverse_brand;
	for (int i = 0; i < m; i++) {
		int pack, each; cin >> pack >> each;
		brand.push_back({pack, each});
		reverse_brand.push_back({ each, pack });
	}
	cout << solution(brand, reverse_brand, n);
}