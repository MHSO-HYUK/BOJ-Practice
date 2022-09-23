#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int cacheSize, vector<string> cities) {
    vector<string> cachename;
    vector<int> cachedegree;
    
    int answer = 0;
    int len = cities.size();
    if(cacheSize == 0) return 5 * len;
    
    for(int i = 0; i < len; i ++){
        string now = cities[i];
        for(int k = 0; k < now.size(); k ++){
            if(isupper(now[k])) now[k] = now[k] - ('A' - 'a');
        }
        
        if(cachename.size() < cacheSize){ // 아직 덜 찼음
            if(find(cachename.begin(), cachename.end(), now) == cachename.end()){ // cache에 없음
                cachename.push_back(now);
                cachedegree.push_back(0);
                answer += 5;
            }
            else{ // cache에 있음
                int idx = find(cachename.begin(), cachename.end(), now) - cachename.begin();
                cachedegree[idx] = 0;
                answer += 1;
            }
        } 
        else{ // 꽉 찼음
            if(find(cachename.begin(), cachename.end(), now) == cachename.end()){ // cache에 없음
                int idx = max_element(cachedegree.begin(), cachedegree.end()) - cachedegree.begin();
                cachename[idx] = now;
                cachedegree[idx] = 0;
                answer += 5;
            }
            else{ // cache에 있음
                int idx = find(cachename.begin(), cachename.end(), now) - cachename.begin();
                cachedegree[idx] = 0;
                answer += 1;
            }
        }
        for(int i = 0; i < cachedegree.size(); i ++) cachedegree[i] ++;
        
    }
    
    return answer;
}