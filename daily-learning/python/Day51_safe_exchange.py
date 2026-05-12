"""
===============================================================
Wonder Exchange Co. — 안전한 환전 계산기 / Safe Exchange Calculator
===============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260509
===============================================================

예외 처리(Exception Handling) 연습 / Exception Handling Practice

지시사항 / Instructions:
- 아래 TODO 번호 순서대로 함수를 완성하세요.
  Complete the functions following the TODO numbers below.
- 함수 이름과 변수 이름은 모두 snake_case 입니다.
  All function and variable names use snake_case.
- 맨 아래 테스트 블록은 수정하지 마세요!
  Do NOT modify the test block at the bottom!
"""

# Bonus Challenge: Easy
def safe_divide(a, b):
    try:
        divide = a / b
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero")
    
    return divide
    
def safe_exchange_rate2(home_amount, foreign_amount):
    if isinstance(home_amount, bool) or not isinstance(home_amount, (int, float)):
        raise TypeError("home_amount must be a number")

    if isinstance(foreign_amount, bool) or not isinstance(foreign_amount, (int, float)):
        raise TypeError("foreign_amount must be a number")

    if home_amount <= 0:
        raise ValueError("home_amount must be positive")

    if foreign_amount < 0:
        raise ValueError("foreign_amount must be positive")

    return safe_divide(foreign_amount, home_amount)
 
def safe_exchange_rate(home_amount, foreign_amount):
    """자국 통화 대비 외국 통화의 환율을 계산합니다.
    Calculate the exchange rate of foreign currency vs home currency.

    잘못된 입력에는 예외를 발생시킵니다.
    Raise exceptions for invalid input.
    """
    # TODO 1: home_amount 가 숫자(int 또는 float) 인지 확인하세요.
    #         Check that home_amount is a number (int or float).
    #         숫자가 아니면 TypeError를 발생시키세요.
    #         If not, raise TypeError with a clear message.
    #         힌트 / Hint: isinstance(x, (int, float)) 사용. bool은 별도로 거름!
    #                      Use isinstance. Filter bool separately!
    if isinstance(home_amount, bool) or not isinstance(home_amount, (int, float)):
        raise TypeError("home_amount must be a number")

    # TODO 2: foreign_amount 도 같은 방식으로 검사하세요.
    #         Check foreign_amount the same way.
    if isinstance(foreign_amount, bool) or not isinstance(foreign_amount, (int, float)):
        raise TypeError("foreign_amount must be a number")

    # TODO 3: home_amount 가 0 이하면 ValueError를 발생시키세요.
    #         If home_amount <= 0, raise ValueError.
    #         메시지 예시 / Example message: "home_amount must be positive"
    if home_amount <= 0:
        raise ValueError("home_amount must be positive")

    # TODO 4: foreign_amount 가 음수면 ValueError를 발생시키세요.
    #         (0은 허용 — 환율 계산에는 의미 없지만 수학적으로 가능)
    #         If foreign_amount < 0, raise ValueError.
    #         (0 is allowed — meaningless rate but mathematically valid)
    if foreign_amount < 0:
        raise ValueError("foreign_amount must be positive")

    # TODO 5: foreign_amount / home_amount 를 반환하세요.
    #         Return foreign_amount / home_amount.
    return foreign_amount / home_amount


