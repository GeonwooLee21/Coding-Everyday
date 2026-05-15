#include <vector>
#include <queue>

using namespace std;

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;

    vector<vector<int>> network(n+1);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (computers[i][j] == 1) {
                int u = i+1;
                int v = j+1;
                network[u].push_back(v);
                network[v].push_back(u);
            }
        }
    }

    queue<int> q;
    vector<bool> visited(n + 1, false);
    for (int c = 1; c <= n; c++) {
        if (!visited[c]) {
            q.push(c);                          // 시작 정점
            visited[c] = true;

            while (!q.empty()) {                // 큐가 빌 때까지
                int cur = q.front(); q.pop();   // 현재 정점 꺼내기

                for (int next : network[cur]) { // 이웃 순회
                    if (!visited[next]) {
                        visited[next] = true;
                        q.push(next);           // 아직 안 간 곳만 큐에 추가
                    }
                }
            }

            answer++;
        }
    }

    return answer;
}