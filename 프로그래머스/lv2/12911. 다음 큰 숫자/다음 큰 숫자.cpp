#include <string>
#include <vector>

using namespace std;
int makeBinary(int n){
    int ret = 0;
    while(n != 0){
        if(n%2 == 1) ret ++;
        n /= 2;
    }
    return ret;
}


int solution(int n) {
    int flag = makeBinary(n);
    for(int i = n+1; i < 1000100; i ++){
        if(flag == makeBinary(i)) return i;
    }
}