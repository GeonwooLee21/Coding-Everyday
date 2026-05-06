#include <string>
#include <vector>

using namespace std;
#define INF 999999999

long long solution(vector<vector<int>> matrix_sizes) {
    long long answer = 0;
    
    int n = matrix_sizes.size();
    int diagonal = n;

    vector<int> m(n+1);
    for (int i = 0; i < n; i++) {
        m[i] = matrix_sizes[i][0];
    }
    m[n] = matrix_sizes[n-1][1];

    // printf("%d\n", n);
    // for (int i = 0; i <= n; i++) {
    //     printf("%d ", m[i]);
    // }
    // printf("\n");
    
    vector<vector<long long>> M(n + 1, vector<long long>(n + 1, INF));
    for (int i = 1; i <= n; i++)
	    M[i][i] = 0;

    for (int d = 0; d < diagonal; d++) {
	    for (int i = 1; i <= n-d; i++) {
			int j = i+d;
			int min = INF;
			for (int k = i; k <= j-1; k++) {
				if (M[i][k] + M[k+1][j] + m[i-1]*m[k]*m[j] < min) {
					M[i][j] = M[i][k] + M[k+1][j] + m[i-1]*m[k]*m[j];
					min = M[i][j];
                }
            }
        }
    }
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (M[i][j] == INF)
                printf("%5lld ", 0);
            else 
                printf("%5lld ", M[i][j]);
        }
        printf("\n");
    }

    answer = M[1][n];
    
    return answer;
}

int main() {
    vector<vector<int>> matrix_sizes = {{5, 3}, {3, 10}, {10, 6}};
        
    printf("%d\n", solution(matrix_sizes));

    return 0;
}