# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(s1, s2):
    # 여기에 코드를 작성해주세요.
    answer = 0
    length01 = len(s1)
    length02 = len(s2)

    for i in range(length01):
        if s1[0:i+1] == s2[-(i+1):]:
            answer = max(answer, i+1)

    for j in range(length02):
        if s2[0:j+1] == s1[-(j+1):]:
            answer = max(answer, j+1)

    answer = length01 + length02 - answer
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
s1 = "ababc"
s2 = "abcdab"
ret = solution(s1, s2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")