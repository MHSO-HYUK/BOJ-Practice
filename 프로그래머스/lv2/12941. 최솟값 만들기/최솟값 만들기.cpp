#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;

int solution(vector<int> A, vector<int> B)
{
    int answer = 0;
    sort(A.begin(), A.end(), greater<>());
    sort(B.begin(), B.end(), less<>());
    int len = A.size();
    for(int i = 0; i < len; i ++){
        answer += A[i] * B[i];
    }
    
    
    

    return answer;
}