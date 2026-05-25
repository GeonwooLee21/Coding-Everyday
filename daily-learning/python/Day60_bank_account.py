"""
===============================================================
Day 4: BankAccount - 캡슐화 연습 / Encapsulation Practice
===============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260525
===============================================================

시나리오 / Scenario:
MintBank의 백엔드 개발자로서 안전한 은행 계좌 클래스를 만드세요.
As a MintBank backend developer, build a safe bank account class.

오늘의 핵심 / Today's focus:
밑줄(_)을 사용한 캡슐화 + getter/setter 메서드
Encapsulation via underscore convention + getter/setter methods
"""


class BankAccount:

    def __init__(self, owner_name: str, initial_balance: float = 0.0):
        # TODO 1: 초기 잔액이 음수인지 확인하고, 음수면 ValueError를 발생시키세요.
        # TODO 1: Check if initial_balance is negative; if so, raise ValueError.
        # 힌트 / Hint: raise ValueError("...")
        if initial_balance < 0:
            raise ValueError("initial_balance is negative")

        # TODO 2: 세 개의 속성을 초기화하세요. 이름은 반드시 밑줄(_)로 시작해야 합니다.
        #   - 소유자 이름 (owner_name)
        #   - 잔액 (balance) — initial_balance로 초기화
        #   - 거래 횟수 (transaction_count) — 0으로 초기화
        # TODO 2: Initialize three attributes. Names MUST start with underscore (_).
        #   - owner name
        #   - balance — initialized from initial_balance
        #   - transaction count — initialized to 0
        self._owner_name = owner_name
        self._balance = initial_balance
        self._transaction_count = 0

    # ------------------------------------------------------------------
    # Getter 메서드들 / Getter methods
    # ------------------------------------------------------------------

    def get_owner_name(self) -> str:
        # TODO 3: 소유자 이름을 반환하세요.
        # TODO 3: Return the owner name.
        return self._owner_name

    def get_balance(self) -> float:
        # TODO 4: 현재 잔액을 반환하세요.
        # TODO 4: Return the current balance.
        return self._balance

    def get_transaction_count(self) -> int:
        # TODO 5: 지금까지 성공한 거래 횟수를 반환하세요.
        # TODO 5: Return the number of successful transactions so far.
        return self._transaction_count

    # ------------------------------------------------------------------
    # 거래 메서드들 / Transaction methods
    # ------------------------------------------------------------------

    def deposit(self, amount: float) -> bool:
        # TODO 6: amount가 0 이하이면 False를 반환하세요 (입금 불가).
        # TODO 6: If amount is 0 or less, return False (cannot deposit).
        if amount <= 0:
            return False

        # TODO 7: 잔액에 amount를 더하고, 거래 횟수를 1 증가시키세요.
        # TODO 7: Add amount to balance, increment transaction count by 1.
        self._balance += amount
        self._transaction_count += 1

        # TODO 8: 성공했으므로 True를 반환하세요.
        # TODO 8: Return True for success.
        return True

    def withdraw(self, amount: float) -> bool:
        # TODO 9: amount가 0 이하이면 False를 반환하세요.
        # TODO 9: If amount is 0 or less, return False.
        if amount <= 0:
            return False

        # TODO 10: amount가 현재 잔액보다 크면 False를 반환하세요 (잔액 부족).
        # TODO 10: If amount is greater than current balance, return False (insufficient funds).
        if amount > self._balance:
            return False

        # TODO 11: 잔액에서 amount를 빼고, 거래 횟수를 1 증가시키세요. 그리고 True 반환.
        # TODO 11: Subtract amount from balance, increment transaction count, return True.
        self._balance -= amount
        self._transaction_count += 1
        return True
    
    # Bonus Challenge: Easy
    # transfer(other_account, amount) 메서드를 추가하세요. 
    # 자신의 계좌에서 amount만큼 빼서 other_account에 넣습니다. 성공하면 True, 실패하면 False.
    def transfer(self, other_account, amount):
        if amount <= 0:
            return False
        
        if amount > self._balance:
            return False
        
        self._balance -= amount
        self._transaction_count += 1
        other_account.deposit(amount)
        return True



# ======================================================================
# ⚠️ 아래 테스트 블록은 수정하지 마세요!
# ⚠️ Do NOT modify the test block below!
# ======================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Test 1: 정상 동작 / Normal operation")
    print("=" * 60)
    acc = BankAccount("Alice", 1000.0)
    print(f"잔액 / Balance: {acc.get_balance()}")           # 1000.0
    print(f"입금 500 / Deposit 500: {acc.deposit(500.0)}")  # True
    print(f"출금 200 / Withdraw 200: {acc.withdraw(200.0)}")# True
    print(f"잔액 / Balance: {acc.get_balance()}")           # 1300.0
    print(f"거래 횟수 / Tx count: {acc.get_transaction_count()}")  # 2

    print()
    print("=" * 60)
    print("Test 2: 잘못된 입력 거부 / Invalid input rejection")
    print("=" * 60)
    acc2 = BankAccount("Bob", 100.0)
    print(f"음수 입금 / Negative deposit: {acc2.deposit(-50)}")    # False
    print(f"초과 출금 / Over-withdraw: {acc2.withdraw(99999)}")    # False
    print(f"0원 출금 / Zero withdraw: {acc2.withdraw(0)}")         # False
    print(f"잔액 / Balance: {acc2.get_balance()}")                  # 100.0
    print(f"거래 횟수 / Tx count: {acc2.get_transaction_count()}") # 0

    print()
    print("=" * 60)
    print("Test 3: 음수 초기 잔액 / Negative initial balance")
    print("=" * 60)
    try:
        BankAccount("Eve", -100)
        print("❌ FAIL: ValueError가 발생해야 함 / should raise ValueError")
    except ValueError:
        print("✅ PASS: ValueError 발생함 / ValueError raised")

    # Bonus Challenge: Easy
    print()
    print("=" * 60)
    print("Test 4: transfer 테스트 / Transfer test")
    print("=" * 60)

    alice = BankAccount("Alice", 1000.0)
    bob = BankAccount("Bob", 500.0)

    # 정상 이체
    print(f"이체 전 Alice 잔액: {alice.get_balance()}")        # 1000.0
    print(f"이체 전 Bob 잔액: {bob.get_balance()}")            # 500.0
    print(f"Alice → Bob 300 이체: {alice.transfer(bob, 300)}") # True
    print(f"이체 후 Alice 잔액: {alice.get_balance()}")        # 700.0
    print(f"이체 후 Bob 잔액: {bob.get_balance()}")            # 800.0
    print(f"Alice 거래 횟수: {alice.get_transaction_count()}") # 1
    print(f"Bob 거래 횟수: {bob.get_transaction_count()}")     # 1

    print()

    # 잘못된 이체 시도
    print(f"잔액 초과 이체: {alice.transfer(bob, 99999)}")     # False
    print(f"0원 이체: {alice.transfer(bob, 0)}")               # False
    print(f"음수 이체: {alice.transfer(bob, -100)}")           # False
    print(f"실패 후 Alice 잔액: {alice.get_balance()}")        # 700.0 (변화 없음)
    print(f"실패 후 거래 횟수: {alice.get_transaction_count()}") # 1 (변화 없음)
