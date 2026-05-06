#include <vector>
#include <queue>

using namespace std;

int solution(int n, vector<vector<int>> results) {
    int ranked_player = 0;

    vector<vector<int>> w2l_adj(n+1);
    vector<vector<int>> l2w_adj(n+1);
    for (int i = 0; i < int(results.size()); i++) {
        int u = results[i][0];
        int v = results[i][1];
        w2l_adj[u].push_back(v);
        l2w_adj[v].push_back(u);
    }

    queue<int> q;
    vector<bool> visited(n + 1, false);
    vector<int> win(n + 1, 0);
    for (int p = 1; p <= n; p++) {
        q.push(p);                          // 시작 정점
        // visited[p] = true;

        while (!q.empty()) {                // 큐가 빌 때까지
            int cur = q.front(); q.pop();   // 현재 정점 꺼내기

            for (int next : w2l_adj[cur]) { // 이웃 순회
                if (!visited[next]) {
                    visited[next] = true;
                    q.push(next);           // 아직 안 간 곳만 큐에 추가
                }
            }
        }

        for (int i = 1; i <= n; i++) {
            if (visited[i]) {
                win[p]++;
            }
        }

        visited.assign(n + 1, false);
    }

    vector<int> lose(n + 1, 0);
    for (int p = 1; p <= n; p++) {
        q.push(p);
        // visited[p] = true;

        while (!q.empty()) {
            int cur = q.front(); q.pop();

            for (int next : l2w_adj[cur]) {
                if (!visited[next]) {
                    visited[next] = true;
                    q.push(next);
                }
            }
        }

        for (int i = 1; i <= n; i++) {
            if (visited[i]) {
                lose[p]++;
            }
        }

        visited.assign(n + 1, false);
    }

    for (int p = 1; p <= n; p++) {
        if ((win[p]+lose[p]) == (n-1)) {
            ranked_player++;
        }
    }

    return ranked_player;
}