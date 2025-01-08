# 문제
# 창영이는 삼각형의 종류를 잘 구분하지 못한다. 따라서 프로그램을 이용해 이를 외우려고 한다.
#
# 삼각형의 세 각을 입력받은 다음,
#
# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error
# 를 출력하는 프로그램을 작성하시오.
#
# 입력
# 총 3개의 줄에 걸쳐 삼각형의 각의 크기가 주어진다. 모든 정수는 0보다 크고, 180보다 작다.
#
# 출력
# 문제의 설명에 따라 Equilateral, Isosceles, Scalene, Error 중 하나를 출력한다.


'''
result = 'Error'
dic = {}
sumV = 0
for i in range(3):
    angle = int(input())
    sumV += angle
    if angle in dic:
        dic[angle] += 1
        result = 'Isosceles'
    else:
        dic[angle] = 1
        result = 'Scalene'

if 60 in dic:
    if dic[60] == 3:
        result = 'Equilateral'

if sumV != 180:
    result = 'Error'

print(result)
'''




#2025.01.08

a1 = int(input())
a2 = int(input())
a3 = int(input())

angle = a1 + a2 + a3
set_angle = set([a1, a2, a3])

if angle == 180:
    if len(set_angle) == 1:
        print('Equilateral')
    elif len(set_angle) == 2:
        print('Isosceles')
    elif len(set_angle) == 3:
        print('Scalene')
else:
    print('Error')
