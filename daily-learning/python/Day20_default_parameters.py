# =============================================================
# default_parameters.py
# 🐍 Default Parameters Practice
# =============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260416
# =============================================================


# ──────────────────────────────────────────────
# 함수 1 / Function 1: greet_user
# ──────────────────────────────────────────────
# 시나리오: 사용자를 환영하는 메시지를 만드세요.
# Scenario: Build a welcome message for a user.
#
# 파라미터 / Parameters:
#   name     : 사용자 이름 / the user's name
#   greeting : 인사말 — 기본값은 "Hello" / greeting word — default is "Hello"
#
# 반환 / Returns:
#   "{greeting}, {name}!" 형태의 문자열 / a string in the format "{greeting}, {name}!"

def greet_user(name: str, greeting: str = "Hello") -> str:
    # TODO 1 (KO): f-string을 사용해서 "{greeting}, {name}!" 형태의 문자열을 만들고 반환하세요.
    # TODO 1 (EN): Use an f-string to build and return a string in the format "{greeting}, {name}!".
    return f"{greeting}, {name}!"


# ──────────────────────────────────────────────
# 함수 2 / Function 2: calculate_shipping
# ──────────────────────────────────────────────
# 시나리오: 쇼핑몰 최종 결제 금액을 계산하세요.
# Scenario: Calculate the final checkout amount for an online store.
#
# 파라미터 / Parameters:
#   price         : 원래 가격 / original price
#   discount_rate : 할인율 (0.1 = 10% 할인) — 기본값 0.0 / discount rate — default 0.0
#   shipping_fee  : 배송비 — 기본값 3000 / shipping fee — default 3000
#
# 공식 / Formula:
#   할인된 가격 / discounted price = price × (1 - discount_rate)
#   최종 금액 / final amount       = 할인된 가격 + shipping_fee
#
# 반환 / Returns:
#   최종 결제 금액 (float) / final payment amount (float)

def calculate_shipping(price: float, discount_rate: float = 0.0, shipping_fee: float = 3000) -> float:
    # TODO 2-1 (KO): price에 (1 - discount_rate)를 곱해서 할인된 가격을 계산하세요.
    # TODO 2-1 (EN): Multiply price by (1 - discount_rate) to get the discounted price.
    discounted_price = price * (1 - discount_rate)  # ← 이 줄을 수정하세요 / modify this line

    # TODO 2-2 (KO): 할인된 가격에 shipping_fee를 더해서 반환하세요.
    # TODO 2-2 (EN): Add shipping_fee to the discounted price and return the result.
    return discounted_price + shipping_fee


# ──────────────────────────────────────────────
# 함수 3 / Function 3: format_leaderboard_entry
# ──────────────────────────────────────────────
# 시나리오: 게임 리더보드 항목을 문자열로 만드세요.
# Scenario: Format a game leaderboard entry as a string.
#
# 파라미터 / Parameters:
#   rank  : 순위 (1, 2, 3, ...) / ranking position
#   name  : 플레이어 이름 / player name
#   score : 점수 / score
#   label : 플레이어 등급 — 기본값 "Player" / player tier label — default "Player"
#
# 출력 형식 / Output format:
#   "#{rank} [{label}] {name} — {score}pts"
#   예시 / example: "#1 [Player] Alice — 9800pts"
#
# ⚠️  주의: — 는 긴 대시(em dash)입니다. 아래에서 복사하세요!
# ⚠️  Note: — is an em dash, not a hyphen. Copy it from below!
#            —

def format_leaderboard_entry(rank: int, name: str, score: int, label: str = "Player") -> str:
    # TODO 3 (KO): f-string으로 "#{rank} [{label}] {name} — {score}pts" 형태의 문자열을 만들어 반환하세요.
    # TODO 3 (EN): Use an f-string to build and return "#{rank} [{label}] {name} — {score}pts".
    return f"#{rank} [{label}] {name} — {score}pts"


