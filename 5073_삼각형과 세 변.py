# 문제
# 삼각형의 세 변의 길이가 주어질 때 변의 길이에 따라 다음과 같이 정의한다.
#
# Equilateral :  세 변의 길이가 모두 같은 경우
# Isosceles : 두 변의 길이만 같은 경우
# Scalene : 세 변의 길이가 모두 다른 경우
# 단 주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우에는 "Invalid" 를 출력한다.
# 예를 들어 6, 3, 2가 이 경우에 해당한다. 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면
# 삼각형의 조건을 만족하지 못한다.
#
# 세 변의 길이가 주어질 때 위 정의에 따른 결과를 출력하시오.
#
# 입력
# 각 줄에는 1,000을 넘지 않는 양의 정수 3개가 입력된다. 마지막 줄은 0 0 0이며 이 줄은 계산하지 않는다.
#
# 출력
# 각 입력에 맞는 결과 (Equilateral, Isosceles, Scalene, Invalid) 를 출력하시오.


'''
while True:
    result = ''
    lst = list(map(int, input().split()))
    lst.sort()
    if lst[0] == lst[1] == lst[2] == 0:
        break
    if lst[-1] >= lst[0]+lst[1]:
        result = 'Invalid'
    else:
        if lst[0] == lst[1] == lst[2]:
            result = 'Equilateral'
        elif lst[0] == lst[1] or lst[0] == lst[2] or lst[1] == lst[2]:
            result = 'Isosceles'
        else:
            result = 'Scalene'

    print(result)
'''





#2025.01.08

while True:
    s1, s2, s3 = map(int, input().split())

    if s1 == s2 == s3 == 0:
        break
    else:
        side = s1 + s2 + s3
        lst_side = sorted([s1, s2, s3])
        set_side = set(lst_side)

        if lst_side[0] + lst_side[1] <= lst_side[2]:
            print('Invalid')
        else:
            if len(set_side) == 1:
                print('Equilateral')
            elif len(set_side) == 2:
                print('Isosceles')
            elif len(set_side) == 3:
                print('Scalene')





