#다음과 같이 import를 사용할 수 있습니다.
#import math
from collections import deque
def solution(n, garden):
    #여기에 코드를 작성해주세요.
    answer = 0
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    def BFS(r, c):
        Q = deque()
        Q.append((r,c))
        while Q:
            sr, sc = Q.popleft()

            for d in range(4):
                nr = sr + dr[d]
                nc = sc + dc[d]
                if nr < 0 or nr >= n or nc < 0 or nc >= n or garden[nr][nc] >= 1:
                    continue
                garden[nr][nc] = garden[sr][sc] + 1
                Q.append((nr,nc))

        return max(max(garden))-1

    for r in range(n):
        for c in range(n):
            if garden[r][c] == 1:
                answer = BFS(r, c)

    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n1 = 3
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(n1, garden1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 2
garden2 = [[1, 1], [1, 1]]
ret2 = solution(n2, garden2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")