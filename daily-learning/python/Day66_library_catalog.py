"""
===============================================================
📚 Day 3 - Inheritance Practice: Library Catalog System
도서관 카탈로그 시스템
===============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260603
===============================================================

목표 / Goal:
- 부모 클래스와 자식 클래스 만들기 (3개의 자식 클래스)
- Build a parent class and three child classes
- isinstance()와 issubclass() 익숙해지기
- Get comfortable with isinstance() and issubclass()
- 보호된 속성 (_attribute) 관습 사용하기
- Use the protected attribute (_attribute) convention

규칙 / Rules:
- 데코레이터 사용 금지 (@property, @classmethod, @staticmethod 등)
- No decorators (@property, @classmethod, @staticmethod, etc.)
- 모든 속성에 _ 접두사 사용
- Use _ prefix for all attributes
- snake_case 사용 (PEP 8)
- Use snake_case (PEP 8)
"""


# ============================================================
# 부모 클래스 / Parent class: LibraryItem
# ============================================================


class LibraryItem:
    """도서관의 모든 자료를 위한 부모 클래스 / Parent class for all library items."""

    def __init__(self, title, item_id, year):
        # TODO 1: 다섯 개의 보호된 속성을 초기화하세요
        # TODO 1: Initialize five protected attributes
        # - self._title (매개변수로 받음 / from parameter)
        # - self._item_id (매개변수로 받음 / from parameter)
        # - self._year (매개변수로 받음 / from parameter)
        # - self._is_checked_out (초기값 False / starts False)
        # - self._borrower (초기값 None / starts None)
        self._title = title
        self._item_id = item_id
        self._year = year
        self._is_checked_out = False
        self._borrower = None

    def check_out(self, borrower_name):
        # TODO 2: 대출 처리 메서드
        # TODO 2: Check out the item
        # 힌트 / Hints:
        #   - 이미 대출 중이면? → "'{제목}' is already checked out by {대출자}" 반환
        #   - If already checked out, return "'{title}' is already checked out by {borrower}"
        #   - 대출 가능하면? → 상태 변경하고 "'{제목}' has been checked out by {이름}" 반환
        #   - If available, update status and return "'{title}' has been checked out by {borrower_name}"
        if self._is_checked_out:
            return f"\'{self._title}\' is already checked out by {self._borrower}"
        else:
            self._is_checked_out = True
            self._borrower = borrower_name
            return f"\'{self._title}\' has been checked out by {borrower_name}"

    def return_item(self):
        # TODO 3: 반납 처리 메서드
        # TODO 3: Return the item
        # 힌트 / Hints:
        #   - 대출 중이 아니면? → "'{제목}' was not checked out" 반환
        #   - If not checked out, return "'{title}' was not checked out"
        #   - 대출 중이면? → 반납자 이름을 저장한 후 상태를 초기화하고 메시지 반환
        #   - If checked out, save borrower name, reset status, return message
        #   - 반환 메시지 / Return message: "'{제목}' has been returned by {이전 대출자}"
        if not self._is_checked_out:
            return f"\'{self._title}\' was not checked out"
        else:
            self._is_checked_out = False
            self._borrower = None
            return f"\'{self._title}\' has been returned by {self._borrower}"

    def get_info(self):
        # TODO 4: 자료 정보를 문자열로 반환
        # TODO 4: Return item info as a string
        # 형식 / Format: "[{ID}] {제목} ({연도}) - {상태}"
        # 상태 / Status: "Checked out" 또는 "Available"
        # 예시 / Example: "[B001] 1984 (1949) - Available"
        status = "Checked out" if self._is_checked_out else "Available"
        return f"[{self._item_id}] {self._title} ({self._year}) - {status}"

    def get_title(self):
        # TODO 5: self._title 반환 / return self._title
        return self._title

    def get_item_id(self):
        # TODO 6: self._item_id 반환 / return self._item_id
        return self._item_id

    def is_available(self):
        # TODO 7: 대출 가능 여부를 True/False로 반환
        # TODO 7: Return availability as True/False
        # 힌트 / Hint: self._is_checked_out의 반대값
        return not self._is_checked_out


# ============================================================
# 자식 클래스 1 / Child class 1: Book
# ============================================================

