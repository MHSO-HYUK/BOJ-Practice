#include <string>
#include <vector>
#include <iostream>
#include <stack>

using namespace std;

int solution(string s) {
    int answer = 0;
    string temp = s;
    int len = temp.size();
    int idx = 0;
    vector<pair<int, int>> dp(3);

    for(int i = 0; i < len; i ++){
        if(temp[i] == '[') dp[0].first +=1;
        if(temp[i] == ']') dp[0].second += 1;
        if(temp[i] == '{') dp[1].first += 1;
        if(temp[i] == '}') dp[1].second += 1;
        if(temp[i] == '(') dp[2].first += 1;
        if(temp[i] == ')') dp[2].second += 1;
    }
    for(int i = 0; i < 3; i ++){
        if(dp[i].first != dp[i].second) return 0;
    }
    
    
    while(true){
        stack <char> stack;
        bool flag = true;
        for(int i = idx; i < idx+len; i++){
            int now = i % len;
            if(stack.empty()) stack.push(temp[now]);
            else{
                if(temp[now] == '[' || temp[now] == '{' || temp[now] == '('){
                    stack.push(temp[now]);
                }
                else{
                    char top = stack.top();
                    if(temp[now] == ']'){
                        if(top == '[') stack.pop();
                    } 
                    if(temp[now] == '}'){
                        if(top == '{') stack.pop();
                    } 
                    if(temp[now] == ')'){
                        if(top == '(') stack.pop();
                    } 
                }
            }
        }            
        if(stack.empty()) answer ++;
        //cout <<idx << " " << len << " " << flag << endl;
        idx ++;
        if(idx == len) break;
    }
    
    return answer;
}