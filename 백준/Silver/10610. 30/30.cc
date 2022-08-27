#include <iostream> // 표준 입출력
#include <vector> // 벡터 (STACK)
#include <algorithm> // 정렬 
#include <string>  // 문자열
#include <sstream> // 문자열 분리에 요구되는 라이브러리
#include <numeric>

using namespace std;

string solution(vector<int> number) {
	/*
		10610 30
		길에서 찾은 N이라는 수를 섞어 30의 배수가 되는 가장 큰 수를 만들자
	*/
	sort(number.begin(), number.end(), greater<>());
	if (number.back() != 0 || accumulate(number.begin(), number.end(), 0) % 3 != 0) {
		return "-1";
	}
	string answer;
	for (int i : number) {
		answer.append(to_string(i));
	}
	return answer;
}

int main() {
	string  n; cin >> n;
	vector <int> number;
	for (char i : n) {
		number.push_back(int(i) - '0');
	}
	cout << solution(number);
}