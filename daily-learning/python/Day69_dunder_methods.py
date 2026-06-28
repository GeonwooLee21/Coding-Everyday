"""
==============================================================
 던더 메서드 연습: Money 클래스 만들기
 Dunder Methods Practice: Build a Money Class
=================================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260618
=================================================================

시나리오 (Scenario):
글로벌 핀테크 스타트업의 주니어 개발자로서, 결제 시스템에서 사용할
Money 클래스를 만드세요. 던더 메서드를 통해 자연스러운 산술 연산과
출력 기능을 구현합니다.

As a junior developer at a global FinTech startup, build a Money
class for the payment system. Use dunder methods to enable natural
arithmetic operations and string representations.
==============================================================
"""


class Money:
    # ----------------------------------------------------------
    # TODO 1: __init__ 메서드 구현
    #         Implement the __init__ method
    #
    # - amount와 currency 두 개의 파라미터를 받습니다
    #   Accept two parameters: amount and currency
    # - 둘 다 인스턴스 속성으로 저장하세요
    #   Store both as instance attributes
    # ----------------------------------------------------------
    def __init__(self, amount, currency):
        # 여기에 코드 작성 / Your code here
        self.amount = amount
        self.currency = currency

    # ----------------------------------------------------------
    # TODO 2: __str__ 메서드 구현 (사용자용 문자열)
    #         Implement __str__ (user-facing string)
    #
    # - 형식: "1,500.00 USD" (천 단위 콤마, 소수점 2자리)
    #   Format: "1,500.00 USD" (comma thousands, 2 decimals)
    # - 힌트: f-string의 :,.2f 포맷 지정자를 사용하세요
    #   Hint: use the :,.2f format specifier in an f-string
    # ----------------------------------------------------------
    def __str__(self):
        # 여기에 코드 작성 / Your code here
        return f"{self.amount:,.2f} {self.currency}"

    # ----------------------------------------------------------
    # TODO 3: __repr__ 메서드 구현 (개발자용 문자열)
    #         Implement __repr__ (developer-facing string)
    #
    # - 형식: "Money(1500, 'USD')"
    #   Format: "Money(1500, 'USD')"
    # - 통화 코드 주위에 작은따옴표가 필요합니다
    #   Note the single quotes around the currency code
    # ----------------------------------------------------------
    def __repr__(self):
        # 여기에 코드 작성 / Your code here
        # return f"Money({self.amount}, \'{self.currency}\')"
        # self.__class__.__name__은 실제 클래스 이름을 동적으로 가져온다
        return f"{self.__class__.__name__}({self.amount}, '{self.currency}')"

    # ----------------------------------------------------------
    # TODO 4: __add__ 메서드 구현
    #         Implement __add__
    #
    # - 같은 통화일 때만 더하기 허용
    #   Only allow addition when currencies match
    # - 다른 통화면 ValueError 발생
    #   Raise ValueError if currencies differ
    # - 새로운 Money 객체를 반환 (원본 수정 금지!)
    #   Return a NEW Money object (do not mutate self!)
    # ----------------------------------------------------------
    def __add__(self, other):
        # 여기에 코드 작성 / Your code here
        if self.currency != other.currency:
            raise ValueError("Currencies are different.")
        
        return Money(self.amount + other.amount, self.currency)

    # ----------------------------------------------------------
    # TODO 5: __sub__ 메서드 구현
    #         Implement __sub__
    #
    # - __add__와 동일한 규칙 적용
    #   Same rules as __add__
    # - 새로운 Money 객체를 반환
    #   Return a NEW Money object
    # ----------------------------------------------------------
    def __sub__(self, other):
        # 여기에 코드 작성 / Your code here
        if self.currency != other.currency:
            raise ValueError("Currencies are different.")
        
        return Money(self.amount - other.amount, self.currency)

    # ----------------------------------------------------------
    # TODO 6: __mul__ 메서드 구현 (스칼라 곱셈)
    #         Implement __mul__ (scalar multiplication)
    #
    # - other는 Money가 아니라 숫자(int 또는 float)
    #   `other` is a number (int or float), NOT another Money
    # - 통화 검증 불필요 (왜일까요? 🤔)
    #   No currency check needed (why? 🤔)
    # - 새로운 Money 객체를 반환
    #   Return a NEW Money object
    # ----------------------------------------------------------
    def __mul__(self, scalar):
        # 여기에 코드 작성 / Your code here
        return Money(self.amount * scalar, self.currency)


