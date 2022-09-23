#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int garo = 3;
    int sero = 3;
    int total = brown + yellow;
    while(true){
        cout << garo << " " << sero << endl;
        if (garo * sero == total &&  (garo-2) * (sero-2) == yellow){
            break;
        }
        if(garo * sero < total) {
            garo ++;
            sero ++;
        }
        else sero--;
    }
    
    answer = {garo, sero};
    return answer;
}