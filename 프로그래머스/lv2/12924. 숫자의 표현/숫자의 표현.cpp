#include <string>
#include <vector>

using namespace std;


int solution(int n) {
    int answer = 0;
    
    int now = 3;
    int w = 2;
    while(true){
        if (n - now >= 0){
            if((n - now) % w == 0){
            answer ++;
            }
        }
        else break; 
        w++;
        now += w;
    }
    
    return answer + 1;
}