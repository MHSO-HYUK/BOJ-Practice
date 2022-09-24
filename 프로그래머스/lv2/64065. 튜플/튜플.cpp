#include <string>
#include <vector>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <map>

using namespace std;
map<int, int> dict;

vector<int> solution(string s) {
    int temp = 0;
    for(int i = 0; i < s.size(); i ++){
        if(isdigit(s[i])){
            if(!isdigit(s[i+1])) {
                temp = 10*temp + (s[i] - '0');
                if(dict.find(temp) == dict.end()) dict.insert({temp, 1});
                else dict[temp] += 1;
                temp = 0;
            }
            else temp = 10 * temp + (s[i] - '0');
        }
        else continue;
    }
    
    map<int, int> :: iterator i;
    vector<pair<int, int>> v;
    for (i = dict.begin(); i != dict.end(); i ++){
        //cout << i->first << " " << i->second << endl;
        v.push_back({-i->second, i->first});
    }
    
    sort(v.begin(), v.end());
    vector<int> answer;
    for(int i = 0; i < v.size(); i ++) answer.push_back(v[i].second);
    return answer;
}