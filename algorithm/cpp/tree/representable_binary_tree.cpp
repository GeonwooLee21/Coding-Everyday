#include <vector>
#include <cmath>

using namespace std;

void make_binary(long long number, vector<int> &binary) {
    // 주어진 정수 이진수 변환
    int size = 0;
    while (number >= (1LL << size)) {
        size++;
    }

    for (int i = size-1; i >= 0; i--) {
        if (number - (1LL << i) < 0) {
            binary.push_back(0);
        }
        else {
            binary.push_back(1);
            number -= (1LL << i);
        }
    }

    // binary의 크기를 2^k - 1로 맞추기 위해 적절한 k 탐색
    int k = 0;
    while (1) {
        if (binary.size() == (1LL << k) - 1) {
            return;
        }
        else if (binary.size() < (1LL << k) - 1) {
            break;
        }
        else if (binary.size() > (1LL << k) - 1) {
            k++;
        }
    }

    // binary의 크기를 2^k - 1로 맞추기 위해 MSB를 0으로 패딩
    while (binary.size() != (1LL << k) - 1) {
        binary.insert(binary.begin(), 0);
    }
}

int flag = 1;
void validate(int st, int fi, int root, vector<int> binary) {
    if (st == fi) {
        return;
    }
    else {
        if (binary[root] == 1) {
            validate(st, root-1, (st + (root-1))/2, binary);
            validate(root+1, fi, ((root+1) + fi)/2, binary);
        }
        else if (binary[root] == 0) {
            int left_subroot = (st + (root-1))/2;
            if (binary[left_subroot] == 0) {
                validate(st, root-1, (st + (root-1))/2, binary);
            }
            else if (binary[left_subroot] == 1) {
                flag = 0;
            }
            
            int right_subroot = ((root+1) + fi)/2;
            if (binary[right_subroot] == 0) {
                validate(root+1, fi, ((root+1) + fi)/2, binary);
            }
            else if (binary[right_subroot] == 1) {
                flag = 0;
            }
        }
    }
}

vector<int> solution(vector<long long> numbers) {
    vector<int> answer;

    vector<int> binary(0);
    for (int i = 0; i < numbers.size(); i++) {
        make_binary(numbers[i], binary);
        flag = 1;
        validate(0, binary.size()-1, (binary.size()-1)/2, binary);
        answer.push_back(flag);
        binary.clear();
    }

    return answer;
}