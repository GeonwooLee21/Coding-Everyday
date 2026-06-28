"""
=================================================================
🏦 Python 연습: FinTech 은행 계좌 시스템
🏦 Python Practice: FinTech Bank Account System
=================================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260604
=================================================================

📌 학습 목표 (Learning Goals):
  - 캡슐화 (Encapsulation): private/protected 속성, @property
  - 상속 (Inheritance): super(), 부모-자식 관계
  - 메서드 오버라이딩 (Method Overriding): 같은 이름, 다른 동작
"""


# =================================================================
# Part 1: BankAccount 클래스 (캡슐화)
# Part 1: BankAccount Class (Encapsulation)
# =================================================================

class BankAccount:
    """
    기본 은행 계좌 클래스. 잔액은 외부에서 직접 수정 불가!
    Base bank account class. Balance cannot be modified externally!
    """

    def __init__(self, owner_name: str, initial_balance: float = 0.0):
        # TODO 1: 소유자 이름을 protected 속성 _owner_name 에 저장하세요.
        # TODO 1: Store owner_name in the protected attribute _owner_name.
        self._owner_name = owner_name

        # TODO 2: 초기 잔액을 PRIVATE 속성 __balance 에 저장하세요. (이중 언더스코어!)
        # TODO 2: Store initial_balance in the PRIVATE attribute __balance (double underscore!).
        self.__balance = initial_balance

        # TODO 3: 거래 내역을 저장할 빈 리스트 _transaction_history 를 만드세요.
        # TODO 3: Create an empty list _transaction_history to store transactions.
        self._transaction_history = []

        # TODO 4: 초기 잔액이 0보다 크면, 거래 내역에 "Opened account with $XXX.XX" 형식으로 기록하세요.
        # TODO 4: If initial_balance > 0, append "Opened account with $XXX.XX" to transaction history.
        # 힌트 (Hint): f"Opened account with ${initial_balance:.2f}"
        if initial_balance > 0:
            self._transaction_history.append(f"Opened account with ${initial_balance:.2f}")

    # TODO 5: @property 데코레이터를 사용하여 balance 를 읽기 전용 속성으로 만드세요.
    # TODO 5: Use @property decorator to make balance a read-only attribute.
    # 💡 setter 를 만들지 마세요! 그래야 외부에서 acc.balance = 999 가 막힙니다.
    # 💡 Do NOT create a setter! That's what prevents acc.balance = 999 from outside.
    @property
    def balance(self) -> float:
        return self.__balance

    # TODO 6: @property 를 사용하여 owner_name 을 읽기 전용 속성으로 만드세요.
    # TODO 6: Use @property to make owner_name a read-only attribute.
    @property
    def owner_name(self) -> str:
        return self._owner_name

    def _apply_balance_change(self, change: float) -> None:
        """
        Protected 헬퍼: 자식 클래스가 잔액을 수정할 수 있도록 도와줍니다.
        Protected helper: lets child classes modify the balance cleanly.
        ⚠️ 외부 사용자는 이 메서드를 직접 호출하면 안 됩니다!
        ⚠️ External users should NOT call this method directly!
        """
        # TODO 7: __balance 를 change 만큼 변경하세요. (양수면 증가, 음수면 감소)
        # TODO 7: Change __balance by `change` (positive = increase, negative = decrease).
        self.__balance += change

    def deposit(self, amount: float) -> bool:
        """입금 (Deposit). 성공 시 True, 실패 시 False 반환."""
        # TODO 8: amount 가 0 이하이면 에러 메시지를 출력하고 False 를 반환하세요.
        # TODO 8: If amount <= 0, print an error message and return False.
        if amount <= 0:
            print(f"❌ Deposit amount must be positive. Got: ${amount:.2f}")
            return False

        # TODO 9: __balance 에 amount 를 더하세요.
        # TODO 9: Add amount to __balance.
        self.__balance += amount

        # TODO 10: 거래 내역에 "Deposited $XX.XX" 를 추가하세요.
        # TODO 10: Append "Deposited $XX.XX" to transaction history.
        self._transaction_history.append(f"Deposited ${amount:.2f}")

        return True

    def withdraw(self, amount: float) -> bool:
        """출금 (Withdraw). 성공 시 True, 실패 시 False 반환."""
        # TODO 11: amount 가 0 이하이면 에러 메시지 출력 후 False 반환.
        # TODO 11: If amount <= 0, print error and return False.
        if amount <= 0:
            print(f"❌ Withdrawal amount must be positive. Got: ${amount:.2f}")
            return False

        # TODO 12: amount 가 현재 __balance 보다 크면 에러 메시지 출력 후 False 반환.
        # TODO 12: If amount > current __balance, print error and return False.
        if amount > self.__balance:
            print(f"❌ Insufficient funds. Balance: ${self.__balance:.2f}, Requested: ${amount:.2f}")
            return False

        # TODO 13: __balance 에서 amount 를 빼고, 거래 내역에 "Withdrew $XX.XX" 추가하세요.
        # TODO 13: Subtract amount from __balance, append "Withdrew $XX.XX" to history.
        self.__balance -= amount
        self._transaction_history.append(f"Withdrew ${amount:.2f}")

        return True

    def get_transaction_history(self) -> list:
        """거래 내역 반환. 원본을 보호하기 위해 복사본을 반환합니다."""
        # TODO 14: _transaction_history 의 복사본을 반환하세요.
        # TODO 14: Return a COPY of _transaction_history (use .copy()).
        # 💡 왜 복사본? 외부에서 리스트를 수정해도 내부 데이터가 보호됩니다.
        # 💡 Why a copy? So external code can't tamper with our internal data.
        return self._transaction_history.copy()

    def __str__(self) -> str:
        return f"BankAccount(owner={self._owner_name}, balance=${self.balance:.2f})"


