#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(int n, int s) {
    vector<int> answer;
    if(n > s){
        answer.push_back(-1);
        return answer;
    }
    
    int num = 0;
    int mid;
    while(num != n){
        mid = s/(n-num);
        answer.push_back(mid);
        num ++;
        s -= mid;
    }
    sort(answer.begin(), answer.end());
    return answer;
}