# ==============================================================
# 테스트 블록 - 수정하지 마세요!
# Test block - DO NOT MODIFY!
# ==============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("Money 클래스 테스트 시작 / Starting Money tests")
    print("=" * 50)

    try:
        # Test 1: __str__
        wallet = Money(1500, "USD")
        result = str(wallet)
        expected = "1,500.00 USD"
        status = "✅ PASS" if result == expected else f"❌ FAIL (got: {result!r})"
        print(f"Test 1 [__str__]:  {status}")

        # Test 2: __repr__
        result = repr(wallet)
        expected = "Money(1500, 'USD')"
        status = "✅ PASS" if result == expected else f"❌ FAIL (got: {result!r})"
        print(f"Test 2 [__repr__]: {status}")

        # Test 3: __add__
        salary = Money(3000, "USD")
        bonus = Money(500, "USD")
        total = salary + bonus
        ok = (
            isinstance(total, Money)
            and total.amount == 3500
            and total.currency == "USD"
        )
        status = "✅ PASS" if ok else f"❌ FAIL (got: {total})"
        print(f"Test 3 [__add__]:  {status}")

        # Test 4: __sub__
        balance = Money(1000, "USD")
        payment = Money(250, "USD")
        remaining = balance - payment
        ok = (
            isinstance(remaining, Money)
            and remaining.amount == 750
            and remaining.currency == "USD"
        )
        status = "✅ PASS" if ok else f"❌ FAIL (got: {remaining})"
        print(f"Test 4 [__sub__]:  {status}")

        # Test 5: __mul__
        hourly_wage = Money(25, "USD")
        weekly_pay = hourly_wage * 40
        ok = (
            isinstance(weekly_pay, Money)
            and weekly_pay.amount == 1000
            and weekly_pay.currency == "USD"
        )
        status = "✅ PASS" if ok else f"❌ FAIL (got: {weekly_pay})"
        print(f"Test 5 [__mul__]:  {status}")

        # Test 6: 다른 통화 거부 / Reject different currencies
        usd = Money(100, "USD")
        krw = Money(100, "KRW")
        try:
            usd + krw
            print("Test 6 [diff currency]: ❌ FAIL (should have raised ValueError)")
        except ValueError:
            print("Test 6 [diff currency]: ✅ PASS")

        # Test 7: 큰 숫자 포맷 / Large number formatting
        big = Money(1234567.89, "USD")
        result = str(big)
        expected = "1,234,567.89 USD"
        status = "✅ PASS" if result == expected else f"❌ FAIL (got: {result!r})"
        print(f"Test 7 [big number]: {status}")

        # Test 8: 체이닝 / Chaining
        chained = (Money(100, "USD") + Money(50, "USD")) * 2
        ok = (
            isinstance(chained, Money)
            and chained.amount == 300
            and chained.currency == "USD"
        )
        status = "✅ PASS" if ok else f"❌ FAIL (got: {chained})"
        print(f"Test 8 [chaining]:   {status}")

        print("=" * 50)
        print("테스트 완료! / Tests complete!")
        print("=" * 50)

    except Exception as e:
        print(f"\n⚠️  에러 발생 / Error occurred: {type(e).__name__}: {e}")
        print("힌트: 모든 TODO를 완성했는지 확인하세요.")
        print("Hint: make sure you've completed all TODOs.")
