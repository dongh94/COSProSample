#You may use import as below.
#import math

def solution(num):
    # Write code here.
    answer = num + 1
    num += 1
    while True:
        flag = False
        while num > 0:
            if num % 10 != 0:
                num //= 10

            else: # 0이 발견됨.
                flag = True
                break

        if flag:
            num = answer + 1
            answer += 1
        else:
            break

    return answer
    # num += 1
    # digit = 1
    # while num // digit % 10 == 0:
    #     print(num // digit)
    #     num += digit
    #     print("num : ",num)
    #
    #     digit *= 10
    #     print("num : ", num)
    #
    # return num


#The following is code to output testcase.
num = 9040999;
ret = solution(num)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".")