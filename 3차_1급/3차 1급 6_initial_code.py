def solution(n):
    answer = 0
    primes = [2]
    for i in range (3, n + 1, 2) : # 홀수 중에서
        is_prime = True
        for j in range(2, i) : # 1보다 큰 수부터 자기자신의 수가 자기자신보다 낮은수로 나누었을 때 나머지가 0이되면 소수 X
            if i % j == 0 :
                is_prime = False
                break
        if is_prime :
            primes.append(i)

    prime_len = len(primes)
    for i in range(0, prime_len - 2) :
        for j in range(i + 1, prime_len - 1) :
            for k in range(j + 1, prime_len) :
                if primes[i] + primes[j] + primes[k] == n :
                    answer += 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n1 = 33
ret1 = solution(n1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 9
ret2 = solution(n2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")