# ──────────────────────────────────────────────
# 함수 4 / Function 4: repeat_message
# ──────────────────────────────────────────────
# 시나리오: 메시지를 여러 번 반복하여 하나의 문자열로 만드세요.
# Scenario: Repeat a message multiple times into a single string.
#
# 파라미터 / Parameters:
#   message   : 반복할 메시지 / the message to repeat
#   times     : 반복 횟수 — 기본값 3 / number of repetitions — default 3
#   separator : 메시지 사이의 구분자 — 기본값 " | " / separator between messages — default " | "
#
# 규칙 / Rules:
#   - 구분자는 메시지 사이에만 붙어요 (마지막 메시지 뒤에는 붙지 않아요!)
#   - Separator goes BETWEEN messages only (NOT after the last one!)
#   - repeat_message("Go!", 3, " | ") → "Go! | Go! | Go!"  ✅
#   - repeat_message("Go!", 3, " | ") → "Go! | Go! | Go! |"  ❌

def repeat_message(message: str, times: int = 3, separator: str = " | ") -> str:
    # TODO 4-1 (KO): 빈 문자열 result = "" 로 시작하세요.
    # TODO 4-1 (EN): Start with an empty string: result = "".
    result = ""

    # TODO 4-2 (KO): range(times)로 반복하면서, 각 반복에서 message를 result에 더하세요.
    # TODO 4-2 (EN): Loop with range(times), adding message to result in each iteration.
    for i in range(times):
        # TODO 4-3 (KO): 마지막 반복이 아닐 때만 separator를 붙이세요.
        #                 힌트: 마지막 인덱스는 times - 1 입니다.
        # TODO 4-3 (EN): Only add the separator when it's NOT the last iteration.
        #                 Hint: the last index is times - 1.if i != times-1:
        if i != times - 1:
            result += message
            result += separator
        else:
            result += message
        
    # TODO 4-4 (KO): 완성된 result를 반환하세요.
    # TODO 4-4 (EN): Return the completed result.
    return result


# ──────────────────────────────────────────────
# 🧪 테스트 / Test Cases
# ──────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50)
    print("테스트 1 / Test 1: greet_user")
    print("=" * 50)
    print(greet_user("Alice"))                       # Hello, Alice!
    print(greet_user("Bob", "Hi"))                   # Hi, Bob!
    print(greet_user("지수", "안녕하세요"))             # 안녕하세요, 지수!
    print(greet_user(greeting="Hey", name="Sam"))    # Hey, Sam!

    print()
    print("=" * 50)
    print("테스트 2 / Test 2: calculate_shipping")
    print("=" * 50)
    print(calculate_shipping(10000))                 # 13000.0
    print(calculate_shipping(10000, 0.1))            # 12000.0
    print(calculate_shipping(10000, 0.1, 0))         # 9000.0
    print(calculate_shipping(50000, shipping_fee=0)) # 50000.0
    print(calculate_shipping(20000, 0.2, 2500))      # 18500.0

    print()
    print("=" * 50)
    print("테스트 3 / Test 3: format_leaderboard_entry")
    print("=" * 50)
    print(format_leaderboard_entry(1, "Alice", 9800))          # #1 [Player] Alice — 9800pts
    print(format_leaderboard_entry(2, "Bob", 8500, "VIP"))     # #2 [VIP] Bob — 8500pts
    print(format_leaderboard_entry(3, "지수", 7200, "챌린저"))  # #3 [챌린저] 지수 — 7200pts

    print()
    print("=" * 50)
    print("테스트 4 / Test 4: repeat_message")
    print("=" * 50)
    print(repeat_message("Go!"))                     # Go! | Go! | Go!
    print(repeat_message("Go!", 2))                  # Go! | Go!
    print(repeat_message("Go!", 4, " / "))           # Go! / Go! / Go! / Go!
    print(repeat_message("Hi", 1, "---"))            # Hi
    print(repeat_message("야호", 3, "🎉"))            # 야호🎉야호🎉야호
