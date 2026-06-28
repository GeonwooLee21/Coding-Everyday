"""
===============================================================
RPG 파티 만들기 — 상속 연습
RPG Party Builder — Inheritance Practice
===============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260531
===============================================================

목표 / Goal:
    Character 부모 클래스와 Warrior, Mage, Archer 자식 클래스를 만드세요.
    Build a Character parent class and Warrior, Mage, Archer child classes.

이름 규칙 / Naming: snake_case
"""


# ============================================================
# 1. Character 클래스 (부모) / Character class (parent)
# ============================================================
class Character:
    # TODO 1: __init__ 메서드를 작성하세요.
    # TODO 1: Write the __init__ method.
    #   - 매개변수 / parameters: name, hp, level (기본값 / default = 1)
    #   - 속성 4개 초기화 / Initialize 4 attributes:
    #       self.name, self.hp, self.max_hp (= hp), self.level
    def __init__(self, name, hp, level=1):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.level = level

    # TODO 2: introduce 메서드를 작성하세요.
    # TODO 2: Write the introduce method.
    #   - 반환 형식 / Return format:
    #       "I am {name}, a level {level} adventurer with {hp} HP."
    def introduce(self):
        return f"I am {self.name}, a level {self.level} adventurer with {self.hp} HP."

    # TODO 3: take_damage 메서드를 작성하세요.
    # TODO 3: Write the take_damage method.
    #   - hp에서 amount만큼 감소 / Subtract amount from hp
    #   - hp가 0 미만이면 0으로 / Clamp to 0 if it goes below
    def take_damage(self, amount):
        self.hp = max(0, self.hp-amount)

    # TODO 4: level_up 메서드를 작성하세요.
    # TODO 4: Write the level_up method.
    #   - level + 1
    #   - max_hp + 10
    #   - hp를 새 max_hp로 회복 / restore hp to the new max_hp
    def level_up(self):
        self.level += 1
        self.max_hp += 10
        self.hp = self.max_hp

    # TODO 5: is_alive 메서드를 작성하세요.
    # TODO 5: Write the is_alive method.
    #   - hp > 0 이면 True, 아니면 False
    def is_alive(self):
        return self.hp > 0

    # TODO 6: __str__ 메서드를 작성하세요.
    # TODO 6: Write the __str__ method.
    #   - 반환 형식 / Return format:
    #       "{name} (Lv.{level}, HP: {hp}/{max_hp})"
    def __str__(self):
        return f"{self.name} (Lv.{self.level}, HP: {self.hp}/{self.max_hp})"


# ============================================================
# 2. Warrior 클래스 / Warrior class (inherits from Character)
# ============================================================
# TODO 7: Warrior 클래스가 Character를 상속받도록 선언하세요.
# TODO 7: Declare Warrior as a class that inherits from Character.
class Warrior(Character):  # ← 여기를 수정 / fix this line
    # TODO 8: __init__ 작성.
    # TODO 8: Write __init__.
    #   - 매개변수 / parameters: name, hp, level=1, weapon="Sword"
    #   - 부모의 __init__ 호출 / call parent's __init__:
    #       Character.__init__(self, name, hp, level)
    #   - self.weapon = weapon
    #   - self.armor = 5
    def __init__(self, name, hp, level=1, weapon="Sword"):
        Character.__init__(self, name, hp, level)
        self.weapon = weapon
        self.armor = 5

    # TODO 9: battle_cry 메서드 작성.
    # TODO 9: Write battle_cry method.
    #   - 반환 / Return:
    #       "{name} swings the {weapon} and shouts: For glory!"
    def battle_cry(self):
        return f"{self.name} swings the {self.weapon} and shouts: For glory!"


# ============================================================
# 3. Mage 클래스 / Mage class (inherits from Character)
# ============================================================
# TODO 10: Mage 클래스가 Character를 상속받도록 선언하세요.
# TODO 10: Declare Mage as a class that inherits from Character.
class Mage(Character):  # ← 여기를 수정 / fix this line
    # TODO 11: __init__ 작성.
    # TODO 11: Write __init__.
    #   - 매개변수: name, hp, level=1, mana=50
    #   - 부모의 __init__ 호출 / call parent's __init__
    #   - self.mana = mana
    #   - self.spell_book = ["Fireball", "Ice Shard"]
    def __init__(self, name, hp, level=1, mana=50):
        Character.__init__(self, name, hp, level)
        self.mana = mana
        self.spell_book = ["Fireball", "Ice Shard"]

    # TODO 12: cast_spell 메서드 작성.
    # TODO 12: Write cast_spell method.
    #   - spell_name이 spell_book에 있고 mana >= 10 이면:
    #     If spell_name is in spell_book AND mana >= 10:
    #       - mana -= 10
    #       - return "{name} casts {spell_name}!"
    #   - 아니면 / else:
    #       - return "{name} cannot cast {spell_name}."
    def cast_spell(self, spell_name):
        if spell_name in self.spell_book and self.mana >= 10:
            self.mana -= 10
            return f"{self.name} casts {spell_name}!"
        else:
            return f"{self.name} cannot cast {spell_name}."


