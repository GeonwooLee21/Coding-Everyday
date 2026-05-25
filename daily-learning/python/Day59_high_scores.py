"""
===============================================================
🎮 Day 3 — Class Design Practice: HighScores
===============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260524
===============================================================
주제 / Topic:  __str__과 __repr__로 객체 예쁘게 출력하기
               Printable objects with __str__ and __repr__

설명 / Brief:  Frogger 게임 스타일의 최고 점수판 클래스를 만드세요.
               Build a Frogger-style leaderboard class.

규칙 / Rules:  - 모든 이름은 snake_case
                 All names in snake_case
               - 원본 점수 리스트의 순서를 절대 바꾸지 마세요
                 Never mutate the original score list
"""


class HighScores:
    """
    게임 플레이어의 최고 점수 리스트를 관리합니다.
    Manage a game player's high score list.
    """

    def __init__(self, scores: list[int]) -> None:
        # TODO 1:
        # 받은 scores 리스트를 self.scores에 저장하세요.
        # Store the passed-in scores list as self.scores.
        self.scores  = scores

    def latest(self) -> int:
        # TODO 2:
        # 가장 최근 점수를 반환하세요 (리스트의 마지막 항목).
        # Return the most recent score (last item in the list).
        return self.scores[len(self.scores)-1]
    
        # 더 파이썬다운 방식
        # return self.scores[-1]

    def personal_best(self) -> int:
        # TODO 3:
        # 가장 높은 점수를 반환하세요. max() 내장 함수를 활용해보세요.
        # Return the highest score. Try using the built-in max().
        return max(self.scores)

    def personal_top_three(self) -> list[int]:
        # TODO 4:
        # 상위 3개 점수를 내림차순 리스트로 반환하세요.
        # 점수가 3개 미만이면 있는 만큼만 반환합니다.
        # ⚠️ 원본 리스트의 순서를 바꾸지 마세요!
        # ⚠️ self.scores.sort() 대신 sorted()를 사용하세요.
        #
        # Return the top 3 scores as a descending list.
        # If fewer than 3 scores exist, return what you have.
        # ⚠️ Don't mutate the original list!
        # ⚠️ Use sorted() instead of self.scores.sort().
        # descending_list =sorted(self.scores, reverse=True)

        # if len(descending_list) < 3:
        #     return descending_list
        # else:
        #     return descending_list[0:3]

        # 개선 : 파이썬 슬라이싱은 범위를 벗어나도 에러 없이 있는 만큼만 반환한다. 따라서 if/else 분기가 필요없다.
        return sorted(self.scores, reverse=True)[:3]

        

    def __str__(self) -> str:
        # TODO 5:
        # 사용자에게 보여줄 친근한 문자열을 반환하세요.
        # 예: "🎮 High Scores — Top: [100, 90, 30] | Latest: 30"
        # 힌트: self.personal_top_three()와 self.latest()를 호출해도 됩니다.
        #
        # Return a friendly string for end users.
        # Example: "🎮 High Scores — Top: [100, 90, 30] | Latest: 30"
        # Hint: feel free to call self.personal_top_three() and self.latest().
        return f"🎮 High Scores — Top: {self.personal_top_three()} | Latest: {self.latest()}"

    def __repr__(self) -> str:
        # TODO 6:
        # 개발자용 명확한 표현을 반환하세요.
        # eval(repr(obj))로 같은 객체를 재현할 수 있어야 합니다.
        # 예: "HighScores(scores=[30, 50, 20, 70])"
        # 힌트: f-string의 {value!r} 포맷팅을 사용해보세요.
        #
        # Return an unambiguous representation for developers.
        # eval(repr(obj)) should produce an equivalent object.
        # Example: "HighScores(scores=[30, 50, 20, 70])"
        # Hint: use the {value!r} formatting in an f-string.
        return f"HighScores(scores={self.scores!r})"


