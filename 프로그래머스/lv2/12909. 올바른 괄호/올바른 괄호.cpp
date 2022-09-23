#include<string>
#include <iostream>

using namespace std;

bool solution(string s)
{
    int len = s.size();
    bool answer = true;
    int left = 0;
    int right = 0;
    
    for(int i = 0; i < len ; i ++){
        if(right > left) {
            answer = false;
            break;
        }
        if(s[i] == '(') left++;
        else right++;
    }
    if(left != right) answer = false;
    return answer;
}