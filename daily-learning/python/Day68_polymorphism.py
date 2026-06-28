"""
=================================================================
🌳 Python 연습: 다형성으로 정원 설계하기 (Polymorphism Practice)
=================================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260612
=================================================================


조경 회사의 신입 개발자가 되어, 다양한 모양의 정원 화단을 다루는
클래스 계층을 다형성으로 설계해봅시다.

Build a class hierarchy using polymorphism to handle garden beds of
different shapes, as a junior developer at a landscaping company.
"""

import math


# =============================================================================
# TODO 1: Shape 부모 클래스 작성하기 (Build the Shape parent class)
# =============================================================================
# 모든 도형이 공유하는 속성과 메서드를 정의합니다.
# Define attributes and methods shared by all shapes.

class Shape:
    def __init__(self, name: str, color: str):
        # TODO 1-1: 비공개 속성 self._name과 self._color를 매개변수로 초기화하세요.
        # TODO 1-1: Initialize private attributes self._name and self._color from the parameters.
        self._name = name
        self._color = color

    def get_name(self) -> str:
        # TODO 1-2: self._name을 반환하세요.
        # TODO 1-2: Return self._name.
        return self._name

    def get_color(self) -> str:
        # TODO 1-3: self._color를 반환하세요.
        # TODO 1-3: Return self._color.
        return self._color

    def area(self) -> float:
        # 부모 버전 — 자식 클래스가 오버라이드할 예정입니다.
        # Parent version — child classes will override this.
        return 0.0

    def perimeter(self) -> float:
        # 부모 버전 — 자식 클래스가 오버라이드할 예정입니다.
        # Parent version — child classes will override this.
        return 0.0


# =============================================================================
# TODO 2: Circle (원) 자식 클래스 작성하기
# =============================================================================
# Shape를 상속받아 원형 화단을 모델링하세요.
# Inherit from Shape to model a circular bed.

class Circle(Shape):
    def __init__(self, name: str, color: str, radius: float):
        # TODO 2-1: super().__init__()을 사용해 부모를 초기화하세요.
        # TODO 2-1: Use super().__init__() to initialize the parent.
        super().__init__(name, color)

        # TODO 2-2: self._radius를 매개변수로 초기화하세요.
        # TODO 2-2: Initialize self._radius from the parameter.
        self._radius = radius

    def area(self) -> float:
        # TODO 2-3: 원의 면적 공식 (π × r²)을 반환하세요. math.pi 사용.
        # TODO 2-3: Return the circle area formula (π × r²). Use math.pi.
        return math.pi * (self._radius**2)

    def perimeter(self) -> float:
        # TODO 2-4: 원의 둘레 공식 (2π × r)을 반환하세요.
        # TODO 2-4: Return the circle perimeter formula (2π × r).
        return 2*math.pi * self._radius


# =============================================================================
# TODO 3: Rectangle (직사각형) 자식 클래스 작성하기
# =============================================================================

class Rectangle(Shape):
    def __init__(self, name: str, color: str, width: float, height: float):
        # TODO 3-1: 부모를 초기화하고, self._width와 self._height를 초기화하세요.
        # TODO 3-1: Initialize the parent, then initialize self._width and self._height.
        super().__init__(name, color)
        self._width = width
        self._height = height        

    def area(self) -> float:
        # TODO 3-2: 직사각형 면적 (width × height)을 반환하세요.
        # TODO 3-2: Return the rectangle area (width × height).
        return self._width * self._height

    def perimeter(self) -> float:
        # TODO 3-3: 직사각형 둘레 (2 × (width + height))를 반환하세요.
        # TODO 3-3: Return the rectangle perimeter (2 × (width + height)).
        return 2 * (self._width + self._height)


# =============================================================================
# TODO 4: Triangle (삼각형) 자식 클래스 작성하기
# =============================================================================
# 세 변의 길이로 삼각형을 정의합니다. Heron의 공식을 사용해 면적을 계산하세요.
# Define a triangle by its three sides. Use Heron's formula for the area.

