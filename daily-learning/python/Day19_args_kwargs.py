# -*- coding: utf-8 -*-
"""
# =============================================================
🎮 *args와 **kwargs 연습
# =============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260416
# =============================================================
"""

# ============================================================
# 🎯 과제 1: 쇼핑 카트 / Assignment 1: Shopping Cart
# ============================================================

def add_to_cart(*items, **item_details):
    """
    온라인 쇼핑몰의 장바구니에 상품을 추가합니다.
    Add products to an online shopping cart.
    
    매개변수 / Parameters:
        *items: 상품명들 (위치 인자) / Product names (positional arguments)
        **item_details: 상품별 세부 정보 (키워드 인자) / Product details (keyword arguments)
    
    반환 / Returns:
        dict: 상품 개수와 정보가 담긴 딕셔너리 / Dictionary with item count and information
    """
    # TODO: 빈 리스트를 만들어서 상품명들을 저장하세요
    # TODO: Create an empty list to store product names
    products = []

    # TODO: items에 있는 모든 상품명을 리스트에 추가하세요 (for 반복문 사용)
    # TODO: Add all product names from items to the list (use for loop)
    for item in items:
        products.append(item)

    # TODO: 총 상품 개수를 출력하세요
    # TODO: Print the total number of items
    print(f"총 상품 개수: {len(items)}")

    # TODO: 각 상품명을 "- 상품명" 형식으로 출력하세요
    # TODO: Print each product name in "- product_name" format
    for name in products:
        print(f"- {name}")

    # TODO: item_details가 비어있지 않으면 "상세 정보:" 출력하세요
    # TODO: If item_details is not empty, print "Details:"
    if item_details:
        print("상세정보:")

    # TODO: item_details의 각 키-값 쌍을 출력하세요 (.items() 사용)
    # TODO: Print each key-value pair from item_details (use .items())
    # for detail in item_details:
    #     print(detail.items())
    for key, value in item_details.items():
        print(f"  {key}: {value}")
    
    # TODO: 결과를 딕셔너리로 반환하세요 (total_items, item_list, details 포함)
    # TODO: Return results as a dictionary (include total_items, item_list, details)
    return {
        "total_items": len(items),    # 총 상품 개수 (정수)
        "item_list": products,        # 상품명 리스트
        "details": item_details       # 세부 정보 딕셔너리
    }


# ============================================================
# 🎯 과제 2: 레스토랑 주문 시스템 / Assignment 2: Restaurant Order System
# ============================================================

def process_order(customer_name, *dishes, **preferences):
    """
    레스토랑 주문을 처리합니다.
    Process a restaurant order.
    
    매개변수 / Parameters:
        customer_name (str): 고객 이름 (필수) / Customer name (required)
        *dishes: 주문한 음식들 / Ordered dishes
        **preferences: 선호 사항 / Preferences
    
    반환 / Returns:
        dict: 주문 확인 정보와 예상 조리 시간 / Order confirmation and estimated cooking time
    """
    # TODO: 고객 이름과 주문 접수 메시지를 출력하세요
    # TODO: Print customer name and order received message
    print(f"고객명: {customer_name}")
    print(f"주문이 접수 되었습니다.")

    # TODO: dishes가 비어있지 않으면 주문한 음식 목록을 출력하세요
    # TODO: If dishes is not empty, print the list of ordered dishes
    if dishes:
        print(f"주문한 음식 목록:")
        for dish in dishes:
            print(f"- {dish}")

    # TODO: preferences가 있으면 "특별 요청사항:" 제목 출력
    # TODO: If preferences exist, print "Special Requests:" heading
    if preferences:
        print(f"특별 요청사항:")

    # TODO: 각 preference를 "키: 값" 형식으로 출력하세요
    # TODO: Print each preference in "key: value" format
        for key, value in preferences.items():
            print(f"{key}: {value}")

    # TODO: 예상 조리 시간을 계산하세요 (음식 1개당 10분)
    # TODO: Calculate estimated cooking time (10 minutes per dish)
    estimated_cooking_time = len(dishes) * 10

    # TODO: 예상 조리 시간을 출력하세요
    # TODO: Print estimated cooking time
    print(f"예상 조리 시간: {estimated_cooking_time}분")

    # TODO: 주문 정보를 딕셔너리로 반환하세요
    # TODO: Return order information as a dictionary
    return {
        "customer": customer_name,
        "dish_list": list(dishes),
        "preferences": preferences,
        "cooking_time": estimated_cooking_time
    }


# ============================================================
# 🎯 과제 3: 학생 성적 관리 / Assignment 3: Student Grade Management
# ============================================================

