#다음과 같이 import를 사용할 수 있습니다.
#import math

def convert10(s, p):
    num = 0
    mul = 1
    for i in reversed(s):
        num += int(i) * mul
        mul *= p
    return num

def convertq(s, q):
    d = ""
    while s > 0:
        d += str(s % q)
        s = s // q

    return d[::-1]


def solution(s1, s2, p, q):
    #여기에 코드를 작성해주세요.

    num1 = convert10(s1, p)
    num2 = convert10(s2, p)
    answer = convertq(num1 + num2,q)
    print(convertq(int(s1, p) + int(s2, p), q))
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
s1 = "112001"
s2 = "12010"
p = 3
q = 8
ret = solution(s1, s2, p, q)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")