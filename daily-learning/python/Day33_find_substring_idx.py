"""
# =============================================================
🔍 Find Substring Index — 부분 문자열 인덱스 찾기
# =============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260421
# =============================================================

시나리오 / Scenario:
  사이버보안 로그 분석 도구의 일부로, 로그 메시지 안에서
  오류 코드가 처음 나타나는 위치를 찾는 함수를 구현합니다.

  Implement a function that finds the first occurrence of a
  substring inside a string — part of a cybersecurity log tool.

규칙 / Rules:
  ⚠️ .find(), .index(), `in` 연산자 사용 금지!
  ⚠️ Do NOT use .find(), .index(), or the `in` operator!
  슬라이싱과 반복문으로 직접 구현하세요.
  Implement it yourself using slicing and loops.
"""


def find_substring_index(haystack: str, needle: str) -> int:
    """
    haystack 안에서 needle이 처음 나타나는 인덱스를 반환합니다.
    needle이 없으면 -1을 반환합니다.

    Return the index of the first occurrence of needle in haystack.
    Return -1 if needle is not found.
    """

    # TODO 1 (KO): needle이 빈 문자열("")이면 0을 반환하세요.
    # TODO 1 (EN): If needle is an empty string (""), return 0.
    if needle == "":
        return 0


    # TODO 2 (KO): haystack과 needle의 길이를 변수에 저장하세요.
    # TODO 2 (EN): Store the lengths of haystack and needle in variables.
    haystack_length = len(haystack)  # ← 바꾸세요 / change this
    needle_length = len(needle)    # ← 바꾸세요 / change this


    # TODO 3 (KO): needle이 haystack보다 길면 찾을 수 없으니 -1을 반환하세요.
    # TODO 3 (EN): If needle is longer than haystack, return -1.
    if needle_length > haystack_length:
        return -1

    # TODO 4 (KO): haystack의 시작 위치 i를 0부터 (haystack_length - needle_length)까지 반복하세요.
    #              각 위치에서 haystack[i : i + needle_length]가 needle과 같은지 확인하고,
    #              같으면 i를 반환하세요.
    # TODO 4 (EN): Loop i from 0 to (haystack_length - needle_length) inclusive.
    #              At each position, check if haystack[i : i + needle_length] equals needle.
    #              If so, return i.
    #
    # 힌트 / Hint: range(haystack_length - needle_length + 1)
    for i in range(haystack_length - needle_length + 1):
        if haystack[i : i + needle_length] == needle:
            return i


    # TODO 5 (KO): 반복이 끝나도 못 찾았으면 -1을 반환하세요.
    # TODO 5 (EN): If the loop finishes without finding needle, return -1.
    return -1  # ← 필요하면 바꾸세요 / change if needed

# Bonus Challenge : Easy
def find_last_substring_index(haystack, needle):
    if needle == "":
        return 0
    
    haystack_length = len(haystack)
    needle_length = len(needle)

    if needle_length > haystack_length:
        return -1
    
    final_idx = 0
    for i in range(0, haystack_length - needle_length + 1):
        if haystack[i : i + needle_length] == needle:
            final_idx = i
    if final_idx != 0:
    
        return final_idx
    else:
        return -1

# Bonus Challenge : Medium
def find_all_occurrences(haystack, needle):
    if needle == "":
        return 0
    
    haystack_length = len(haystack)
    needle_length = len(needle)

    if needle_length > haystack_length:
        return -1
    
    idx_list = []
    for i in range(0, haystack_length - needle_length + 1):
        if haystack[i : i + needle_length] == needle:
            idx_list.append(i)
    
    if idx_list != None:
        return idx_list
    else:
        return -1

# Bonus Challenge : Hard
'''    
# Q. KMP 알고리즘이 필요한 이유가 무엇인가?
# - "부분 일치"가 실패했을 때, 얼마나 뒤로 돌아가야 할까요?
# - "ABCABD"에서 앞쪽의 "ABC"를 이미 봤다면, 다음엔 어디서부터 비교하면 될까요?
# A.
# 기존의 Naive한 방식에선 haystack 문자열 내의 부분문자열과 needle 문자열이 서로 같지 않으면, 
# haystack 내를 순회하는 인덱스 i를 하나씩 늘려 needle 크기의 haystack 내 부분문자열과 needle 문자열을 처음부터 다시 비교한다. 
# 따라서 Naive한 방식에선 총 비교횟수가 (needle의 길이) * (haystack의 길이 - needle의 길이 + 1)이다.
#
# 반면, KMP 알고리즘에서는 우선 needle의 맨 앞에서부터 j+1글자를 잘랐을 때 
# 그 안에서 앞부분(접두사)과 뒷부분(접미사)이 똑같은 가장 긴 길이를 저장하는 리스트 f[j]를 구성한다. 
# 그 뒤로 haystack 내에선 i 인덱스를, needle 내에선 j 인덱스를 통해 haystack[i]와 needle[j]를 서로 한 글자씩 비교하기 시작한다. 
# 만약 이러한 탐색 중 haystack 내 부분문자열과 needle이 j번째 글자에서 불일치가 발생한다면, 
# haystack은 i부터, needle은 j = f[j-1]인 남은 문자열부터 다시 비교되기 시작한다. 
# 즉, haystack과 needle을 서로 비교했을 때 일정 길이만큼은 두 문자열이 같다고 확정났을 때, haystack의 i는 뒤로 돌아가지 않고, 
# needle의 j만 f[j-1]로 점프하여, 이미 일치가 확정된 접두사 부분을 제외하고 두 문자열이 비교된다. 
# 따라서 KMP 알고리즘을 이용하는 방식의 경우, 총 비교 횟수가 (needle의 길이) + (haystack의 길이) 정도이므로 
# Naive한 방식과 비교했을 때 훨씬 효율적이다.
'''
def kmp_algorithm(haystack, needle):
    pass

# ==========================================================================
# 🚫 아래 코드는 수정하지 마세요! (채점용 테스트 코드)
# 🚫 DO NOT MODIFY below this line (test harness for grading)
# ==========================================================================
if __name__ == "__main__":
    print("=" * 50)
    print("🧪 Testing find_substring_index")
    print("=" * 50)

    # 테스트 케이스 / Test cases: (haystack, needle, expected)
    test_cases = [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("ERROR_404 not found in server", "404", 6),
        ("hello", "", 0),
        ("abc", "abcd", -1),
        ("mississippi", "issip", 4),
        ("banana", "nan", 2),
        ("python is fun", "fun", 10),
    ]

    passed = 0
    for haystack, needle, expected in test_cases:
        result = find_substring_index(haystack, needle)
        status = "✅" if result == expected else "❌"
        if result == expected:
            passed += 1
        print(f"{status} find_substring_index({haystack!r}, {needle!r})")
        print(f"   → got {result}, expected {expected}")

    print("=" * 50)
    print(f"결과 / Result: {passed}/{len(test_cases)} tests passed")
    print("=" * 50)

    # ==========================================================================
    # Bonus Challenge
    # ==========================================================================
    print("Bonus Challenge #1")
    print(find_last_substring_index("sadbutsad", "sad")) # 예상: 6
    print()

    print("Bonus Challenge #2")
    print(find_all_occurrences("ababab", "ab"))  # 예상: [0, 2, 4]
    print(find_all_occurrences("aaaa", "aa"))    # 예상: [0, 1, 2]  (겹치는 경우 포함!)
    print()
