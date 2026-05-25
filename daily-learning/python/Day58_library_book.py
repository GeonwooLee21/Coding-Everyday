"""
===============================================================
Day 2 Class Practice: Library Book System
Day 2 클래스 연습: 도서관 책 시스템
===============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260522
===============================================================

학습 목표 (Learning Objectives):
  - Private 속성 사용하기 (using private attributes)
  - Getter / Setter 메서드 만들기 (creating getters and setters)
  - 행동 메서드 구현하기 (implementing behavior methods)
  - 검증(validation)을 통한 데이터 보호 (data protection via validation)
"""


class Book:
    def __init__(self, title: str, author: str):
        # TODO 1: title이 빈 문자열이거나 공백만 있으면 ValueError를 발생시키세요
        #         Raise ValueError if title is empty or only whitespace.
        #         힌트 / Hint: not title.strip()
        if not title.strip():
            raise ValueError("title is empty.")

        # TODO 2: author도 동일하게 검증하세요
        #         Validate author the same way.
        if not author.strip():
            raise ValueError("author is empty.")

        # TODO 3: 다음 private 속성들을 초기화하세요 (모두 밑줄 _ 로 시작!)
        #         Initialize these private attributes (all start with underscore _!)
        #   self._title         → title.strip() (앞뒤 공백 제거)
        #   self._author        → author.strip()
        #   self._is_borrowed   → False (처음에는 대출 중 아님 / not borrowed initially)
        #   self._borrower      → None  (빌린 사람 없음 / no borrower)
        #   self._borrow_count  → 0     (대출 횟수 0 / count starts at 0)
        self._title = title.strip()
        self._author = author.strip()
        self._is_borrowed = False
        self._borrower = None
        self._borrow_count = 0

    # Easy Bonus Challenge: __str__ 메서드 추가
    def __str__(self):
        if self._is_borrowed:
            return f"\"{self._title}\" by {self._author} [대출 중: {self._borrower}]"
        else:
            return f"\"{self._title}\" by {self._author} [대출 가능]"

    # ─────────────────────────────────────────────
    # Getter 메서드 / Getter Methods
    # ─────────────────────────────────────────────

    def get_title(self) -> str:
        # TODO 4: self._title을 반환하세요 / Return self._title
        return self._title

    def get_author(self) -> str:
        # TODO 5: self._author를 반환하세요 / Return self._author
        return self._author

    def get_borrower(self):
        # TODO 6: self._borrower를 반환하세요 / Return self._borrower
        #         (대출 중이 아니면 None / None if not borrowed)
        if not self._is_borrowed:
            return None
        else:
            return self._borrower

    def get_borrow_count(self) -> int:
        # TODO 7: self._borrow_count를 반환하세요 / Return self._borrow_count
        return self._borrow_count

    def is_available(self) -> bool:
        # TODO 8: 대출 가능하면 True, 아니면 False를 반환하세요
        #         Return True if available, False otherwise.
        #         힌트 / Hint: self._is_borrowed의 반대 / opposite of self._is_borrowed
        if not self._is_borrowed:
            return True
        else:
            return False

    # ─────────────────────────────────────────────
    # Setter 메서드 (검증 포함!) / Setter Method (with validation!)
    # ─────────────────────────────────────────────

    def set_title(self, new_title: str) -> None:
        # TODO 9: new_title이 비어있거나 공백만 있으면 ValueError를 발생시키세요
        #         Raise ValueError if new_title is empty or whitespace-only.
        if not new_title.strip():
            raise ValueError("new_title is empty.")

        # TODO 10: 검증을 통과하면 self._title을 업데이트하세요 (strip()도 잊지 마세요!)
        #          If validation passes, update self._title (don't forget strip()!)
        self._title = new_title.strip()


    # ─────────────────────────────────────────────
    # 행동 메서드 / Behavior Methods
    # ─────────────────────────────────────────────

    def borrow(self, borrower_name: str) -> bool:
        # TODO 11: 이미 대출 중이면 False를 반환하세요 (대출 실패)
        #          If already borrowed, return False (borrow failed).
        if self._is_borrowed:
            return False

        # TODO 12: borrower_name이 비어있으면 ValueError를 발생시키세요
        #          If borrower_name is empty, raise ValueError.
        if not borrower_name.strip():
            raise ValueError("borrower_name is empty.")

        # TODO 13: 다음 세 가지 상태를 업데이트하세요:
        #          Update these three states:
        #   self._is_borrowed   → True
        #   self._borrower      → borrower_name.strip()
        #   self._borrow_count  → 1 증가 / increment by 1
        self._is_borrowed = True
        self._borrower = borrower_name.strip()
        self._borrow_count += 1

        # TODO 14: True를 반환하세요 (대출 성공) / Return True (borrow successful)
        return True

    def return_book(self) -> bool:
        # TODO 15: 대출 중이 아니면 False를 반환하세요 (반납 실패)
        #          If not currently borrowed, return False (return failed).
        if not self._is_borrowed:
            return False

        # TODO 16: 대출 상태를 초기화하세요:
        #          Reset borrow state:
        #   self._is_borrowed → False
        #   self._borrower    → None
        #          (주의: _borrow_count는 그대로! / Note: don't touch _borrow_count!)
        self._is_borrowed = False
        self._borrower = None

        # TODO 17: True를 반환하세요 / Return True
        return True


