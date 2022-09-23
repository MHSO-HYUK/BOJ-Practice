#include <string>
#include <vector>

using namespace std;

long long dp[2001];

long long solution(int n) {
    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 2;
    for(int i = 3; i < n+1; i ++){
        dp[i] = (dp[i-1] + dp[i-2])%1234567;
    }
    return dp[n];
}