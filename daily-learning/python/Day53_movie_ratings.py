"""
===============================================================
🎬 Movie Ratings CSV Analysis
영화 평점 CSV 분석
===============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260515
===============================================================

Fill in the TODOs below. The test block at the bottom will run automatically.
아래 TODO를 채워주세요. 맨 아래의 테스트 블록은 자동으로 실행됩니다.

⚠️ Allowed / 사용 가능:
   open(), with, .split(), .strip(), int(), float(), len()
   for, if, list methods

⚠️ NOT allowed / 사용 금지:
   import csv, import pandas
   max() / min() / sum() shortcuts for rating logic
"""


def load_ratings(file_path):
    """
    Read the CSV file and return a list of [title, genre, year, rating].
    CSV 파일을 읽어서 [title, genre, year, rating] 리스트의 리스트를 반환합니다.

    Steps / 단계:
        1. Open the file with `with open(...)` / `with open(...)`으로 파일 열기
        2. Read all lines / 모든 줄 읽기
        3. Skip the header (first line) / 헤더(첫 줄) 건너뛰기
        4. For each line: strip(), split(","), convert types
           각 줄에 대해: strip(), split(","), 타입 변환
        5. Append [title, genre, int(year), float(rating)] to the result list
           [title, genre, int(year), float(rating)]를 결과 리스트에 추가
    """
    ratings = []
    # TODO: Open the file and read its contents
    # TODO: 파일을 열고 내용을 읽으세요
    with open(file_path, "r", encoding="utf-8") as f:

    # TODO: Loop through lines, skip the header, parse each row
    # TODO: 줄들을 반복하면서, 헤더를 건너뛰고, 각 행을 파싱하세요
        count = 0
        for line in f:
            if count == 0:
                count += 1
                continue
            else:
                count += 1
                title, genre, year, rating = line.strip().split(",")
                ratings.append([title, genre, int(year), float(rating)])

    return ratings


def count_movies(ratings):
    """
    Return the total number of movies. (len() is allowed here.)
    영화의 총 개수를 반환합니다. (여기서는 len() 사용 가능)
    """
    # TODO: Return the count / 개수를 반환하세요
    return len(ratings)


def average_rating(ratings):
    """
    Return the average of all movie ratings.
    모든 영화 평점의 평균을 반환합니다.
    Return 0.0 if the list is empty. / 리스트가 비어 있으면 0.0을 반환하세요.

    Hint / 힌트: Use a for loop to accumulate the total, then divide by count.
                for 반복문으로 합계를 누적한 뒤, 개수로 나누세요.
                Do NOT use sum(). / sum()을 사용하지 마세요.
    """
    # TODO: Handle empty list / 빈 리스트 처리
    if ratings == []: # or len(ratings) == 0 or not ratings(-> 파이썬에서 빈 리스트는 항상 falsy하므로)
        return 0.0

    # TODO: Loop and accumulate / 반복하면서 누적
    total = 0
    for rating in ratings:
        total += rating[3]

    # TODO: Return average / 평균 반환
    return total / count_movies(ratings)


def highest_rated(ratings):
    """
    Return the title of the movie with the highest rating.
    가장 높은 평점을 가진 영화의 제목을 반환합니다.
    Return None if the list is empty. / 리스트가 비어 있으면 None을 반환하세요.

    Hint / 힌트: Initialize "best" with the first movie, then compare each row.
                "best"를 첫 번째 영화로 초기화하고, 각 행을 비교하세요.
                Do NOT use max(). / max()를 사용하지 마세요.
    """
    # TODO: Handle empty list / 빈 리스트 처리
    if count_movies(ratings) == 0:
        return None

    # TODO: Initialize best title and best score / 최고 제목과 최고 점수 초기화
    best = ratings[0]

    # TODO: Loop and update / 반복하면서 갱신
    for movie in ratings:
        if movie[3] > best[3]:
            best = movie

    # TODO: Return the best title / 최고 제목 반환
    return best[0]


def filter_by_genre(ratings, genre):
    """
    Return a list of movies that match the given genre.
    주어진 장르와 일치하는 영화들의 리스트를 반환합니다.
    """
    # TODO: Build a new list with matching rows
    # TODO: 일치하는 행들로 새 리스트 만들기
    matching_list = []
    for movie in ratings:
        if movie[1] == genre:
            matching_list.append(movie)

    return matching_list


def count_above_threshold(ratings, threshold):
    """
    Return the count of movies whose rating is >= threshold.
    평점이 threshold 이상인 영화의 개수를 반환합니다.
    """
    # TODO: Count rows where rating >= threshold
    # TODO: rating >= threshold인 행의 개수 세기
    count = 0
    for movie in ratings:
        if movie[3] >= threshold:
            count += 1

    return count


# ============================================================
# 🔒 PROTECTED TEST BLOCK — DO NOT MODIFY / 수정 금지
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("Running tests... / 테스트 실행 중...")
    print("=" * 50)

    try:
        ratings = load_ratings("./daily-learning/python/data/input/movie_ratings.csv")
        print(f"\n[1] Loaded {len(ratings)} rows (expected 12)")
        print(f"    First row: {ratings[0] if ratings else 'None'}")
        print(f"    Expected:  ['The Shawshank Redemption', 'Drama', 1994, 9.3]")

        print(f"\n[2] count_movies: {count_movies(ratings)} (expected 12)")

        avg = average_rating(ratings)
        if avg is not None:
            print(f"\n[3] average_rating: {avg:.4f} (expected ~8.6500)")
        else:
            print(f"\n[3] average_rating: None — not implemented yet")

        print(f"\n[4] highest_rated: {highest_rated(ratings)}")
        print(f"    Expected: The Shawshank Redemption")

        action = filter_by_genre(ratings, "Action")
        if action is not None:
            print(f"\n[5] filter_by_genre('Action'): {len(action)} movies (expected 3)")
            print(f"    Titles: {[r[0] for r in action]}")

        print(f"\n[6] count_above_threshold(8.5): {count_above_threshold(ratings, 8.5)} (expected 9)")
        print(f"    count_above_threshold(9.0): {count_above_threshold(ratings, 9.0)} (expected 2)")

        print(f"\n[7] Edge cases / 경계 조건:")
        print(f"    average_rating([]) = {average_rating([])} (expected 0.0)")
        print(f"    highest_rated([])  = {highest_rated([])} (expected None)")

    except Exception as e:
        print(f"\n❌ Error / 오류: {type(e).__name__}: {e}")
        print("Keep going! / 계속 진행하세요!")
