#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
vector<int> v;

string solution(string s) {
    int len = s.size();
    bool flag = true;
    int temp = 0;
    int idx = 0;
    while(idx <= len){
        if(s[idx] == ' ' || idx == len){
            if(flag) v.push_back(temp);
            else v.push_back(-temp);
            temp = 0;
            flag = true;
        }
        else if(s[idx] == '-'){
            flag = false;
        }
        else{
            temp = 10 * temp + (s[idx] - '0');
        }    
        idx++;
    }
    int maxima = *max_element(v.begin(), v.end());
    int minima = *min_element(v.begin(), v.end());
    string answer = to_string(minima) + " " + to_string(maxima);
    return answer;
}