class Book(LibraryItem):

    def __init__(self, title, item_id, year, author, pages):
        # TODO 9: 부모의 __init__을 호출하고, _author와 _pages를 초기화하세요
        # TODO 9: Call parent's __init__, then initialize _author and _pages
        # 힌트 / Hint: super().__init__(title, item_id, year)
        super().__init__(title, item_id, year)
        self._author = author
        self._pages = pages


    def get_info(self):
        # TODO 10: 부모의 get_info()를 호출한 후 저자와 페이지 정보를 추가
        # TODO 10: Call parent's get_info() then add author and page info
        # 형식 / Format: "{부모의 정보} | Author: {저자}, {페이지} pages"
        # 힌트 / Hint: super().get_info()를 변수에 저장한 후 문자열에 추가
        # Hint: store super().get_info() in a variable, then append to it
        return f"{super().get_info()} | Author: {self._author}, {self._pages} pages"

    def get_author(self):
        # TODO 11: self._author 반환 / return self._author
        return self._author


# ============================================================
# 자식 클래스 2 / Child class 2: DVD
# ============================================================

class DVD(LibraryItem):  # TODO 12: LibraryItem을 상속받도록 채우세요 / fill in

    def __init__(self, title, item_id, year, director, runtime_minutes):
        # TODO 13: 부모의 __init__ 호출 + _director, _runtime_minutes 초기화
        # TODO 13: Call parent's __init__, then initialize _director and _runtime_minutes
        super().__init__(title, item_id, year)
        self._director = director
        self._runtime_minutes = runtime_minutes

    def get_info(self):
        # TODO 14: 부모의 get_info() + 감독과 상영시간 추가
        # TODO 14: parent's get_info() + add director and runtime
        # 형식 / Format: "{부모의 정보} | Director: {감독}, {상영시간} min"
        return f"{super().get_info()} | Director: {self._director}, {self._runtime_minutes} min"

    def get_director(self):
        # TODO 15: self._director 반환 / return self._director
        return self._director


# ============================================================
# 자식 클래스 3 / Child class 3: Magazine
# ============================================================

class Magazine(LibraryItem):  # TODO 16: LibraryItem을 상속받도록 채우세요 / fill in

    def __init__(self, title, item_id, year, issue_number, month):
        # TODO 17: 부모의 __init__ 호출 + _issue_number, _month 초기화
        # TODO 17: Call parent's __init__, then initialize _issue_number and _month
        super().__init__(title, item_id, year)
        self._issue_number = issue_number
        self._month = month

    def get_info(self):
        # TODO 18: 부모의 get_info() + 발행호와 월 추가
        # TODO 18: parent's get_info() + add issue number and month
        # 형식 / Format: "{부모의 정보} | Issue #{발행호}, {월}"
        return f"{super().get_info()} | Issue #{self._issue_number}, {self._month}"

    def get_issue_number(self):
        # TODO 19: self._issue_number 반환 / return self._issue_number
        return self._issue_number


# ============================================================
# 헬퍼 함수 (일반 함수, 클래스 외부)
# Helper functions (regular functions, outside the classes)
# ============================================================

def count_books(items):
    """리스트에서 Book 인스턴스의 개수를 반환 / Count Book instances in the list."""
    # TODO 20: isinstance(item, Book)을 사용하여 Book의 개수를 세세요
    # TODO 20: Use isinstance(item, Book) to count Book instances
    # 힌트 / Hint: for문으로 리스트를 순회하면서 isinstance()로 확인
    # Hint: loop through the list and check with isinstance()
    count = 0
    for item in items:
        if isinstance(item, Book):
            count += 1
    return count


def filter_by_type(items, item_type):
    """주어진 타입의 인스턴스만 새 리스트로 반환 / Return only instances of the given type."""
    # TODO 21: isinstance(item, item_type)을 사용하여 필터링하세요
    # TODO 21: Filter using isinstance(item, item_type)
    # 주의 / Note: item_type은 변수입니다 (Book, DVD 등의 클래스가 전달됨)
    # Note: item_type is a variable (a class like Book or DVD is passed in)
    result = []
    for item in items:
        if isinstance(item, item_type):
            result.append(item)
    return result # 주어진 타입의 인스턴스만을 포함한 새로운 리스트를 만들어 반환


def is_library_item_subclass(some_class):
    """어떤 클래스가 LibraryItem의 자식 클래스인지 확인 (단, LibraryItem 자기 자신은 제외).
    Check if a class is a subclass of LibraryItem (excluding LibraryItem itself)."""
    # TODO 22: issubclass()로 확인 + LibraryItem 자기 자신은 False 반환
    # TODO 22: Check with issubclass() AND exclude LibraryItem itself
    # 힌트 / Hint: issubclass(some_class, LibraryItem) and some_class is not LibraryItem
    return issubclass(some_class, LibraryItem) and some_class != LibraryItem


