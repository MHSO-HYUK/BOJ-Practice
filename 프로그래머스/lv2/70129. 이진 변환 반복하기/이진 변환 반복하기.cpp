#include <iostream>
#include <string>
#include <vector>

using namespace std;

pair<int, string> removeZero(string s){
    int len = s.size();
    int ret = 0;
    string r = "";
    for(int i = 0; i < len; i ++){
        if(s[i] == '0') ret++;
    }
    int afterlen = len - ret;
    while(afterlen != 0){
        r = to_string(afterlen % 2) + r; 
        afterlen /= 2;
    }
    return {ret, r};
}



vector<int> solution(string s) {
    int a = 0;
    int b = 0;
    pair<int, string> now = {-1, ""};
    while(true){
        now = removeZero(s);
        a++;
        b += now.first;
        s = now.second;
        if(s == "1") break;
        
    }
    
    vector<int> answer = {a, b};
    return answer;
}