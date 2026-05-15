#include <vector>
#include <queue>

using namespace std;

int solution(int N, vector<vector<int>> road, int K) {

    vector<vector<pair<int, int>>> graph(N + 1);

    for (int i = 0; i < road.size(); i++) {
        int a = road[i][0];
        int b = road[i][1];
        int c = road[i][2];

        graph[a].push_back({b, c});
        graph[b].push_back({a, c});
    }

    vector<int> dist(N + 1, 987654321);
    dist[1] = 0;

    priority_queue<
        pair<int, int>,
        vector<pair<int, int>>,
        greater<pair<int, int>>
    > pq;

    pq.push({0, 1});

    while (!pq.empty()) {

        int curDist = pq.top().first;
        int cur = pq.top().second;
        pq.pop();

        if (curDist > dist[cur]) continue;

        for (auto nextInfo : graph[cur]) {

            int next = nextInfo.first;
            int cost = nextInfo.second;

            if (dist[next] > dist[cur] + cost) {

                dist[next] = dist[cur] + cost;
                pq.push({dist[next], next});
            }
        }
    }

    int answer = 0;

    for (int i = 1; i <= N; i++) {
        if (dist[i] <= K) {
            answer++;
        }
    }

    return answer;
}