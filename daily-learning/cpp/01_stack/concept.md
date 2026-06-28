# Stack

## 핵심 특성
- 삽입/삭제가 일어나는 방향은? 두 연산 모두 top
- LIFO란 무슨 뜻? Last In First Out

## 핵심 연산 (push / pop / top / empty / size)
- push: top idx에 원소를 삽입 
- pop: top idx의 원소를 제거 
- top: top idx의 원소를 반환 
- empty: ~~stack을 비움~~ 🔴 stack이 현재 비어있는지 확인 후 bool 반환
- size: stack의 현재 크기 반환

## 배열로 구현할 때 핵심 변수
- 뭘 추적해야 push/pop이 가능한가? top 인덱스를 추적해야 한다.

## STL std::stack과 차이점
- 내가 직접 구현하면 뭘 신경 써야 하나? ~~스택의 삽입/삭제 연산을 할 때마다 top idx가 바뀌는 것도 반영해줘야 한다.~~ ⚠️ 크기 관리. STL `std::stack`은 내부적으로 deque나 vector를 써서 크기가 자동으로 늘어나지만, 배열로 직접 구현하면 `MAX_SIZE`를 넘었을 때 어떻게 할지를 직접 처리해야 한다.