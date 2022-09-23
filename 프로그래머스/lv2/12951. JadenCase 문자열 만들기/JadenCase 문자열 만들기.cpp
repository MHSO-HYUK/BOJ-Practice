#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    int len = s.size();
    int weight = 'A' - 'a';
    string answer = "";
    for(int i = 0; i < len; i ++){
        if(i == 0 || isspace(s[i-1])){
            if(islower(s[i])) answer += s[i] + weight;
            else answer += s[i];
        }
        else{
            if(isupper(s[i])) answer += s[i] - weight;
            else answer += s[i];
        }
    }

    return answer;
}