#include <string>
#include <vector>
#include <algorithm>
#include <deque>
#include <iostream>

using namespace std;
int INF = 987654321;
vector<int> q;
vector<int> deleted_q;

vector<int> solution(vector<string> operations) {
    vector<int> answer(2);
    int maxima = 0;
    int minima = INF;

    for(string s : operations){
        if(s[0] == 'I'){ // 큐에 주어진 숫자 삽입
            int num = stoi(s.substr(1, sizeof(s)));
            q.push_back(num);
            maxima = *max_element(q.begin(), q.end());
            minima = *min_element(q.begin(), q.end());
        }
        else{
            if(!q.empty()){
                int num = stoi(s.substr(1, sizeof(s)));
                if(num == 1){ // 최댓값 삭제
                    int idx = max_element(q.begin(), q.end()) - q.begin();
                    q.erase(q.begin() + idx);
                }
                else{ // 최소값 삭제
                    int idx = min_element(q.begin(), q.end()) - q.begin();
                    q.erase(q.begin() + idx);
                }
            }
        }
    }
    
    if(q.empty()){
        answer[0] = 0;
        answer[1] = 0;
    }
    else{
        answer[0] = *max_element(q.begin(), q.end());
        answer[1] = *min_element(q.begin(), q.end());
    }
    return answer;
}