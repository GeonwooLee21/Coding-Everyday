"""
===============================================================
🎬 The csv Library
표준 csv 라이브러리
===============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260519
===============================================================

Fill in the TODOs below. The test block at the bottom will run automatically.
아래 TODO를 채워주세요. 맨 아래의 테스트 블록은 자동으로 실행됩니다.

⚠️ Allowed / 사용 가능:
   import csv ✨ (NEW! / 새로움!)
   csv.reader, csv.writer, next()
   open(..., newline=""), encoding="utf-8"
   for, if, list methods, try/except

⚠️ NOT allowed / 사용 금지:
   import pandas
   dict / dictionaries  (parallel lists again / 평행 리스트로)
   sorted()
"""
import csv

def load_ratings_manual(file_path):
    """
    Last week's manual loader — provided for compare_with_manual.
    지난 시간의 수동 로더 — compare_with_manual에서 사용하라고 제공됩니다.

    DO NOT modify this function. / 수정하지 마세요.
    """
    ratings = []
    with open(file_path, "r", encoding="utf-8") as f:
        header_skipped = False
        for line in f:
            if not header_skipped:
                header_skipped = True
                continue
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            ratings.append([parts[0], parts[1], int(parts[2]), float(parts[3])])
    return ratings


def load_ratings_with_csv(file_path):
    """
    Load ratings using csv.reader.
    csv.reader를 사용해서 영화 평점을 로딩합니다.

    Steps / 단계:
        1. Open with encoding="utf-8" and newline=""
           encoding="utf-8"과 newline=""로 열기
        2. Create a csv.reader / csv.reader 생성
        3. Skip the header with next(reader) / next(reader)로 헤더 건너뛰기
        4. For each row (list of strings): / 각 row (문자열 리스트)에 대해:
              - Convert year to int / year를 int로 변환
              - Convert rating to float / rating을 float로 변환
              - Append [title, genre, year, rating] / [title, genre, year, rating] 추가

    ⚠️ Reminder: csv.reader returns STRINGS — you MUST convert types yourself!
                csv.reader는 문자열을 반환합니다 — 타입 변환은 직접!
    """
    ratings = []
    # TODO: Open the file with encoding="utf-8", newline=""
    # TODO: encoding="utf-8", newline=""로 파일 열기
    with open(file_path, "r", encoding="utf-8", newline="") as f:

    # TODO: Create csv.reader and skip the header with next()
    # TODO: csv.reader 생성 후 next()로 헤더 건너뛰기
        reader = csv.reader(f)
        next(reader)

    # TODO: Loop through rows, convert types, append
    # TODO: 행 반복, 타입 변환, 추가
        for row in reader:
            # parts = line.split(",")
            ratings.append([row[0], row[1], int(row[2]), float(row[3])])

    return ratings


def save_ratings_with_csv(ratings, file_path):
    """
    Save the movie list to CSV using csv.writer.
    csv.writer를 사용해서 영화 리스트를 CSV로 저장합니다.

    Steps / 단계:
        1. Open the file in "w" mode with encoding="utf-8", newline=""
           "w" 모드, encoding="utf-8", newline=""로 열기
        2. Create a csv.writer / csv.writer 생성
        3. Write the header with writer.writerow([...])
           writer.writerow([...])로 헤더 작성
        4. Use writer.writerows(ratings) to write all rows at once! (efficient)
           writer.writerows(ratings)로 모든 행을 한 번에! (효율적)

    ⚠️ NEVER forget newline="" — or you'll get blank lines between rows!
                newline=""을 절대 잊지 마세요 — 빈 줄이 생깁니다!
    """
    # TODO: Open the file in "w" mode with newline=""
    # TODO: "w" 모드, newline=""로 파일 열기
    with open(file_path, "w", encoding="utf-8", newline="") as f:

    # TODO: Create csv.writer / csv.writer 생성
        writer = csv.writer(f)

    # TODO: Write the header row / 헤더 행 작성
        writer.writerow(["title", "genre", "year", "rating"])

    # TODO: Write all data rows with writerows() / writerows()로 모든 데이터 작성
        writer.writerows(ratings)


def save_filtered_by_genre(ratings, genre, file_path):
    """
    Filter by genre, save, and return the saved count.
    장르 필터링 후 저장하고, 저장된 개수를 반환합니다.

    Hint / 힌트: Reuse save_ratings_with_csv! / save_ratings_with_csv를 재사용하세요!
    """
    # TODO: Build a filtered list / 필터링된 리스트 만들기
    filtered_list = []
    for movie in ratings:
        if movie[1] == genre:
            filtered_list.append(movie)

    # TODO: Call save_ratings_with_csv() / save_ratings_with_csv() 호출
    save_ratings_with_csv(filtered_list, file_path)

    # TODO: Return the count / 개수 반환
    return len(filtered_list)


