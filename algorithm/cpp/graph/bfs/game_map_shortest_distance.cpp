#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int solution(vector<vector<int>> maps) {
    int n = maps.size() - 1;
    int m = maps[0].size() - 1;
    vector<vector<int>> dist(n+1, vector<int>(m+1, 0));

    queue<pair<int, int>> location;
    location.push({0, 0});
    maps[0][0] = -1;
    dist[0][0] = 1;

    pair<int, int> current = location.front();
    int current_row = current.first;
    int current_col = current.second;
    location.pop();
    do {
        // down
        if (current_row+1 <= n && maps[current_row+1][current_col] != -1 && maps[current_row+1][current_col] != 0) {
            location.push({current_row+1, current_col});
            maps[current_row+1][current_col] = -1;
            if (dist[current_row+1][current_col] == 0)
                dist[current_row+1][current_col] = dist[current_row][current_col]+1;
        }

        // left
        if (current_col-1 >= 0 && maps[current_row][current_col-1] != -1 && maps[current_row][current_col-1] != 0) {
            location.push({current_row, current_col-1});
            maps[current_row][current_col-1] = -1;
            if (dist[current_row][current_col-1] == 0)
                dist[current_row][current_col-1] = dist[current_row][current_col]+1;
        }

        // up
        if (current_row-1 >= 0 && maps[current_row-1][current_col] != -1 && maps[current_row-1][current_col] != 0) {
            location.push({current_row-1, current_col});
            maps[current_row-1][current_col] = -1;
            if (dist[current_row-1][current_col] == 0)
                dist[current_row-1][current_col] = dist[current_row][current_col]+1;
        }

        // right
        if (current_col+1 <= m && maps[current_row][current_col+1] != -1 && maps[current_row][current_col+1] != 0) {
            location.push({current_row, current_col+1});
            maps[current_row][current_col+1] = -1;
            if (dist[current_row][current_col+1] == 0)
                dist[current_row][current_col+1] = dist[current_row][current_col]+1;
        }
        
        if (location.empty())
            break;

        current = location.front();
        current_row = current.first;
        current_col = current.second;

        location.pop();
    } while (!(current_row == n && current_col == m));
    
    if (current_row == n && current_col == m)
        return dist[n][m];
    else
        return -1;
}