class Triangle(Shape):
    def __init__(self, name: str, color: str, side_a: float, side_b: float, side_c: float):
        # TODO 4-1: 부모를 초기화하고, 세 변 self._side_a, self._side_b, self._side_c를 초기화하세요.
        # TODO 4-1: Initialize the parent, then initialize self._side_a, self._side_b, self._side_c.
        super().__init__(name, color)
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

    def area(self) -> float:
        # TODO 4-2: Heron의 공식을 사용해 면적을 계산하세요.
        # TODO 4-2: Compute the area using Heron's formula.
        #   s = (a + b + c) / 2
        #   area = √(s × (s−a) × (s−b) × (s−c))
        #   math.sqrt()를 사용하세요 / use math.sqrt()
        s = (self._side_a + self._side_b + self._side_c) / 2
        return math.sqrt(s * (s - self._side_a) * (s - self._side_b) * (s - self._side_c))

    def perimeter(self) -> float:
        # TODO 4-3: 세 변의 합을 반환하세요.
        # TODO 4-3: Return the sum of the three sides.
        return self._side_a + self._side_b + self._side_c


# =============================================================================
# TODO 5: 다형성 함수 — total_garden_area
# =============================================================================
# 이 함수가 다형성의 핵심입니다! 도형이 무엇이든 .area()만 호출하면 됩니다.
# This is where polymorphism shines! Just call .area() — Python handles the rest.

def total_garden_area(shapes: list) -> float:
    # TODO 5-1: total 변수를 0.0으로 초기화하세요.
    # TODO 5-1: Initialize a total variable to 0.0.
    total = 0.0

    # TODO 5-2: shapes 리스트의 각 shape를 반복하면서 shape.area()를 total에 더하세요.
    # TODO 5-2: Loop through each shape in shapes and add shape.area() to total.
    for shape in shapes:
        total += shape.area()

    # TODO 5-3: total을 반환하세요.
    # TODO 5-3: Return total.
    return total


# =============================================================================
# TODO 6: 다형성 함수 — total_fence_length
# =============================================================================

def total_fence_length(shapes: list) -> float:
    # TODO 6-1: total_garden_area와 동일한 패턴으로, perimeter()의 합을 반환하세요.
    # TODO 6-1: Same pattern as total_garden_area, but sum the perimeters instead.
    total = 0.0
    for shape in shapes:
        total += shape.perimeter()
    return total


# =============================================================================
# 🎪 테스트 코드 — 이 아래는 수정하지 마세요!
# 🎪 Test code — DO NOT modify below this line!
# =============================================================================

if __name__ == "__main__":
    try:
        # Test 1: 개별 도형 / Individual shapes
        rose = Circle("Rose Bed", "red", 5)
        veggie = Rectangle("Vegetable Patch", "green", 4, 6)
        herb = Triangle("Herb Garden", "yellow", 3, 4, 5)

        print("=" * 50)
        print("Test 1: 개별 도형 / Individual shapes")
        print("=" * 50)
        print(f"{rose.get_name()}: 면적/area = {rose.area():.2f}")
        print(f"  예상/Expected: 78.54")
        print(f"{veggie.get_name()}: 면적/area = {veggie.area():.2f}")
        print(f"  예상/Expected: 24.00")
        print(f"{herb.get_name()}: 면적/area = {herb.area():.2f}")
        print(f"  예상/Expected: 6.00")

        # Test 2: 다형성 / Polymorphism
        print()
        print("=" * 50)
        print("Test 2: 다형성 / Polymorphism")
        print("=" * 50)
        garden = [rose, veggie, herb]
        print(f"전체 면적/Total area: {total_garden_area(garden):.2f}")
        print(f"  예상/Expected: 108.54")
        print(f"전체 둘레/Total perimeter: {total_fence_length(garden):.2f}")
        print(f"  예상/Expected: 63.42")

        # Test 3: 빈 정원 / Empty garden
        print()
        print("=" * 50)
        print("Test 3: 빈 정원 / Empty garden")
        print("=" * 50)
        print(f"빈 정원 면적/Empty garden area: {total_garden_area([])}")
        print(f"  예상/Expected: 0.0")

        print()
        print("🎉 모든 테스트 완료! / All tests complete!")

    except TypeError as e:
        print(f"❌ TypeError: {e}")
        print("   힌트: TODO를 모두 완성했나요? '___'가 남아있지 않은지 확인하세요.")
        print("   Hint: Did you finish all TODOs? Check for any remaining '___'.")
    except AttributeError as e:
        print(f"❌ AttributeError: {e}")
        print("   힌트: 메서드 이름과 self._속성 이름을 확인하세요.")
        print("   Hint: Check method names and self._attribute names.")
    except Exception as e:
        print(f"❌ {type(e).__name__}: {e}")
        print("   힌트: 위의 에러 메시지를 읽고 해당 TODO를 다시 확인하세요.")
        print("   Hint: Read the error message above and revisit that TODO.")
