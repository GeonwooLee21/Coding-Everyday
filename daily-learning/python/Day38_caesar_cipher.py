"""
=============================================================
시저 암호 (Caesar Cipher) 연습
Caesar Cipher Practice
=============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260501
=============================================================

각 글자를 key만큼 밀어서 암호화합니다.
Encrypt by shifting each letter by `key` positions.

규칙 / Rules:
- ord()와 chr() 함수를 반드시 사용 / Must use ord() and chr()
- 영문자만 암호화, 나머지는 그대로 / Only shift letters, keep other characters
- 대소문자 유지 / Preserve uppercase/lowercase
"""


def caesar_encode(message: str, key: int) -> str:
    # TODO 1: 결과를 저장할 빈 문자열을 만드세요
    result = ""

    # TODO 2: message의 각 글자(char)를 반복하세요
    for char in message:

        # TODO 3: char가 소문자인지 확인하세요 (a-z)
        # 힌트 / Hint: "a" <= char <= "z"
        if "a" <= char <= "z":
            # TODO 4: 소문자를 key만큼 밀어서 변환하세요
            # 공식 / Formula: chr((ord(char) - ord("a") + key) % 26 + ord("a"))
            shifted_char = chr((ord(char) - ord("a") + key) % 26 + ord("a"))
            result = result + shifted_char

        # TODO 5: char가 대문자인지 확인하세요 (A-Z)
        elif "A" <= char <= "Z":
            # TODO 6: 대문자를 key만큼 밀어서 변환하세요
            # 힌트 / Hint: 위 공식에서 "a"를 "A"로 바꾸세요
            shifted_char = chr((ord(char) - ord("A") + key) % 26 + ord("A"))
            result = result + shifted_char

        # TODO 7: 영문자가 아니면 그대로 추가하세요 (숫자, 공백, 특수문자)
        else:
            result = result + char

    # TODO 8: 최종 결과를 반환하세요
    return result


# ============================================================
# 테스트 코드 — 이 부분은 수정하지 마세요!
# Test code — DO NOT modify below this line!
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("시저 암호 테스트 / Caesar Cipher Tests")
    print("=" * 50)

    # 테스트 1: 기본 소문자 / Basic lowercase
    result1 = caesar_encode("hello", 3)
    print(f"Test 1: caesar_encode('hello', 3) = {result1!r}")
    print(f"        Expected: 'khoor' → {'PASS' if result1 == 'khoor' else 'FAIL'}")

    # 테스트 2: 대문자 / Uppercase
    result2 = caesar_encode("HELLO", 3)
    print(f"Test 2: caesar_encode('HELLO', 3) = {result2!r}")
    print(f"        Expected: 'KHOOR' → {'PASS' if result2 == 'KHOOR' else 'FAIL'}")

    # 테스트 3: 알파벳 끝 넘기기 / Wrapping
    result3 = caesar_encode("xyz", 3)
    print(f"Test 3: caesar_encode('xyz', 3) = {result3!r}")
    print(f"        Expected: 'abc' → {'PASS' if result3 == 'abc' else 'FAIL'}")

    # 테스트 4: 혼합 / Mixed
    result4 = caesar_encode("Hello, World!", 5)
    print(f"Test 4: caesar_encode('Hello, World!', 5) = {result4!r}")
    print(f"        Expected: 'Mjqqt, Btwqi!' → {'PASS' if result4 == 'Mjqqt, Btwqi!' else 'FAIL'}")

    # 테스트 5: 숫자와 특수문자 / Numbers and special chars
    result5 = caesar_encode("Python 3.10", 13)
    print(f"Test 5: caesar_encode('Python 3.10', 13) = {result5!r}")
    print(f"        Expected: 'Clguba 3.10' → {'PASS' if result5 == 'Clguba 3.10' else 'FAIL'}")

    # 테스트 6: key=26 (한 바퀴) / Full rotation
    result6 = caesar_encode("zebra", 26)
    print(f"Test 6: caesar_encode('zebra', 26) = {result6!r}")
    print(f"        Expected: 'zebra' → {'PASS' if result6 == 'zebra' else 'FAIL'}")

    # 테스트 7: key > 26 / Key greater than 26
    result7 = caesar_encode("abc", 27)
    print(f"Test 7: caesar_encode('abc', 27) = {result7!r}")
    print(f"        Expected: 'bcd' → {'PASS' if result7 == 'bcd' else 'FAIL'}")
