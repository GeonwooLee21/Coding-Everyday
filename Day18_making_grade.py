# =============================================================
# 🐍 Making the Grade — Skeleton Code / 뼈대 코드
# =============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260416
# =============================================================

# =====================================================
# 함수 1 / Function 1: round_scores
# =====================================================
# 🇰🇷 소수점 점수들을 정수로 반올림해서 새 리스트로 반환하세요.
# 🇺🇸 Round each float score to the nearest int and return a new list.

def round_scores(student_scores):
    # TODO (KR): 반올림된 점수를 담을 빈 리스트를 만드세요.
    # TODO (EN): Create an empty list to hold the rounded scores.
    rounded = []

    # TODO (KR): student_scores를 반복하면서 각 점수를 round()로 반올림하세요.
    # TODO (EN): Loop through student_scores and round() each score.
    for score in student_scores:
        rounded.append(round(score))  # 여기를 수정하세요 / Replace this line

    # TODO (KR): 완성된 리스트를 반환하세요.
    # TODO (EN): Return the completed list.
    return rounded


# =====================================================
# 함수 2 / Function 2: count_failed_students
# =====================================================
# 🇰🇷 40점 이하인 학생의 수를 세어서 반환하세요.
# 🇺🇸 Count and return how many students scored 40 or below.

def count_failed_students(student_scores):
    # TODO (KR): 불합격자 수를 세는 카운터 변수를 만드세요.
    # TODO (EN): Create a counter variable to count failures.
    failed_count = 0

    # TODO (KR): 각 점수를 확인해서 40 이하이면 카운터를 1 올리세요.
    # TODO (EN): Check each score — if it's 40 or below, add 1 to your counter.
    for score in student_scores:
        if score <= 40:  # 여기를 수정하세요 / Replace this line
            failed_count += 1

    # TODO (KR): 최종 카운터를 반환하세요.
    # TODO (EN): Return the final counter.
    return failed_count


# =====================================================
# 함수 3 / Function 3: above_threshold
# =====================================================
# 🇰🇷 threshold 이상인 점수들만 골라서 새 리스트로 반환하세요.
# 🇺🇸 Collect scores >= threshold and return them as a new list.

def above_threshold(student_scores, threshold):
    # TODO (KR): 조건에 맞는 점수를 담을 빈 리스트를 만드세요.
    # TODO (EN): Create an empty list to hold qualifying scores.
    top_scores = []

    # TODO (KR): 각 점수가 threshold 이상인지 확인하고, 맞으면 리스트에 추가하세요.
    # TODO (EN): Check each score — if it's >= threshold, add it to the list.
    for score in student_scores:
        if score >= threshold:  # 여기를 수정하세요 / Replace this line
            top_scores.append(score)

    # TODO (KR): 완성된 리스트를 반환하세요.
    # TODO (EN): Return the completed list.
    return top_scores


# =====================================================
# 함수 4 / Function 4: student_ranking
# =====================================================
# 🇰🇷 점수와 이름을 매칭해서 순위 문자열 리스트를 반환하세요.
#     형식: "1. 이름: 점수"
# 🇺🇸 Match scores and names into a ranked list of strings.
#     Format: "1. Name: Score"

def student_ranking(student_scores, student_names):
    # TODO (KR): 순위 문자열을 담을 빈 리스트를 만드세요.
    # TODO (EN): Create an empty list to hold the ranking strings.
    rankings = []

    # TODO (KR): range(len(student_scores))로 각 인덱스 i를 반복하세요.
    #            student_scores[i]와 student_names[i]로 같은 위치의 값을 가져오세요.
    #            i + 1이 순위가 됩니다.
    # TODO (EN): Use range(len(student_scores)) to loop through each index i.
    #            Access matching values with student_scores[i] and student_names[i].
    #            i + 1 is the rank.
    for i in range(len(student_scores)):
        rankings.append(f'{i+1}. {student_names[i]}: {student_scores[i]}')  # 여기를 수정하세요 / Replace this line

    # TODO (KR): 완성된 리스트를 반환하세요.
    # TODO (EN): Return the completed list.
    return rankings


# =====================================================
# 🧪 테스트 / Tests — 수정하지 마세요! / Do not modify!
# =====================================================

if __name__ == "__main__":
    print("=" * 50)
    print("🧪 테스트 시작 / Running Tests")
    print("=" * 50)

    # Test 1: round_scores
    scores1 = [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]
    result1 = round_scores(scores1)
    print(f"\n[함수1/Func1] round_scores 결과: {result1}")
    print(f"  → 모두 정수인가요? {all(isinstance(s, int) for s in result1)}")

    # Test 2: count_failed_students
    scores2 = [90, 40, 55, 70, 30, 25, 80, 95, 38, 40]
    result2 = count_failed_students(scores2)
    print(f"\n[함수2/Func2] 불합격자 수: {result2}")
    print(f"  → 정답(Expected): 5 | 맞나요? {result2 == 5}")

    # Test 3: above_threshold — 75점 이상
    scores3 = [90, 40, 55, 70, 30, 68, 70, 75, 83, 96]
    result3 = above_threshold(scores3, 75)
    print(f"\n[함수3/Func3] 75점 이상: {result3}")
    print(f"  → 정답(Expected): [90, 75, 83, 96] | 맞나요? {result3 == [90, 75, 83, 96]}")

    # Test 3b: above_threshold — 빈 결과 확인
    result3b = above_threshold(scores3, 100)
    print(f"[함수3/Func3] 100점 이상: {result3b}")
    print(f"  → 정답(Expected): [] | 맞나요? {result3b == []}")

    # Test 4: student_ranking
    s_scores = [100, 99, 90, 84, 66, 53, 47]
    s_names  = ['Joci', 'Sara', 'Kora', 'Jan', 'John', 'Bern', 'Fred']
    result4 = student_ranking(s_scores, s_names)
    expected4 = ['1. Joci: 100', '2. Sara: 99', '3. Kora: 90',
                 '4. Jan: 84', '5. John: 66', '6. Bern: 53', '7. Fred: 47']
    print(f"\n[함수4/Func4] 순위표:")
    for line in result4:
        print(f"  {line}")
    print(f"  → 맞나요? {result4 == expected4}")

    print("\n" + "=" * 50)
    print("✅ 테스트 완료! / Tests done!")
    print("=" * 50)