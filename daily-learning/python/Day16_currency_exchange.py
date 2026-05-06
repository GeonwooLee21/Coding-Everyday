# =============================================================
# 💱 currency_exchange_skeleton.py
# 환전 계산기 / Currency Exchange Calculator
# =============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260415
# =============================================================


# ══════════════════════════════════════════════════════════════════
# 함수 1 / Function 1
# 환전 후 받는 금액 / Value received after exchange
# ══════════════════════════════════════════════════════════════════

def exchange_money(budget, exchange_rate):
    """
    매개변수 / Parameters:
        budget        : 환전할 금액 / Amount of money to exchange
        exchange_rate : 외국 돈 1단위당 내 나라 돈의 금액
                        / Home currency needed to buy 1 unit of foreign currency
    반환값 / Returns:
        환전 후 받는 외국 돈의 금액 / Amount of foreign currency received
    예시 / Example:
        exchange_money(127.5, 1.2)  →  106.25
    """

    # TODO 1: budget을 exchange_rate로 나누어 반환하세요.
    #         Divide budget by exchange_rate and return the result.
    return budget / exchange_rate


# ══════════════════════════════════════════════════════════════════
# 함수 2 / Function 2
# 환전 후 남은 금액 / Money left after exchange
# ══════════════════════════════════════════════════════════════════

def get_change(budget, exchanging_value):
    """
    매개변수 / Parameters:
        budget           : 환전 전 총 보유 금액 / Total money before exchange
        exchanging_value : 환전에 사용한 금액 / Amount handed over for exchange
    반환값 / Returns:
        지갑에 남아있는 원래 화폐 금액 / Remaining original currency
    예시 / Example:
        get_change(127.5, 120)  →  7.5
    """

    # TODO 1: budget에서 exchanging_value를 빼서 반환하세요.
    #         Subtract exchanging_value from budget and return the result.
    return budget - exchanging_value


# ══════════════════════════════════════════════════════════════════
# 함수 3 / Function 3
# 지폐 다발의 총 가치 / Total value of a stack of bills
# ══════════════════════════════════════════════════════════════════

def get_value_of_bills(denomination, number_of_bills):
    """
    매개변수 / Parameters:
        denomination    : 지폐 한 장의 금액 (예: 5, 20)
                          / Value of one bill (e.g. 5, 20)
        number_of_bills : 지폐의 장수 / Number of bills
    반환값 / Returns:
        지폐 다발의 총 가치 / Total value of all bills
    예시 / Example:
        get_value_of_bills(5, 128)  →  640
    """

    # TODO 1: denomination과 number_of_bills를 곱하여 반환하세요.
    #         Multiply denomination by number_of_bills and return the result.
    return denomination * number_of_bills


# ══════════════════════════════════════════════════════════════════
# 함수 4 / Function 4
# 받을 수 있는 지폐 장수 / Number of whole bills receivable
# ══════════════════════════════════════════════════════════════════

