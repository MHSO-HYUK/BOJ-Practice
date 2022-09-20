#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <queue> // 우선순위 큐
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <numeric>
#include <math.h>
#include<cstring>

using namespace std;
int n;
string s, t;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> s >> t;
	int lens = s.size();
	int lent = t.size();
	while (true) {
		
		if (lent == lens) {
			if (t.compare(s) == 0)	cout << 1;
			else cout << 0;
			break;
		}
		
		if (t[lent - 1] ==  'B') {
			t.pop_back();
			reverse(t.begin(), t.end());

		}
		else {
			t.pop_back();
		}

		lent--;
	}
}