# ============================================================
# 4. Archer 클래스 / Archer class (inherits from Character)
# ============================================================
# TODO 13: Archer 클래스가 Character를 상속받도록 선언하세요.
# TODO 13: Declare Archer as a class that inherits from Character.
class Archer(Character):  # ← 여기를 수정 / fix this line
    # TODO 14: __init__ 작성.
    # TODO 14: Write __init__.
    #   - 매개변수: name, hp, level=1, arrows=20
    #   - 부모의 __init__ 호출 / call parent's __init__
    #   - self.arrows = arrows
    #   - self.range = 50
    def __init__(self, name, hp, level=1, arrows=20):
        Character.__init__(self, name, hp, level)
        self.arrows = arrows
        self.range = 50

    # TODO 15: shoot_arrow 메서드 작성.
    # TODO 15: Write shoot_arrow method.
    #   - arrows > 0 이면 / if arrows > 0:
    #       - arrows -= 1
    #       - return "{name} shoots an arrow! Arrows left: {arrows}"
    #   - 아니면 / else:
    #       - return "{name} is out of arrows!"
    def shoot_arrow(self):
        if self.arrows > 0:
            self.arrows -= 1
            return f"{self.name} shoots an arrow! Arrows left: {self.arrows}"
        else:
            return f"{self.name} is out of arrows!"


