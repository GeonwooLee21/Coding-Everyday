"""
=============================================================
Valid Sudoku
스도쿠 검증기
=============================================================
# 👤 이름 / Name: 이건우
# 📅 날짜 / Date: 260426
=============================================================

[KO] 함수 본문(TODO 부분)만 작성하세요. 아래 if __name__ == "__main__" 블록은 수정하지 마세요!
[EN] Only write the function body (TODO sections). Do NOT modify the if __name__ == "__main__" block below!
"""


def is_valid_sudoku(board: list[list[str]]) -> bool:
    # TODO 1: [KO] 각 행(row)에 중복된 숫자가 있는지 확인하세요. 0은 무시합니다.
    #         [EN] Check each row for duplicate numbers. Ignore 0 (empty cells).
    #         힌트 / Hint: for row in board: ... 안에서 set을 사용
    for row in board:
        dup_count = 0
        set_row = set()
        for num in row:
            if num != 0:
                dup_count += 1
                set_row.add(num)
        if dup_count != len(set_row):
            return False

    # TODO 2: [KO] 각 열(column)에 중복된 숫자가 있는지 확인하세요. 0은 무시합니다.
    #         [EN] Check each column for duplicate numbers. Ignore 0.
    #         힌트 / Hint: 열 인덱스를 고정하고 행을 순회: board[row_index][col_index]
    for col in range(0, 9):
        dup_count = 0
        set_col = set()
        for row in range(0, 9):
            if board[row][col] != 0:
                dup_count += 1
                set_col.add(board[row][col])
        if dup_count != len(set_col):
            return False

    # TODO 3: [KO] 9개의 3x3 박스 각각에 중복된 숫자가 있는지 확인하세요. 0은 무시합니다.
    #         [EN] Check each of the nine 3x3 boxes for duplicates. Ignore 0.
    #         힌트 / Hint: 박스의 시작 좌표는 (box_row * 3, box_col * 3)
    #                     where box_row, box_col in range(3)
    box_start_idx = ((0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6))
    for box_row, box_col in box_start_idx:
        dup_count = 0
        set_box = set()
        for row in range(box_row, box_row+3):
            for col in range(box_col, box_col+3):
                if board[row][col] != 0:
                    dup_count += 1
                    set_box.add(board[row][col])
        if dup_count != len(set_box):
            return False

    # TODO 4: [KO] 모든 검사를 통과하면 True를 반환하세요.
    #         [EN] If all checks pass, return True.
    return True  # [KO] 이 줄을 적절히 수정하세요 / [EN] Modify this line appropriately


# ============================================================
# [KO] 아래 코드는 절대 수정하지 마세요! / [EN] DO NOT modify the code below!
# ============================================================
if __name__ == "__main__":
    # Test 1: Valid board / 유효한 보드
    valid_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    print(f"Test 1 (valid):       {is_valid_sudoku(valid_board)}  | Expected: True")

    # Test 2: Empty board / 빈 보드
    empty_board = [[0] * 9 for _ in range(9)]
    print(f"Test 2 (empty):       {is_valid_sudoku(empty_board)}  | Expected: True")

    # Test 3: Row duplicate / 행 중복 (첫 행에 8이 두 번)
    invalid_row = [
        [8, 3, 0, 0, 7, 0, 0, 0, 8],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    print(f"Test 3 (row dup):     {is_valid_sudoku(invalid_row)} | Expected: False")

    # Test 4: Column duplicate / 열 중복 (첫 열에 8이 두 번)
    invalid_col = [
        [8, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    print(f"Test 4 (col dup):     {is_valid_sudoku(invalid_col)} | Expected: False")

    # Test 5: Box duplicate / 박스 중복 (좌상단 박스에 5가 두 번)
    invalid_box = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 5, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    print(f"Test 5 (box dup):     {is_valid_sudoku(invalid_box)} | Expected: False")
