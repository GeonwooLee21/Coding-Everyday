"""
===============================================================
🎮 PlayerCharacter — `_` vs `__` 캡슐화 연습
🎮 PlayerCharacter — `_` vs `__` Encapsulation Practice
===============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260530
===============================================================

목표 / Goal:
- Single underscore (_)와 double underscore (__)의 차이를 직접 경험합니다.
- Experience the difference between single (_) and double (__) underscores firsthand.

규칙 / Rules:
- 모든 메서드와 변수 이름은 snake_case
- All method and variable names use snake_case
- 음수 입력은 ValueError 발생
- Negative inputs raise ValueError
"""


class PlayerCharacter:
    """게임 플레이어 캐릭터 / Game player character"""

    def __init__(self, name: str, level: int = 1):
        # TODO 1: Public 속성 저장 / Store public attributes
        # 힌트 / Hint: name과 level은 누구나 볼 수 있는 정보입니다.
        # Hint: name and level are info anyone can see.
        # self.name = ?
        # self.level = ?
        self.name = name
        self.level = level

        # TODO 2: Single underscore 속성 초기화
        # TODO 2: Initialize single underscore attributes
        # 힌트 / Hint: 내부 사용 권장이지만, 막지는 않음
        # Hint: Recommended for internal use, but not blocked
        # self._experience = 0
        # self._stamina = 100
        self._experience = 0
        self._stamina = 100

        # TODO 3: Double underscore 속성 초기화
        # TODO 3: Initialize double underscore attributes
        # 힌트 / Hint: 정말로 외부 접근을 막고 싶은 핵심 데이터
        # Hint: Core data you really want to block from outside
        # self.__health = 100
        # self.__damage_multiplier = 1.0
        self.__health = 100
        self.__damage_multiplier = 1.0

    # ========================================================
    # Getters / 게터 메서드
    # ========================================================

    def get_health(self) -> int:
        # TODO 4: __health 값을 반환하세요.
        # TODO 4: Return the __health value.
        # 힌트 / Hint: 클래스 *내부에서는* self.__health로 접근 가능합니다.
        # Hint: Inside the class, self.__health is accessible.
        return self.__health

    def get_damage_multiplier(self) -> float:
        # TODO 5: __damage_multiplier 값을 반환하세요.
        # TODO 5: Return the __damage_multiplier value.
        return self.__damage_multiplier

    def get_experience(self) -> int:
        # TODO 6: _experience 값을 반환하세요.
        # TODO 6: Return the _experience value.
        return self._experience

    def get_stamina(self) -> int:
        # TODO 7: _stamina 값을 반환하세요.
        # TODO 7: Return the _stamina value.
        return self._stamina

    # ========================================================
    # Behavior methods / 동작 메서드
    # ========================================================

    def take_damage(self, amount: int) -> None:
        # TODO 8: 음수 검증 / Validate non-negative
        # 힌트 / Hint: amount < 0이면 raise ValueError(...)
        # Hint: If amount < 0, raise ValueError(...)
        if amount < 0:
            raise ValueError("amount must be non-negative value.")

        # TODO 9: 체력 감소 (0 미만으로 내려가지 않도록)
        # TODO 9: Reduce health (clamped at 0)
        # 힌트 / Hint: max(0, ...) 사용 / Use max(0, ...)
        self.__health = max(0, self.__health-amount)

    def heal(self, amount: int) -> None:
        # TODO 10: 음수 검증 / Validate non-negative
        if amount < 0:
            raise ValueError("amount must be non-negative value.")

        # TODO 11: 체력 회복 (100 초과하지 않도록)
        # TODO 11: Restore health (capped at 100)
        # 힌트 / Hint: min(100, ...) 사용 / Use min(100, ...)
        self.__health = min(100, self.__health+amount)

    def gain_experience(self, amount: int) -> None:
        # TODO 12: 음수 검증 / Validate non-negative
        if amount < 0:
            raise ValueError("amount must be non-negative value.")

        # TODO 13: XP 추가 / Add XP
        self._experience += amount

        # TODO 14: 자동 레벨업 처리 / Auto level-up
        # 힌트 / Hint: while 루프로 처리 (한 번에 여러 레벨 업 가능)
        # Hint: Use a while loop (could level up multiple times at once)
        # 조건 / Condition: self._experience >= self.level * 100
        # 처리 / Actions:
        #   1) self._experience -= self.level * 100
        #   2) self.level += 1
        #   3) self.__damage_multiplier += 0.1
        while self._experience >= self.level * 100: # 현재 경험치 >= level별 경험치 요구치
            self._experience -= self.level * 100
            self.level += 1
            self.__damage_multiplier += 0.1

    def is_alive(self) -> bool:
        # TODO 15: 체력이 0보다 크면 True, 아니면 False
        # TODO 15: True if health > 0, else False
        # if self.__health > 0:
        #     return True
        # else:
        #     return False
        return self.__health > 0 # self.__health > 0 자체가 이미 bool!


