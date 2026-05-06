# =============================================================
# palindrome_skeleton.py
# 가장 큰 대칭수 곱 찾기 / Find the Largest Palindrome Product
# =============================================================
# 미션 / Mission:
#   세 자리 수 두 개의 곱으로 만들 수 있는 가장 큰 대칭수를 구하세요.
#   Find the largest palindrome made from the product of two 3-digit numbers.
#
# 참고 / Reference:
#   두 자리 수로 만들 수 있는 가장 큰 대칭수: 9009 = 91 × 99
#   Largest palindrome from two 2-digit numbers: 9009 = 91 × 99
# =============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260420
# =============================================================


def is_palindrome_number(n: int) -> bool:
    """
    주어진 정수가 대칭수(palindrome)인지 확인합니다.
    Returns True if the integer n is a palindrome, False otherwise.

    대칭수: 앞에서 읽으나 뒤에서 읽으나 같은 수
    Palindrome: a number that reads the same forwards and backwards

    예 / Examples:
        is_palindrome_number(9009)  → True
        is_palindrome_number(12321) → True
        is_palindrome_number(12345) → False
        is_palindrome_number(11)    → True
        is_palindrome_number(10)    → False
    """
    # TODO (1/2): n을 문자열로 변환하세요 / Convert n to a string
    # 힌트 / Hint: str_n = str(n)
    str_n = str(n)

    # TODO (2/2): 문자열과 뒤집은 문자열이 같은지 비교해서 반환하세요
    #             Compare str_n with its reverse and return the result
    # 힌트 / Hint: 문자열을 뒤집으려면 슬라이싱 [::-1] 을 사용하세요
    #             To reverse a string, use slicing [::-1]
    return str_n[::] == str_n[::-1]


def find_largest_palindrome_product() -> int:
    """
    세 자리 수 두 개의 곱 중 가장 큰 대칭수를 반환합니다.
    Returns the largest palindrome made from the product of two 3-digit numbers.

    세 자리 수 범위 / 3-digit number range: 100 ~ 999 (포함 / inclusive)

    예 / Example:
        find_largest_palindrome_product() → 906609
    """
    # TODO (1/4): 지금까지 찾은 가장 큰 대칭수를 저장할 변수를 만드세요
    #             Create a variable to store the largest palindrome found so far
    # 힌트 / Hint: 아직 아무것도 못 찾았을 때의 초깃값은? / What's a good starting value?
    largest = 0

    # TODO (2/4): 첫 번째 세 자리 수를 반복하는 바깥쪽 반복문을 작성하세요
    #             Write the outer loop iterating over the first 3-digit number
    # 힌트 / Hint: 세 자리 수의 범위는 100부터 999까지입니다 (999 포함!)
    #             Range of 3-digit numbers is 100 to 999 (999 inclusive!)
    for i in range(100, 1000):

        # TODO (3/4): 두 번째 세 자리 수를 반복하는 안쪽 반복문을 작성하세요
        #             Write the inner loop iterating over the second 3-digit number
        # 힌트 / Hint: i부터 시작해도 됩니다 — 왜일까요? (중복 계산 방지!)
        #             You can start from i — why? (avoids counting pairs twice!)
        for j in range(i, 1000):

            # TODO (4/4): 두 수의 곱을 구하고, 대칭수이면서 지금까지의 최댓값보다
            #             크면 largest를 업데이트하세요
            #             Calculate the product, and if it's a palindrome AND
            #             larger than largest, update largest
            product = i * j
            if is_palindrome_number(product) and product > largest:
                largest = product

    return largest


# ---------------------------------------------------------------
# 아래 테스트 코드는 수정하지 마세요! / Do NOT modify the test block below!
# ---------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 50)
    print("🔍 is_palindrome_number 테스트 / Tests")
    print("=" * 50)

    test_cases = [
        (9009, True),
        (12321, True),
        (12345, False),
        (11, True),
        (10, False),
        (1, True),
        (906609, True),
    ]

    all_passed = True
    for num, expected in test_cases:
        result = is_palindrome_number(num)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        if result != expected:
            all_passed = False
        print(f"  {status} | is_palindrome_number({num}) → {result} (예상 / expected: {expected})")

    print()
    print("=" * 50)
    print("🏆 find_largest_palindrome_product 테스트 / Test")
    print("=" * 50)

    answer = find_largest_palindrome_product()
    is_correct_palindrome = is_palindrome_number(answer)
    print(f"  결과 / Result: {answer}")
    print(f"  대칭수 확인 / Palindrome check: {is_correct_palindrome}")
    if is_correct_palindrome and answer > 0:
        print(f"  ✅ 대칭수가 맞습니다! / It is a palindrome!")
    else:
        print(f"  ❌ 대칭수가 아닙니다. 다시 확인해보세요! / Not a palindrome. Check your logic!")

    print()
    if all_passed and is_correct_palindrome and answer > 0:
        print("🎉 모든 테스트 통과! / All tests passed!")
    else:
        print("⚠️  일부 테스트 실패. 로직을 다시 확인해보세요! / Some tests failed. Review your logic!")
    print("=" * 50)