# ============================================================
# 🧪 테스트 영역 — 이 아래는 수정하지 마세요!
# 🧪 Test zone — do not edit below this line!
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("🎮 HighScores Class — 자동 테스트 / Auto Tests")
    print("=" * 50)

    try:
        # Test 1: scores attribute preserved
        hs1 = HighScores([30, 50, 20, 70])
        assert hs1.scores == [30, 50, 20, 70], \
            f"Test 1 실패: scores={hs1.scores}"
        print("✅ Test 1 (scores 속성 저장) 통과")
    except (AssertionError, AttributeError, TypeError) as e:
        print(f"❌ Test 1: {e}")

    try:
        # Test 2: latest()
        assert HighScores([100, 0, 90, 30]).latest() == 30
        assert HighScores([40]).latest() == 40
        print("✅ Test 2 (latest) 통과")
    except (AssertionError, AttributeError, TypeError) as e:
        print(f"❌ Test 2: {e}")

    try:
        # Test 3: personal_best()
        assert HighScores([40, 100, 70]).personal_best() == 100
        assert HighScores([7]).personal_best() == 7
        assert HighScores([5, 5, 5]).personal_best() == 5
        print("✅ Test 3 (personal_best) 통과")
    except (AssertionError, AttributeError, TypeError) as e:
        print(f"❌ Test 3: {e}")

    try:
        # Test 4: personal_top_three() — basic
        assert HighScores([10, 30, 90, 30, 100, 20, 10, 0, 30, 40, 40, 70, 70]) \
            .personal_top_three() == [100, 90, 70]
        # ascending input
        assert HighScores([20, 10, 30]).personal_top_three() == [30, 20, 10]
        print("✅ Test 4 (personal_top_three 기본) 통과")
    except (AssertionError, AttributeError, TypeError) as e:
        print(f"❌ Test 4: {e}")

    try:
        # Test 5: personal_top_three() — ties
        assert HighScores([40, 20, 40, 30]).personal_top_three() == [40, 40, 30]
        print("✅ Test 5 (동점 처리 / ties) 통과")
    except (AssertionError, AttributeError, TypeError) as e:
        print(f"❌ Test 5: {e}")

    try:
        # Test 6: personal_top_three() — fewer than 3
        assert HighScores([30, 70]).personal_top_three() == [70, 30]
        assert HighScores([40]).personal_top_three() == [40]
        print("✅ Test 6 (3개 미만 점수) 통과")
    except (AssertionError, AttributeError, TypeError) as e:
        print(f"❌ Test 6: {e}")

    try:
        # Test 7: original list preserved
        hs7 = HighScores([30, 50, 20, 70])
        _ = hs7.personal_top_three()
        assert hs7.scores == [30, 50, 20, 70], \
            "원본 리스트가 변경되었습니다 / Original list was mutated"
        print("✅ Test 7 (원본 리스트 보존) 통과")
    except (AssertionError, AttributeError, TypeError) as e:
        print(f"❌ Test 7: {e}")

    try:
        # Test 8: __str__ exists and returns a non-trivial string
        hs8 = HighScores([100, 0, 90, 30])
        s = str(hs8)
        assert isinstance(s, str) and len(s) > 0
        assert "object at" not in s, \
            "__str__를 구현하세요 / Implement __str__"
        print(f"✅ Test 8 (__str__) 통과 — 출력: {s}")
    except (AssertionError, AttributeError, TypeError) as e:
        print(f"❌ Test 8: {e}")

    try:
        # Test 9: __repr__ round-trip
        hs9 = HighScores([30, 50, 20, 70])
        r = repr(hs9)
        assert "object at" not in r, \
            "__repr__를 구현하세요 / Implement __repr__"
        hs9_copy = eval(r)
        assert hs9_copy.scores == hs9.scores, \
            "__repr__가 라운드트립되지 않습니다 / __repr__ does not round-trip"
        print(f"✅ Test 9 (__repr__ 라운드트립) 통과 — 출력: {r}")
    except (AssertionError, AttributeError, TypeError, SyntaxError, NameError) as e:
        print(f"❌ Test 9: {e}")

    print("=" * 50)
    print("끝났습니다! 통과하지 못한 테스트가 있으면 해당 TODO를 다시 보세요.")
    print("Done! If any test failed, revisit the corresponding TODO.")
    print("=" * 50)