# =================================================================
# Part 2: SavingsAccount (상속 + 메서드 오버라이딩)
# Part 2: SavingsAccount (Inheritance + Method Overriding)
# =================================================================

# TODO 15: SavingsAccount 가 BankAccount 를 상속받도록 작성하세요.
# TODO 15: Make SavingsAccount inherit from BankAccount.
class SavingsAccount(BankAccount):
    """
    적금 계좌: 최소 잔액 $100 유지 필수
    Savings account: must maintain minimum balance of $100
    """

    MINIMUM_BALANCE = 100.0  # 클래스 상수 (Class constant)

    def __init__(self, owner_name: str, initial_balance: float = 0.0, interest_rate: float = 0.02):
        # TODO 16: super().__init__() 를 사용하여 부모 클래스의 __init__ 을 호출하세요.
        # TODO 16: Use super().__init__() to call the parent's __init__.
        # 힌트 (Hint): owner_name 과 initial_balance 를 전달해야 합니다.
        super().__init__(owner_name, initial_balance)

        # TODO 17: 이자율을 protected 속성 _interest_rate 에 저장하세요.
        # TODO 17: Store interest_rate in the protected attribute _interest_rate.
        self._interest_rate = interest_rate

    # TODO 18: withdraw 메서드를 오버라이드하세요!
    # TODO 18: Override the withdraw method!
    def withdraw(self, amount: float) -> bool:
        # 음수/0 검증은 부모와 동일하게 처리
        # Same negative/zero validation as parent
        if amount <= 0:
            print(f"❌ Withdrawal amount must be positive. Got: ${amount:.2f}")
            return False

        # TODO 19: 출금 후 잔액이 MINIMUM_BALANCE 미만이 되면 거부하세요.
        # TODO 19: If balance - amount < MINIMUM_BALANCE, reject the withdrawal.
        # 💡 self.balance 를 사용하세요 (property 로 접근).
        # 💡 Use self.balance (access via property).
        if self.balance - amount < self.MINIMUM_BALANCE:
            print(f"❌ Savings account requires minimum balance of ${self.MINIMUM_BALANCE:.2f}")
            return False

        # TODO 20: 검증 통과 시, super().withdraw(amount) 를 호출하여 실제 출금을 처리하세요.
        # TODO 20: If validation passes, call super().withdraw(amount) to perform the actual withdrawal.
        # 💡 이것이 DRY 원칙입니다 — 부모의 검증/기록 로직을 재사용!
        # 💡 This is the DRY principle — reuse parent's validation/logging logic!
        return super().withdraw(amount)

    def __str__(self) -> str:
        return f"SavingsAccount(owner={self.owner_name}, balance=${self.balance:.2f}, rate={self._interest_rate*100:.1f}%)"


# =================================================================
# Part 3: CheckingAccount (상속 + 메서드 오버라이딩)
# Part 3: CheckingAccount (Inheritance + Method Overriding)
# =================================================================

