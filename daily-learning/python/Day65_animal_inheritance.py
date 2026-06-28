"""
===============================================================
🐍 Python 연습: 동물 보호소 시스템 (상속 Day 2)
🐍 Python Practice: Animal Shelter System (Inheritance Day 2)
===============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260531
===============================================================


핵심 학습 목표 / Core Learning Goal:
  - super().method() 호출로 부모의 동작을 확장하기
  - Extend parent's behavior by calling super().method()

규칙 / Rules:
  - 자식 클래스의 speak()와 describe()는 반드시 super()를 사용할 것!
  - Child's speak() and describe() MUST use super()!
"""


# ============================================================
# 부모 클래스 / PARENT CLASS (이미 작성됨 / Already written)
# ============================================================
class Animal:
    def __init__(self, name: str, age: int, sound: str):
        self.name = name
        self.age = age
        self.sound = sound

    def speak(self) -> str:
        return f"{self.name} says {self.sound}!"

    def describe(self) -> str:
        return f"{self.name} is {self.age} years old."


# ============================================================
# 자식 클래스 1 / CHILD CLASS 1: Dog
# ============================================================
class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        # TODO 1: super().__init__() 호출하여 부모 속성 초기화
        #         sound는 "Woof"로 고정
        # TODO 1: Call super().__init__() to initialize parent attributes
        #         sound is fixed as "Woof"
        super().__init__(name, age, "Woof")

        # TODO 2: breed 속성 저장
        # TODO 2: Store the breed attribute
        self.breed = breed

    def speak(self) -> str:
        # TODO 3: 부모의 speak() 결과를 받아서 변수에 저장
        # TODO 3: Call parent's speak() and store the result
        parent_message = super().speak()

        # TODO 4: 부모 결과 뒤에 " (A {breed} barking happily)"를 붙여서 반환
        # TODO 4: Return parent's result + " (A {breed} barking happily)"
        return parent_message + f" (A {self.breed} barking happily)"

    def describe(self) -> str:
        # TODO 5: 부모의 describe() 결과를 받아서 변수에 저장
        # TODO 5: Call parent's describe() and store the result
        parent_description = super().describe()

        # TODO 6: 부모 결과 뒤에 " It is a {breed} dog."를 붙여서 반환
        # TODO 6: Return parent's result + " It is a {breed} dog."
        return parent_description + f" It is a {self.breed} dog."


# ============================================================
# 자식 클래스 2 / CHILD CLASS 2: Cat
# ============================================================
class Cat(Animal):
    def __init__(self, name: str, age: int, indoor: bool):
        # TODO 7: super().__init__() 호출, sound는 "Meow"
        # TODO 7: Call super().__init__(), sound is "Meow"
        super().__init__(name, age, "Meow")

        # TODO 8: indoor 속성 저장
        # TODO 8: Store the indoor attribute
        self.indoor = indoor

    def speak(self) -> str:
        # TODO 9: 부모의 speak() 호출
        # TODO 9: Call parent's speak()
        parent_message = super().speak()

        # TODO 10: indoor가 True면 "purring softly", 아니면 "hissing at strangers"
        # TODO 10: If indoor is True, "purring softly"; otherwise "hissing at strangers"
        if self.indoor:
            mood = "purring softly"
        else:
            mood = "hissing at strangers"

        # TODO 11: f"{parent_message} ({mood})" 반환
        # TODO 11: Return f"{parent_message} ({mood})"
        return f"{parent_message} ({mood})"

    def describe(self) -> str:
        # TODO 12: 부모의 describe() 호출
        # TODO 12: Call parent's describe()
        parent_description = super().describe()

        # TODO 13: indoor가 True면 "an indoor", 아니면 "an outdoor"
        # TODO 13: If indoor is True, "an indoor"; otherwise "an outdoor"
        if self.indoor:
            living = "an indoor"
        else:
            living = "an outdoor"

        # TODO 14: f"{parent_description} It is {living} cat." 반환
        # TODO 14: Return f"{parent_description} It is {living} cat."
        return f"{parent_description} It is {living} cat."


# ============================================================
# 자식 클래스 3 / CHILD CLASS 3: Bird
# ============================================================
class Bird(Animal):
    def __init__(self, name: str, age: int, can_fly: bool):
        # TODO 15: super().__init__() 호출, sound는 "Tweet"
        # TODO 15: Call super().__init__(), sound is "Tweet"
        super().__init__(name, age, "Tweet")

        # TODO 16: can_fly 속성 저장
        # TODO 16: Store the can_fly attribute
        self.can_fly = can_fly

    def speak(self) -> str:
        # TODO 17: 부모의 speak() 호출
        # TODO 17: Call parent's speak()
        parent_message = super().speak()

        # TODO 18: can_fly가 True면 "while flying around", 아니면 "from its perch"
        # TODO 18: If can_fly is True, "while flying around"; otherwise "from its perch"
        if self.can_fly:
            action = "while flying around"
        else:
            action = "from its perch"

        # TODO 19: f"{parent_message} ({action})" 반환
        # TODO 19: Return f"{parent_message} ({action})"
        return f"{parent_message} ({action})"

    def describe(self) -> str:
        # TODO 20: 부모의 describe() 호출
        # TODO 20: Call parent's describe()
        parent_description = super().describe()

        # TODO 21: can_fly가 True면 "can fly", 아니면 "cannot fly"
        # TODO 21: If can_fly is True, "can fly"; otherwise "cannot fly"
        if self.can_fly:
            flight = "can fly"
        else:
            flight = "cannot fly"

        # TODO 22: f"{parent_description} This bird {flight}." 반환
        # TODO 22: Return f"{parent_description} This bird {flight}."
        return f"{parent_description} This bird {flight}."


