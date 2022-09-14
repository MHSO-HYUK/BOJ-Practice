#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>
using namespace std;
int seq[40001];
vector<int> v;

int main() {
	int n; cin >> n;
	for (int i = 1; i <= n; i++) cin >> seq[i];
	
	for (int i = 1; i <= n; i++) {
		if (v.size() == 0 || v.back() < seq[i]) v.push_back(seq[i]);
		else {
			int pos = lower_bound(v.begin(), v.end(), seq[i]) - v.begin();
			v[pos] = seq[i];
		}
	}
	cout << v.size();
}