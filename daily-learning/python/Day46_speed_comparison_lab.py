"""
=============================================================
속도 비교 실험실 / Speed Comparison Lab
=============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260504
=============================================================

목표 / Goal:
- KO: time 모듈로 두 가지 합계 방식의 속도를 비교한다
- EN: Use the time module to compare the speed of two ways to sum a list
"""

# TODO 1:
# KO: time 모듈을 import 하세요
# EN: Import the time module
# (여기에 import 문 작성 / Write your import statement here)
import time

def sum_with_loop(numbers):
    """
    KO: for 루프를 사용해서 numbers의 합계를 반환
    EN: Return the sum of numbers using a for loop
    """
    # TODO 2:
    # KO: total을 0으로 초기화
    # EN: Initialize total to 0
    total = 0

    # TODO 3:
    # KO: for 루프로 numbers의 각 원소를 total에 더한다
    # EN: Use a for loop to add each element of numbers to total
    for num in numbers:
        total += num

    # TODO 4:
    # KO: total을 반환
    # EN: Return total
    return total


def sum_with_builtin(numbers):
    """
    KO: sum() 내장 함수를 사용해서 numbers의 합계를 반환
    EN: Return the sum of numbers using the built-in sum() function
    """
    # TODO 5:
    # KO: sum() 내장 함수를 호출하고 그 결과를 반환 (한 줄!)
    # EN: Call the built-in sum() and return the result (one line!)
    return sum(numbers)


def measure_function_time(func, numbers):
    """
    KO: 함수와 데이터를 받아서 (결과, 실행 시간)을 튜플로 반환
    EN: Take a function and data, return (result, elapsed_time) as a tuple

    💡 KO: func는 함수 자체입니다. func(numbers)로 호출하면 됩니다.
    💡 EN: func is the function itself. Call it with func(numbers).
    """
    # TODO 6:
    # KO: 시작 시각을 start_time에 저장 (time.time() 사용)
    # EN: Save the start time to start_time (use time.time())
    start_time = time.time()

    # TODO 7:
    # KO: func(numbers)를 호출하고 결과를 result에 저장
    # EN: Call func(numbers) and save the result in `result`
    result = func(numbers)

    # TODO 8:
    # KO: 종료 시각을 end_time에 저장
    # EN: Save the end time to end_time
    end_time = time.time()

    # TODO 9:
    # KO: 경과 시간 elapsed = end_time - start_time
    # EN: Calculate elapsed = end_time - start_time
    elapsed = end_time - start_time

    # TODO 10:
    # KO: (result, elapsed)를 튜플로 반환
    # EN: Return (result, elapsed) as a tuple
    return (result, elapsed)


def run_speed_lab():
    """
    KO: 전체 속도 비교 실험을 실행하고 결과 보고
    EN: Run the full speed comparison experiment and report
    """
    # TODO 11:
    # KO: 실험 시작 메시지와 데이터 준비 메시지 출력
    # EN: Print experiment start and data preparation messages
    print("=== 속도 비교 실험 시작 / Speed Comparison Lab ===")
    print("데이터 준비 중... / Preparing data... (5,000,000 numbers)")

    # TODO 12:
    # KO: 5,000,000개의 숫자 리스트 생성 — list(range(5_000_000))
    # EN: Create a list of 5,000,000 numbers — list(range(5_000_000))
    numbers = list(range(5000000))

    # TODO 13:
    # KO: measure_function_time을 사용해서 sum_with_loop 측정
    #     주의: sum_with_loop 뒤에 ()를 붙이지 마세요! 함수 자체를 전달해야 함
    # EN: Use measure_function_time to measure sum_with_loop
    #     Note: do NOT add () after sum_with_loop! Pass the function itself
    loop_result, loop_time = measure_function_time(sum_with_loop, numbers)

    # TODO 14:
    # KO: sum_with_loop 결과 출력 (시간은 :.4f 형식)
    # EN: Print sum_with_loop results (time with :.4f format)
    print()
    print("[방법 1 / Method 1] for 루프 / for-loop")
    print(f"결과: {loop_result}")
    print(f"실행 시간: {loop_time:.4f}")


    # TODO 15:
    # KO: measure_function_time을 사용해서 sum_with_builtin 측정
    # EN: Use measure_function_time to measure sum_with_builtin
    builtin_result, builtin_time = measure_function_time(sum_with_builtin, numbers)

    # TODO 16:
    # KO: sum_with_builtin 결과 출력
    # EN: Print sum_with_builtin results
    print()
    print("[방법 2 / Method 2] sum() 내장 / sum() built-in")
    print(f"결과: {builtin_result}")
    print(f"실행 시간: {builtin_time:.4f}")


    # TODO 17:
    # KO: 두 결과가 같은지 검증 (== 사용)
    #     같으면 "✅ 두 결과가 같음을 확인! / Both results match!" 출력
    #     다르면 "❌ 결과가 다름! / Results differ!" 출력하고 함수 종료 (return)
    # EN: Verify both results match (use ==)
    #     If equal: print "✅ Both results match!"
    #     If different: print "❌ Results differ!" and return
    print()
    if loop_result == builtin_result:
        print("✅ Both results match!")
    else:
        print("❌ Results differ!")
        return

    # TODO 18:
    # KO: 어느 쪽이 더 빠른지 판단해서 우승자 출력
    #     속도 비율도 계산: ratio = (느린 시간) / (빠른 시간)
    #     예: "🏆 우승: sum() 내장 함수 (4.4배 빠름)"
    # EN: Determine the winner and print it
    #     Calculate ratio: ratio = (slower_time) / (faster_time)
    #     e.g., "🏆 Winner: sum() built-in (4.4x faster)"
    if loop_time > builtin_time:
        print(f"🏆 Winner: sum() built-in ({(loop_time)/(builtin_time):.4f}x faster)")
        return
    else:
        print(f"🏆 Winner: sum_with_loop function ({(builtin_time)/(loop_time):.4f}x faster)")
        return



if __name__ == "__main__":
    # KO: 작은 데이터로 정확성 먼저 확인
    # EN: Check correctness with small data first
    print("=== 정확성 테스트 / Correctness Tests ===")
    print(f"sum_with_loop([1,2,3,4,5]) = {sum_with_loop([1, 2, 3, 4, 5])}")  # 15
    print(f"sum_with_builtin([1,2,3,4,5]) = {sum_with_builtin([1, 2, 3, 4, 5])}")  # 15
    print(f"sum_with_loop([]) = {sum_with_loop([])}")  # 0
    print(f"sum_with_loop([-5, 5]) = {sum_with_loop([-5, 5])}")  # 0
    print(f"sum_with_loop([-1, -2, -3]) = {sum_with_loop([-1, -2, -3])}")  # -6

    print()
    print("=== 시간 측정 도구 테스트 / Timer Tool Test ===")
    result, elapsed = measure_function_time(sum_with_builtin, [1, 2, 3])
    print(f"결과 / Result: {result}, 시간 / Time: {elapsed:.6f}s")

    print()
    print("=== 전체 실험 실행 / Run Full Experiment ===")
    run_speed_lab()
