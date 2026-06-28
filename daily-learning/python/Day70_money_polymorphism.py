"""
=================================================================
💰 Money 클래스 만들기 — 폴리모피즘과 던더 메서드 연습
💰 Build a Money Class — Polymorphism & Dunder Methods Practice
=================================================================
시나리오 / Scenario:
  핀테크 스타트업의 결제 시스템에서 사용할 Money 클래스를 만드세요.
  Build a Money class for a FinTech startup's payment system.
=================================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260618
=================================================================
"""


class Money:
    # ========================================
    # TODO 1: __init__ 메서드
    # ========================================
    # 한국어: amount(금액)와 currency(통화)를 받아서 인스턴스 변수로 저장하세요.
    # English: Accept amount and currency, store them as instance attributes.
    #
    # 예시 / Example: Money(100, "USD") 를 만들면
    #   self.amount = 100
    #   self.currency = "USD"
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    # ========================================
    # TODO 2: __str__ 메서드
    # ========================================
    # 한국어: print()와 str()이 호출됩니다. 사람이 읽기 좋은 형식으로 반환.
    # English: Called by print() and str(). Return a human-readable format.
    #
    # 형식 / Format: "{금액(소수점 2자리)} {통화}"
    # 예시 / Example: Money(100, "USD") → "100.00 USD"
    # 힌트 / Hint: f-string에서 {self.amount:.2f} 를 사용하세요.
    def __str__(self):
        return f"{self.amount:,.2f} {self.currency}"

    # ========================================
    # TODO 3: __repr__ 메서드
    # ========================================
    # 한국어: repr()와 REPL에서 호출됩니다. 개발자용 명확한 형식으로 반환.
    # English: Called by repr() and REPL. Return an unambiguous developer-readable format.
    #
    # 형식 / Format: "Money({금액}, '{통화}')"
    # 예시 / Example: Money(100, "USD") → "Money(100, 'USD')"
    # 주의 / Note: 통화 주변의 따옴표가 결과 문자열에 포함되어야 합니다.
    def __repr__(self):
        return f"{self.__class__.__name__}({self.amount}, \'{self.currency}\')"

    # ========================================
    # TODO 4: __eq__ 메서드
    # ========================================
    # 한국어: == 연산자가 호출. 금액과 통화가 모두 같으면 True, 아니면 False.
    # English: Called by ==. Return True if both amount AND currency match.
    #
    # 중요 / Important:
    #   - 통화가 다르면 에러를 발생시키지 말고 False를 반환하세요.
    #   - Different currencies: return False, do NOT raise an error.
    #
    # 예시 / Example:
    #   Money(100, "USD") == Money(100, "USD")  → True
    #   Money(100, "USD") == Money(100, "KRW")  → False
    #   Money(100, "USD") == Money(50,  "USD")  → False
    def __eq__(self, other):
        if self.amount == other.amount and self.currency == other.currency:
            return True
        else:
            return False

    # ========================================
    # TODO 5: __lt__ 메서드
    # ========================================
    # 한국어: < 연산자가 호출. self의 금액이 other보다 작으면 True 반환.
    # English: Called by <. Return True if self.amount < other.amount.
    #
    # 중요 / Important:
    #   - 통화가 다르면 ValueError를 발생시키세요.
    #   - Different currencies: raise ValueError (cannot compare apples to oranges).
    #
    # 메시지 형식 / Error message format:
    #   "Cannot compare {self.currency} with {other.currency}"
    def __lt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Currencies are different.")
        
        return self.amount < other.amount

    # ========================================
    # TODO 6: __add__ 메서드
    # ========================================
    # 한국어: + 연산자가 호출. 두 Money 객체를 더한 새로운 Money 객체 반환.
    # English: Called by +. Return a NEW Money object representing the sum.
    #
    # 중요 / Important:
    #   - 통화가 다르면 ValueError를 발생시키세요.
    #   - self.amount를 직접 수정하지 말고, 새 객체를 만들어 반환하세요.
    #   - Do NOT modify self.amount; create and return a new object.
    #
    # 메시지 형식 / Error message format:
    #   "Cannot add {self.currency} and {other.currency}"
    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Currencies are different.")
        
        return Money(self.amount + other.amount, self.currency)
    # ========================================
    # TODO 7: __sub__ 메서드
    # ========================================
    # 한국어: - 연산자가 호출. 두 Money 객체를 뺀 새로운 Money 객체 반환.
    # English: Called by -. Return a NEW Money object representing the difference.
    #
    # 메시지 형식 / Error message format:
    #   "Cannot subtract {other.currency} from {self.currency}"
    def __sub__(self, other):
        if self.currency != other.currency:
            raise ValueError("Currencies are different.")
        
        return Money(self.amount - other.amount, self.currency)

    # ========================================
    # TODO 8: __mul__ 메서드
    # ========================================
    # 한국어: * 연산자가 호출. 금액에 정수를 곱한 새로운 Money 객체 반환.
    # English: Called by *. Return a NEW Money object with amount × multiplier.
    #
    # 예시 / Example:
    #   Money(10, "USD") * 5  →  Money(50, "USD")
    #
    # 주의 / Note: multiplier는 정수입니다. 통화 검사는 필요 없습니다.
    def __mul__(self, multiplier):
        return Money(self.amount * multiplier, self.currency)


