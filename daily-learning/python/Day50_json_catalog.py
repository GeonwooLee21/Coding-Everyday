"""
=============================================================
도서관 카탈로그 JSON 변환 연습 / Library Catalog JSON Practice
=============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260509
=============================================================
각 함수에서 TODO 주석을 따라 코드를 작성하세요.
Follow the TODO comments in each function to write your code.
"""

import json


# ============================================================
# 과제 1 / Task 1: dict_to_json_string
# ============================================================
def dict_to_json_string(book: dict) -> str:
    """
    책 딕셔너리를 JSON 문자열로 변환합니다.
    Convert a book dictionary into a JSON string.
    """
    # TODO 1-1: json 모듈의 dumps() 함수를 사용하여 book을 JSON 문자열로 변환하세요.
    # TODO 1-1: Use json.dumps() to convert book into a JSON string.
    # TODO 1-2: 변환된 문자열을 return 하세요.
    # TODO 1-2: Return the converted string.
    return json.dumps(book)


# ============================================================
# 과제 2 / Task 2: json_string_to_dict
# ============================================================
def json_string_to_dict(json_text: str) -> dict:
    """
    JSON 문자열을 Python 딕셔너리로 변환합니다.
    Convert a JSON string into a Python dictionary.
    """
    # TODO 2-1: json 모듈의 loads() 함수를 사용하여 json_text를 딕셔너리로 변환하세요.
    # TODO 2-1: Use json.loads() to convert json_text into a dictionary.
    # TODO 2-2: 변환된 딕셔너리를 return 하세요.
    # TODO 2-2: Return the converted dictionary.
    return json.loads(json_text)


# ============================================================
# 과제 3 / Task 3: count_available_books
# ============================================================
def count_available_books(catalog_json: str) -> int:
    """
    JSON 카탈로그에서 대출 가능한 책의 수를 반환합니다.
    Return the number of available books in the JSON catalog.
    """
    # TODO 3-1: json.loads()를 사용하여 catalog_json을 리스트로 변환하세요.
    # TODO 3-1: Use json.loads() to convert catalog_json into a list.
    book_list = json.loads(catalog_json)

    # TODO 3-2: 카운터 변수를 0으로 초기화하세요.
    # TODO 3-2: Initialize a counter variable to 0.
    count = 0

    # TODO 3-3: 리스트의 각 책(딕셔너리)을 순회하면서, "available" 키의 값이 True이면 카운터를 1 증가시키세요.
    # TODO 3-3: Loop through each book in the list. If its "available" value is True, increment the counter.
    for book in book_list:
        if book["available"]:
            count += 1

    # TODO 3-4: 카운터를 return 하세요.
    # TODO 3-4: Return the counter.
    return count


# ============================================================
# 과제 4 / Task 4: add_new_book
# ============================================================
def add_new_book(catalog_json: str, new_book: dict) -> str:
    """
    카탈로그에 새 책을 추가하고, 업데이트된 카탈로그를 JSON 문자열로 반환합니다.
    Add a new book to the catalog and return the updated catalog as a JSON string.
    """
    # TODO 4-1: json.loads()를 사용하여 catalog_json을 리스트로 변환하세요.
    # TODO 4-1: Use json.loads() to convert catalog_json into a list.
    book_list = json.loads(catalog_json)

    # TODO 4-2: 리스트의 append() 메서드를 사용하여 new_book을 리스트에 추가하세요.
    # TODO 4-2: Use the list's append() method to add new_book to the list.
    book_list.append(new_book)

    # TODO 4-3: json.dumps()를 사용하여 리스트를 다시 JSON 문자열로 변환하고 return 하세요.
    # TODO 4-3: Use json.dumps() to convert the list back into a JSON string and return it.
    return json.dumps(book_list)


# ============================================================
# 과제 5 / Task 5: find_books_by_author
# ============================================================
def find_books_by_author(catalog_json: str, author_name: str) -> list:
    """
    특정 저자의 모든 책 제목을 리스트로 반환합니다.
    Return a list of all book titles by a given author.
    """
    # TODO 5-1: json.loads()를 사용하여 catalog_json을 리스트로 변환하세요.
    # TODO 5-1: Use json.loads() to convert catalog_json into a list.
    book_list = json.loads(catalog_json)

    # TODO 5-2: 빈 리스트를 만들어 결과를 담을 준비를 하세요.
    # TODO 5-2: Create an empty list to hold the results.
    title_list = []

    # TODO 5-3: 카탈로그를 순회하면서, "author"가 author_name과 같으면 그 책의 "title"을 결과 리스트에 추가하세요.
    # TODO 5-3: Loop through the catalog. If "author" matches author_name, append the book's "title" to the result list.
    for book in book_list:
        if book["author"] == author_name:
            title_list.append(book["title"])

    # TODO 5-4: 결과 리스트를 return 하세요.
    # TODO 5-4: Return the result list.
    return title_list


# ============================================================
# 🎁 보너스 / BONUS (선택 / Optional)
# ============================================================

