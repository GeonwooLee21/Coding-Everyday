# =====================================================
# 🐍 최대 소인수 구하기 / Largest Prime Factor
# Skeleton Code — 여기에 코드를 작성하세요! / Write your code here!
# =====================================================

# 💡 소인수분해 복습 / Prime Factorization Recap
#
# 소인수분해란 어떤 수를 소수들의 곱으로 나타내는 것입니다.
# Prime factorization means expressing a number as a product of primes.
#
# 예 / Example:
#   12 = 2 × 2 × 3   → 소인수: 2, 3  / prime factors: 2, 3
#   100 = 2 × 2 × 5 × 5 → 소인수: 2, 5  / prime factors: 2, 5
#
# 전략 / Strategy:
#   1. 2부터 나누기 시작 / Start dividing from 2
#   2. 나누어 떨어지면, 계속 나누기 / If it divides evenly, keep dividing
#   3. 더 이상 안 되면 다음 수로 / When it doesn't, move to the next number
#   4. 소인수를 발견할 때마다 기록 / Record each prime factor you find


def find_largest_prime_factor(n: int) -> int:
    """
    주어진 정수 n의 최대 소인수를 반환합니다.
    Returns the largest prime factor of the given integer n.

    매개변수 / Parameter:
        n (int): 1보다 큰 정수 / An integer greater than 1

    반환값 / Returns:
        int: n의 최대 소인수 / The largest prime factor of n
    """

    # TODO 1: 최대 소인수를 저장할 변수를 만드세요.
    # TODO 1: Create a variable to store the largest prime factor found so far.
    # 힌트: 아직 아무것도 못 찾았으니 1로 시작하면 어떨까요?
    # Hint: We haven't found anything yet — maybe start with 1?
    largest_factor = 1

    # TODO 2: 나눌 수(divisor)를 2부터 시작하세요.
    # TODO 2: Start your divisor at 2.
    divisor = 2

    # TODO 3: divisor * divisor <= n 인 동안 반복하세요.
    # TODO 3: Loop while divisor * divisor <= n.
    # 힌트: while 문을 사용하세요!
    # Hint: Use a while loop!
    while divisor * divisor <= n:
    # 4. 'divisor * divisor <= n' 까지만 확인하면 충분한 이유가 뭘까요?
    # n을 소인수로 나눌 경우, n이 divisor의 제곱 값을 넘어선 다는 것은 n이 divisor로 충분히 나누어졌다는 뜻이기 때문이다.
    # 위 답변은 정확하지 않다. divisor가 n을 나눌 수 있을 만큼 나누어 while문이 멈추는 게 아니라, 남은 n이 소수임이 확정돼서 멈추는 것이기 때문이다.
    # 즉, divisor * divisor가 n보다 큰 시점에서 남은 n이 1보다 크면, 그 자체가 소수라는 게 수학적으로 보장되기 때문에 'divisor * divisor <= n' 까지만 확인하면 충분하다.


        # TODO 4: n이 divisor로 나누어 떨어지는 동안 반복하세요.
        # TODO 4: While n is divisible by divisor, keep dividing.
        # 힌트: n % divisor == 0 이면 나누어 떨어집니다.
        # Hint: n % divisor == 0 means it divides evenly.
        while n % divisor == 0:
            largest_factor = divisor    # 소인수 발견! / Prime factor found!
            n = n // divisor            # n을 줄이세요 / Shrink n

        # TODO 5: 다음 수로 넘어가세요.
        # TODO 5: Move to the next divisor.
        divisor = divisor + 1

    # TODO 6: 루프가 끝난 후 n이 1보다 크면, n 자체가 소수입니다!
    # TODO 6: After the loop, if n > 1, then n itself is a prime factor!
    if n > 1:
        largest_factor = n

    return largest_factor


# =====================================================
# 🎪 테스트 / Test Your Code
# =====================================================

# 테스트 1: 합성수 / composite number
print(find_largest_prime_factor(12))
# 예상 / Expected: 3  (12 = 2 × 2 × 3)

# 테스트 2: 완전 제곱수 / perfect square
print(find_largest_prime_factor(100))
# 예상 / Expected: 5  (100 = 2 × 2 × 5 × 5)

# 테스트 3: 소수 입력 / prime input
print(find_largest_prime_factor(13))
# 예상 / Expected: 13

# 테스트 4: 큰 수 / larger number
print(find_largest_prime_factor(13195))
# 예상 / Expected: 29  (13195 = 5 × 7 × 13 × 29)

# 테스트 5: 경계값 / boundary value
print(find_largest_prime_factor(2))
# 예상 / Expected: 2
