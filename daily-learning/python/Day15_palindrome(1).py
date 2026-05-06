# =============================================================
# 🐍 Palindrome Detector / 회문 감지기
# =============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260415
# =============================================================
# 미션: 주어진 단어가 회문(palindrome)인지 확인하세요.
# Mission: Check if the given word is a palindrome.
#
# 회문이란? 앞에서 읽어도 뒤에서 읽어도 같은 단어!
# A palindrome reads the same forwards and backwards.
# =============================================================


def is_palindrome(word: str) -> bool:
    """
    주어진 단어가 회문인지 확인합니다. (대소문자 무시)
    Returns True if word is a palindrome, False otherwise. (case-insensitive)

    Args:
        word: 확인할 문자열 / The string to check

    Returns:
        True if palindrome, False otherwise
    """

    # TODO 1: 먼저 word를 전부 소문자로 바꾸세요.
    # TODO 1: Convert word to all lowercase first.
    # 힌트 / Hint: use .lower()
    cleaned = word.lower()

    # TODO 2: 왼쪽 포인터(left)와 오른쪽 포인터(right)를 초기화하세요.
    # TODO 2: Initialize your left and right pointers.
    # 힌트 / Hint: left starts at 0, right starts at the last index
    left = 0
    right = len(word) - 1

    # TODO 3: left가 right보다 작은 동안 반복하세요.
    # TODO 3: Loop while left is less than right.
    while left < right:

        # TODO 4: cleaned[left]와 cleaned[right]를 비교하세요.
        # TODO 4: Compare the characters at left and right.
        # 같지 않으면 / If they don't match:
        if cleaned[left] != cleaned[right]:
            return False  # TODO 5: 회문이 아닙니다! / Not a palindrome!

        # TODO 6: 두 포인터를 가운데로 이동하세요.
        # TODO 6: Move both pointers toward the middle.
        left = left + 1
        right = right - 1

    # TODO 7: 반복문을 통과했다면? 회문입니다!
    # TODO 7: If you made it through the loop — it's a palindrome!
    return True


# -------------------------------------------
# 🎪 테스트 / Tests
# 아래 코드를 실행해서 결과를 확인하세요!
# Run the code below to check your results!
# -------------------------------------------

if __name__ == "__main__":
    test_cases = [
        ("racecar", True),
        ("hello", False),
        ("madam", True),
        ("Racecar", True),
        ("a", True),
        ("level", True),
        ("python", False),
    ]

    for word, expected in test_cases:
        result = is_palindrome(word)
        status = "✅" if result == expected else "❌"
        print(f"{status} is_palindrome({repr(word)}) = {result}  (expected {expected})")