def convert_money(amount_str, rate_str):
    """문자열로 받은 금액과 환율로 환전 결과를 계산합니다.
    Convert money using string-form amount and rate.

    파싱 실패나 잘못된 값이면 ValueError를 발생시킵니다.
    Raise ValueError for parsing failures or invalid values.
    """
    # TODO 6: try / except 를 사용해서 amount_str 을 float 로 변환하세요.
    #         Use try/except to convert amount_str to float.
    #         실패하면 더 친절한 메시지의 ValueError 를 raise 하세요.
    #         On failure, raise a ValueError with a friendlier message.
    #         예시 / Example: f"amount must be a number, got: {amount_str!r}"
    #         힌트 / Hint: float() 는 TypeError 와 ValueError 둘 다 낼 수 있어요.
    #                      float() can raise both TypeError and ValueError.
    try:
        amount = float(amount_str)
    except (ValueError, TypeError):
        raise ValueError(f"amount must be a number, got: {amount_str!r}")

    # TODO 7: 같은 방식으로 rate_str 도 float 로 변환하세요.
    #         Convert rate_str to float the same way.
    try:
        rate = float(rate_str)
    except (ValueError, TypeError):
        raise ValueError(f"rate must be a number, got: {rate_str!r}")

    # TODO 8: amount 가 음수이면 ValueError 를 발생시키세요.
    #         If amount < 0, raise ValueError.
    if amount < 0:
        raise ValueError("amount must be positive")

    # TODO 9: rate 가 0 이하이면 ValueError 를 발생시키세요.
    #         If rate <= 0, raise ValueError.
    if rate <= 0:
        raise ValueError("rate must be positive")

    # TODO 10: amount * rate 를 반환하세요.
    #          Return amount * rate.
    return amount * rate

# Bonus Challenge: Medium
def convert_money_with_log(amount_str, rate_str):
    try:
        amount = float(amount_str)
        rate = float(rate_str)
    except (ValueError, TypeError):
        print("Conversion failed.")
        raise ValueError(f"amount must be a number, got: {amount_str!r}")
    else:
        print("Conversion successful!")
    finally:
        print("Transaction logged.")

    # try 블록 밖에서 검증
    if amount < 0:
        raise ValueError("amount must be positive")
    if rate <= 0:
        raise ValueError("rate must be positive")

    return amount * rate

# ============================================================
# 테스트 블록 (수정하지 마세요!) / Test Block (Do NOT modify!)
# ============================================================
if __name__ == "__main__":
    print("=== 정상 케이스 / Happy Path ===")
    try:
        print(f"safe_exchange_rate(100, 130) = {safe_exchange_rate(100, 130)}")
        print(f"convert_money('100', '1.3') = {convert_money('100', '1.3')}")
    except Exception as e:
        print(f"❌ 예상치 못한 예외 / Unexpected exception: {type(e).__name__}: {e}")

    print("\n=== ValueError 테스트 / ValueError Tests ===")
    for h, f in [(0, 130), (-5, 130), (100, -10)]:
        try:
            safe_exchange_rate(h, f)
            print(f"❌ FAIL: safe_exchange_rate({h}, {f}) did not raise")
        except ValueError as e:
            print(f"✅ PASS: safe_exchange_rate({h}, {f}) → ValueError: {e}")
        except Exception as e:
            print(f"❌ FAIL: safe_exchange_rate({h}, {f}) → {type(e).__name__}: {e}")

    print("\n=== TypeError 테스트 / TypeError Tests ===")
    for h, f in [("100", 130), (100, "130"), (None, 130)]:
        try:
            safe_exchange_rate(h, f)
            print(f"❌ FAIL: safe_exchange_rate({h!r}, {f!r}) did not raise")
        except TypeError as e:
            print(f"✅ PASS: safe_exchange_rate({h!r}, {f!r}) → TypeError: {e}")
        except Exception as e:
            print(f"❌ FAIL: safe_exchange_rate({h!r}, {f!r}) → {type(e).__name__}: {e}")

    print("\n=== convert_money 파싱 테스트 / Parsing Tests ===")
    for a, r in [("abc", "1.3"), ("100", "xyz"), ("-50", "1.3"), ("100", "0")]:
        try:
            convert_money(a, r)
            print(f"❌ FAIL: convert_money({a!r}, {r!r}) did not raise")
        except ValueError as e:
            print(f"✅ PASS: convert_money({a!r}, {r!r}) → ValueError: {e}")
        except Exception as e:
            print(f"❌ FAIL: convert_money({a!r}, {r!r}) → {type(e).__name__}: {e}")
