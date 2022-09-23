#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    int len = words.size();
    vector<int> answer;

    vector<string> temp;
    for(int i = 0; i < len/n ; i ++){
        for(int j = 0; j < n ; j ++){
            string now = words[n*i + j];
            if(!temp.empty() && temp.back().back() != now[0]) return {j+1, i+1}; 
            if(find(temp.begin(), temp.end(), now) == temp.end()) temp.push_back(now);
            else {
                answer = {j+1, i+1};
                return answer;
            }
        }
    }
    answer = {0, 0};
    return answer;
}