def save_summary_report(ratings, file_path):
    """
    Save a per-genre summary using csv.writer.
    csv.writer로 장르별 요약을 저장합니다.

    Format / 형식:
        genre,count,average_rating
        Drama,3,8.87
        Action,3,8.83
        ...

    ⚠️ NO dict — use parallel lists / dict 금지 — 평행 리스트 사용:
        genres = []
        counts = []
        totals = []

    Steps / 단계:
        1. Loop through ratings, update the three lists
           ratings 반복, 세 리스트 갱신
        2. Open file with csv.writer, newline=""
           csv.writer, newline=""로 파일 열기
        3. Write header: ["genre", "count", "average_rating"]
           헤더 작성: ["genre", "count", "average_rating"]
        4. For each genre, write [genre, count, round(avg, 2)]
           각 장르마다 [genre, count, round(avg, 2)] 작성
        5. Return number of unique genres / 고유 장르 수 반환
    """
    # TODO: Initialize parallel lists / 평행 리스트 초기화
    genres = []
    counts = []
    totals = []

    for movie in ratings:
        found_genre = False
        for idx, genre in enumerate(genres):
            if genre == movie[1]:
                counts[idx] += 1
                totals[idx] += movie[3]
                found_genre = True
                break
        if not found_genre:
            genres.append(movie[1])
            counts.append(1)
            totals.append(movie[3])
    

    # TODO: Write report file with csv.writer / csv.writer로 보고서 작성
    with open(file_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["genre", "count", "average_rating"])
        for genre, count, total in zip(genres, counts, totals):
            writer.writerow([genre, count, round(total/count, 2)])


    # TODO: Return number of genres / 장르 수 반환
    return len(genres)


def count_rows_in_file(file_path):
    """
    Return the number of DATA rows in the CSV (excludes header).
    CSV 파일의 데이터 행 개수를 반환합니다 (헤더 제외).

    Hint / 힌트:
        - Use next(reader, None) to safely skip header even on empty files
          빈 파일이어도 안전하게 헤더를 건너뛰려면 next(reader, None)
        - Count by iterating / 반복하면서 카운트
    """
    # TODO: Open and create csv.reader / 파일 열고 csv.reader 생성
    with open(file_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)

    # TODO: Skip header safely with next(reader, None) / next(reader, None)로 안전하게 헤더 건너뛰기
        next(reader, None)

    # TODO: Count rows / 행 수 카운트
        count = 0
        for row in reader:
            count += 1

    return count


def compare_with_manual(file_path):
    """
    Compare csv.reader vs manual .split(",") parsing on the same file.
    동일한 파일에 대해 csv.reader와 수동 .split(",")의 결과를 비교합니다.

    Returns True if results match, False otherwise.
    결과가 일치하면 True, 아니면 False.

    ⚠️ Either approach may crash on tricky files — handle with try/except!
        어느 쪽이든 까다로운 파일에서 크래시할 수 있음 — try/except로 처리!
    """
    # TODO: Try loading with manual loader, on exception use None
    # TODO: 수동 로더로 시도, 예외 발생 시 None 사용
    manual = None
    try:
        manual = load_ratings_manual(file_path)
    except:
        pass

    # TODO: Try loading with csv loader, on exception use None
    # TODO: csv 로더로 시도, 예외 발생 시 None 사용
    with_csv = None
    try:
        with_csv = load_ratings_with_csv(file_path)
    except:
        pass

    # TODO: Return whether they're equal / 일치 여부 반환
    return manual == with_csv


