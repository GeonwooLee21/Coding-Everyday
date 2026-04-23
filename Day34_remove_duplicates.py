"""
# =============================================================
🐍 Python 연습: 정렬된 배열에서 중복 제거하기 / Remove Duplicates from Sorted Array
# =============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260422
# =============================================================

📚 시나리오 / Scenario:
여러분은 대학교 도서관의 주니어 개발자 인턴입니다.
정렬된 학생 ID 리스트에서 중복을 제거해야 합니다 — 새 리스트를 만들지 말고!

You're a junior developer intern at your university library.
Remove duplicates from the sorted student ID list — without creating a new list!

규칙 / Rules:
- in-place 수정 (새 리스트 만들기 금지!)  / Modify in-place (no new lists!)
- 고유 값의 개수 k를 반환  / Return the count k of unique values
- nums의 처음 k개 위치에 고유값이 정렬된 순서로 저장됨
  / First k positions of nums hold unique values in sorted order
"""


def remove_duplicates(nums: list[int]) -> int:
    # ------------------------------------------------------------------
    # TODO 1: 빈 리스트 처리 / Handle empty list
    # 힌트 / Hint: len(nums) == 0 이면 0을 반환하세요
    #              If len(nums) == 0, just return 0
    # ------------------------------------------------------------------
    if len(nums) == 0:
        return 0

    # ------------------------------------------------------------------
    # TODO 2: "쓰기 위치"를 추적할 변수 만들기
    #         / Create a variable to track the "write position"
    # 힌트 / Hint: 첫 번째 요소는 항상 고유하므로, 1부터 시작합니다
    #              First element is always unique, so start at 1
    # ------------------------------------------------------------------
    write_index = 1

    # ------------------------------------------------------------------
    # TODO 3: 인덱스 1부터 리스트 끝까지 반복
    #         / Loop from index 1 to the end of the list
    # 힌트 / Hint: range(1, len(nums))를 사용하세요
    #              Use range(1, len(nums))
    # ------------------------------------------------------------------
    for read_index in range(1, len(nums)):

        # --------------------------------------------------------------
        # TODO 4: 현재 값이 이전 값과 다른지 확인
        #         / Check if current value is different from the previous one
        # 힌트 / Hint: nums[read_index]와 nums[read_index - 1]을 비교하세요
        #              Compare nums[read_index] and nums[read_index - 1]
        # --------------------------------------------------------------
        if nums[read_index] != nums[read_index - 1]:

            # ----------------------------------------------------------
            # TODO 5: 고유한 값을 write_index 위치에 쓰고,
            #         write_index를 1 증가시키세요
            #         / Write the unique value at write_index position,
            #         then increase write_index by 1
            # ----------------------------------------------------------
            nums[write_index] = nums[read_index]
            write_index += 1


    # ------------------------------------------------------------------
    # TODO 6: 고유한 값의 개수(write_index)를 반환
    #         / Return the count of unique values (write_index)
    # ------------------------------------------------------------------
    return write_index

# Bonus Challenge : Easy
def count_duplicates(nums):
    if len(nums) == 0:
        return 0
    
    count = 0

    for read_idx in range(1, len(nums)):
        if nums[read_idx] == nums[read_idx - 1]:
            count += 1

    return count

# Bonus Challenge : Medium
def remove_duplicates_twice(nums):
    if len(nums) == 0:
        return 0
    
    write_idx, count = 1, 1
    for read_idx in range(1, len(nums)):
        if   nums[read_idx] == nums[read_idx - 1] and count < 2:
            nums[write_idx] = nums[read_idx]
            write_idx += 1
            count += 1
        elif nums[read_idx] != nums[read_idx - 1]:
            nums[write_idx] = nums[read_idx]
            write_idx += 1
            count = 1 # 현재 인덱스와 이전 인덱스의 값이 다른 경계이므로 중복된 숫자의 개수를 새는 count 변수를 0으로 초기화

    return write_idx

# Bonus Challenge : Hard
def remove_duplicates_with_counts(nums):
    if len(nums) == 0:
        return 0
    
    
    pass

# ======================================================================
# ⚠️ 아래 코드는 수정하지 마세요! / DO NOT MODIFY THE CODE BELOW!
# ======================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("🧪 테스트 시작 / Running tests")
    print("=" * 60)

    test_cases = [
        ([1, 1, 2], 2, [1, 2], "기본 케이스 / Basic case"),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4], "여러 중복 / Multiple duplicates"),
        ([7], 1, [7], "요소 하나 / Single element"),
        ([5, 5, 5, 5, 5], 1, [5], "전부 같은 값 / All same"),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5], "중복 없음 / No duplicates"),
        ([-3, -3, -1, 0, 0, 2], 4, [-3, -1, 0, 2], "음수 포함 / With negatives"),
    ]

    passed = 0
    for original, expected_k, expected_front, label in test_cases:
        nums = list(original)
        k = remove_duplicates(nums)
        front = nums[:k] if isinstance(k, int) and k >= 0 else None
        ok = (k == expected_k and front == expected_front)
        mark = "✅" if ok else "❌"
        print(f"{mark} {label}")
        print(f"   입력 / input:    {original}")
        print(f"   결과 / got:      k={k}, 앞 / front={front}")
        print(f"   예상 / expected: k={expected_k}, 앞 / front={expected_front}")
        if ok:
            passed += 1
        print()

    print("=" * 60)
    print(f"결과 / Result: {passed} / {len(test_cases)} 통과 / passed")
    print("=" * 60)

    # Bonus Challenge : Easy
    print(count_duplicates([1, 1, 2, 2, 2, 3]))  # 3 반환 (중복 3개: 1 한 번, 2 두 번)
    print(count_duplicates([1, 2, 3]))           # 0 반환

    # Bonus Challenge : Medium
    nums = [1, 1, 1, 2, 2, 3]
    k = remove_duplicates_twice(nums)
    print(k, nums[:k])

    # Bonus Challenge : Hard
    nums = [1, 1, 2, 3, 3, 3]
    counts, k = remove_duplicates_with_counts(nums) # counts = {1: 2, 2: 1, 3: 3}, k = 3, nums의 처음 3개: [1, 2, 3]
