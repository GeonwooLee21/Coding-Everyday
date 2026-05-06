"""
=============================================================
🏹 양궁 점수 계산기 — `import` 문법 연습
🏹 Archery Score Calculator — `import` syntax practice
=============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260507
=============================================================

학생용 스켈레톤 파일. TODO 주석을 따라 함수를 완성하세요.
Student skeleton file. Follow the TODO comments to complete the function.
"""

# TODO 1: math 모듈을 import 하세요.
# TODO 1: Import the math module.
import math

def calculate_arrow_score(x: float, y: float) -> int:
    """
    화살이 (x, y)에 꽂혔을 때의 점수를 반환합니다.
    Returns the score when an arrow lands at position (x, y).

    정중앙 (0, 0)으로부터의 거리에 따라 점수가 결정됩니다.
    Score is based on distance from the bullseye at (0, 0).
    """
    # TODO 2: math.sqrt를 사용해 (0, 0)으로부터의 거리를 계산하세요.
    #         거리 공식: √(x² + y²)
    # TODO 2: Use math.sqrt to compute distance from (0, 0).
    #         Distance formula: √(x² + y²)
    distance = math.sqrt(x**2+y**2)  # ← 이 줄을 수정하세요 / modify this line

    # TODO 3: 거리가 50을 초과하면 0을 반환하세요. (과녁 벗어남)
    # TODO 3: If distance exceeds 50, return 0. (missed the target)
    if distance > 50:  # ← 이 줄을 수정하세요 / modify this line
        return 0

    # TODO 4: math.floor를 사용해 (10 - distance / 5) 의 내림값을 반환하세요.
    # TODO 4: Use math.floor to return the floor of (10 - distance / 5).
    return math.floor(10 - distance / 5)  # ← 이 줄을 수정하세요 / modify this line

# Bonus Challenge - Easy: import 스타일 바꾸기
from math import sqrt, floor

def calculate_arrow_score_v2(x: float, y: float) -> int:
    distance = sqrt(x**2+y**2)

    if distance > 50:
        return 0
    
    return floor(10 - distance / 5)

# Bonus Challenge - Medium: as로 별칭 사용하기
import math as m

def calculate_arrow_score_v3(x: float, y: float) -> int:
    distance = m.sqrt(x**2+y**2)

    if distance > 50:
        return 0
    
    return m.floor(10 - distance / 5)

# Bonus Challenge - Hard: random 모듈 미리보기
import math
import random

def arrow_simulation():
    total = 0

    for _ in range(10):
        x = random.uniform(-30, 30)
        y = random.uniform(-30, 30)
        total += calculate_arrow_score(x, y)
    
    print(f"무작위 화살 10발의 총점: {total}점")



# ===== 테스트 블록 (수정 금지) / Test block (do not modify) =====
if __name__ == "__main__":
    test_cases = [
        ((0, 0), 10),       # 정중앙 / bullseye
        ((3, 4), 9),        # 3-4-5 직각삼각형 / right triangle
        ((6, 8), 8),        # 거리 10 / distance 10
        ((30, 40), 0),      # 거리 50 (경계) / distance 50 (boundary)
        ((60, 0), 0),       # 과녁 벗어남 / off-target
        ((-6, -8), 8),      # 음수 좌표 / negative coords
        ((10, 0), 8),       # 거리 10, x축 위 / distance 10, on x-axis
    ]

    print("=" * 50)
    print("양궁 점수 테스트 / Archery Score Tests")
    print("=" * 50)

    passed = 0
    for (x, y), expected in test_cases:
        try:
            result = calculate_arrow_score_v3(x, y)
            status = "✓ PASS" if result == expected else "✗ FAIL"
            if result == expected:
                passed += 1
            print(f"  {status} | ({x:4}, {y:4}) → {result} (예상/expected: {expected})")
        except Exception as e:
            print(f"  ✗ ERROR | ({x:4}, {y:4}) → {type(e).__name__}: {e}")

    print("=" * 50)
    print(f"결과 / Result: {passed}/{len(test_cases)} 통과 / passed")
    print("=" * 50)
    
    # Bonus Challenge - Hard: random 모듈 미리보기
    print("Bonus Challenge - Hard: 화살 시뮬레이션 결과")
    arrow_simulation()