def get_number_of_bills(amount, denomination):
    """
    매개변수 / Parameters:
        amount       : 환전할 총 금액 / Total amount to exchange
        denomination : 지폐 한 장의 금액 / Value of one bill
    반환값 / Returns:
        받을 수 있는 완전한 지폐의 장수 (소수점 이하 버림)
        / Number of whole bills receivable (round down)
    예시 / Example:
        get_number_of_bills(127.5, 5)  →  25
        get_number_of_bills(19.99, 20) →  0   ← 경계값! / Edge case!
    힌트 / Hint:
        // 연산자는 나눗셈 후 소수점 이하를 버립니다.
        The // operator divides and drops the decimal part.
    """

    # TODO 1: amount를 denomination으로 나누되, 소수점 이하를 버리세요.
    #         Divide amount by denomination, dropping any decimal portion.
    # TODO 2: 결과를 int 타입으로 반환하세요.
    #         Return the result as an int.
    return int(amount // denomination)


# ══════════════════════════════════════════════════════════════════
# 함수 5 / Function 5
# 지폐로 받지 못하는 나머지 금액 / Leftover amount the booth keeps
# ══════════════════════════════════════════════════════════════════

def get_leftover_of_bills(amount, denomination):
    """
    매개변수 / Parameters:
        amount       : 환전할 총 금액 / Total amount to exchange
        denomination : 지폐 한 장의 금액 / Value of one bill
    반환값 / Returns:
        지폐로 돌려받지 못하는 나머지 금액 / Leftover amount not returned as bills
    예시 / Example:
        get_leftover_of_bills(127.5, 20)  →  7.5
        get_leftover_of_bills(100, 20)    →  0   ← 경계값! / Edge case!
    힌트 / Hint:
        % 연산자는 나눗셈의 나머지를 반환합니다.
        The % operator returns the remainder of a division.
    """

    # TODO 1: amount를 denomination으로 나눈 나머지를 반환하세요.
    #         Return the remainder when amount is divided by denomination.
    return amount % denomination


# ══════════════════════════════════════════════════════════════════
# 함수 6 / Function 6
# 수수료 포함 최종 환전 금액 / Exchangeable value after spread fee
# ══════════════════════════════════════════════════════════════════

def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    매개변수 / Parameters:
        budget        : 환전할 금액 / Amount of money to exchange
        exchange_rate : 기본 환율 / Base exchange rate
        spread        : 수수료 (정수, 퍼센트 단위) / Fee percentage as a whole integer
                        예: 10은 10%를 의미 / e.g. 10 means 10%
        denomination  : 지폐 한 장의 금액 / Value of one bill
    반환값 / Returns:
        수수료 포함 후 받을 수 있는 최대 금액 (int 타입)
        / Maximum receivable amount after the spread fee (int type)
    예시 / Example:
        exchangeable_value(127.25, 1.20, 10, 20)  →  80
        exchangeable_value(127.25, 1.20, 10, 5)   →  95
    """

    # TODO 1: 실제 환율을 계산하세요 (수수료 포함).
    #         Calculate the actual exchange rate including the spread.
    #         실제 환율 = exchange_rate × (1 + spread / 100)
    #         actual_rate = exchange_rate * (1 + spread / 100)
    actual_rate = exchange_rate * (1 + spread / 100)  # ← 여기를 수정하세요 / Replace this

    # TODO 2: budget을 actual_rate로 나누어 환전 금액을 구하세요.
    #         Divide budget by actual_rate to get the exchanged amount.
    exchanged = budget / actual_rate  # ← 여기를 수정하세요 / Replace this

    # TODO 3: 지폐 단위로 나누어 받을 수 있는 완전한 금액을 구하세요.
    #         Find the largest amount receivable in whole bills.
    #         힌트: (exchanged // denomination) * denomination
    #         Hint:  (exchanged // denomination) * denomination
    result = (exchanged // denomination) * denomination # ← 여기를 수정하세요 / Replace this

    # TODO 4: result를 int 타입으로 반환하세요.
    #         Return result as an int.
    return int(result)


# ══════════════════════════════════════════════════════════════════
# 🎪 테스트 블록 — 수정하지 마세요! / Test block — do not modify!
# ══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 50)
    print("함수 1: exchange_money / Function 1: exchange_money")
    print(exchange_money(127.5, 1.2))          # 예상 / Expected: 106.25
    print(exchange_money(100, 2.0))            # 예상 / Expected: 50.0
    print(exchange_money(0, 1.5))              # 예상 / Expected: 0.0

    print("\n함수 2: get_change / Function 2: get_change")
    print(get_change(127.5, 120))             # 예상 / Expected: 7.5
    print(get_change(500, 500))               # 예상 / Expected: 0

    print("\n함수 3: get_value_of_bills / Function 3: get_value_of_bills")
    print(get_value_of_bills(5, 128))         # 예상 / Expected: 640
    print(get_value_of_bills(20, 0))          # 예상 / Expected: 0

    print("\n함수 4: get_number_of_bills / Function 4: get_number_of_bills")
    print(get_number_of_bills(127.5, 5))      # 예상 / Expected: 25
    print(get_number_of_bills(19.99, 20))     # 예상 / Expected: 0
    print(get_number_of_bills(100, 20))       # 예상 / Expected: 5

    print("\n함수 5: get_leftover_of_bills / Function 5: get_leftover_of_bills")
    print(get_leftover_of_bills(127.5, 20))   # 예상 / Expected: 7.5
    print(get_leftover_of_bills(100, 20))     # 예상 / Expected: 0

    print("\n함수 6: exchangeable_value / Function 6: exchangeable_value")
    print(exchangeable_value(127.25, 1.20, 10, 20))  # 예상 / Expected: 80
    print(exchangeable_value(127.25, 1.20, 10, 5))   # 예상 / Expected: 95
    print(exchangeable_value(100, 1.0, 0, 10))       # 예상 / Expected: 100

    print("\nBonus(Easy): exchange_money()를 사용해서, 200달러를 환율 1.35로 환전하면 얼마인지 출력해보세요.")
    print(exchange_money(200, 1.35))
