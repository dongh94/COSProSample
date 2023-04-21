#You may use import as below.
#import math

def solution(n):
    # Write code here.
    answer = 0
    arr = [[0]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    # 우하좌상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    d = 0
    start = 1
    end = n * n - 1

    r = c = 0
    arr[r][c] = start
    # visited[r][c] = 1
    while end:
        nr = r + dr[d]
        nc = c + dc[d]
        if nr < 0 or nr >= n or nc < 0 or nc >= n or arr[nr][nc] != 0:
            d = (d + 1) % 4
            continue
        if arr[nr][nc] == 0:
            visited[nr][nc] = 1
            r = nr
            c = nc
            start += 1
            arr[nr][nc] = start
            end -= 1

    for i in range(n):
        answer += arr[i][i]
    return answer


#The following is code to output testcase.
n1 = 3
ret1 = solution(n1)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret1, ".")
    
n2 = 2
ret2 = solution(n2)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret2, ".")

n2 = 4
ret2 = solution(n2)

#Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")