# 🥉 Easy: pretty_print_book(book)
# 책 딕셔너리를 들여쓰기가 적용된 JSON 문자열로 변환하세요.
# Convert a book dictionary into a JSON string with indentation.
# 힌트 / Hint: json.dumps(book, indent=2)


# 🥈 Medium: get_oldest_book(catalog_json)
# 카탈로그에서 가장 오래된(year가 가장 작은) 책의 제목을 반환하세요.
# Return the title of the oldest book in the catalog (smallest year value).


# 🥇 Hard: catalog_summary(catalog_json)
# 저자별 책 권수를 담은 딕셔너리를 반환하세요.
# Return a dictionary mapping each author to their book count.
# 예 / Example: {"George Orwell": 2, "Frank Herbert": 1}


# ============================================================
# 🚫 아래 코드는 수정하지 마세요! / DO NOT MODIFY BELOW!
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("도서관 카탈로그 테스트 / Library Catalog Tests")
    print("=" * 60)

    # ----- Test 1 -----
    print("\n[Test 1] dict_to_json_string")
    book_1 = {"title": "1984", "author": "George Orwell", "year": 1949, "available": True}
    result_1 = dict_to_json_string(book_1)
    print(f"  결과 / Result: {result_1}")
    print(f"  타입 / Type:   {type(result_1).__name__}")
    assert isinstance(result_1, str), "결과가 문자열이 아닙니다 / Result is not a string"
    assert json.loads(result_1) == book_1, "변환된 JSON이 원본과 다릅니다 / Converted JSON differs from original"
    print("  ✅ PASS")

    # ----- Test 2 -----
    print("\n[Test 2] json_string_to_dict")
    json_text_2 = '{"title": "Dune", "author": "Frank Herbert", "year": 1965, "available": false}'
    result_2 = json_string_to_dict(json_text_2)
    print(f"  결과 / Result: {result_2}")
    print(f"  타입 / Type:   {type(result_2).__name__}")
    assert isinstance(result_2, dict), "결과가 딕셔너리가 아닙니다 / Result is not a dict"
    assert result_2["available"] is False, "'available' 값이 False여야 합니다 / 'available' must be False"
    print("  ✅ PASS")

    # ----- Test 3 -----
    print("\n[Test 3] count_available_books")
    catalog_3 = json.dumps([
        {"title": "1984", "author": "George Orwell", "year": 1949, "available": True},
        {"title": "Dune", "author": "Frank Herbert", "year": 1965, "available": False},
        {"title": "Foundation", "author": "Isaac Asimov", "year": 1951, "available": True},
        {"title": "Neuromancer", "author": "William Gibson", "year": 1984, "available": True},
        {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932, "available": False},
    ])
    result_3 = count_available_books(catalog_3)
    print(f"  결과 / Result: {result_3} (예상 / Expected: 3)")
    assert result_3 == 3, f"3을 반환해야 합니다 / Should return 3, got {result_3}"
    print("  ✅ PASS")

    # ----- Test 4 -----
    print("\n[Test 4] add_new_book")
    catalog_4 = json.dumps([
        {"title": "1984", "author": "George Orwell", "year": 1949, "available": True}
    ])
    new_book_4 = {"title": "Animal Farm", "author": "George Orwell", "year": 1945, "available": True}
    result_4 = add_new_book(catalog_4, new_book_4)
    print(f"  결과 / Result: {result_4}")
    parsed_4 = json.loads(result_4)
    assert isinstance(result_4, str), "결과가 문자열이어야 합니다 / Result must be a string"
    assert len(parsed_4) == 2, "카탈로그에 책이 2권이어야 합니다 / Catalog should have 2 books"
    assert parsed_4[1] == new_book_4, "새 책이 마지막에 추가되어야 합니다 / New book should be appended last"
    print("  ✅ PASS")

    # ----- Test 5 -----
    print("\n[Test 5] find_books_by_author")
    catalog_5 = json.dumps([
        {"title": "1984", "author": "George Orwell", "year": 1949, "available": True},
        {"title": "Animal Farm", "author": "George Orwell", "year": 1945, "available": True},
        {"title": "Dune", "author": "Frank Herbert", "year": 1965, "available": False},
    ])
    result_5a = find_books_by_author(catalog_5, "George Orwell")
    print(f"  결과 / Result (Orwell):  {result_5a} (예상 / Expected: ['1984', 'Animal Farm'])")
    assert result_5a == ["1984", "Animal Farm"], f"잘못된 결과 / Wrong result: {result_5a}"

    result_5b = find_books_by_author(catalog_5, "Unknown Author")
    print(f"  결과 / Result (Unknown): {result_5b} (예상 / Expected: [])")
    assert result_5b == [], f"빈 리스트를 반환해야 합니다 / Should return empty list, got {result_5b}"
    print("  ✅ PASS")

    print("\n" + "=" * 60)
    print("🎉 모든 테스트 통과! / ALL TESTS PASSED!")
    print("=" * 60)
