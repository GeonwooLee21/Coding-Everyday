"""
# =============================================================
🏃 Next Permutation Practice
다음 순열 만들기 — 시작 코드
# =============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260421
# =============================================================

규칙 (Rules):
- nums를 in-place로 수정하세요 (Modify nums in-place)
- sorted(), sort(), reversed(), [::-1] 사용 금지 (Forbidden)
- itertools 등 라이브러리 사용 금지 (No libraries)
- while 반복문과 a, b = b, a 교환을 활용하세요
"""

def next_permutation(nums: list[int]) -> None:
    n = len(nums)

    # ---------------------------------------------------------------
    # TODO 1: 피벗(pivot) 찾기
    # KO: 오른쪽에서 왼쪽으로 보면서, nums[i] < nums[i+1]이 되는 가장 오른쪽 i를 찾으세요.
    # 못 찾으면 i는 -1로 끝나야 합니다 (전체가 내림차순이라는 뜻).
    # ---------------------------------------------------------------
    i = n - 2
    while i >= 0:
        if nums[i] < nums[i+1]:
            break
        i -= 1

    # ---------------------------------------------------------------
    # TODO 2: 교환 대상(swap target) 찾고 교환하기
    # KO: i >= 0인 경우에만, 오른쪽에서 왼쪽으로 보면서 nums[j] > nums[i]인 가장 오른쪽 j를 찾으세요.
    #     그런 다음 nums[i]와 nums[j]를 교환하세요.
    # 힌트 (Hint): a, b = b, a 문법으로 교환할 수 있습니다.
    # ---------------------------------------------------------------
    if i >= 0:
        j = n - 1
        while j >= 0:
            if nums[j] > nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                break
            j -= 1

    # ---------------------------------------------------------------
    # TODO 3: i+1부터 끝까지 뒤집기 (두 포인터 방식)
    # KO: left = i+1, right = n-1로 시작해서, left < right인 동안 교환하면서 안쪽으로 좁혀오세요.
    # 주의 (Note): i = -1인 경우에도 left = 0이 되어 전체가 뒤집혀야 합니다.
    # ---------------------------------------------------------------
    left = i + 1
    right = n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# Bonus Challenge : Easy
def previous_permutation(nums):
    n = len(nums)
    i = n - 2
    
    while i >= 0:
        if nums[i] < nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            break
        i -= 1

    if i >= 0:
        j = n - 1
        while j >= 0:
            if nums[j] < nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                break
            j -= 1

    left = i + 1
    right = n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# Bonus Challenge : Medium
def kth_next_permutation(nums, k):
    for rep in range(0, k):
        n = len(nums)
        i = n - 2

        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1

        if i >= 0:
            j = n - 1
            while j >= 0:
                if nums[j] > nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
                    break
                j -= 1

        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# Bonus Challenge : Hard
def is_last_permutation(nums):
    n = len(nums)

    flag = True
    for i in range(0, n-1):
        if nums[i] < nums[i+1]:
            flag = False
            break

    if flag:
        return "It is last permutation"
    else:
        return "It is not last permutation"
    


# ============================================================
# ⚠️ 아래 부분은 수정하지 마세요 (DO NOT MODIFY BELOW)
# ============================================================
if __name__ == "__main__":
    # 테스트 1: 일반적인 경우 (Typical case)
    nums1 = [1, 2, 3]
    next_permutation(nums1)
    print(f"테스트 1 (Test 1): {nums1}")
    # 예상 (Expected): [1, 3, 2]

    # 테스트 2: 가장 큰 → 가장 작은 (Largest → smallest)
    nums2 = [3, 2, 1]
    next_permutation(nums2)
    print(f"테스트 2 (Test 2): {nums2}")
    # 예상 (Expected): [1, 2, 3]

    # 테스트 3: 중복 (With duplicates)
    nums3 = [1, 1, 5]
    next_permutation(nums3)
    print(f"테스트 3 (Test 3): {nums3}")
    # 예상 (Expected): [1, 5, 1]

    # 테스트 4: 길이 1 (Length 1)
    nums4 = [1]
    next_permutation(nums4)
    print(f"테스트 4 (Test 4): {nums4}")
    # 예상 (Expected): [1]

    # 테스트 5: 까다로운 경우 (Tricky case)
    nums5 = [1, 3, 2]
    next_permutation(nums5)
    print(f"테스트 5 (Test 5): {nums5}")
    # 예상 (Expected): [2, 1, 3]

    # Bonus 1: 사전순으로 이전 순열을 만드는 함수
    nums6 = [1, 3, 2]
    previous_permutation(nums6)
    print(f"테스트 6 (Bonus 1): {nums6}")
    # 예상 (Expected): [1, 2, 3]

    nums7 = [1, 2, 3]
    previous_permutation(nums7)
    print(f"테스트 7 (Bonus 1): {nums7}")
    # 예상 (Expected): [3, 2, 1]

    nums8 = [1, 2, 4, 3, 5, 6]
    previous_permutation(nums8)
    print(f"테스트 8 (Bonus 1): {nums8}")
    # 예상 (Expected): [1, 2, 3, 6, 5, 4]

    # Bonus 2: next_permutation을 k번 적용한 결과를 만드는 함수
    nums9 = [1, 2, 4, 3, 5, 6]
    kth_next_permutation(nums9, 0)
    print(f"테스트 9 (Bonus 2): {nums9}")

    nums10 = [1, 2, 4, 3, 5, 6]
    kth_next_permutation(nums10, 1)
    print(f"테스트 9 (Bonus 2): {nums10}")

    nums11 = [1, 2, 4, 3, 5, 6]
    kth_next_permutation(nums11, 2)
    print(f"테스트 9 (Bonus 2): {nums11}")

    # Bonus 3: 현재 배치가 사전순으로 가장 마지막 순열인지 판단하는 함수
    nums12 = [6, 5, 4, 3, 2, 1]
    print(f"테스트 12 (Bonus 3): {is_last_permutation(nums12)}")

    nums13 = [1, 2, 4, 3, 5, 6]
    print(f"테스트 13 (Bonus 3): {is_last_permutation(nums13)}")

    nums14 = [6, 2, 1]
    print(f"테스트 14 (Bonus 3): {is_last_permutation(nums14)}")