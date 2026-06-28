"""
=================================================================
🏦 Wonder Pay 결제 게이트웨이
🏦 Wonder Pay Payment Gateway
=================================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260618
=================================================================

지시사항 / Instructions:
- 각 TODO를 채워 네 개의 클래스를 완성하세요.
- Fill in each TODO to complete the four classes.
- 아래 테스트 블록(TEST BLOCK)은 수정하지 마세요!
- Do NOT modify the protected test block at the bottom!
"""

# TODO 1: abc 모듈에서 ABC와 abstractmethod를 import 하세요.
#         Import ABC and abstractmethod from the abc module.
from abc import ABC, abstractmethod


# TODO 2: PaymentMethod 클래스를 정의하세요. ABC를 상속해야 합니다.
#         Define the PaymentMethod class. It must inherit from ABC.
class PaymentMethod(ABC):

    # TODO 3: fee_rate를 추상 메서드로 만드세요.
    #         Make fee_rate an abstract method.
    @abstractmethod
    def fee_rate(self) -> float:
        ...

    # TODO 4: label을 추상 메서드로 만드세요.
    #         Make label an abstract method.
    @abstractmethod
    def label(self) -> str:
        ...

    # TODO 5: process_payment 템플릿 메서드를 구현하세요 (일반 메서드).
    #         Implement the process_payment template method (a concrete method).
    def process_payment(self, amount: int) -> str:
        # TODO 5a: amount가 0 이하이면 ValueError("amount must be positive") 발생
        #          If amount <= 0, raise ValueError("amount must be positive")
        if amount <= 0:
            raise ValueError("amount must be positive")

        # TODO 5b: fee = amount * 수수료율, round()로 반올림
        #          fee = amount * fee rate, rounded with round()
        fee = round(amount * self.fee_rate())

        # TODO 5c: total = amount + fee
        total = amount + fee

        # TODO 5d: 영수증 문자열 반환
        #          Return the receipt string
        return f"[{self.label()}] amount={amount}, fee={fee}, total={total}"


# TODO 6: CardPayment 클래스 — fee_rate=0.03, label="Credit Card"
class CardPayment(PaymentMethod):
    def fee_rate(self) -> float:
        return 0.03

    def label(self) -> str:
        return "Credit Card"


# TODO 7: BankTransfer 클래스 — fee_rate=0.0, label="Bank Transfer"
class BankTransfer(PaymentMethod):
    def fee_rate(self) -> float:
        return 0.0

    def label(self) -> str:
        return "Bank Transfer"


# TODO 8: MobilePay 클래스 — fee_rate=0.015, label="Mobile Pay"
class MobilePay(PaymentMethod):
    def fee_rate(self) -> float:
        return 0.015

    def label(self) -> str:
        return "Mobile Pay"


# ============================================================
# 🔒 PROTECTED TEST BLOCK — 수정하지 마세요 / DO NOT MODIFY
# ============================================================
if __name__ == "__main__":
    # Test 1: ABC cannot be instantiated
    try:
        PaymentMethod()
        print("❌ FAIL: ABC should not be instantiable")
    except TypeError:
        print("✅ PASS: ABC cannot be instantiated")

    # Test 2: concrete methods + template
    assert CardPayment().process_payment(1000) == "[Credit Card] amount=1000, fee=30, total=1030"
    assert BankTransfer().process_payment(1000) == "[Bank Transfer] amount=1000, fee=0, total=1000"
    assert MobilePay().process_payment(333) == "[Mobile Pay] amount=333, fee=5, total=338"
    print("✅ PASS: concrete subclasses use the shared template correctly")

    # Test 3: validation
    try:
        CardPayment().process_payment(0)
        print("❌ FAIL: non-positive amount should raise")
    except ValueError:
        print("✅ PASS: non-positive amount raises ValueError")

    # Test 4: polymorphism
    methods = [CardPayment(), BankTransfer(), MobilePay()]
    receipts = [m.process_payment(2000) for m in methods]
    assert receipts == [
        "[Credit Card] amount=2000, fee=60, total=2060",
        "[Bank Transfer] amount=2000, fee=0, total=2000",
        "[Mobile Pay] amount=2000, fee=30, total=2030",
    ]
    print("✅ PASS: polymorphism works across all payment methods")
    print("\n🎉 ALL TESTS PASSED!")
