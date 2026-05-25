"""
===============================================================
☕ Drink Class Practice
   카페 음료 클래스 연습
===============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260521
===============================================================

Fill in each TODO. Run this file to test as you go.
각 TODO를 채우세요. 실행하면서 테스트해보세요.
"""


class Drink:
    def __init__(self, name, size, base_price, add_milk=False):
        self.name = name
        self.size = size
        self.base_price = base_price
        self.add_milk = add_milk
        self.extra_shots = 0
        self.syrups = []
        self.discount = 0

    def add_shot(self):
        # TODO 6: self.extra_shots를 1 증가시키세요
        #         Increase self.extra_shots by 1
        self.extra_shots += 1


    # Easy Bonus Challenge: 시럽 추가 기능
    def add_syrup(self, flavor):
        self.syrups.append(flavor)


    # Medium Bonus Challenge: 할인 적용
    def apply_discount(self, percent):
        self.discount = percent


    def get_price(self):
        # TODO 7: size_fee를 계산하세요 (Small=0, Medium=500, Large=1000)
        #         Compute size_fee (Small=0, Medium=500, Large=1000)
        size_fee = 0
        if self.size == "Small":
            size_fee = 0
        elif self.size == "Medium":
            size_fee = 500
        elif self.size == "Large":
            size_fee = 1000

        # TODO 8: 우유 추가 요금을 계산하세요 (True면 500, 아니면 0)
        #         Compute milk fee (500 if add_milk else 0)
        milk_fee = 0
        if self.add_milk:
            milk_fee = 500
        else:
            milk_fee = 0

        # TODO 9: 샷 추가 요금을 계산하세요 (extra_shots × 500)
        #         Compute shot fee (extra_shots × 500)
        shot_fee = self.extra_shots * 500

        syrup_fee = len(self.syrups) * 500

        # TODO 10: 최종 가격을 계산해서 반환하세요
        #          Compute and return the total price
        # total = base_price + size_fee + milk_fee + shot_fee
        total = self.base_price + size_fee + milk_fee + shot_fee + syrup_fee
        total -= total * (self.discount / 100)
        return total
        


    def describe(self):
        # TODO 11: 우유 여부를 나타내는 문자열을 만드세요
        #          Build a string showing whether milk is added
        # 힌트 / Hint: "with milk" if self.add_milk else "no milk"
        milk_text = ""
        if self.add_milk:
            milk_text += "with milk"
        else:
            milk_text += "no milk"

        syrup_text = ""
        if self.syrups: 
            syrup_text = ", ".join(self.syrups) 
            syrup_text += " syrup"
        else:
            syrup_text = "no syrup"

        return f"{self.size} {self.name} ({milk_text}, {syrup_text},+{self.extra_shots} shot)"
    
    

# ============================================================
# 테스트 블록 / Test Block — 수정하지 마세요 / Do not modify
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("테스트 시작 / Running tests")
    print("=" * 50)

    try:
        # Test 1
        d1 = Drink("Americano", "Small", 3000)
        print(f"\n[Test 1] Price: {d1.get_price()}원 / Desc: {d1.describe()}")
        print("        Expected: 3000원 / Small Americano (no milk, +0 shot)")

        # Test 2
        d2 = Drink("Latte", "Medium", 4000, add_milk=True)
        print(f"\n[Test 2] Price: {d2.get_price()}원")
        print("        Expected: 5000원")

        # Test 3
        d3 = Drink("Latte", "Large", 4000, add_milk=True)
        d3.add_shot()
        d3.add_shot()
        print(f"\n[Test 3] Price: {d3.get_price()}원 / Desc: {d3.describe()}")
        print("        Expected: 6500원 / Large Latte (with milk, +2 shot)")

        # Test 4: independence
        d4a = Drink("Espresso", "Small", 2500)
        d4b = Drink("Espresso", "Small", 2500)
        d4a.add_shot()
        print(f"\n[Test 4] d4a shots: {d4a.extra_shots} / d4b shots: {d4b.extra_shots}")
        print("        Expected: 1 / 0")

        # Test 5: syrup
        d5 = Drink("Vanilla Latte", "Medium", 4500, add_milk=True)
        d5.add_syrup("vanilla")
        d5.add_syrup("hazelnut")
        print(f"\n[Test 5] Price: {d5.get_price()}원 / Desc: {d5.describe()}")
        print("        Expected: 6500원 / Medium Vanilla Latte (with milk, vanilla, hazelnut syrup, +0 shot)")
        # 4500 + 500(Medium) + 500(milk) + 1000(syrup×2) = 7000원

        # Test 6: discount
        d6 = Drink("Latte", "Medium", 4000, add_milk=True)
        d6.apply_discount(10)
        print(f"\n[Test 6] Price: {d6.get_price()}원")
        print("        Expected: 4500원")
        # 4000 + 500(Medium) + 500(milk) = 5000원 → 10% 할인 → 4500원

    except AttributeError as e:
        print(f"\n⚠️  AttributeError: {e}")
        print("   __init__에서 속성을 제대로 저장했는지 확인하세요")
        print("   Check that all attributes are stored in __init__")
    except Exception as e:
        print(f"\n⚠️  에러 / Error: {type(e).__name__}: {e}")
