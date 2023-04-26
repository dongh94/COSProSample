# 다음과 같이 import를 사용할 수 있습니다.
# import math
def solution(hour, minute):
    answer = ''
    newhour = hour * 30
    newhour += 0.5 * minute
    newminu = minute * 6
    answer = abs(newhour - newminu)
    if answer > 360 - answer:
        answer = 360 - answer

    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
hour = 12
minute = 25
ret = solution(hour, minute)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")