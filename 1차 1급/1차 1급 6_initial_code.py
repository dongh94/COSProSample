#You may use import as below.
#import math

def solution(pos):
    # Write code here.
    answer = 0
    arr = [[0]*8 for _ in range(8)]
    # 상상우, 우우상, 우우하, 하하우, 하하좌, 좌좌하, 좌좌상, 상상좌
    dr = [-2, -1, 1, 2, 2, 1, -1, -2]
    dc = [1, 2, 2, 1, -1, -2, -2, -1]
    alpha_dict = dict()
    for d in range(8):
        alpha_dict[chr(65+d)] = d
    sc = alpha_dict[pos[0]]
    sr = 8 - int(pos[1])

    for d in range(8):
        nr = sr + dr[d]
        nc = sc + dc[d]
        if nr >= 8 or nr < 0 or nc >= 8 or nc < 0:
            continue
        else:
            answer += 1

    return answer

#The following is code to output testcase.
pos = "A7"
ret = solution(pos)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")