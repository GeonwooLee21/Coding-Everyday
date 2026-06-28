#include <string>
#include <vector>

using namespace std;

long find_min(int idx, vector<long> &ballon, vector<long> &previous_min) {
    long min = 100000000001;
    if (idx == -1) {
        return min;
    }
    else if (idx == ballon.size()) {
        return min;
    }
    else {
        if (ballon[idx] < previous_min[idx])
            return ballon[idx];
        else
            return previous_min[idx];
    }
}

int solution(vector<int> a) {
    int answer = 0;

    int n = a.size();
    vector<long> ballon(n, 0);
    for (int i = 0; i < n; i++) {
        ballon[i] = a[i];
    }
    vector<long> left_side_min(n, 0);
    vector<long> right_side_min(n, 0);

    for (int i = 0; i < n; i++) {
        left_side_min[i] = find_min(i-1, ballon, left_side_min);
    }
    for (int i = n-1; i >= 0; i--) {
        right_side_min[i] = find_min(i+1, ballon, right_side_min);
    }

    for (int i = 0; i < n; i++) {
        bool survival = false;
        if (left_side_min[i] < a[i] && right_side_min[i] < a[i])
            survival = false;
        else
            survival = true;

        if (survival)
            answer++;
    }

    return answer;
}