# =============================================================================
# 🎪 자동 테스트 / Automated Tests  (수정하지 마세요 / DO NOT MODIFY)
# =============================================================================
if __name__ == "__main__":
    total = 0
    passed = 0

    def check(label, condition):
        global total, passed
        total += 1
        if condition:
            passed += 1
            print(f"  ✓ {label}")
        else:
            print(f"  ✗ {label}")

    def check_raises(label, func, exception_type):
        global total, passed
        total += 1
        try:
            func()
            print(f"  ✗ {label}  (에러 발생 안 함 / no error raised)")
        except exception_type:
            passed += 1
            print(f"  ✓ {label}")
        except Exception as error:
            print(f"  ✗ {label}  (잘못된 에러 / wrong error: {type(error).__name__})")

    print("=" * 60)
    print("Money 클래스 테스트 / Money class tests")
    print("=" * 60)

    try:
        # ----- 기본 / Basic -----
        print("\n[기본 / Basic]")
        m = Money(100, "USD")
        check("__init__ 의 amount 속성 / __init__ amount", m.amount == 100)
        check("__init__ 의 currency 속성 / __init__ currency", m.currency == "USD")
        check("__str__ 형식 / __str__ format", str(m) == "100.00 USD")
        check("__repr__ 형식 / __repr__ format", repr(m) == "Money(100, 'USD')")

        # ----- 비교 / Comparison -----
        print("\n[비교 / Comparison]")
        check(
            "__eq__ 같은 값 / __eq__ equal",
            Money(100, "USD") == Money(100, "USD"),
        )
        check(
            "__eq__ 다른 금액 / __eq__ different amount",
            not (Money(100, "USD") == Money(50, "USD")),
        )
        check(
            "__eq__ 다른 통화 → False / __eq__ different currency → False",
            not (Money(100, "USD") == Money(100, "KRW")),
        )
        check(
            "__lt__ 기본 / __lt__ basic",
            Money(50, "USD") < Money(100, "USD"),
        )

        # ----- 산술 / Arithmetic -----
        print("\n[산술 / Arithmetic]")
        check(
            "__add__ / addition",
            Money(100, "USD") + Money(50, "USD") == Money(150, "USD"),
        )
        check(
            "__sub__ / subtraction",
            Money(100, "USD") - Money(30, "USD") == Money(70, "USD"),
        )
        check(
            "__mul__ / multiplication",
            Money(25, "USD") * 4 == Money(100, "USD"),
        )

        # ----- 에러 처리 / Error Handling -----
        print("\n[에러 처리 / Error Handling]")
        check_raises(
            "통화 불일치 + / currency mismatch +",
            lambda: Money(100, "USD") + Money(100, "KRW"),
            ValueError,
        )
        check_raises(
            "통화 불일치 - / currency mismatch -",
            lambda: Money(100, "USD") - Money(100, "KRW"),
            ValueError,
        )
        check_raises(
            "통화 불일치 < / currency mismatch <",
            lambda: Money(100, "USD") < Money(100, "KRW"),
            ValueError,
        )

        # ----- 폴리모피즘 / Polymorphism -----
        print("\n[폴리모피즘 / Polymorphism]")
        items = [Money(50, "USD"), Money(10, "USD"), Money(100, "USD")]
        items.sort()
        check("sort() 최솟값 / sort min", items[0] == Money(10, "USD"))
        check("sort() 최댓값 / sort max", items[-1] == Money(100, "USD"))
        check("max() 호환 / max() compat", max(items) == Money(100, "USD"))
        check("min() 호환 / min() compat", min(items) == Money(10, "USD"))

        # ----- 실전 시나리오 / Real-world -----
        print("\n[실전 / Real-world]")
        expenses = [Money(120, "USD"), Money(85, "USD"), Money(200, "USD")]
        total_expense = expenses[0] + expenses[1] + expenses[2]
        check(
            "팀 지출 합계 / team total expenses",
            total_expense == Money(405, "USD"),
        )

    except Exception as error:
        print(f"\n❌ 예상치 못한 에러 / Unexpected error: {type(error).__name__}: {error}")
        print("    먼저 위쪽 TODO 부분을 확인하세요.")
        print("    Check the TODOs above first.")

    # ----- 결과 / Results -----
    print("\n" + "=" * 60)
    if total > 0 and passed == total:
        print(f"🎉 모든 테스트 통과! / All tests passed! ({passed}/{total})")
    else:
        print(f"📊 결과 / Result: {passed}/{total} 통과 / passed")
        print("    실패한 테스트를 확인하고 다시 시도하세요.")
        print("    Review failed tests and try again.")
    print("=" * 60)
