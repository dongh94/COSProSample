#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(number, target):
    #여기에 코드를 작성해주세요.
    answer = 0
    INF = float('inf')
    dp = [INF]*20001
    dp[number] = 0
    for i in range(number, 20000):
        if i + 1 <= 20000:
            dp[i+1] = min(dp[i]+1, dp[i+1])
        if i - 1 >= 0:
            dp[i-1] = min(dp[i]+1, dp[i-1])
        if i * 2 <= 20000:
            dp[i*2] = min(dp[i]+1, dp[i*2])
    answer =dp[target]
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
number1 = 5
target1 = 9
ret1 = solution(number1, target1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

number2 = 3
target2 = 11
ret2 = solution(number2, target2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")