# TODO 21: CheckingAccount 가 BankAccount 를 상속받도록 작성하세요.
# TODO 21: Make CheckingAccount inherit from BankAccount.
class CheckingAccount(BankAccount):
    """
    입출금 계좌: 마이너스 통장 $500 까지 허용, 마이너스 시 $35 수수료
    Checking account: overdraft up to $500 allowed, $35 fee when going negative
    """

    OVERDRAFT_LIMIT = 500.0   # 마이너스 한도 (Overdraft limit)
    OVERDRAFT_FEE = 35.0      # 마이너스 시 수수료 (Fee when overdrafting)

    # CheckingAccount 는 __init__ 을 따로 정의하지 않습니다.
    # 부모의 __init__ 이 그대로 상속되어 사용됩니다.
    # CheckingAccount does NOT define its own __init__.
    # The parent's __init__ is inherited as-is.

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print(f"❌ Withdrawal amount must be positive. Got: ${amount:.2f}")
            return False

        # TODO 22: 이 출금이 마이너스 잔액을 발생시키는지 확인하세요.
        # TODO 22: Determine whether this withdrawal will cause a negative balance.
        # 💡 (self.balance - amount) < 0 이면 마이너스 발생.
        will_overdraft = (self.balance - amount) < 0 

        # TODO 23: 최종 잔액 계산 (수수료 포함). 마이너스가 발생하면 수수료도 차감.
        # TODO 23: Compute final_balance including the fee if overdraft happens.
        final_balance = self.balance - amount
        if will_overdraft:
            final_balance -= self.OVERDRAFT_FEE

        # TODO 24: final_balance 가 -OVERDRAFT_LIMIT 보다 작으면 거부.
        # TODO 24: If final_balance < -OVERDRAFT_LIMIT, reject.
        # ⚠️ 부등호 방향에 주의! < vs <=
        # ⚠️ Watch the inequality direction! < vs <=
        if final_balance < -self.OVERDRAFT_LIMIT:
            print(f"❌ Withdrawal exceeds overdraft limit of ${self.OVERDRAFT_LIMIT:.2f}")
            return False

        # TODO 25: _apply_balance_change(-amount) 를 호출하여 출금 처리.
        # TODO 25: Call _apply_balance_change(-amount) to perform the withdrawal.
        super()._apply_balance_change(-amount)

        # TODO 26: 거래 내역에 "Withdrew $XX.XX" 추가.
        # TODO 26: Append "Withdrew $XX.XX" to transaction history.
        self._transaction_history.append(f"Withdrew ${amount:.2f}")

        # TODO 27: 마이너스가 발생했다면 수수료 차감 및 기록.
        # TODO 27: If overdraft happened, deduct fee and record it.
        if will_overdraft:
            self._apply_balance_change(-self.OVERDRAFT_FEE)
            self._transaction_history.append(f"Withdrew ${self.OVERDRAFT_FEE:.2f}")
            print(f"⚠️  Overdraft fee of ${self.OVERDRAFT_FEE:.2f} applied")

        return True

    def __str__(self) -> str:
        return f"CheckingAccount(owner={self.owner_name}, balance=${self.balance:.2f})"


