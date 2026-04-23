# =============================================================
# multiple_return_values_skeleton.py
# 🐍 Multiple Return Values Practice — Skeleton File
# =============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260420
# =============================================================

# ──────────────────────────────────────────────
# 함수 1 / Function 1: split_bill
# ──────────────────────────────────────────────
# 시나리오: 식당 계산서를 여러 명이 나눠 냅니다.
# Scenario: Split a restaurant bill among a group.
#
# 반환 순서 / Return order: tip, total_with_tip, per_person
#
# 공식 / Formula:
#   tip            = total × tip_rate
#   total_with_tip = total + tip
#   per_person     = total_with_tip ÷ num_people

def split_bill(total: float, num_people: int, tip_rate: float = 0.1):
    # TODO 1-1 (KO): total에 tip_rate를 곱해서 팁 금액을 계산하세요.
    # TODO 1-1 (EN): Multiply total by tip_rate to calculate the tip amount.
    tip = total * tip_rate  # ← 이 줄을 수정하세요 / modify this line

    # TODO 1-2 (KO): total에 tip을 더해서 팁 포함 총액을 계산하세요.
    # TODO 1-2 (EN): Add tip to total to get the total amount including tip.
    total_with_tip = total + tip  # ← 이 줄을 수정하세요 / modify this line

    # TODO 1-3 (KO): total_with_tip을 num_people로 나눠서 1인당 금액을 계산하세요.
    # TODO 1-3 (EN): Divide total_with_tip by num_people to get each person's share.
    per_person = total_with_tip / num_people  # ← 이 줄을 수정하세요 / modify this line

    # TODO 1-4 (KO): 세 값을 한 번에 반환하세요: tip, total_with_tip, per_person
    # TODO 1-4 (EN): Return all three values at once: tip, total_with_tip, per_person
    return tip, total_with_tip, per_person


# ──────────────────────────────────────────────
# 함수 2 / Function 2: get_grade
# ──────────────────────────────────────────────
# 시나리오: 시험 점수로 등급, 합불, 피드백을 동시에 반환합니다.
# Scenario: From a test score, return letter grade, pass/fail, and feedback.
#
# 반환 순서 / Return order: letter, status, message
#
# 기준 / Criteria:
#   90 이상 / and above → "A", "Pass", "Excellent!"
#   80 이상 / and above → "B", "Pass", "Good job!"
#   70 이상 / and above → "C", "Pass", "Keep it up!"
#   60 이상 / and above → "D", "Pass", "Needs improvement."
#   60 미만 / below 60  → "F", "Fail", "Please retake."

def get_grade(score: int):
    # TODO 2-1 (KO): if/elif/else로 score에 따라 letter, status, message를 결정하세요.
    #                경계값 주의: 90점은 A, 60점은 D입니다.
    # TODO 2-1 (EN): Use if/elif/else to set letter, status, and message based on score.
    #                Watch the boundaries: 90 is an A, 60 is a D.
    letter = ""
    status = ""
    message = ""

    if score >= 90:
        letter, status, message = "A", "Pass", "Excellent!"
    elif score >= 80:
        letter, status, message = "B", "Pass", "Good job!"
    elif score >= 70:
        letter, status, message = "C", "Pass", "Keep it up!"
    elif score >= 60:
        letter, status, message = "D", "Pass", "Needs improvement."
    else:
        letter, status, message = "F", "Fail", "Please retake"

    # TODO 2-2 (KO): 세 값을 한 번에 반환하세요: letter, status, message
    # TODO 2-2 (EN): Return all three values at once: letter, status, message
    return letter, status, message


# ──────────────────────────────────────────────
# 함수 3 / Function 3: analyze_temperature
# ──────────────────────────────────────────────
# 시나리오: 온도를 받아 섭씨, 화씨, 체감 상태를 동시에 반환합니다.
# Scenario: Take a temperature and return Celsius, Fahrenheit, and a feel description.
#
# 반환 순서 / Return order: celsius, fahrenheit, condition
#
# 변환 공식 / Conversion formulas:
#   섭씨 → 화씨 / C → F: fahrenheit = celsius × 9/5 + 32
#   화씨 → 섭씨 / F → C: celsius    = (fahrenheit - 32) × 5/9
#
# 체감 상태 (섭씨 기준) / Feel condition (based on Celsius):
#   0 이하     / 0 or below    → "Freezing"
#   0 초과~15 미만 / above 0, below 15 → "Cold"
#   15~25 미만 / 15 to below 25 → "Comfortable"
#   25~35 미만 / 25 to below 35 → "Warm"
#   35 이상    / 35 and above   → "Hot"

def analyze_temperature(temp: float, unit: str = "C"):
    # TODO 3-1 (KO): unit이 "F"이면 섭씨로 변환하고, 아니면 temp를 그대로 celsius로 사용하세요.
    # TODO 3-1 (EN): If unit is "F", convert to Celsius. Otherwise, use temp directly as celsius.
    if unit == "F":
        celsius = (temp - 32) * (5/9)  # ← 변환 공식으로 수정하세요 / replace with conversion formula
    else:
        celsius = temp  # ← temp를 그대로 사용하세요 / just use temp as-is

    # TODO 3-2 (KO): celsius를 화씨로 변환하세요.
    # TODO 3-2 (EN): Convert celsius to Fahrenheit.
    fahrenheit = (celsius * (9/5)) + 32  # ← 이 줄을 수정하세요 / modify this line

    # TODO 3-3 (KO): celsius 값에 따라 condition을 결정하세요 (위의 기준표 참고).
    # TODO 3-3 (EN): Determine the condition based on celsius (see the table above).
    condition = ""
    if celsius <= 0:
        condition = "Freezing"
    elif celsius > 0 and celsius < 15:
        condition = "Cold"
    elif celsius >= 15 and celsius < 25:
        condition = "Comfortable"
    elif celsius >= 25 and celsius < 35:
        condition = "Warm"
    elif celsius >= 35:
        condition = "Hot"


    # TODO 3-4 (KO): 세 값을 한 번에 반환하세요: celsius, fahrenheit, condition
    # TODO 3-4 (EN): Return all three values at once: celsius, fahrenheit, condition
    return celsius, fahrenheit, condition


