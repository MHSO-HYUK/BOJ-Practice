#include <iostream>
#include <vector>
#include <stack>
#include <string>
using namespace std;
stack <char> v;
int solution(string s){
    for(char c : s){
        if(!v.empty()){
            if(v.top() == c) v.pop();
             else v.push(c);
        }
        else v.push(c);
    }
    if(v.empty()) return 1;
    return 0;
}