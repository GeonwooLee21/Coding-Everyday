#include <string>
#include <vector>

using namespace std;

long long solution(int cap, int n, vector<int> deliveries, vector<int> pickups) {
    long long answer = 0;

    int d = n - 1; // 가장 먼 배달 필요 집
    int p = n - 1; // 가장 먼 수거 필요 집

    while (d >= 0 || p >= 0) {
        // 배달이 필요한 가장 먼 집 찾기
        while (d >= 0 && deliveries[d] == 0) {
            d--;
        }

        // 수거가 필요한 가장 먼 집 찾기
        while (p >= 0 && pickups[p] == 0) {
            p--;
        }

        // 둘 다 끝났으면 종료
        if (d < 0 && p < 0) {
            break;
        }

        // 이번 트립에서 가야 하는 가장 먼 거리
        int farthest = max(d, p) + 1;
        answer += 2LL * farthest;

        // 이번 트립에서 cap개만큼 배달 처리
        int box = cap;
        while (d >= 0 && box > 0) {
            if (deliveries[d] <= box) {
                box -= deliveries[d];
                deliveries[d] = 0;
                d--;
            } else {
                deliveries[d] -= box;
                box = 0;
            }
        }

        // 이번 트립에서 cap개만큼 수거 처리
        box = cap;
        while (p >= 0 && box > 0) {
            if (pickups[p] <= box) {
                box -= pickups[p];
                pickups[p] = 0;
                p--;
            } else {
                pickups[p] -= box;
                box = 0;
            }
        }
    }

    return answer;
}