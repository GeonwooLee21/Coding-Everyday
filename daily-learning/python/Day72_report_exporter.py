"""
=================================================================
📄 리포트 내보내기 시스템 (추상 클래스) - 스켈레톤 코드
📄 Report Exporter System (Abstract Classes) - Skeleton Code
=================================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260618
=================================================================

빈칸(___)과 TODO를 채워서 완성하세요.
Fill in the blanks (___) and TODOs to complete the code.
"""

# TODO 1: abc 모듈에서 ABC와 abstractmethod를 가져오세요
#         Import ABC and abstractmethod from the abc module
from abc import ABC, abstractmethod


# ============================================================
# 추상 클래스 / Abstract Base Class
# ============================================================
class ReportExporter(ABC):  # TODO 2: ABC를 상속하세요 / Inherit from ABC
    """모든 내보내기 도구의 부모가 되는 추상 클래스
       Abstract base class for all report exporters"""

    def __init__(self, title: str):
        self.title = title

    # TODO 4: 아래 메서드를 추상 메서드로 만드세요 (데코레이터 추가)
    #         Make the method below abstract (add the decorator)
    @abstractmethod
    def file_extension(self) -> str:
        """파일 확장자를 반환 (예: "csv") / Return the file extension (e.g. "csv")"""
        ...

    # TODO 5: 이 메서드도 추상 메서드로 만드세요
    #         Make this one abstract too
    @abstractmethod
    def render(self, rows: list[dict]) -> str:
        """데이터를 형식에 맞는 문자열로 변환 / Render data into a formatted string"""
        ...

    # 구체 메서드 (모든 자식이 공유) / Concrete method (shared by all children)
    def export(self, rows: list[dict]) -> str:
        """ "제목.확장자" + 줄바꿈 + 렌더링 결과를 반환
            Return "title.ext" + newline + rendered output """
        # TODO 6: file_extension()과 render()를 모두 활용해 완성하세요
        #         Use both file_extension() and render() to build this
        body = f"\n{self.render(rows)}"
        return f"{self.title}.{self.file_extension()}\n{body}"


# ============================================================
# 구체 클래스 / Concrete Classes
# ============================================================
class CsvExporter(ReportExporter):
    """CSV 형식 / CSV format"""

    def file_extension(self) -> str:
        # TODO 7: "csv"를 반환 / Return "csv"
        return "csv"

    def render(self, rows: list[dict]) -> str:
        if not rows:
            return ""
        headers = list(rows[0].keys())
        lines = [",".join(headers)]
        for row in rows:
            # TODO 8: 각 행의 값들을 콤마로 연결해 lines에 추가하세요
            #         Join each row's values with commas and append to lines
            lines.append(",".join(str(row[h]) for h in headers))
        return "\n".join(lines)


class JsonExporter(ReportExporter):
    """JSON 형식 / JSON format"""

    def file_extension(self) -> str:
        # TODO 9: "json"을 반환 / Return "json"
        return "json"

    def render(self, rows: list[dict]) -> str:
        import json
        # ensure_ascii=False → 한글이 깨지지 않음 / keeps Korean readable
        return json.dumps(rows, ensure_ascii=False)


class TextExporter(ReportExporter):
    """사람이 읽는 텍스트 형식 / Human-readable text format"""

    def file_extension(self) -> str:
        return "txt"

    def render(self, rows: list[dict]) -> str:
        lines = []
        # enumerate의 start=1 → 1번부터 번호 매기기 / number from 1
        for i, row in enumerate(rows, start=1):
            parts = [f"{k}: {v}" for k, v in row.items()]
            # TODO 10: "1. name: Alice, score: 90" 형식을 만드세요
            #          Build the "1. name: Alice, score: 90" format
            lines.append(f"{i}. " + ", ".join(parts))
        return "\n".join(lines)


# ============================================================
# 🌟 보너스 (선택) / Bonus (optional)
# ============================================================
# 🥈 Medium: MarkdownExporter 클래스를 추가하세요 (확장자 "md", 표 형식)
#            Add a MarkdownExporter class (extension "md", table format)

# 🥇 Hard: 형식 문자열로 알맞은 도구를 돌려주는 함수
#          Function that returns the right exporter from a format string
def get_exporter(fmt, title):
    # TODO (보너스): {문자열: 클래스} 딕셔너리를 사용
    #               Use a {string: class} dictionary
    pass


# ============================================================
# 테스트 블록 (수정하지 마세요) / Test block (do not modify)
# ============================================================
if __name__ == "__main__":
    rows = [
        {"name": "Alice", "score": 90},
        {"name": "Bob", "score": 85},
    ]
    try:
        csv_exporter = CsvExporter("grades")
        json_exporter = JsonExporter("grades")
        text_exporter = TextExporter("grades")

        print(f"확장자 / Extensions: "
              f"{csv_exporter.file_extension()}, "
              f"{json_exporter.file_extension()}, "
              f"{text_exporter.file_extension()}")
        print()
        print("--- CSV ---")
        print(csv_exporter.render(rows))
        print("--- TEXT ---")
        print(text_exporter.render(rows))
        print()
        print("--- export() ---")
        for exporter in (csv_exporter, json_exporter, text_exporter):
            print(exporter.export(rows))
            print()

        try:
            ReportExporter("test")
            print("❌ 추상 클래스가 생성되었습니다 (잘못됨) / ABC was instantiated (wrong)")
        except TypeError:
            print("✅ 추상 클래스는 인스턴스화 불가 / ABC cannot be instantiated")

    except Exception as e:
        print(f"⚠️ 에러 발생 / Error occurred: {type(e).__name__}: {e}")
        print("TODO를 모두 채웠는지 확인하세요 / Check that you filled in all TODOs")