# ═══════════════════════════════════════════════════════════════════
# 테스트 영역 / Test Block — 수정하지 마세요! / Do not modify!
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 50)
    print("🧪 Book 클래스 테스트 / Book Class Tests")
    print("=" * 50)

    try:
        # Test 1: 기본 생성 / Basic creation
        b1 = Book("Effective Python", "Brett Slatkin")
        assert b1.get_title() == "Effective Python"
        assert b1.get_author() == "Brett Slatkin"
        assert b1.is_available() == True
        assert b1.get_borrower() is None
        assert b1.get_borrow_count() == 0
        print("✅ Test 1: 기본 생성 / Basic creation")

        # Test 2: 대출 / Borrow
        assert b1.borrow("Alice") == True
        assert b1.is_available() == False
        assert b1.get_borrower() == "Alice"
        assert b1.get_borrow_count() == 1
        print("✅ Test 2: 대출 / Borrow")

        # Test 3: 중복 대출 방지 / Block double borrow
        assert b1.borrow("Bob") == False
        assert b1.get_borrower() == "Alice"
        assert b1.get_borrow_count() == 1
        print("✅ Test 3: 중복 대출 방지 / Block double borrow")

        # Test 4: 반납 / Return
        assert b1.return_book() == True
        assert b1.is_available() == True
        assert b1.get_borrower() is None
        print("✅ Test 4: 반납 / Return")

        # Test 5: 중복 반납 방지 / Block double return
        assert b1.return_book() == False
        print("✅ Test 5: 중복 반납 방지 / Block double return")

        # Test 6: 대출 횟수 누적 / Cumulative borrow count
        b1.borrow("Bob")
        b1.return_book()
        b1.borrow("Carol")
        assert b1.get_borrow_count() == 3
        print("✅ Test 6: 대출 횟수 누적 / Cumulative borrow count")

        # Test 7: 빈 제목 거부 / Reject empty title
        try:
            bad = Book("", "Author")
            print("❌ Test 7: 빈 제목이 통과됨 / Empty title was accepted")
        except ValueError:
            print("✅ Test 7: 빈 제목 거부 / Empty title rejected")

        # Test 8: set_title 검증 / set_title validation
        b2 = Book("Old Title", "Author")
        b2.set_title("New Title")
        assert b2.get_title() == "New Title"
        try:
            b2.set_title("")
            print("❌ Test 8: 빈 제목 setter 통과됨")
        except ValueError:
            print("✅ Test 8: set_title 검증 / set_title validates")

        # Test 9: __str__ 출력 확인 / __str__ output check
        b3 = Book("Clean Code", "Robert Martin")
        assert str(b3) == '"Clean Code" by Robert Martin [대출 가능]'
        b3.borrow("Alice")
        assert str(b3) == '"Clean Code" by Robert Martin [대출 중: Alice]'
        print("✅ Test 9: __str__ 출력 확인 / __str__ output check")

        print("\n🎉 모든 테스트 통과! / All tests passed!")

    except AssertionError as e:
        print(f"\n❌ 테스트 실패 / Test failed: {e}")
    except TypeError as e:
        print(f"\n❌ 함수가 아직 구현되지 않았어요 / Function not implemented yet: {e}")
    except Exception as e:
        print(f"\n❌ 예상치 못한 오류 / Unexpected error: {type(e).__name__}: {e}")
