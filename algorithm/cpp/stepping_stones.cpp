#include <vector>
#include <deque>

using namespace std;

int solution(vector<int> stones, int k) {
    int answer = 0;

    int n = stones.size();
    vector<int> max_in_sec(n-k+1, 0);

    deque<int> dq;
    int j = 0;
    for (int i = 0; i < n; i++) {
        while (!dq.empty() && stones[i] > stones[dq.back()]) {
            dq.pop_back();
        }
        dq.push_back(i);

        if (dq.front() < i - k + 1) {
            dq.pop_front();
        }

        if (i > k-2) {
            max_in_sec[j++] = stones[dq.front()];
        }
    }

    int min = 200000001;
    for (int i = 0; i < n-k+1; i++)
        if (max_in_sec[i] < min)
            min = max_in_sec[i];

    answer = min;

    return answer;
}