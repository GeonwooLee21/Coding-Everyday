"""
=============================================================
🎰 숫자 맞추기 미니게임 부스 (Number Guessing Game Booth)
=============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260507
=============================================================


여러분은 신입 게임 개발자입니다. 1~20 사이의 숫자를 맞추는
미니게임 프로토타입을 완성해 주세요!

You are a junior game developer. Complete the prototype for a
number guessing mini-game (range 1~20)!
"""

import random

def play_guessing_game() -> int:
    """
    숫자 맞추기 게임을 실행하고, 손님이 사용한 시도 횟수를 반환합니다.
    Run the guessing game and return the number of attempts.
    """
    # TODO 1: random.randrange()를 사용해 1~20 사이의 비밀 숫자를 생성하세요.
    #         (힌트: randrange(1, 21)은 1부터 20까지의 숫자를 반환합니다)
    # TODO 1: Use random.randrange() to generate a secret number from 1 to 20.
    #         (Hint: randrange(1, 21) returns a number from 1 to 20)
    secret = random.randrange(1, 21)  # 여기를 수정하세요 / Replace this

    # TODO 2: 시도 횟수를 저장할 변수 n을 0으로 초기화하세요.
    # TODO 2: Initialize the attempt counter n to 0.
    n = 0  # 여기를 수정하세요 / Replace this

    # TODO 3: 정답을 맞출 때까지 반복하는 루프를 작성하세요.
    #         while True 루프를 사용하고, 정답을 맞추면 break로 빠져나오세요.
    # TODO 3: Write a loop that runs until the customer guesses correctly.
    #         Use `while True` and `break` when they get it right.
    while True:  # 여기를 수정하세요 / Replace this
        # TODO 4: int(input())을 사용해 손님의 추측을 정수로 받으세요.
        #         프롬프트 메시지: "숫자를 입력하세요 (1~20): "
        # TODO 4: Use int(input()) to get the customer's guess as an integer.
        #         Prompt message: "숫자를 입력하세요 (1~20): "
        try:
            guess = int(input("숫자를 입력하세요 (1~20): "))
        except ValueError:
            print("숫자를 입력해주세요.")
            continue 
        # continue가 없으면 UnboundLocalError가 발생한다.
        # 1. "abc" 같은 문자열 입력 → int() 변환 실패 → ValueError
        # 2. guess = ... 대입이 실행되지 않음 (guess에 값 없음)
        # 3. except 블록 실행 후 continue 없이 아래로 내려감
        # 4. guess < 1 에서 guess를 읽으려 하지만 바인딩된 값이 없음 → 에러

        # TODO 5: 입력값이 1~20 범위 밖이면 안내 메시지를 출력하고
        #         continue로 다시 입력받으세요. (n은 증가시키지 마세요!)
        # TODO 5: If the guess is outside 1~20, print a warning and `continue`
        #         to re-prompt. (Do NOT increment n!)
        if guess < 1 and guess > 20:  # 여기를 수정하세요 / Replace this
            print("1에서 20 사이의 수를 입력하세요.")
            continue

        # TODO 6: n을 1 증가시키세요. (유효한 입력일 때만!)
        # TODO 6: Increment n by 1. (Only for valid inputs!)
        n += 1  # 여기를 수정하세요 / Replace this

        # TODO 7: guess와 secret을 비교하여 다음과 같이 분기하세요:
        #         - guess < secret: "더 큰 숫자입니다!" 출력
        #         - guess > secret: "더 작은 숫자입니다!" 출력
        #         - guess == secret: "정답입니다!" 출력 후 break
        # TODO 7: Compare guess and secret with branching:
        #         - guess < secret: print "더 큰 숫자입니다!"
        #         - guess > secret: print "더 작은 숫자입니다!"
        #         - guess == secret: print "정답입니다!" and break
        if guess < secret:  # 여기를 수정하세요 / Replace this
            print("더 큰 숫자입니다!")
        elif guess > secret:
            print("더 작은 숫자입니다!")
        elif guess == secret:
            print("정답입니다!")
            break

    # TODO 8: 시도 횟수 n에 따라 다른 메시지를 출력하세요:
    #         - 1 ~ 3번:  "n번만에 맞춘 당신은 천재!"
    #         - 4 ~ 6번:  "n번만에 맞추셨네요. 잘했어요^^"
    #         - 7번 이상: "n번만에 맞추다니 분발하세요."
    # TODO 8: Print different messages based on n:
    #         - 1~3:  "n번만에 맞춘 당신은 천재!"
    #         - 4~6:  "n번만에 맞추셨네요. 잘했어요^^"
    #         - 7+:   "n번만에 맞추다니 분발하세요."
    if n >= 1 and n <= 3:
        print("n번만에 맞춘 당신은 천재!")
    if n >= 4 and n <= 6:
        print("n번만에 맞추셨네요. 잘했어요^^")
    elif n > 7:
        print("n번만에 맞추다니 분발하세요.")

    # TODO 9: 시도 횟수 n을 반환하세요.
    # TODO 9: Return the attempt count n.
    return n


# ============================================================
# ⚠️ 아래 테스트 블록은 수정하지 마세요!
# ⚠️ Do NOT modify the test block below!
# ============================================================
if __name__ == "__main__":
    print("🎰 숫자 맞추기 게임을 시작합니다!")
    print("🎰 Starting the number guessing game!")
    print("-" * 40)

    total_attempts = play_guessing_game()

    print("-" * 40)
    print(f"게임 종료! 총 시도 횟수: {total_attempts}")
    print(f"Game over! Total attempts: {total_attempts}")
