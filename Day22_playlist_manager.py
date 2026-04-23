# 🎵 Playlist Manager - Skeleton Code
# 플레이리스트 매니저 - 뼈대 코드

# ============================================================
# 함수를 완성하세요! Complete each function below.
# 각 TODO 주석을 읽고 코드를 채워 넣으세요.
# Read each TODO comment and fill in the code.
# ============================================================


def add_song(playlist: list, song: str) -> None:
    """
    플레이리스트에 노래를 추가합니다.
    Adds a song to the playlist.

    - 이미 있는 노래면 중복 추가하지 않습니다.
      If the song is already in the playlist, do not add it again.
    - 없는 노래면 맨 끝에 추가합니다.
      If it's new, add it to the end.
    """
    # TODO 1: 노래가 이미 플레이리스트에 있는지 확인하세요.
    #         Check if the song is already in the playlist.
    #         힌트 / Hint: use the `in` keyword

    # TODO 2: 이미 있으면 메시지를 출력하세요.
    #         If already there, print a message.
    #         예시 / Example: "APT.은(는) 이미 플레이리스트에 있어요!"
    #                         "APT. is already in the playlist!"

    # TODO 3: 없으면 playlist에 추가하고 메시지를 출력하세요.
    #         If not there, add it and print a message.
    #         힌트 / Hint: use append()
    pass


def remove_song(playlist: list, song: str) -> None:
    """
    플레이리스트에서 노래를 삭제합니다.
    Removes a song from the playlist.

    - 노래가 있으면 삭제합니다.
      If found, remove the song.
    - 없으면 메시지를 출력합니다.
      If not found, print a message.
    """
    # TODO 1: 노래가 플레이리스트에 있는지 확인하세요.
    #         Check if the song is in the playlist.

    # TODO 2: 있으면 삭제하고 메시지를 출력하세요.
    #         If found, remove it and print a message.
    #         힌트 / Hint: use remove()

    # TODO 3: 없으면 "찾을 수 없다"는 메시지를 출력하세요.
    #         If not found, print a "not found" message.
    pass


def find_song(playlist: list, song: str) -> None:
    """
    노래가 플레이리스트에 있는지 검색합니다.
    Searches for a song in the playlist.

    - 있으면 몇 번째 트랙인지 출력합니다.
      If found, print which track number it is.
    - 없으면 없다고 출력합니다.
      If not found, print that it's not there.
    """
    # TODO 1: 반복문(for loop)으로 playlist를 순회하세요.
    #         Use a for loop to go through the playlist.
    #         힌트 / Hint: you'll need a counter variable to track the position

    # TODO 2: 각 항목을 song과 비교하세요.
    #         Compare each item with song.

    # TODO 3: 찾으면 트랙 번호와 함께 출력하고 함수를 끝내세요.
    #         If found, print with track number and stop the loop.
    #         예시 / Example: "✅ APT. - 플레이리스트에 있어요! (2번째 트랙)"
    #                         "✅ APT. - Found! (Track #2)"

    # TODO 4: 반복문이 끝날 때까지 못 찾으면 없다고 출력하세요.
    #         If the loop ends without finding it, print not found.
    pass


def show_playlist(playlist: list) -> None:
    """
    현재 플레이리스트를 번호와 함께 출력합니다.
    Displays the current playlist with track numbers.

    - 비어 있으면 안내 메시지를 출력합니다.
      If empty, print a message telling the user to add songs.
    - 있으면 번호를 붙여서 출력합니다.
      If not empty, print each song with its number.
    """
    # TODO 1: 플레이리스트가 비어 있는지 확인하세요.
    #         Check if the playlist is empty.
    #         힌트 / Hint: use len()

    # TODO 2: 비어 있으면 안내 메시지를 출력하세요.
    #         If empty, print the "add some songs" message.

    # TODO 3: 비어 있지 않으면 반복문으로 번호와 함께 출력하세요.
    #         If not empty, loop through and print each song with a number.
    #         예시 / Example:
    #         1. Supernova
    #         2. APT.
    #         3. Whiplash
    pass


# ============================================================
# 🌟 보너스 챌린지 / Bonus Challenge
# ============================================================

def move_to_top(playlist: list, song: str) -> None:
    """
    노래를 플레이리스트 맨 앞으로 이동합니다.
    Moves a song to the front of the playlist.

    보너스 도전! 기본 과제를 모두 마친 후 시도해보세요.
    Bonus challenge! Try this only after finishing the main tasks.
    """
    # TODO 1: 노래가 플레이리스트에 있는지 확인하세요.
    #         Check if the song is in the playlist.

    # TODO 2: 없으면 "찾을 수 없다"는 메시지를 출력하세요.
    #         If not found, print a not found message.

    # TODO 3: 이미 첫 번째 트랙이면 메시지를 출력하세요.
    #         If it's already the first track, print a message.
    #         힌트 / Hint: how do you access the first item in a list?

    # TODO 4: 아니면 노래를 지우고 맨 앞에 삽입하세요.
    #         Otherwise, remove the song and insert it at position 0.
    #         힌트 / Hint: remove() then insert(0, song)
    pass


# ============================================================
# 🎪 테스트 코드 / Test Code
# 아래 코드를 실행해서 함수가 잘 작동하는지 확인하세요!
# Run the code below to check if your functions work correctly!
# ============================================================

if __name__ == "__main__":
    print("=" * 40)
    print("테스트 1: 노래 추가 / Test 1: Adding songs")
    print("=" * 40)
    playlist = []
    add_song(playlist, "Supernova")
    add_song(playlist, "APT.")
    add_song(playlist, "Whiplash")
    add_song(playlist, "APT.")      # duplicate
    show_playlist(playlist)

    print()
    print("=" * 40)
    print("테스트 2: 검색 / Test 2: Finding songs")
    print("=" * 40)
    find_song(playlist, "Whiplash")
    find_song(playlist, "Dynamite")

    print()
    print("=" * 40)
    print("테스트 3: 삭제 / Test 3: Removing songs")
    print("=" * 40)
    remove_song(playlist, "Supernova")
    remove_song(playlist, "Dynamite")
    show_playlist(playlist)

    print()
    print("=" * 40)
    print("테스트 4: 빈 리스트 / Test 4: Empty playlist")
    print("=" * 40)
    empty = []
    show_playlist(empty)

    print()
    print("=" * 40)
    print("🌟 보너스 테스트 / Bonus Test")
    print("=" * 40)
    bonus_playlist = ["APT.", "Whiplash", "Supernova"]
    show_playlist(bonus_playlist)
    move_to_top(bonus_playlist, "Supernova")
    show_playlist(bonus_playlist)
    move_to_top(bonus_playlist, "Supernova")   # already first
    move_to_top(bonus_playlist, "Dynamite")    # not found
