"""
=============================================================
숫자의 표현 / Express a Number as Consecutive Sum
=============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260504
=============================================================

KO: 자연수 n을 연속된 자연수들의 합으로 표현하는 방법의 수를 반환하세요.
EN: Return the number of ways to express n as a sum of consecutive natural numbers.

예 / Example:
    n = 15  ->  4
        (1+2+3+4+5, 4+5+6, 7+8, 15)
"""


def count_consecutive_sums(n: int) -> int:
    # ------------------------------------------------------------------
    # TODO 1: 방법의 개수를 셀 변수를 만드세요
    #         Create a variable to count the number of ways.
    #         (KO: 0부터 시작 / EN: start from 0)
    # ------------------------------------------------------------------
    count = 0  # 여기에 작성 / write here

    # ------------------------------------------------------------------
    # TODO 2: 시작 숫자를 1부터 n까지 반복하세요
    #         Loop the starting number from 1 to n.
    #         (KO: range()를 사용 / EN: use range())
    # ------------------------------------------------------------------
    for start in range(1, n + 1):

        # --------------------------------------------------------------
        # TODO 3: 누적 합을 저장할 변수를 만드세요 (시작 숫자로 초기화)
        #         Create a variable for the running sum (init with start).
        # --------------------------------------------------------------
        total = 0  # 여기에 작성 / write here

        # --------------------------------------------------------------
        # TODO 4: 다음 숫자(start, start+1, start+2, ...)를 더하면서
        #         합이 n 이상이 될 때까지 반복하세요.
        #         Add the next number (start, start+1, start+2, ...)
        #         and keep going until the sum is >= n.
        #         (KO: while 반복문 사용 / EN: use a while loop)
        # --------------------------------------------------------------
        current = start
        while total < n:
            # TODO 4-1: total에 current를 더하세요 / add current to total
            pass  # 여기에 작성 / write here

            # TODO 4-2: current를 1 증가시키세요 / increment current by 1
            pass  # 여기에 작성 / write here

        # --------------------------------------------------------------
        # TODO 5: 누적 합이 정확히 n과 같으면 count를 1 증가시키세요
        #         If the running sum equals n exactly, increment count by 1.
        # --------------------------------------------------------------
        # 여기에 작성 / write here

    # ------------------------------------------------------------------
    # TODO 6: 최종 count를 반환하세요 / Return the final count.
    # ------------------------------------------------------------------
    return 0  # 여기를 수정 / modify here


# ====================================================================
# 아래 코드는 수정하지 마세요!  /  Do NOT modify the code below!
# ====================================================================
if __name__ == "__main__":
    test_cases = [
        (15, 4),
        (9, 3),
        (1, 1),
        (10, 2),
        (100, 3),
    ]

    print("=" * 50)
    print("테스트 결과 / Test Results")
    print("=" * 50)
    for n, expected in test_cases:
        result = count_consecutive_sums(n)
        mark = "✅" if result == expected else "❌"
        print(f"{mark}  count_consecutive_sums({n}) = {result}  (expected: {expected})")
