#include <vector>
#include <queue>

using namespace std;

int solution(vector<vector<int>> rectangle, int characterX, int characterY, int itemX, int itemY) {
    int answer = 0;
    
    // x2 Scaling
    characterX = 2*characterX;
    characterY = 2*characterY;
    itemX = 2*itemX;
    itemY = 2*itemY;
    for (int i = 0; i < rectangle.size(); i++) {
        for (int j = 0; j < 4; j++) {
            rectangle[i][j] = 2*rectangle[i][j];
        }
    }

    int max_x = 0;
    int max_y = 0;
    for (int i = 0; i < rectangle.size(); i++) {
        if (rectangle[i][2] > max_x) max_x = rectangle[i][2];
        if (rectangle[i][3] > max_y) max_y = rectangle[i][3];
    }

    // Draw map
    vector<vector<int>> map(max_x+1, vector<int>(max_y+1, 0));
    for (int i = 0; i < rectangle.size(); i++) { // Total rectangle
        for (int x = rectangle[i][0]; x <= rectangle[i][2]; x++) {
            for (int y = rectangle[i][1]; y <= rectangle[i][3]; y++) {
                if (map[x][y] == -1) {
                    continue;
                }
                else {
                    if (x == rectangle[i][0] || x == rectangle[i][2] || y == rectangle[i][1] || y == rectangle[i][3]) { // 윤곽선인 경우
                        map[x][y] = 1;
                    }
                    else { // 사각형 내부인 경우
                        map[x][y] = -1;
                    }
                }
            }
        }
    }   

    // Set Character
    vector<vector<int>> dist(max_x+1, vector<int>(max_y+1, 0));

    queue<pair<int, int>> location;
    location.push({characterX, characterY});
    map[characterX][characterY] = -1;

    // BFS
    pair<int, int> current = location.front();
    int current_row = current.first;
    int current_col = current.second;
    location.pop();
    do {
        // down
        if (current_row+1 <= max_x && map[current_row+1][current_col] != -1 && map[current_row+1][current_col] != 0) {
            location.push({current_row+1, current_col});
            map[current_row+1][current_col] = -1;
            if (dist[current_row+1][current_col] == 0)
                dist[current_row+1][current_col] = dist[current_row][current_col]+1;
        }

        // left
        if (current_col-1 >= 0 && map[current_row][current_col-1] != -1 && map[current_row][current_col-1] != 0) {
            location.push({current_row, current_col-1});
            map[current_row][current_col-1] = -1;
            if (dist[current_row][current_col-1] == 0)
                dist[current_row][current_col-1] = dist[current_row][current_col]+1;
        }

        // up
        if (current_row-1 >= 0 && map[current_row-1][current_col] != -1 && map[current_row-1][current_col] != 0) {
            location.push({current_row-1, current_col});
            map[current_row-1][current_col] = -1;
            if (dist[current_row-1][current_col] == 0)
                dist[current_row-1][current_col] = dist[current_row][current_col]+1;
        }

        // right
        if (current_col+1 <= max_y && map[current_row][current_col+1] != -1 && map[current_row][current_col+1] != 0) {
            location.push({current_row, current_col+1});
            map[current_row][current_col+1] = -1;
            if (dist[current_row][current_col+1] == 0)
                dist[current_row][current_col+1] = dist[current_row][current_col]+1;
        }
        
        if (location.empty())
            break;

        current = location.front();
        current_row = current.first;
        current_col = current.second;

        location.pop();
    } while (!(current_row == itemX && current_col == itemY));
    
    answer = dist[itemX][itemY]/2;    

    return answer;
}