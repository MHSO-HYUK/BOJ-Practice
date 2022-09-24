#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    sort(citations.begin(), citations.end());
    int mid = citations.back();
    while(true){
        if(citations.end() - lower_bound(citations.begin(), citations.end(), mid) < mid){
            mid --;
        }
        else {
            answer = mid;
            break;
        }
    }
    return answer;
}