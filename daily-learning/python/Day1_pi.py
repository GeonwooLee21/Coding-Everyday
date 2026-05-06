pi = 3.14159
radius = 14

circle_area = radius ** 2 * pi

circle_perimeter = radius * 2 * pi

print("넓이:", round(circle_area, 2)) # round( , n) : n자리 소수점까지 출력
print("둘레:", round(circle_perimeter, 2))

# 코딩을 마친 후, 다음을 생각해보세요:
# 1. 왜 3.14 대신 pi = 3.14159 변수를 사용하는 게 더 좋을까요? 
# A. pi 값은 무한소수이므로 pi 변수의 소수점 자리수를 늘림으로서 더 정확한 넓이/둘레를 구하는 것이 가능하기 때문이다.
# 2. 반지름이 2배가 되면 넓이는 몇 배가 될까요? 
# A. 4배