# ============================================================
# 테스트 블록 / Test block — DO NOT MODIFY 수정 금지
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("RPG 파티 테스트 / RPG Party Tests")
    print("=" * 50)

    # Test 1: Character 기본 동작
    try:
        hero = Character("Hero", 100)
        assert hero.name == "Hero"
        assert hero.hp == 100
        assert hero.max_hp == 100
        assert hero.level == 1
        print("[PASS] Test 1: Character __init__")
    except Exception as e:
        print(f"[FAIL] Test 1: Character __init__ — {e}")

    # Test 2: introduce
    try:
        hero = Character("Hero", 100)
        result = hero.introduce()
        assert result == "I am Hero, a level 1 adventurer with 100 HP.", f"Got: {result}"
        print("[PASS] Test 2: introduce()")
    except Exception as e:
        print(f"[FAIL] Test 2: introduce() — {e}")

    # Test 3: take_damage (정상 + clamp)
    try:
        hero = Character("Hero", 100)
        hero.take_damage(30)
        assert hero.hp == 70
        hero.take_damage(200)
        assert hero.hp == 0, f"HP should clamp to 0, got {hero.hp}"
        print("[PASS] Test 3: take_damage()")
    except Exception as e:
        print(f"[FAIL] Test 3: take_damage() — {e}")

    # Test 4: level_up
    try:
        hero = Character("Hero", 80, 3)
        hero.take_damage(50)  # hp = 30
        hero.level_up()
        assert hero.level == 4
        assert hero.max_hp == 90
        assert hero.hp == 90, f"hp should restore to max_hp, got {hero.hp}"
        print("[PASS] Test 4: level_up()")
    except Exception as e:
        print(f"[FAIL] Test 4: level_up() — {e}")

    # Test 5: is_alive
    try:
        hero = Character("Hero", 100)
        assert hero.is_alive() == True
        hero.take_damage(100)
        assert hero.is_alive() == False
        print("[PASS] Test 5: is_alive()")
    except Exception as e:
        print(f"[FAIL] Test 5: is_alive() — {e}")

    # Test 6: __str__
    try:
        hero = Character("Hero", 100)
        assert str(hero) == "Hero (Lv.1, HP: 100/100)", f"Got: {str(hero)}"
        print("[PASS] Test 6: __str__")
    except Exception as e:
        print(f"[FAIL] Test 6: __str__ — {e}")

    # Test 7: Warrior 상속 확인
    try:
        conan = Warrior("Conan", 120)
        assert conan.name == "Conan"
        assert conan.hp == 120
        assert conan.max_hp == 120
        assert conan.level == 1
        assert conan.weapon == "Sword"
        assert conan.armor == 5
        # Inherits Character?
        assert isinstance(conan, Character), "Warrior must inherit from Character"
        print("[PASS] Test 7: Warrior __init__ & inheritance")
    except Exception as e:
        print(f"[FAIL] Test 7: Warrior __init__ & inheritance — {e}")

    # Test 8: Warrior battle_cry
    try:
        conan = Warrior("Conan", 120)
        assert conan.battle_cry() == "Conan swings the Sword and shouts: For glory!"
        # Custom weapon
        aragorn = Warrior("Aragorn", 150, 5, "Andúril")
        assert aragorn.battle_cry() == "Aragorn swings the Andúril and shouts: For glory!"
        print("[PASS] Test 8: battle_cry()")
    except Exception as e:
        print(f"[FAIL] Test 8: battle_cry() — {e}")

    # Test 9: Warrior가 상속받은 메서드 사용
    try:
        conan = Warrior("Conan", 120)
        conan.take_damage(20)
        assert conan.hp == 100
        conan.level_up()
        assert conan.level == 2
        assert str(conan) == "Conan (Lv.2, HP: 130/130)", f"Got: {str(conan)}"
        print("[PASS] Test 9: Warrior inherits parent methods")
    except Exception as e:
        print(f"[FAIL] Test 9: Warrior inherits parent methods — {e}")

    # Test 10: Mage
    try:
        gandalf = Mage("Gandalf", 70)
        assert gandalf.mana == 50
        assert gandalf.spell_book == ["Fireball", "Ice Shard"]
        assert isinstance(gandalf, Character), "Mage must inherit from Character"
        print("[PASS] Test 10: Mage __init__ & inheritance")
    except Exception as e:
        print(f"[FAIL] Test 10: Mage __init__ & inheritance — {e}")

    # Test 11: cast_spell
    try:
        gandalf = Mage("Gandalf", 70)
        r1 = gandalf.cast_spell("Fireball")
        assert r1 == "Gandalf casts Fireball!", f"Got: {r1}"
        assert gandalf.mana == 40
        r2 = gandalf.cast_spell("Lightning")  # not in spell book
        assert r2 == "Gandalf cannot cast Lightning.", f"Got: {r2}"
        assert gandalf.mana == 40  # mana not deducted
        # Out of mana
        gandalf.mana = 5
        r3 = gandalf.cast_spell("Fireball")
        assert r3 == "Gandalf cannot cast Fireball.", f"Got: {r3}"
        print("[PASS] Test 11: cast_spell()")
    except Exception as e:
        print(f"[FAIL] Test 11: cast_spell() — {e}")

    # Test 12: Archer
    try:
        legolas = Archer("Legolas", 90)
        assert legolas.arrows == 20
        assert legolas.range == 50
        assert isinstance(legolas, Character), "Archer must inherit from Character"
        print("[PASS] Test 12: Archer __init__ & inheritance")
    except Exception as e:
        print(f"[FAIL] Test 12: Archer __init__ & inheritance — {e}")

    # Test 13: shoot_arrow
    try:
        legolas = Archer("Legolas", 90)
        r1 = legolas.shoot_arrow()
        assert r1 == "Legolas shoots an arrow! Arrows left: 19", f"Got: {r1}"
        assert legolas.arrows == 19
        # Out of arrows
        legolas.arrows = 0
        r2 = legolas.shoot_arrow()
        assert r2 == "Legolas is out of arrows!", f"Got: {r2}"
        print("[PASS] Test 13: shoot_arrow()")
    except Exception as e:
        print(f"[FAIL] Test 13: shoot_arrow() — {e}")

    # Test 14: __str__이 자식 클래스에 상속되는지 확인
    try:
        conan = Warrior("Conan", 120)
        gandalf = Mage("Gandalf", 70)
        legolas = Archer("Legolas", 90)
        assert str(conan) == "Conan (Lv.1, HP: 120/120)"
        assert str(gandalf) == "Gandalf (Lv.1, HP: 70/70)"
        assert str(legolas) == "Legolas (Lv.1, HP: 90/90)"
        print("[PASS] Test 14: __str__ inherited by all children")
    except Exception as e:
        print(f"[FAIL] Test 14: __str__ inherited — {e}")

    print("=" * 50)
    print("끝났습니다! / Done! 모든 [PASS]가 보이면 성공입니다.")
    print("All [PASS] = success!")
