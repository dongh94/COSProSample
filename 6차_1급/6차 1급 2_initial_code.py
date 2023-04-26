#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(K, words):
    #여기에 코드를 작성해주세요.
    answer = 0
    limitK = 0
    for word in words:
        if limitK == 0:
            limitK += len(word)
        elif limitK == 10:
            answer += 1
            limitK = len(word)

        elif limitK > 0:
            if limitK + len(word) + 1 <= K:
                limitK += len(word) + 1
            else:
                answer += 1
                limitK = len(word)
    answer += 1

    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
K = 10
words = ["nice", "happy", "hello", "world", "hi"]
ret = solution(10, words)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")