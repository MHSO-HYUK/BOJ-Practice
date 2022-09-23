#include <string>
#include <vector>
#include <cstring>
#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;
int visit[50001];

int solution(vector<int> people, int limit) {
    int len = people.size();
    memset(visit, 0, sizeof(visit));
    sort(people.begin(), people.end(), greater<>());
    int s = 0;
    int f = len-1;
    int answer = 0;
    while(s <= f){
        if (people[s] + people[f] <= limit){
            s += 1;
            f -= 1;
            answer ++;
        }
        else {
            s += 1;
            answer ++;
        }
    }
    return answer;
}