# ──────────────────────────────────────────────
# 함수 4 / Function 4: calculate_rectangle
# ──────────────────────────────────────────────
# 시나리오: 직사각형의 넓이, 둘레, 대각선 길이를 동시에 반환합니다.
# Scenario: Return the area, perimeter, and diagonal of a rectangle.
#
# 반환 순서 / Return order: area, perimeter, diagonal
#
# 공식 / Formula:
#   area      = width × height
#   perimeter = 2 × (width + height)
#   diagonal  = (width**2 + height**2) ** 0.5    ← 제곱근 / square root

def calculate_rectangle(width: float, height: float):
    # TODO 4-1 (KO): width × height로 넓이를 계산하세요.
    # TODO 4-1 (EN): Calculate area as width × height.
    area = width * height  # ← 이 줄을 수정하세요 / modify this line

    # TODO 4-2 (KO): 2 × (width + height)로 둘레를 계산하세요.
    # TODO 4-2 (EN): Calculate perimeter as 2 × (width + height).
    perimeter = 2 * (width + height)  # ← 이 줄을 수정하세요 / modify this line

    # TODO 4-3 (KO): (width**2 + height**2) ** 0.5 로 대각선 길이를 계산하세요.
    #                import math 없이 가능합니다!
    # TODO 4-3 (EN): Calculate diagonal as (width**2 + height**2) ** 0.5.
    #                No import math needed!
    diagonal = (width**2 + height**2) ** 0.5  # ← 이 줄을 수정하세요 / modify this line

    # TODO 4-4 (KO): 세 값을 한 번에 반환하세요: area, perimeter, diagonal
    # TODO 4-4 (EN): Return all three values at once: area, perimeter, diagonal
    return area, perimeter, diagonal


# ──────────────────────────────────────────────
# 🧪 테스트 / Test Cases
# ──────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50)
    print("테스트 1 / Test 1: split_bill")
    print("=" * 50)
    tip, total_with_tip, per_person = split_bill(100000, 4)
    print(tip, total_with_tip, per_person)   # 10000.0 110000.0 27500.0

    tip, total_with_tip, per_person = split_bill(80000, 2, 0.15)
    print(tip, total_with_tip, per_person)   # 12000.0 92000.0 46000.0

    tip, total_with_tip, per_person = split_bill(60000, 3, 0.0)
    print(tip, total_with_tip, per_person)   # 0.0 60000.0 20000.0

    print()
    print("=" * 50)
    print("테스트 2 / Test 2: get_grade")
    print("=" * 50)

    letter, status, message = get_grade(95)
    result = get_grade(95)
    
    print(letter, status, message) # 언패킹 → 각 변수에 분리 저장
    print(result) # Q2 : 언패킹 없음 → tuple 값이 반환된다.

    letter, status, message = get_grade(83)
    print(letter, status, message)   # B Pass Good job!

    letter, status, message = get_grade(71)
    print(letter, status, message)   # C Pass Keep it up!

    letter, status, message = get_grade(65)
    print(letter, status, message)   # D Pass Needs improvement.

    letter, status, message = get_grade(50)
    print(letter, status, message)   # F Fail Please retake.

    letter, status, message = get_grade(90)
    print(letter, status, message)   # A Pass Excellent!   (경계값 / boundary)

    letter, status, message = get_grade(60)
    print(letter, status, message)   # D Pass Needs improvement.  (경계값 / boundary)

    print()
    print("=" * 50)
    print("테스트 3 / Test 3: analyze_temperature")
    print("=" * 50)
    celsius, fahrenheit, condition = analyze_temperature(0)
    print(celsius, fahrenheit, condition)          # 0 32.0 Freezing

    celsius, fahrenheit, condition = analyze_temperature(20)
    print(celsius, fahrenheit, condition)          # 20 68.0 Comfortable

    celsius, fahrenheit, condition = analyze_temperature(100)
    print(celsius, fahrenheit, condition)          # 100 212.0 Hot

    celsius, fahrenheit, condition = analyze_temperature(32, "F")
    print(celsius, fahrenheit, condition)          # 0.0 32.0 Freezing

    celsius, fahrenheit, condition = analyze_temperature(98.6, "F")
    print(celsius, fahrenheit, condition)          # 37.0 98.6 Hot

    print()
    print("=" * 50)
    print("테스트 4 / Test 4: calculate_rectangle")
    print("=" * 50)
    area, perimeter, diagonal = calculate_rectangle(3, 4)
    print(area, perimeter, diagonal)   # 12 14 5.0

    area, perimeter, diagonal = calculate_rectangle(5, 5)
    print(area, perimeter, diagonal)   # 25 20 7.07...

    area, perimeter, diagonal = calculate_rectangle(1, 1)
    print(area, perimeter, diagonal)   # 1 4 1.414...

    area, perimeter, diagonal = calculate_rectangle(10, 2)
    print(area, perimeter, diagonal)   # 20 24 10.198...