def get_available_items(items):
    """대출 가능한 자료들만 반환 / Return only available items."""
    # TODO 23: isinstance()와 is_available() 둘 다 사용하세요
    # TODO 23: Use BOTH isinstance() AND is_available()
    # 힌트 / Hint: LibraryItem 인스턴스인지 먼저 확인하고, 그 다음 is_available()
    # Hint: First check if it's a LibraryItem instance, then check is_available()
    result = []
    for item in items:
        if isinstance(item, LibraryItem) and item.is_available():
            result.append(item)
    return result


# ============================================================
# 테스트 / Tests
# ⚠️ 아래 코드는 수정하지 마세요! / Do not modify the code below!
# ============================================================

if __name__ == "__main__":
    try:
        print("=" * 60)
        print("Test 1: 객체 생성 / Object creation")
        print("=" * 60)
        book1 = Book("1984", "B001", 1949, "George Orwell", 328)
        dvd1 = DVD("The Matrix", "D001", 1999, "Wachowskis", 136)
        mag1 = Magazine("Time", "M001", 2024, 12, "January")
        print(f"  Book: {book1.get_info()}")
        print(f"  DVD:  {dvd1.get_info()}")
        print(f"  Mag:  {mag1.get_info()}")

        print("\n" + "=" * 60)
        print("Test 2: 대출/반납 / Check out & return")
        print("=" * 60)
        print(f"  {book1.check_out('Alice')}")
        print(f"  {book1.check_out('Bob')}")   # already checked out
        print(f"  {book1.return_item()}")
        assert book1.is_available() is True, "Should be available after return"

        print("\n" + "=" * 60)
        print("Test 3: isinstance() 동작 확인 / isinstance() behavior")
        print("=" * 60)
        assert isinstance(book1, Book) is True
        assert isinstance(book1, LibraryItem) is True  # 부모 클래스도 True!
        assert isinstance(book1, DVD) is False
        print("  ✓ Book is instance of Book AND LibraryItem")
        print("  ✓ Book is NOT instance of DVD")

        print("\n" + "=" * 60)
        print("Test 4: count_books() with isinstance")
        print("=" * 60)
        catalog = [book1, dvd1, mag1, Book("Dune", "B002", 1965, "Herbert", 412)]
        assert count_books(catalog) == 2, f"Expected 2, got {count_books(catalog)}"
        print(f"  ✓ count_books(catalog) = 2")

        print("\n" + "=" * 60)
        print("Test 5: filter_by_type()")
        print("=" * 60)
        dvds = filter_by_type(catalog, DVD)
        assert len(dvds) == 1
        all_items = filter_by_type(catalog, LibraryItem)
        assert len(all_items) == 4, "Parent class filter should return ALL items"
        print(f"  ✓ DVDs only: {len(dvds)} item(s)")
        print(f"  ✓ LibraryItem filter returns all: {len(all_items)} items")

        print("\n" + "=" * 60)
        print("Test 6: issubclass()")
        print("=" * 60)
        assert is_library_item_subclass(Book) is True
        assert is_library_item_subclass(DVD) is True
        assert is_library_item_subclass(Magazine) is True
        assert is_library_item_subclass(str) is False
        assert is_library_item_subclass(LibraryItem) is False, \
            "Should exclude LibraryItem itself"
        print("  ✓ Book, DVD, Magazine → True")
        print("  ✓ str → False")
        print("  ✓ LibraryItem itself → False (excluded)")

        print("\n" + "=" * 60)
        print("Test 7: get_available_items()")
        print("=" * 60)
        dvd1.check_out("Charlie")
        available = get_available_items(catalog)
        assert dvd1 not in available, "Checked-out DVD should not be available"
        print(f"  ✓ Available: {[item.get_title() for item in available]}")
        print(f"  ✓ Checked-out DVD correctly excluded")

        print("\n" + "=" * 60)
        print("🎉 모든 테스트 통과! / ALL TESTS PASSED! 🎉")
        print("=" * 60)

    except NotImplementedError:
        print("\n💡 아직 구현 안 된 메서드가 있어요. TODO를 모두 채우세요!")
        print("💡 Some methods aren't implemented yet. Complete all TODOs!")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        print("💡 코드를 다시 확인해보세요! / Recheck your code!")
    except TypeError as e:
        print(f"\n❌ TypeError: {e}")
        print("💡 클래스 정의나 super() 호출을 확인하세요!")
        print("💡 Check your class definition or super() call!")
    except AttributeError as e:
        print(f"\n❌ AttributeError: {e}")
        print("💡 속성 이름의 _ 접두사 확인! 메서드 이름 철자 확인!")
        print("💡 Check _ prefix on attributes! Check method spelling!")
    except Exception as e:
        print(f"\n❌ Error: {type(e).__name__}: {e}")