# ============================================================
# 🔒 PROTECTED TEST BLOCK — DO NOT MODIFY / 수정 금지
# ============================================================
if __name__ == "__main__":
    import os
    import shutil

    if os.path.exists("output"):
        shutil.rmtree("output")
    os.makedirs("output")

    print("=" * 60)
    print("Testing csv library pipeline / csv 라이브러리 파이프라인 테스트")
    print("=" * 60)

    # [1] Loading
    print("\n[1] load_ratings_with_csv")
    try:
        ratings = load_ratings_with_csv("./daily-learning/python/data/input/movie_ratings.csv")
        print(f"    Loaded {len(ratings)} rows (expected 12)")
        if ratings:
            print(f"    First: {ratings[0]}")
            print(f"    year type: {type(ratings[0][2]).__name__} (expected int)")
            print(f"    rating type: {type(ratings[0][3]).__name__} (expected float)")
    except Exception as e:
        print(f"    ⏳ Not implemented yet — {type(e).__name__}: {e}")
        ratings = []

    # [2] Save round trip
    print("\n[2] save_ratings_with_csv — round trip / 왕복")
    try:
        save_ratings_with_csv(ratings, "./daily-learning/python/data/output/round_trip.csv")
        if os.path.exists("./daily-learning/python/data/output/round_trip.csv"):
            reloaded = load_ratings_with_csv("./daily-learning/python/data/output/round_trip.csv")
            print(f"    Round trip match: {reloaded == ratings}")
            # Check the newline gotcha
            with open("./daily-learning/python/data/output/round_trip.csv", "rb") as f:
                content = f.read()
            has_blanks = b"\n\n" in content
            print(f"    No blank lines: {not has_blanks}")
            if has_blanks:
                print(f"    🐛 You probably forgot newline=\"\" / newline=\"\"를 잊으셨네요!")
        else:
            print(f"    ⏳ output/round_trip.csv not created yet")
    except Exception as e:
        print(f"    ⏳ Not implemented — {type(e).__name__}: {e}")

    # [3] Filter
    print("\n[3] save_filtered_by_genre('Drama')")
    try:
        n = save_filtered_by_genre(ratings, "Drama", "./daily-learning/python/data/output/drama.csv")
        print(f"    Saved {n} (expected 3)")
        if os.path.exists("./daily-learning/python/data/output/drama.csv"):
            drama = load_ratings_with_csv("./daily-learning/python/data/output/drama.csv")
            print(f"    Titles: {[r[0] for r in drama]}")
    except Exception as e:
        print(f"    ⏳ Not implemented — {type(e).__name__}: {e}")

    # [4] Summary
    print("\n[4] save_summary_report")
    try:
        n = save_summary_report(ratings, "./daily-learning/python/data/output/summary.csv")
        print(f"    {n} genres (expected 6)")
        if os.path.exists("./daily-learning/python/data/output/summary.csv"):
            with open("./daily-learning/python/data/output/summary.csv", encoding="utf-8") as f:
                for line in f:
                    print(f"      {line.rstrip()}")
    except Exception as e:
        print(f"    ⏳ Not implemented — {type(e).__name__}: {e}")

    # [5] Count rows
    print("\n[5] count_rows_in_file")
    try:
        if os.path.exists("./daily-learning/python/data/output/round_trip.csv"):
            n = count_rows_in_file("./daily-learning/python/data/output/round_trip.csv")
            print(f"    round_trip.csv: {n} rows (expected 12)")
        if os.path.exists("./daily-learning/python/data/output/drama.csv"):
            n = count_rows_in_file("./daily-learning/python/data/output/drama.csv")
            print(f"    drama.csv: {n} rows (expected 3)")
    except Exception as e:
        print(f"    ⏳ Not implemented — {type(e).__name__}: {e}")

    # [6] Compare with manual — clean data
    print("\n[6] compare_with_manual on clean data / 깨끗한 데이터")
    try:
        result = compare_with_manual("./daily-learning/python/data/input/movie_ratings.csv")
        print(f"    Agree on clean data: {result} (expected True)")
    except Exception as e:
        print(f"    ⏳ Not implemented — {type(e).__name__}: {e}")

    # [7] THE BIG DEMO: quoted commas
    print("\n[7] 🎓 Quoted-comma demo / 따옴표 콤마 시연")
    try:
        tricky = [
            ["Crazy, Stupid, Love", "Comedy", 2011, 7.4],
            ["Eat, Pray, Love", "Drama", 2010, 5.7],
        ]
        save_ratings_with_csv(tricky, "./daily-learning/python/data/output/tricky.csv")
        if os.path.exists("./daily-learning/python/data/output/tricky.csv"):
            print(f"    Raw file contents / 파일 원본:")
            with open("./daily-learning/python/data/output/tricky.csv", encoding="utf-8") as f:
                for line in f:
                    print(f"      {line.rstrip()}")

            reloaded = load_ratings_with_csv("./daily-learning/python/data/output/tricky.csv")
            match = reloaded == tricky
            print(f"    csv.reader round trip OK: {match}")

            agree = compare_with_manual("./daily-learning/python/data/output/tricky.csv")
            print(f"    Manual .split(',') agrees: {agree}")
            if not agree:
                print(f"    ✨ csv library wins! Library beats manual on tricky data.")
                print(f"       라이브러리 승! 까다로운 데이터에서 라이브러리가 수동 코드를 이깁니다.")
    except Exception as e:
        print(f"    ⏳ Not implemented — {type(e).__name__}: {e}")

    # [8] Edge case: empty
    print("\n[8] Edge case — empty list / 경계: 빈 리스트")
    try:
        save_ratings_with_csv([], "./daily-learning/python/data/input/empty.csv")
        if os.path.exists("./daily-learning/python/data/input/empty.csv"):
            empty = load_ratings_with_csv("./daily-learning/python/data/input/empty.csv")
            n = count_rows_in_file("./daily-learning/python/data/input/empty.csv")
            print(f"    Empty round trip: {len(empty)} rows (expected 0)")
            print(f"    count_rows_in_file: {n} (expected 0)")
    except Exception as e:
        print(f"    ⏳ Empty list — {type(e).__name__}: {e}")

    print("\n" + "=" * 60)
    print("Keep going! / 계속 진행하세요!")
