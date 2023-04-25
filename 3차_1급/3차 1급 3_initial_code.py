#다음과 같이 import를 사용할 수 있습니다.
#import math
arr = [[0] * 8 for _ in range(8)]

def solution(bishops):
    #여기에 코드를 작성해주세요.
    global arr
    answer = 0

    alpah_dict = dict()
    for i in range(8):
        alpah_dict[chr(65+i)] = i

    length = len(bishops)
    for i in range(length):
        alpha = bishops[i][0]

        alp_num = alpah_dict[alpha] # c
        number = 8-int(bishops[i][1]) # r
        arr[number][alp_num] = 2

    for r in range(8):
        for c in range(8):
            if arr[r][c] == 2:
                Find(r, c)

    for r in range(8):
        for c in range(8):
            if arr[r][c] == 0:
                answer += 1
    return answer


# 상좌, 상우, 하좌, 하우
dr = [-1, -1, 1, 1]
dc = [-1, 1, -1, 1]
def Find(r, c):
    global arr
    Q = [(r, c)]
    for d in range(4):
        sr = r
        sc = c
        for _ in range(7):
            nr = sr + dr[d]
            nc = sc + dc[d]
            if nr < 0 or nr >= 8 or nc < 0 or nc >= 8 or arr[nr][nc] == 2:
                continue

            arr[nr][nc] = 1
            sr = nr
            sc = nc

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
bishops1 = ["D5"]
ret1 = solution(bishops1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")