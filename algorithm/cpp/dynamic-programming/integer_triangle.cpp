#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> triangle) {
    int answer = 0;

    int len = triangle.size();

    for (int i = 1; i < len; i++) {
        for (int j = 0; j <= i; j++) {
            if (j == 0) {
                triangle[i][j] = triangle[i][j] + triangle[i-1][j];
            }
            else if (i == j) {
                triangle[i][j] = triangle[i][j] + triangle[i-1][j-1];
            }
            else {
                int left = triangle[i][j] + triangle[i-1][j-1];
                int right = triangle[i][j] + triangle[i-1][j];
                triangle[i][j] = left > right ? left : right;
            }
        } 
    }

    for (int i = 0; i < len; i++) {
        if (triangle[len-1][i] > answer) {
            answer = triangle[len-1][i];
        } 
    }

    return answer;
}