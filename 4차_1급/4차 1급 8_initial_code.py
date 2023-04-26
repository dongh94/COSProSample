# 다음과 같이 import를 사용할 수 있습니다.
# import math
def count(card, n):
    card_count = [0]*10
    for i in range(len(card)):
        card_count[card[i]] += 1
    return card_count

def choose(cardlist, n):
    if n in cardlist:
        return cardlist.index(n) + 1
    return -1

def solution(card, n):
    # 여기에 코드를 작성해주세요.
    card_list = []
    card_count = count(card, n)

    def dfs_card(dept, maxdept, pre_count, card_count, num):
        nonlocal card_list

        if dept >= maxdept:
            card_list.append(num)
            return

        for i in range(1, 10):
            if pre_count[i] < card_count[i]:
                pre_count[i] += 1
                dfs_card(dept + 1, maxdept, pre_count, card_count, num * 10 + i)
                pre_count[i] -= 1

    dfs_card(0, len(card), [0]*10, card_count, 0)

    print(card_list)
    answer = choose(card_list, n)
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
card1 = [1, 2, 1, 3]
n1 = 1312
ret1 = solution(card1, n1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
card2 = [9, 9, 9, 9, 8, 9, 9, 9, 9]
n2 = 999999998
ret2 = solution(card2, n2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")