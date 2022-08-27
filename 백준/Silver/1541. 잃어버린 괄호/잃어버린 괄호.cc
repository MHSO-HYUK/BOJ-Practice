#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

int solution(string line) {
	/*
		1541 잃어버린 괄호 
		괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
	*/
	istringstream ss(line);
	string stringbuffer;
	vector <string> splited;
	while (getline(ss, stringbuffer, '-')) {
		splited.push_back(stringbuffer);
	}

	vector <int> num;
	for (string s : splited) {
		int eq = 0;
		istringstream ss(s);
		string stringbuffer;
		vector <string> insideSplited;
		while (getline(ss, stringbuffer, '+')) {
			insideSplited.push_back(stringbuffer);
		}
		for (string ins : insideSplited) {
			eq += stoi(ins);
		}
		num.push_back(eq);
	}
	int answer = 2*num[0];
	for (int i : num) {
		answer -= i;
	}
	return answer;
}

int main() {
	string line;
	cin >> line;
	cout << solution(line);
	return 0;
}