# =================================================================
# 🎪 테스트 영역 (수정 금지!)
# 🎪 Test Section (DO NOT MODIFY!)
# =================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("🧪 TEST 1: BankAccount 캡슐화 (Encapsulation)")
    print("=" * 60)
    try:
        acc = BankAccount("Alice", 500)
        assert acc.balance == 500, f"잔액이 500이어야 합니다. 현재: {acc.balance}"
        assert acc.owner_name == "Alice"
        print(f"✓ 계좌 생성: {acc}")

        # balance 가 읽기 전용인지 확인
        try:
            acc.balance = 999999
            print("❌ FAIL: balance 에 setter 가 있으면 안 됩니다!")
        except AttributeError:
            print("✓ balance 는 읽기 전용 (read-only)")

        assert acc.deposit(200) == True
        assert acc.balance == 700
        print(f"✓ 입금 $200 후: {acc}")

        assert acc.deposit(-50) == False, "음수 입금은 거부되어야 합니다"
        assert acc.balance == 700, "음수 입금 후에도 잔액은 동일해야 합니다"
        print("✓ 음수 입금 거부됨")

        assert acc.withdraw(300) == True
        assert acc.balance == 400
        print(f"✓ 출금 $300 후: {acc}")

        assert acc.withdraw(1000) == False, "잔액 초과 출금은 거부되어야 합니다"
        assert acc.balance == 400
        print("✓ 잔액 초과 출금 거부됨")

        history = acc.get_transaction_history()
        assert len(history) == 3, f"거래 내역이 3개여야 합니다. 현재: {len(history)}"
        print(f"✓ 거래 내역: {history}")

        # 거래 내역이 복사본인지 확인
        history.append("HACK!")
        real_history = acc.get_transaction_history()
        assert "HACK!" not in real_history, "거래 내역은 복사본을 반환해야 합니다"
        print("✓ 거래 내역은 복사본을 반환 (내부 데이터 보호됨)")

        print("\n✅ TEST 1 PASSED!\n")
    except AssertionError as e:
        print(f"\n❌ TEST 1 FAILED: {e}\n")
    except Exception as e:
        print(f"\n💥 TEST 1 ERROR: {type(e).__name__}: {e}\n")

    print("=" * 60)
    print("🧪 TEST 2: SavingsAccount (상속 + 오버라이딩)")
    print("=" * 60)
    try:
        sav = SavingsAccount("Bob", 1000, 0.03)
        assert sav.balance == 1000
        assert sav.owner_name == "Bob"
        print(f"✓ 적금 계좌 생성: {sav}")

        # 상속된 deposit 동작 확인
        assert sav.deposit(500) == True
        assert sav.balance == 1500
        print(f"✓ 상속된 입금 동작: {sav}")

        # 일반 출금
        assert sav.withdraw(1000) == True
        assert sav.balance == 500
        print(f"✓ 정상 출금: {sav}")

        # 최소 잔액 위반
        assert sav.withdraw(450) == False, "최소 잔액 미만은 거부되어야 합니다"
        assert sav.balance == 500
        print("✓ 최소 잔액 위반 거부됨")

        # 경계값: 정확히 최소 잔액
        assert sav.withdraw(400) == True, "정확히 최소 잔액까지는 허용되어야 합니다"
        assert sav.balance == 100
        print(f"✓ 경계값 (정확히 최소 잔액) 허용: {sav}")

        # 최소 미만으로 1원도 안 됨
        assert sav.withdraw(1) == False
        print("✓ 최소 잔액 아래로는 단돈 $1 도 출금 불가")

        print("\n✅ TEST 2 PASSED!\n")
    except AssertionError as e:
        print(f"\n❌ TEST 2 FAILED: {e}\n")
    except Exception as e:
        print(f"\n💥 TEST 2 ERROR: {type(e).__name__}: {e}\n")

    print("=" * 60)
    print("🧪 TEST 3: CheckingAccount (마이너스 통장)")
    print("=" * 60)
    try:
        chk = CheckingAccount("Carol", 200)
        print(f"✓ 입출금 계좌 생성: {chk}")

        # 일반 출금
        assert chk.withdraw(100) == True
        assert chk.balance == 100
        print(f"✓ 정상 출금: {chk}")

        # 마이너스 통장 발동 (수수료 포함)
        assert chk.withdraw(200) == True
        assert chk.balance == -135, f"잔액 -135 예상, 현재: {chk.balance}"
        print(f"✓ 마이너스 통장 + 수수료: {chk}")

        # 한도 초과
        chk2 = CheckingAccount("Dave", 100)
        assert chk2.withdraw(700) == False, "한도 초과는 거부되어야 합니다"
        assert chk2.balance == 100
        print("✓ 한도 초과 출금 거부됨")

        print("\n✅ TEST 3 PASSED!\n")
    except AssertionError as e:
        print(f"\n❌ TEST 3 FAILED: {e}\n")
    except Exception as e:
        print(f"\n💥 TEST 3 ERROR: {type(e).__name__}: {e}\n")

    print("=" * 60)
    print("🧪 TEST 4: 다형성 (Polymorphism) — 같은 메서드, 다른 동작")
    print("=" * 60)
    try:
        accounts = [
            BankAccount("Eve", 500),
            SavingsAccount("Frank", 500),
            CheckingAccount("Grace", 500),
        ]
        # 모두 $450 출금 시도
        # 예상: BankAccount → 잔액 50 ✓ / SavingsAccount → 거부 (최소 잔액 위반) /
        #       CheckingAccount → 잔액 50 ✓ (마이너스 안 됨, 수수료 없음)
        for a in accounts:
            result = a.withdraw(450)
            print(f"  {type(a).__name__}: withdraw(450) = {result}, 잔액 = ${a.balance:.2f}")

        assert accounts[0].balance == 50, "BankAccount: 500 - 450 = 50"
        assert accounts[1].balance == 500, "SavingsAccount: 거부되어 변동 없음"
        assert accounts[2].balance == 50, "CheckingAccount: 마이너스 아니므로 수수료 없음"
        print("\n✓ 같은 메서드 호출, 클래스별 다른 동작 = 다형성!\n")

        print("\n✅ TEST 4 PASSED!\n")
    except AssertionError as e:
        print(f"\n❌ TEST 4 FAILED: {e}\n")
    except Exception as e:
        print(f"\n💥 TEST 4 ERROR: {type(e).__name__}: {e}\n")

    print("=" * 60)
    print("🎉 모든 테스트 완료! All tests complete!")
    print("=" * 60)
