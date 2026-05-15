#include <vector>
#include <queue>
using namespace std;

int solution(int n, vector<vector<int>> edge) {
    int answer = 0;

    vector<vector<int>> adj(n+1);
    for (int i = 0; i < int(edge.size()); i++) {
        int u = edge[i][0];
        int v = edge[i][1];
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    queue<int> q;
    vector<bool> visited(n + 1, false);
    vector<int> distance(n + 1, 0);

    q.push(1);                          // 시작 정점 1로 고정
    visited[1] = true;

    while (!q.empty()) {                  // 큐가 빌 때까지
        int cur = q.front(); q.pop();     // 현재 정점 꺼내기

        for (int next : adj[cur]) {       // 이웃 순회
            if (!visited[next]) {
                distance[next] = distance[cur] + 1;
                visited[next] = true;
                q.push(next);             // 아직 안 간 곳만 큐에 추가
            }
        }
    }

    int max_distance = 0;
    for (int i = 2; i <= n; i++)
        if (distance[i] > max_distance)
            max_distance = distance[i];

    for (int i = 2; i <= n; i++)
        if (distance[i] == max_distance)
            answer++;

    return answer;
}