#include <string>
#include <vector>

using namespace std;

// 좌표 인덱싱에 유의하기!
int solution(int x, int y, vector<vector<int>> puddles_idx) {
    int answer = 0;
    
    vector<vector<int>>       P(y + 1, vector<int>(x + 1, 0));
    vector<vector<int>> puddles(y + 1, vector<int>(x + 1, 0));

    int puddles_x, puddles_y;
    for (int i = 0; i < puddles_idx.size(); i++) {
        puddles_x = puddles_idx[i][0];
        puddles_y = puddles_idx[i][1];

        puddles[puddles_y][puddles_x] = 1;
    }

    for (int i = 1; i <= y; i++) {
        for (int j = 1; j<= x; j++) {
            if (i == 1 && j == 1)
                P[i][j] = 1;
            else if (puddles[i][j])
                P[i][j] = 0;
            else
                P[i][j] = (P[i-1][j] + P[i][j-1]) % 1000000007;        
        }
    }

    // for (int i = 1; i <= y; i++) {
    //     for (int j = 1; j <= x; j++) {
    //         printf("%4d", P[i][j]);
    //     }
    //     printf("\n");
    // }
    
    answer = P[y][x];
    
    return answer;
}

int main() {
    vector<vector<int>> puddles_idx = {{4, 1}};

    printf("%d\n", solution(4, 3, puddles_idx));

    return 0;
}