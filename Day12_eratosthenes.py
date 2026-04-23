# ============================================================
# 🐍 Python 연습: 에라토스테네스의 체 / Sieve of Eratosthenes
# ============================================================
# 이름 / Name: 이건우
# 날짜 / Date: 260415
# ============================================================


def find_primes_up_to_100() -> list[int]:
    """
    에라토스테네스의 체 방법으로 1~100 사이의 소수를 모두 찾아 반환합니다.
    Find all prime numbers from 1 to 100 using the Sieve of Eratosthenes.

    Returns:
        list[int]: 오름차순으로 정렬된 소수 리스트 / sorted list of prime numbers
    """

    # ----------------------------------------------------------------
    # 단계 1 / Step 1: is_prime 리스트 초기화
    #   - 크기 101짜리 리스트를 만들고 모두 True로 설정하세요.
    #   - Create a list of size 101 and set every element to True.
    #   - 힌트 / Hint: [True] * 101
    # ----------------------------------------------------------------
    # TODO: is_prime 리스트를 만드세요 / Create the is_prime list
    is_prime = [True] * 101  # 이 줄을 수정하세요 / Replace this line

    # ----------------------------------------------------------------
    # 단계 2 / Step 2: 0과 1은 소수가 아닙니다
    #   - is_prime[0]과 is_prime[1]을 False로 설정하세요.
    #   - Set is_prime[0] and is_prime[1] to False.
    # ----------------------------------------------------------------
    # TODO: 0과 1을 소수 후보에서 제외하세요 / Exclude 0 and 1
    is_prime[0] = False
    is_prime[1] = False

    # ----------------------------------------------------------------
    # 단계 3 / Step 3: 배수 제거 루프
    #   - 2부터 100까지 반복하면서:
    #     * 현재 숫자가 is_prime에서 True이면 (소수 후보라면),
    #     * 그 숫자의 배수를 모두 False로 표시하세요.
    #   - Loop from 2 to 100:
    #     * If the current number is still True in is_prime,
    #     * mark all of its multiples as False.
    #   - 힌트 / Hint: range(i * 2, 101, i) 로 배수를 건너뛸 수 있어요!
    # ----------------------------------------------------------------
    # TODO: 배수 제거 루프를 작성하세요 / Write the multiples-removal loop
    for i in range(2, 101):
        if is_prime[i]:
            pass  # TODO: i의 배수를 False로 표시 / Mark multiples of i as False
            for num in range(i * 2, 101, i):
                is_prime[num] = False

    # ----------------------------------------------------------------
    # 단계 4 / Step 4: 소수 리스트 수집
    #   - is_prime에서 True인 인덱스만 모아 리스트로 반환하세요.
    #   - Collect all indices still marked True and return them as a list.
    #   - 힌트 / Hint: for 루프로 range(101)을 돌며 True인 것만 모으세요.
    # ----------------------------------------------------------------
    # TODO: 소수 리스트를 만들고 반환하세요 / Build and return the prime list
    prime_list = []
    pass  # TODO: prime_list를 채우고 반환하세요 / Fill prime_list and return it
    for i in range(101):
        if is_prime[i]:
            prime_list.append(i)
    return prime_list


# ============================================================
# 테스트 코드 / Test Code  (수정하지 마세요 / Do not modify)
# ============================================================
if __name__ == "__main__":
    primes = find_primes_up_to_100()

    print("=" * 50)
    print("테스트 결과 / Test Results")
    print("=" * 50)

    # 테스트 1: 소수의 개수 / Test 1: Count of primes
    print(f"\n[테스트 1] 소수의 개수 / Number of primes: {len(primes)}")
    print(f"  예상 / Expected : 25")
    print(f"  결과 / Got      : {len(primes)}")
    print(f"  통과 / Pass     : {len(primes) == 25}")

    # 테스트 2: 전체 소수 목록 / Test 2: Full prime list
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    print(f"\n[테스트 2] 소수 목록 / Prime list:")
    print(f"  예상 / Expected : {expected}")
    print(f"  결과 / Got      : {primes}")
    print(f"  통과 / Pass     : {primes == expected}")

    # 테스트 3: 경계값 / Test 3: Boundary values
    print(f"\n[테스트 3] 경계값 / Boundary values:")
    print(f"  가장 작은 소수 / Smallest prime  : {primes[0] if primes else 'N/A'}  (예상 / Expected: 2)")
    print(f"  가장 큰 소수 / Largest prime     : {primes[-1] if primes else 'N/A'}  (예상 / Expected: 97)")
    print(f"  97은 소수? / Is 97 prime?        : {97 in primes}   (예상 / Expected: True)")
    print(f"  100은 소수? / Is 100 prime?      : {100 in primes}  (예상 / Expected: False)")
    print(f"  1은 소수? / Is 1 prime?          : {1 in primes}   (예상 / Expected: False)")

    print("\n" + "=" * 50)
