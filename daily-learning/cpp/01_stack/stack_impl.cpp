/**
 * 자료구조: Stack (배열 기반)
 * 날짜: 2026-06-28
 */

#include <iostream>
using namespace std;

const int MAX_SIZE = 1000;

class Stack {
private:
    int data[MAX_SIZE];
    int top_idx;

public:
    Stack() {
        // TODO: top_idx 초기화
        top_idx = 0;
    }

    void push(int val) {
        // TODO: 꽉 찼을 때 예외처리 + 삽입
        if (top_idx == MAX_SIZE) {
            throw out_of_range("Stack is Full. You have to pop some data.");
        }
        else {
            data[top_idx++] = val;
        }
    }

    void pop() {
        // TODO: 비었을 때 예외처리 + 제거
        if (top_idx == 0) {
            throw out_of_range("Stack is already Empty.");
        }
        else {
            data[--top_idx] = 0;
        }
    }

    int top() {
        // TODO: 비었을 때 예외처리 + 반환
        if (top_idx == 0) {
            throw out_of_range("Stack is Empty.");
        }
        else {
            return data[top_idx-1];
        }
    }

    bool empty() {
        if (top_idx == 0)
            return true;
        else
            return false;
    }

    int size() {
        return top_idx;
    }
};

int main() {
    Stack s;

    s.push(1);
    s.push(2);
    s.push(3);

    cout << s.top() << "\n";   // 기대값: 3
    s.pop();
    cout << s.top() << "\n";   // 기대값: 2
    cout << s.size() << "\n";  // 기대값: 2
    cout << s.empty() << "\n"; // 기대값: 0 (false)

    return 0;
}