"""
===============================================================
Python Practice: 성적 기록 처리하기 (파일 입출력)
Python Practice: Process Grade Records (File I/O)
===============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260513
===============================================================

시나리오 / Scenario:
    여러분은 데이터 분석 인턴입니다. 학생 성적 파일을 읽고
    요약 보고서를 만들어 파일로 저장해야 합니다.
    You are a data analytics intern. Read student grades from a file
    and save a summary report to another file.
"""


# ============================================================
# 함수 1 / Function 1: read_grades
# ============================================================
def read_grades(file_path: str) -> list:
    """
    파일에서 성적을 읽어 (이름, 점수) 튜플의 리스트로 반환합니다.
    Read grades from a file and return a list of (name, score) tuples.

    예시 / Example:
        파일 내용 / File contents:
            Alice,85
            Bob,72

        반환값 / Returns:
            [("Alice", 85), ("Bob", 72)]
    """
    # TODO 1: 결과를 담을 빈 리스트를 만드세요.
    # TODO 1: Create an empty list to store the results.
    grades = []

    # TODO 2: with 문을 사용해 파일을 "r" 모드, encoding="utf-8"로 여세요.
    # TODO 2: Open the file in "r" mode with encoding="utf-8" using the with statement.
    # 힌트 / Hint:  with open(...) as f:
    with open(file_path, "r", encoding="utf-8") as f:

    # TODO 3: 파일에서 한 줄씩 반복해서 읽으세요.
    # TODO 3: Iterate through the file line by line.
        for line in f:

    # TODO 4: 각 줄에서 strip()으로 줄바꿈 문자(\n)를 제거하세요.
    # TODO 4: Use strip() to remove the newline character (\n) from each line.
            txt_line = line.strip()

    # TODO 5: split(",")로 이름과 점수를 분리하세요.
    # TODO 5: Use split(",") to separate the name and score.
            name, score = txt_line.split(",")

    # TODO 6: 점수를 int()로 정수로 변환한 뒤, (이름, 점수) 튜플로 grades에 추가하세요.
    # TODO 6: Convert the score to an integer with int(), then append (name, score) as a tuple.
            grades.append((name, int(score)))

    return grades


# ============================================================
# 함수 2 / Function 2: write_summary
# ============================================================
def write_summary(file_path: str, grades: list) -> None:
    """
    성적 리스트를 받아 요약 보고서를 파일로 저장합니다.
    Take a list of grades and save a summary report to a file.

    출력 형식 / Output format:
        === Grade Summary ===
        Total students: 5
        Average score: 82.00
        Highest: Eve (95)
        Lowest: Diana (68)
    """
    # TODO 7: 합계와 학생 수를 계산하세요. (sum() 함수 없이!)
    # TODO 7: Calculate total and student count. (Without sum()!)
    total = 0
    count = len(grades)

    # TODO 8: 최고점/최저점 학생을 추적할 변수를 초기화하세요.
    # TODO 8: Initialize variables to track the highest/lowest scorers.
    # 힌트 / Hint: 첫 번째 학생을 기준으로 시작하면 편합니다.
    # Hint: It's easier to start with the first student as the baseline.
    highest_name = ""
    highest_score = -1
    lowest_name = ""
    lowest_score = 101

    # TODO 9: grades 리스트를 반복하며 합계, 최고점, 최저점을 갱신하세요.
    # TODO 9: Loop through grades and update total, highest, and lowest.
    for student in grades:
        name, score = student
        total += score
        if score >= highest_score:
            highest_score = score
            highest_name += name
        if score <= lowest_score:
            lowest_score = score
            lowest_name += name


    # TODO 10: 평균을 계산하세요. (소수점이 나올 수 있도록 / division)
    # TODO 10: Calculate the average. (Use division to allow decimals.)
    average = total / count

    # TODO 11: with 문으로 파일을 "w" 모드, encoding="utf-8"로 여세요.
    # TODO 11: Open the file in "w" mode with encoding="utf-8" using the with statement.
    with open(file_path, "w", encoding="utf-8") as f:

    # TODO 12: 다음 5줄을 파일에 쓰세요. 각 줄 끝에 \n을 잊지 마세요!
    # TODO 12: Write the following 5 lines to the file. Don't forget \n at the end of each!
    #   === Grade Summary ===
    #   Total students: <count>
    #   Average score: <average to 2 decimal places>
    #   Highest: <highest_name> (<highest_score>)
    #   Lowest: <lowest_name> (<lowest_score>)
    #
    # 힌트 / Hint: f"{average:.2f}" 형식을 사용하세요.
    # Hint: Use f"{average:.2f}" formatting.
        f.write("=== Grade Summary ===\n")
        f.write(f"Total students: {count}\n")
        f.write(f"Average score: {average:.2f}\n")
        f.write(f"Highest: {highest_name} ({highest_score})\n")
        f.write(f"Lowest: {lowest_name} ({lowest_score})")


