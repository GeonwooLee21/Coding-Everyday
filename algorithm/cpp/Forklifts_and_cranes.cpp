#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<string> storage, vector<string> requests) {
    int answer = 0;

    int row = storage.size();
    int col = storage[0].size();
    vector<vector<char>> padded_storage(row+2, vector<char>(col+2, '\0'));
    for (int i = 1; i <= row; i++) {
        for (int j = 1; j <= col; j++) {
            padded_storage[i][j] = storage[i-1][j-1];
        }
    }

    for (int i = 0; i < requests.size(); i++) {
        char target;
        if (requests[i].size() == 1) { // 알파벳 하나로만 출고 요청이 들어온 경우
            target = requests[i][0];

            vector<vector<bool>> visited(row + 2, vector<bool>(col + 2, false));
            queue<pair<int, int>> q;

            // (0,0) 시작
            q.push({0, 0});
            visited[0][0] = true;

            int dx[4] = {-1, 1, 0, 0};
            int dy[4] = {0, 0, -1, 1};

            while (!q.empty()) {
                int x = q.front().first;
                int y = q.front().second;
                q.pop();

                for (int d = 0; d < 4; d++) {
                    int nx = x + dx[d];
                    int ny = y + dy[d];

                    // 범위 체크
                    if (nx < 0 || nx >= row + 2 || ny < 0 || ny >= col + 2)
                        continue;

                    // 이미 방문
                    if (visited[nx][ny])
                        continue;

                    // 빈 공간이면 BFS 계속
                    if (padded_storage[nx][ny] == '\0') {
                        visited[nx][ny] = true;
                        q.push({nx, ny});
                    }
                }
            }

            // BFS 완료 후, 방문한 칸 주변의 target 제거
            vector<pair<int, int>> remove_list;

            for (int x = 0; x < row + 2; x++) {
                for (int y = 0; y < col + 2; y++) {
                    if (!visited[x][y])
                        continue;

                    for (int d = 0; d < 4; d++) {
                        int nx = x + dx[d];
                        int ny = y + dy[d];

                        if (nx < 0 || nx >= row + 2 || ny < 0 || ny >= col + 2)
                            continue;

                        if (padded_storage[nx][ny] == target) {
                            remove_list.push_back({nx, ny});
                        }
                    }
                }
            }

            // 실제 제거
            for (auto [x, y] : remove_list) {
                padded_storage[x][y] = '\0';
            }
        }
        else if (requests[i].size() == 2) { // 알파벳이 두 번 반복되어 출고 요청이 들어온 경우
            target = requests[i][0];
            for (int i = 1; i <= row; i++) {
                for (int j = 1; j <= col; j++) {
                    if (target == padded_storage[i][j]) {
                        padded_storage[i][j] = '\0';
                    }
                }
            }
        }
    }

    for (int i = 1; i <= row; i++) {
        for (int j = 1; j <= col; j++) {
            if (padded_storage[i][j] != '\0') {
                answer++;
            }
        }
    }

    return answer;
}