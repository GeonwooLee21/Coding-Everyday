# ============================================================
# 🐍 Little Sister's Essay | 여동생의 에세이 편집하기
# ============================================================
# 📌 Snake_case 변수명을 사용하세요! Use snake_case naming!
# ============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260416
# ============================================================


# ────────────────────────────────────────────────────────────
# 함수 1 | Function 1
# ────────────────────────────────────────────────────────────
def capitalize_title(title):
    """
    제목의 각 단어 첫 글자를 대문자로 만들기
    Capitalize the first letter of each word in the title.

    매개변수 | Parameter:
        title (str): 원본 제목 문자열 | the original title string

    반환값 | Returns:
        str: 각 단어 첫 글자가 대문자인 문자열 | title-cased string
    """
    # TODO 1: title 문자열에 적절한 문자열 메서드를 호출하여 반환하세요.
    #         (힌트: 각 단어의 첫 글자를 대문자로 만드는 메서드가 있어요!)
    # TODO 1: Call the appropriate string method on `title` and return it.
    #         (Hint: there is a method that makes the first letter of each word uppercase!)
    return title.capitalize()


# ────────────────────────────────────────────────────────────
# 함수 2 | Function 2
# ────────────────────────────────────────────────────────────
def check_sentence_ending(sentence):
    """
    문장이 마침표(.)로 끝나는지 확인하기
    Check whether the sentence ends with a period.

    매개변수 | Parameter:
        sentence (str): 확인할 문장 | the sentence to check

    반환값 | Returns:
        bool: 마침표로 끝나면 True, 아니면 False
              True if the sentence ends with a period, False otherwise
    """
    # TODO 2: sentence가 마침표(".")로 끝나는지 확인하는 메서드를 호출하여 반환하세요.
    #         (힌트: 문자열이 특정 문자로 끝나는지 확인하는 메서드가 있어요!)
    # TODO 2: Call a string method that checks if `sentence` ends with "." and return it.
    #         (Hint: there is a method that checks if a string ends with a specific character!)
    return sentence.endswith(".")


# ────────────────────────────────────────────────────────────
# 함수 3 | Function 3
# ────────────────────────────────────────────────────────────
def clean_up_spacing(sentence):
    """
    문장 앞뒤의 불필요한 공백 제거하기
    Remove unnecessary whitespace from both ends of the sentence.

    매개변수 | Parameter:
        sentence (str): 공백이 포함된 문장 | sentence with extra whitespace

    반환값 | Returns:
        str: 앞뒤 공백이 제거된 문장 | sentence with leading/trailing spaces removed
    """
    # TODO 3: sentence의 앞뒤 공백을 제거하는 메서드를 호출하여 반환하세요.
    #         (힌트: 앞뒤를 "벗겨낸다(strip)"는 느낌의 메서드가 있어요!)
    # TODO 3: Call a string method that removes whitespace from both ends and return it.
    #         (Hint: think of a method that "strips" off the edges!)
    return sentence.strip()


# ────────────────────────────────────────────────────────────
# 함수 4 | Function 4
# ────────────────────────────────────────────────────────────
def replace_word_choice(sentence, old_word, new_word):
    """
    문장 안의 특정 단어를 새 단어로 모두 교체하기
    Replace every occurrence of old_word with new_word in the sentence.

    매개변수 | Parameters:
        sentence (str): 원본 문장 | the original sentence
        old_word (str): 교체할 단어 | the word to replace
        new_word (str): 새로운 단어 | the replacement word

    반환값 | Returns:
        str: 단어가 교체된 새 문장 | new sentence with the word replaced
    """
    # TODO 4: sentence에서 old_word를 new_word로 교체하는 메서드를 호출하여 반환하세요.
    #         (힌트: 문자열 안의 특정 부분을 "바꾸는(replace)" 메서드가 있어요!)
    # TODO 4: Call a string method that replaces old_word with new_word and return it.
    #         (Hint: there is a method that literally "replaces" one substring with another!)
    return sentence.replace(old_word, new_word)


# ============================================================
# 🎪 테스트 코드 | Test Code — 수정하지 마세요! Do not edit!
# ============================================================
if __name__ == "__main__":
    print("=" * 55)
    print("✅ 테스트 실행 중 | Running Tests")
    print("=" * 55)

    # Test 1: capitalize_title
    print("\n📌 [1] capitalize_title")
    print(capitalize_title("my hobbies"))
    # 예상 | Expected: My Hobbies
    print(capitalize_title("a day in the life"))
    # 예상 | Expected: A Day In The Life
    print(capitalize_title("python is fun"))
    # 예상 | Expected: Python Is Fun

    # Test 2: check_sentence_ending
    print("\n📌 [2] check_sentence_ending")
    print(check_sentence_ending("I like to hike, bake, and read."))
    # 예상 | Expected: True
    print(check_sentence_ending("This is great"))
    # 예상 | Expected: False
    print(check_sentence_ending("Hello!"))
    # 예상 | Expected: False

    # Test 3: clean_up_spacing
    print("\n📌 [3] clean_up_spacing")
    print(clean_up_spacing("   I like to go on hikes with my dog.  "))
    # 예상 | Expected: I like to go on hikes with my dog.
    print(clean_up_spacing("  No extra spaces."))
    # 예상 | Expected: No extra spaces.

    # Test 4: replace_word_choice
    print("\n📌 [4] replace_word_choice")
    print(replace_word_choice("I bake good cakes.", "good", "amazing"))
    # 예상 | Expected: I bake amazing cakes.
    print(replace_word_choice("The big dog saw a big cat.", "big", "tiny"))
    # 예상 | Expected: The tiny dog saw a tiny cat.
    print(replace_word_choice("Happy happy day.", "happy", "great"))
    # 예상 | Expected: Happy great day.  (대소문자 구분! case-sensitive!)

    print("\n" + "=" * 55)
    print("🏁 테스트 완료 | Tests Complete")
    print("=" * 55)
