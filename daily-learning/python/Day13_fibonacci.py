# =============================================================
# 🐍 Python 연습: 피보나치 짝수 합 구하기
# 🐍 Python Practice: Sum of Even Fibonacci Numbers
# =============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260415
# =============================================================


def sum_even_fibonacci(limit: int) -> int:
    """
    limit 이하의 피보나치 수 중 짝수의 합을 반환합니다. 
    Returns the sum of even-valued Fibonacci terms up to and including limit.

    Args:
        limit (int): 피보나치 수의 최댓값 / Maximum value for Fibonacci terms

    Returns:
        int: 짝수 피보나치 수의 합 / Sum of even Fibonacci numbers
    """

    # TODO (1/4): 누적 합계를 저장할 변수를 0으로 초기화하세요
    # TODO (1/4): Initialize a variable to store the running total, starting at 0
    total = 0

    # TODO (2/4): 피보나치 수열의 첫 두 항을 변수로 설정하세요 (1과 2)
    # TODO (2/4): Set up the first two terms of the Fibonacci sequence as variables (1 and 2)
    # fib_list = [1, 2]
    a, b = 1, 2


    # TODO (3/4): while 루프를 작성하세요
    #   - 조건: 현재 항이 limit 이하인 동안 반복
    #   - 루프 안에서:
    #       a) 현재 항이 짝수인지 확인하고, 짝수라면 합계에 더하기
    #       b) 다음 피보나치 수를 계산하여 변수 업데이트
    #          힌트: a, b = b, a + b  패턴을 활용하세요!
    # TODO (3/4): Write a while loop
    #   - Condition: keep looping while the current term is <= limit
    #   - Inside the loop:
    #       a) Check if the current term is even; if so, add it to the total
    #       b) Calculate the next Fibonacci number and update your variables
    #          Hint: use the  a, b = b, a + b  pattern!
    while b < limit:
        if b % 2 == 0:
            total += b
        a, b = b, a + b

    # i = 1
    # while fib_list[i] < limit:
    #     if fib_list[i] % 2 == 0:
    #             total += fib_list[i]
    #     i += 1
    #     fib_list[i].append(fib_list[i-1]+fib_list[i])

    # TODO (4/4): 최종 합계를 반환하세요
    # TODO (4/4): Return the final total
    # return fib_list[len(fib_list)]
    return total


# =============================================================
# 메인 실행 블록 / Main execution block
# =============================================================

if __name__ == "__main__":

    # 테스트 1: 소규모 — 손으로 직접 확인해보세요!
    # Test 1: Small scale — verify by hand!
    result_small = sum_even_fibonacci(10)
    print(f"10 이하 짝수 피보나치 합 / Even Fibonacci sum up to 10: {result_small}")
    # 예상 / Expected: 10  (2 + 8)

    # 테스트 2: 중간 규모
    # Test 2: Medium scale
    result_medium = sum_even_fibonacci(100)
    print(f"100 이하 짝수 피보나치 합 / Even Fibonacci sum up to 100: {result_medium}")
    # 예상 / Expected: 44  (2 + 8 + 34)

    # 테스트 3: 실제 미션!
    # Test 3: The real mission!
    result_million = sum_even_fibonacci(1_000_000)
    print(f"100만 이하 짝수 피보나치 합 / Even Fibonacci sum up to 1,000,000: {result_million}")
    # 예상 / Expected: 1089154