def record_grades(student_name, *test_scores, **subject_info):
    """
    학생의 성적을 기록하고 분석합니다.
    Record and analyze student grades.
    
    매개변수 / Parameters:
        student_name (str): 학생 이름 (필수) / Student name (required)
        *test_scores: 시험 점수들 / Test scores
        **subject_info: 과목 정보 / Subject information
    
    반환 / Returns:
        dict: 평균 점수와 성적 정보 / Average score and grade information
    """
    # TODO: 학생 이름을 출력하세요
    # TODO: Print student name
    print(f"학생명: {student_name}")

    # TODO: test_scores가 있으면 모든 점수를 출력하세요
    # TODO: If test_scores exist, print all scores
    i = 1
    if test_scores:
        for score in test_scores:
            print(f"시험{i}- {score}점")
            i += 1
    
    # TODO: test_scores의 평균을 계산하세요 (sum과 len 함수 사용)
    # TODO: Calculate average of test_scores (use sum and len functions)
        scores_avg = sum(test_scores) / len(test_scores)
    else:
        scores_avg = 0

    # TODO: 평균을 출력하세요 (소수점 2자리까지)
    # TODO: Print average (round to 2 decimal places)
    print(f"시험 평균: {scores_avg:.2f}")
    
    # TODO: 평균에 따라 등급을 결정하세요
    # TODO: Determine grade based on average
    # 90 이상 / >= 90: "우수" / "Excellent"
    # 80 이상 / >= 80: "양호" / "Good"  
    # 그 외 / Otherwise: "보통" / "Average"
    if   scores_avg >= 90:
        test_grade = "우수"
    elif scores_avg >= 80:
        test_grade = "양호"
    else:
        test_grade = "보통"
    print(f"성적 등급: {test_grade}")

    # TODO: subject_info가 있으면 과목 정보를 출력하세요
    # TODO: If subject_info exists, print subject information
    if subject_info:
        for key, value in subject_info.items():
            print(f"{key}: {value}")

    # TODO: 결과를 딕셔너리로 반환하세요 (student, average, grade, info 포함)
    # TODO: Return results as dictionary (include student, average, grade, info)
    return {
        "student": student_name,
        "average": scores_avg,
        "grade": test_grade,
        "info": subject_info
    }


# ============================================================
# 🔥 보너스 챌린지 / Bonus Challenges
# ============================================================

# 🌟 보너스 1 / Bonus 1: Function Call Logger
def log_function_call(func_name, *args, **kwargs):
    """
    함수 호출 시 모든 인자를 로깅합니다.
    Log all arguments when a function is called.
    """
    # TODO: 함수 이름 출력
    # TODO: Print function name
    
    # TODO: args가 있으면 "위치 인자:" 출력 후 각 인자 출력
    # TODO: If args exist, print "Positional arguments:" then each argument
    
    # TODO: kwargs가 있으면 "키워드 인자:" 출력 후 각 키-값 쌍 출력
    # TODO: If kwargs exist, print "Keyword arguments:" then each key-value pair
    
    pass


# 🌟 보너스 2 / Bonus 2: Multi-language Greetings
def greet_in_languages(*names, **language_greetings):
    """
    여러 언어로 인사말을 출력합니다.
    Output greetings in multiple languages.
    """
    # TODO: 각 이름에 대해 반복
    # TODO: Loop through each name
    
    # TODO: 각 언어의 인사말로 인사 (이름과 함께)
    # TODO: Greet with each language's greeting (with name)
    
    pass


# 🌟 보너스 3 / Bonus 3: API Request Simulator
def api_request(endpoint, method="GET", *params, **headers):
    """
    API 요청을 시뮬레이션합니다.
    Simulate an API request.
    """
    # TODO: 엔드포인트와 메서드 출력
    # TODO: Print endpoint and method
    
    # TODO: params가 있으면 URL 파라미터로 출력
    # TODO: If params exist, print as URL parameters
    
    # TODO: headers가 있으면 HTTP 헤더로 출력
    # TODO: If headers exist, print as HTTP headers
    
    # TODO: 요청 정보를 딕셔너리로 반환
    # TODO: Return request information as dictionary
    
    pass


# ============================================================
# 🎪 테스트 코드 / Test Code
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("🎯 과제 1 테스트 / Assignment 1 Test")
    print("=" * 60)
    
    result1 = add_to_cart(
        "노트북", "마우스", "키보드",
        laptop_price=1200000,
        mouse_quantity=2,
        keyboard_color="black"
    )
    print(f"\n반환값 / Return value: {result1}")
    
    print("\n" + "=" * 60)
    print("🎯 과제 2 테스트 / Assignment 2 Test")
    print("=" * 60)
    
    order1 = process_order(
        "홍길동",
        "떡볶이", "순대", "튀김",
        spicy_level=3,
        no_onions=True,
        extra_cheese=True
    )
    print(f"\n반환값 / Return value: {order1}")
    
    print("\n" + "=" * 60)
    print("🎯 과제 3 테스트 / Assignment 3 Test")
    print("=" * 60)
    
    grades1 = record_grades(
        "박민수",
        95, 88, 92, 90,
        subject="Python 프로그래밍",
        semester="2024-2",
        professor="김교수"
    )
    print(f"\n반환값 / Return value: {grades1}")
    
    print("\n" + "=" * 60)
    print("🔥 보너스 테스트 / Bonus Tests")
    print("=" * 60)
    
    print("\n보너스 1 / Bonus 1:")
    log_function_call("test_function", 1, 2, 3, debug=True, verbose=False)
    
    print("\n보너스 2 / Bonus 2:")
    greet_in_languages(
        "철수", "영희",
        korean="안녕하세요",
        english="Hello",
        spanish="Hola"
    )
    
    print("\n보너스 3 / Bonus 3:")
    api_result = api_request(
        "/api/users",
        "POST",
        "user_id=123", "action=update",
        Authorization="Bearer token123",
        Content_Type="application/json"
    )
    print(f"\n반환값 / Return value: {api_result}")