# ============================================================
# 🧪 테스트 / Tests
# ============================================================

if __name__ == "__main__":
    try:
        print("=" * 50)
        print("🧪 Core Tests / 핵심 테스트")
        print("=" * 50)

        # Test 1: 기본 생성 / Basic creation
        hero = PlayerCharacter("아서", 1)
        assert hero.name == "아서", f"name 불일치: {hero.name}"
        assert hero.level == 1
        assert hero.get_health() == 100
        assert hero.get_stamina() == 100
        assert hero.get_experience() == 0
        assert hero.get_damage_multiplier() == 1.0
        assert hero.is_alive() == True
        print("✅ Test 1: 기본 생성 / Basic creation")

        # Test 2: 데미지 / Damage
        hero.take_damage(40)
        assert hero.get_health() == 60
        print("✅ Test 2: take_damage 작동 / works")

        # Test 3: 0 미만 방지 / No negative health
        hero.take_damage(999)
        assert hero.get_health() == 0
        assert hero.is_alive() == False
        print("✅ Test 3: 체력 하한 / Health lower bound")

        # Test 4: 회복 / Healing
        hero2 = PlayerCharacter("힐러")
        hero2.take_damage(50)
        hero2.heal(20)
        assert hero2.get_health() == 70
        print("✅ Test 4: heal 작동 / works")

        # Test 5: 100 초과 방지 / No exceeding 100
        hero2.heal(999)
        assert hero2.get_health() == 100
        print("✅ Test 5: 체력 상한 / Health upper bound")

        # Test 6: 자동 레벨업 / Auto level-up
        hero3 = PlayerCharacter("레벨러")
        hero3.gain_experience(150)
        assert hero3.level == 2, f"레벨 불일치: {hero3.level}"
        assert hero3.get_experience() == 50
        assert abs(hero3.get_damage_multiplier() - 1.1) < 0.001
        print("✅ Test 6: 자동 레벨업 / Auto level-up")

        # Test 7: 검증 / Validation
        try:
            hero3.take_damage(-5)
            print("❌ Test 7 실패: 음수 검증 없음 / no negative validation")
        except ValueError:
            print("✅ Test 7: 음수 검증 / Negative validation")

        # Test 8: __health 직접 접근 차단 / __health blocked
        try:
            _ = hero.__health
            print("❌ Test 8 실패: __health 접근됨 / accessed!")
        except AttributeError:
            print("✅ Test 8: __health 직접 접근 차단 / direct access blocked")

        # Test 9: _experience 직접 접근 가능 (의도된 동작!)
        # Test 9: _experience direct access works (intended!)
        hero4 = PlayerCharacter("실험체")
        _ = hero4._experience  # AttributeError 안 남
        print("✅ Test 9: _experience 접근 가능 (관례만) / accessible (convention only)")

        # Test 10: Name mangling 확인 / Verify name mangling
        assert hasattr(hero4, "_PlayerCharacter__health")
        print("✅ Test 10: Name mangling 작동 / works")


        # Easy Bonus Challenge: _ vs __ 직접 비교 실험
        hero = PlayerCharacter("실험체")

        # 실험 1: Single underscore
        print(hero._experience)      # 결과: 0
        hero._experience = 9999      # 결과: PlayerCharacter 클래스의 hero 객체의 경험치가 9999가 됨
        print(hero._experience)      # 결과: 9999
                                     # single underscore는 관례상의 표기일 뿐이므로, 해당 객체의 속성에 접근 또는 수정가능하다.

        # 실험 2: Double underscore  
        try:
            print(hero.__health)
        except AttributeError as e:
            print(f"에러: {e}")
        # 결과: AttributeError가 발생한다. double underscore로 선언된 객체의 속성은 name mangling으로 한 번 숨겨지므로
        # 속성의 이름을 그대로 사용하는 것으론 해당 속성에 접근하지 못하기 때문이다.

        # 실험 3: 우회 접근
        print(hero._PlayerCharacter__health)  # 결과: 100
        # 왜 이것은 작동할까? double underscore로 선언된 객체의 속성의 이름은 '_[클래스명]__[속성]'으로 mangling되어 저장되므로,
        # 속성의 '진짜' 이름을 통해서는 접근 또는 수정이 가능하다.

        print("\n" + "=" * 50)
        print("🎉 모든 테스트 통과! / All tests passed!")
        print("=" * 50)

    except AssertionError as e:
        print(f"\n❌ 테스트 실패 / Test failed: {e}")
    except Exception as e:
        print(f"\n⚠️ 예상치 못한 오류 / Unexpected error: {type(e).__name__}: {e}")
