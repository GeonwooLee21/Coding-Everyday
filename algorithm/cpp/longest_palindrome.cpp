#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solution(string s)
{
    int answer=0;

    vector<int> palindrome_length;
    // 홀수 펠린드롬 체크
    for (int i = 1; i < s.size()-1; i++) {
        int k;
        for (k = 1; i-k >= 0 && i+k < s.size(); k++) {
            if (s[i-k] == s[i+k]) {
                continue;
            }
            else {
                break;
            }
        }

        // 펠린드롬 길이 저장
        if (k == 1) {
            palindrome_length.push_back(1);
        }
        else {
            palindrome_length.push_back(2*(k-1)+1);
        }
    }

    // 짝수 펠린드롬 체크
    for (int i = 0; i < s.size()-1; i++) {
        if (s[i] == s[i+1]) {
            int k;
            for (k = 1; i-k >= 0 && i+1+k < s.size(); k++) {
                if (s[i-k] == s[i+1+k]) {
                    continue;
                }
                else {
                    break;
                }
            }

            // 펠린드롬 길이 저장
            if (k == 1) {
                palindrome_length.push_back(2);
            }
            else {
            palindrome_length.push_back(2*(k-1)+2);
            }
        }
        else {
            continue;
        }
    }

    int max = 0;
    if (palindrome_length.empty()) {
        answer = 1;
    }
    else {
        for (int i = 0; i < palindrome_length.size(); i++) {
            if (palindrome_length[i] > max) {
                max = palindrome_length[i];
            }
        }
        answer = max;
    }

    return answer;
}