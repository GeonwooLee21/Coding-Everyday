#include <unordered_set>
using namespace std;

int solution(int N, int number) {
    unordered_set<int> dp[9];
    
    for (int k = 1; k <= 8; k++) {
        // 1. dp[k] 초기값 넣기 (N을 k번 이어붙인 숫자)
        
        // 2. a + b = k 인 모든 쌍에 대해
        for (int a = 1; a < k; a++) {
            int b = k - a;
            // dp[a]의 원소 x, dp[b]의 원소 y에 대해
            // 사칙연산 결과를 dp[k]에 insert
        }
        
        // 3. dp[k]에 number가 있으면 k 반환
    }
    
    return -1;
}