# ============================================================
# 테스트 블록 / TEST BLOCK
# 아래 코드는 수정하지 마세요! / Do NOT modify the code below!
# ============================================================
if __name__ == "__main__":
    try:
        print("=" * 60)
        print("테스트 1 / Test 1: Dog")
        print("=" * 60)
        buddy = Dog("Buddy", 3, "Golden Retriever")
        speak_result = buddy.speak()
        describe_result = buddy.describe()
        print(f"speak():    {speak_result}")
        print(f"describe(): {describe_result}")
        assert speak_result == "Buddy says Woof! (A Golden Retriever barking happily)", \
            f"❌ Dog.speak() 실패 / failed: got {speak_result!r}"
        assert describe_result == "Buddy is 3 years old. It is a Golden Retriever dog.", \
            f"❌ Dog.describe() 실패 / failed: got {describe_result!r}"
        print("✅ 통과 / PASS\n")

        print("=" * 60)
        print("테스트 2 / Test 2: Cat (indoor=True)")
        print("=" * 60)
        whiskers = Cat("Whiskers", 5, True)
        speak_result = whiskers.speak()
        describe_result = whiskers.describe()
        print(f"speak():    {speak_result}")
        print(f"describe(): {describe_result}")
        assert speak_result == "Whiskers says Meow! (purring softly)", \
            f"❌ Cat.speak() 실패 / failed: got {speak_result!r}"
        assert describe_result == "Whiskers is 5 years old. It is an indoor cat.", \
            f"❌ Cat.describe() 실패 / failed: got {describe_result!r}"
        print("✅ 통과 / PASS\n")

        print("=" * 60)
        print("테스트 3 / Test 3: Cat (indoor=False)")
        print("=" * 60)
        shadow = Cat("Shadow", 2, False)
        speak_result = shadow.speak()
        describe_result = shadow.describe()
        print(f"speak():    {speak_result}")
        print(f"describe(): {describe_result}")
        assert speak_result == "Shadow says Meow! (hissing at strangers)", \
            f"❌ Cat.speak() 실패 / failed: got {speak_result!r}"
        assert describe_result == "Shadow is 2 years old. It is an outdoor cat.", \
            f"❌ Cat.describe() 실패 / failed: got {describe_result!r}"
        print("✅ 통과 / PASS\n")

        print("=" * 60)
        print("테스트 4 / Test 4: Bird (can_fly=True)")
        print("=" * 60)
        tweety = Bird("Tweety", 1, True)
        speak_result = tweety.speak()
        describe_result = tweety.describe()
        print(f"speak():    {speak_result}")
        print(f"describe(): {describe_result}")
        assert speak_result == "Tweety says Tweet! (while flying around)", \
            f"❌ Bird.speak() 실패 / failed: got {speak_result!r}"
        assert describe_result == "Tweety is 1 years old. This bird can fly.", \
            f"❌ Bird.describe() 실패 / failed: got {describe_result!r}"
        print("✅ 통과 / PASS\n")

        print("=" * 60)
        print("테스트 5 / Test 5: Bird (can_fly=False)")
        print("=" * 60)
        pingu = Bird("Pingu", 4, False)
        speak_result = pingu.speak()
        describe_result = pingu.describe()
        print(f"speak():    {speak_result}")
        print(f"describe(): {describe_result}")
        assert speak_result == "Pingu says Tweet! (from its perch)", \
            f"❌ Bird.speak() 실패 / failed: got {speak_result!r}"
        assert describe_result == "Pingu is 4 years old. This bird cannot fly.", \
            f"❌ Bird.describe() 실패 / failed: got {describe_result!r}"
        print("✅ 통과 / PASS\n")

        print("=" * 60)
        print("🎉 모든 테스트 통과! / ALL TESTS PASSED!")
        print("=" * 60)

    except AssertionError as e:
        print(f"\n{e}")
        print("\n💡 힌트 / Hint: 출력 문자열의 띄어쓰기, 마침표, 괄호를 다시 확인해보세요.")
        print("💡 Hint: Double-check spaces, periods, and parentheses in your output strings.")
    except TypeError as e:
        print(f"\n❌ TypeError: {e}")
        print("\n💡 힌트 / Hint: __init__의 인자 개수나 super().__init__() 호출을 확인해보세요.")
        print("💡 Hint: Check the number of arguments or your super().__init__() call.")
    except AttributeError as e:
        print(f"\n❌ AttributeError: {e}")
        print("\n💡 힌트 / Hint: 속성 이름(self.name, self.age 등)이 정확한지 확인해보세요.")
        print("💡 Hint: Check that attribute names (self.name, self.age, etc.) are correct.")
    except Exception as e:
        print(f"\n❌ 예상치 못한 에러 / Unexpected error: {type(e).__name__}: {e}")
