#다음과 같이 import를 사용할 수 있습니다.
import math

def solution(a, b):
    # 여기에 코드를 작성해주세요.
    answer = 0
    l2_maxv = int(100000000**(1/2)) + 1
    l3_maxv = int(100000000**(1/3)) + 1

    initnum = 2
    if a <= initnum * initnum <= b:
        answer += 1

    for i in range(3, l2_maxv, 2):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime and i * i <= b and i * i >= a:
            answer += 1

    if a <= initnum * initnum * initnum <= b:
        answer += 1

    for i in range(3, l3_maxv, 2):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime and i * i * i <= b and i * i * i>= a:
            answer += 1

    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
a =  6
b =  30
ret = solution(a, b)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")