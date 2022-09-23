#include <string>
#include <vector>
#include <numeric>
using namespace std;

int solution(vector<int> arr) {
    int answer = 0;
    int len = arr.size();
    int now = arr[0];
    for(int i = 0; i < len - 1; i ++){
        now = lcm(now, arr[i+1]);
    }
    return now;
}