# ============================================================
# 🎪 테스트 코드 (수정하지 마세요!) / Test Code (Do not modify!)
# ============================================================
if __name__ == "__main__":
    # 테스트용 입력 파일 만들기 / Create test input file
    with open("./daily-learning/python/data/grades.txt", "w", encoding="utf-8") as f:
        f.write("Alice,85\n")
        f.write("Bob,72\n")
        f.write("Charlie,90\n")
        f.write("Diana,68\n")
        f.write("Eve,95\n")

    print("=" * 50)
    print("테스트 1 / Test 1: read_grades")
    print("=" * 50)
    grades = read_grades("./daily-learning/python/data/grades.txt")
    print(f"결과 / Result: {grades}")
    expected = [("Alice", 85), ("Bob", 72), ("Charlie", 90),
                ("Diana", 68), ("Eve", 95)]
    print(f"예상 / Expected: {expected}")
    print(f"통과 / Pass: {grades == expected}")

    print()
    print("=" * 50)
    print("테스트 2 / Test 2: write_summary")
    print("=" * 50)
    write_summary("./daily-learning/python/data/summary.txt", grades)
    try:
        with open("./daily-learning/python/data/summary.txt", "r", encoding="utf-8") as f:
            output = f.read()
        print("--- summary.txt 내용 / contents ---")
        print(output)
    except FileNotFoundError:
        print("⚠️  summary.txt 파일이 아직 만들어지지 않았어요. write_summary를 완성하세요!")
        print("⚠️  summary.txt was not created yet. Complete write_summary!")
        output = ""
    print("--- 예상 / Expected ---")
    print("=== Grade Summary ===")
    print("Total students: 5")
    print("Average score: 82.00")
    print("Highest: Eve (95)")
    print("Lowest: Diana (68)")


# ============================================================
# 🌟 보너스 챌린지 / Bonus Challenges
# ============================================================

# 🥉 Easy: 일기장 (Append 모드) / Diary Log (Append mode)
def add_diary_entry(file_path: str, entry: str) -> None:
    """
    일기장 파일 끝에 새 항목을 추가합니다.
    Append a new entry to the end of the diary file.
    힌트 / Hint: "a" 모드를 사용하세요. / Use "a" mode.
    """
    pass


# 🥈 Medium: CSV 형식 (헤더 처리) / CSV Format (with header)
def process_grades_csv(input_path: str, output_path: str) -> None:
    """
    헤더가 있는 CSV 파일을 읽어, PASS/FAIL 상태를 추가한 새 CSV로 저장합니다.
    Read a CSV file with a header, and save a new CSV with PASS/FAIL status added.

    입력 / Input:                출력 / Output:
        name,score                  name,score,status
        Alice,85                    Alice,85,PASS
        Diana,68                    Diana,68,FAIL

    힌트 / Hint: 첫 줄은 readline()으로 건너뛰세요. 70점 이상이면 PASS.
    Hint: Skip the first line with readline(). PASS if score >= 70.
    """
    pass


# 🥇 Hard: 예외 처리 미리보기 / Exception handling preview
def safe_read_grades(file_path: str) -> list:
    """
    파일이 없어도 프로그램이 멈추지 않도록 안전하게 읽습니다.
    Safely read so the program doesn't crash if the file doesn't exist.

    힌트 / Hint:
        try:
            return read_grades(file_path)
        except FileNotFoundError:
            print(...)
            return []
    """
    pass
