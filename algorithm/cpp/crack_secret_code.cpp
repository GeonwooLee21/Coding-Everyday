#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<vector<int>> q, vector<int> ans) {
    int answer = 0;

    vector<int> data (n, 0);
    for (int i = 0; i < n; i++) {
        data[i] = i+1;
    }
    int r = 5; // 고를 원소 개수

    // data와 같은 크기의 flag 배열 생성 
    // 앞에는 0을 (n-r)개, 뒤에는 1을 r개 채움 -> 사전 순으로 가장 작은 상태 만듦
    vector<int> mask(data.size(), 0);
    for (int i = data.size() - r; i < data.size(); ++i) {
        mask[i] = 1;
    } // mask 상태: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1}

    // mask의 순열을 돌리면서 1이 위치한 인덱스의 data를 뽑아, candidate에 저장
    vector<int> candidate;
    do {
        // 1~n에서 5개 숫자 조합 생성
        for (int i = 0; i < mask.size(); ++i) {
            if (mask[i] == 1) {
                candidate.push_back(data[i]);
            }
        }

        // 생성된 숫자 조합에 대해 m번(q.size())의 시도 결과 전부 검증
        bool valid = true;
        for (int i = 0; i < q.size(); i++) {
            // 공통 원소를 임시로 담을 벡터
            vector<int> intersection_result; 

            // 두 배열(candidate, q[i])의 교집합 구하기
            // back_inserter는 결과를 intersection_result에 push_back 하듯이 채워넣어 줌
            set_intersection(
                candidate.begin(), candidate.end(),
                q[i].begin(), q[i].end(),
                back_inserter(intersection_result)
            );

            // 교집합의 개수가 문제의 조건(ans[i])과 다르면 반복문 종료
            if (intersection_result.size() != ans[i]) {
                valid = false;
                break;
            }
        }

        // 검증 통과하면 카운트
        if (valid) {
            answer++;
        }

        candidate.clear();
    } while (next_permutation(mask.begin(), mask.end()));

    return answer;
}