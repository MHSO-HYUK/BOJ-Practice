#include <string>
#include <vector>
#include <iostream>

using namespace std;
/*
a b     A B     a*A + b * C / a*B + b*D
c d     C D     c*A + d * C / c*B + d*D
*/

vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
    vector<vector<int>> answer;
    vector<int> a(arr2[0].size());
    for(int i = 0; i < arr1.size(); i ++) answer.push_back(a);
    
    for(int i = 0; i < arr1.size(); i ++){
        for(int j = 0; j < arr2[0].size(); j ++){
            //cout << i << " " << j << endl;
            for(int k = 0; k < arr2.size(); k ++){
                //cout << arr1[i][k] << " " << arr2[k][j] << endl;
                answer[i][j] += arr1[i][k] * arr2[k][j];
            }
        }
    }
    
    return answer;
}





