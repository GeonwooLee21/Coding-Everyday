"""
🎬 Movie Data Pipeline — Practice Skeleton
영화 데이터 파이프라인 — 연습 스켈레톤

Fill in the TODOs below. The test block at the bottom will run automatically.
아래 TODO를 채워주세요. 맨 아래의 테스트 블록은 자동으로 실행됩니다.

⚠️ Allowed / 사용 가능:
   open("w"), f.write(), f-strings, try/except
   for, if, list methods, slicing

⚠️ NOT allowed / 사용 금지:
   import csv, import pandas
   sorted() in save_top_n
   dict / dictionaries
"""


def load_ratings(file_path):
    """
    Reuse from the previous session — load and parse the CSV.
    지난 시간의 함수를 재사용합니다 — CSV를 로딩하고 파싱합니다.
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


def save_ratings(ratings, file_path):
    """
    Save a list of movies to a CSV file (with header).
    영화 리스트를 CSV 파일로 저장합니다 (헤더 포함).

    Steps / 단계:
        1. Open the file in write mode / 쓰기 모드로 파일 열기
        2. Write the header line: "title,genre,year,rating\\n"
           헤더 줄 작성: "title,genre,year,rating\\n"
        3. For each movie, write one line / 각 영화마다 한 줄씩 작성
        4. Don't forget the trailing "\\n"! / 줄 끝에 "\\n"을 잊지 마세요!
    """
    # TODO: Open the file in "w" mode with utf-8 encoding
    # TODO: "w" 모드, utf-8 인코딩으로 파일 열기

    # TODO: Write the header / 헤더 작성

    # TODO: Loop and write each row / 각 행을 반복하면서 작성
    pass


def save_filtered_by_genre(ratings, genre, file_path):
    """
    Filter by genre, save the result, and return the count saved.
    장르로 필터링한 후 저장하고, 저장된 개수를 반환합니다.

    Hint / 힌트: Build a filtered list first, then call save_ratings().
                먼저 필터링된 리스트를 만든 후 save_ratings()를 호출하세요.
    """
    # TODO: Build a filtered list / 필터링된 리스트 만들기

    # TODO: Save it using save_ratings() / save_ratings()로 저장

    # TODO: Return the count / 개수 반환
    pass


def save_top_n(ratings, n, file_path):
    """
    Save the top N movies by rating (descending).
    평점이 높은 순서대로 상위 N개 영화를 저장합니다.

    ⚠️ NO sorted() allowed! / sorted() 사용 금지!
    Use selection-sort style: repeatedly find the max and append.
    선택 정렬 방식: 최대값을 찾아 추가하기를 반복하세요.

    Steps / 단계:
        1. Make a COPY of the input list (don't modify original!)
           입력 리스트의 복사본을 만드세요 (원본 수정 금지!)
        2. While the copy isn't empty / 복사본이 비지 않은 동안:
              - Find the index of the highest-rated movie / 최고 평점 영화의 인덱스 찾기
              - Append it to the result list / 결과 리스트에 추가
              - Remove it from the copy with .pop(index) / .pop(index)로 제거
        3. Slice the result to first n items / 결과를 앞에서 n개만 슬라이싱
        4. Save using save_ratings() / save_ratings()로 저장
        5. Return how many were saved (could be less than n if list is small)
           실제 저장된 개수 반환 (리스트가 작으면 n보다 적을 수 있음)
    """
    # TODO: Make a copy of ratings / ratings의 복사본 만들기

    # TODO: Build a sorted list (descending by rating)
    # TODO: 정렬된 리스트 만들기 (평점 내림차순)

    # TODO: Take the top n / 상위 n개 선택

    # TODO: Save and return count / 저장하고 개수 반환
    pass


def save_summary_report(ratings, file_path):
    """
    Save a per-genre summary report.
    장르별 요약 보고서를 저장합니다.

    Output format / 출력 형식:
        genre,count,average_rating
        Drama,3,8.87
        Action,3,8.83
        ...

    ⚠️ NO dictionaries allowed! Use parallel lists instead.
    딕셔너리 사용 금지! 평행 리스트를 사용하세요.

    Approach with parallel lists / 평행 리스트 접근법:
        genres = []   # ["Drama", "Action", ...]
        counts = []   # [3, 3, ...]      <- same index as genres
        totals = []   # [26.6, 26.5, ...] <- sum of ratings per genre

    Steps / 단계:
        1. Loop through each movie / 각 영화를 반복:
              - Check if its genre is already in `genres`
                해당 장르가 이미 genres에 있는지 확인
              - If yes: increment count, add to total
                있으면: count 증가, total에 더하기
              - If no: append new genre, count=1, total=rating
                없으면: 새 장르 추가, count=1, total=rating
        2. Write the report file / 보고서 파일 작성:
              - Header: "genre,count,average_rating\\n"
              - For each genre: write "genre,count,avg" where avg = totals[i] / counts[i]
                각 장르마다: "genre,count,avg" 작성, avg = totals[i] / counts[i]
              - Format average to 2 decimal places: f"{avg:.2f}"
                평균은 소수점 2자리로: f"{avg:.2f}"
        3. Return the number of unique genres / 고유 장르 개수 반환

    Hint / 힌트: To check if a genre is already in the list:
                장르가 리스트에 이미 있는지 확인하려면:
                for i in range(len(genres)):
                    if genres[i] == current_genre:
                        ...
    """
    # TODO: Initialize three parallel lists / 평행 리스트 3개 초기화

    # TODO: Loop through ratings and update the lists
    # TODO: ratings를 반복하면서 리스트 갱신

    # TODO: Write the summary file / 요약 파일 작성

    # TODO: Return number of genres / 장르 개수 반환
    pass


def load_ratings_safe(file_path):
    """
    Load ratings, but return [] if the file doesn't exist.
    영화 평점을 로딩하되, 파일이 없으면 []를 반환합니다.

    Use try/except to catch FileNotFoundError.
    try/except로 FileNotFoundError를 잡으세요.

    Don't let the program crash! / 프로그램이 크래시하지 않도록!
    """
    # TODO: Wrap load_ratings() in try/except
    # TODO: load_ratings()를 try/except로 감싸기

    # TODO: On FileNotFoundError, return []
    # TODO: FileNotFoundError 발생 시 [] 반환
    pass


# ============================================================
# 🔒 PROTECTED TEST BLOCK — DO NOT MODIFY / 수정 금지
# ============================================================
if __name__ == "__main__":
    import os
    import shutil

    # Wipe prior output so unimplemented functions don't look like they "worked"
    # 이전 출력을 지워서 미구현 함수가 "동작한 것처럼" 보이지 않게 합니다
    if os.path.exists("output"):
        shutil.rmtree("output")
    os.makedirs("output", exist_ok=True)

    print("=" * 60)
    print("Running pipeline tests... / 파이프라인 테스트 실행 중...")
    print("=" * 60)

    try:
        ratings = load_ratings("movie_ratings.csv")
        print(f"\n[0] Loaded {len(ratings)} rows from movie_ratings.csv")

        # Test 1: save_ratings round trip
        print("\n[1] save_ratings — round trip / 왕복 테스트")
        try:
            save_ratings(ratings, "output/all_movies.csv")
            reloaded = load_ratings("output/all_movies.csv")
            if reloaded == ratings:
                print("    ✅ Round trip successful")
            else:
                print(f"    ❌ Mismatch: got {len(reloaded)} rows, expected {len(ratings)}")
        except Exception as e:
            print(f"    ⏳ Not implemented yet — {type(e).__name__}: {e}")

        # Test 2: save_filtered_by_genre
        print("\n[2] save_filtered_by_genre('Drama')")
        try:
            count = save_filtered_by_genre(ratings, "Drama", "output/drama.csv")
            print(f"    Got count: {count} (expected 3)")
            if os.path.exists("output/drama.csv"):
                drama = load_ratings("output/drama.csv")
                print(f"    Reloaded: {[r[0] for r in drama]}")
            else:
                print(f"    ⏳ output/drama.csv not created yet")
        except Exception as e:
            print(f"    ⏳ Not implemented yet — {type(e).__name__}: {e}")

        # Test 3: save_top_n
        print("\n[3] save_top_n(3)")
        try:
            n = save_top_n(ratings, 3, "output/top3.csv")
            print(f"    Saved count: {n} (expected 3)")
            if os.path.exists("output/top3.csv"):
                top = load_ratings("output/top3.csv")
                for movie in top:
                    print(f"      - {movie[0]}: {movie[3]}")
            else:
                print(f"    ⏳ output/top3.csv not created yet")
        except Exception as e:
            print(f"    ⏳ Not implemented yet — {type(e).__name__}: {e}")

        # Test 4: save_summary_report
        print("\n[4] save_summary_report")
        try:
            n_genres = save_summary_report(ratings, "output/summary.csv")
            print(f"    Genres: {n_genres} (expected 6)")
            if os.path.exists("output/summary.csv"):
                with open("output/summary.csv", "r", encoding="utf-8") as f:
                    for line in f:
                        print(f"      {line.rstrip()}")
            else:
                print(f"    ⏳ output/summary.csv not created yet")
        except Exception as e:
            print(f"    ⏳ Not implemented yet — {type(e).__name__}: {e}")

        # Test 5: load_ratings_safe
        print("\n[5] load_ratings_safe — missing file / 없는 파일")
        try:
            data = load_ratings_safe("does_not_exist.csv")
            if data == []:
                print(f"    ✅ Returned [] safely")
            else:
                print(f"    ❌ Expected [], got {data}")
        except Exception as e:
            print(f"    ❌ Crashed — should have caught the error! {type(e).__name__}")

        # Test 6: Edge cases
        print("\n[6] Edge cases / 경계 조건")
        try:
            save_ratings([], "output/empty.csv")
            if os.path.exists("output/empty.csv"):
                empty = load_ratings("output/empty.csv")
                print(f"    Empty list round trip: {len(empty)} rows (expected 0)")
            else:
                print(f"    ⏳ Empty file not created")
        except Exception as e:
            print(f"    ⏳ Empty list — {type(e).__name__}")

        try:
            save_top_n(ratings, 100, "output/top100.csv")
            if os.path.exists("output/top100.csv"):
                top100 = load_ratings("output/top100.csv")
                print(f"    TOP 100 (only 12 exist): {len(top100)} saved (expected 12)")
            else:
                print(f"    ⏳ top100 file not created")
        except Exception as e:
            print(f"    ⏳ n > total — {type(e).__name__}")

    except Exception as e:
        print(f"\n❌ Setup failed / 초기 설정 실패: {type(e).__name__}: {e}")

    print("\n" + "=" * 60)
    print("Keep going! / 계속 진행하세요!")
