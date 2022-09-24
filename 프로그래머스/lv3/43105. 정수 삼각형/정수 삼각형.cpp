#include <string>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> triangle) {
    int answer = 0;
    int h = triangle.size();
    for(int i = 1; i < h; i++) {
        for(int j = 0; j <= i; j ++){
            if(j == 0) triangle[i][j] += triangle[i-1][j];
            else if(j == i) triangle[i][j] += triangle[i-1][j-1];
            else triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j]);
        }   
    }
    
    for(int i = 0; i < h; i ++){
        answer = max(answer, triangle[h-1][i]);
    }

    return answer;
}