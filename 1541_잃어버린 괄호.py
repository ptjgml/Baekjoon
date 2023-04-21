# 문제
# 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
#
# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
#
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고,
# 가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고,
# 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.
#
# 출력
# 첫째 줄에 정답을 출력한다.

import sys
inputV = sys.stdin.readline()
lst = []

n = ''
for i in inputV:
    if i == '-' or i == '+':
        lst.append(int(n))
        n = ''
        lst.append(i)
    else:
        n += i
lst.append(int(n))

flag = 0
plus = []
minus = []
for j in range(len(lst)):
    if lst[j] == '-':
        flag = 1

    else:
        if flag == 0:
            if lst[j] == '+':
                continue
            else:
                plus.append(int(lst[j]))

        else:
            if type(lst[j]) == int:
                minus.append(int(lst[j]))

# print(plus)
# print(minus)
result = sum(plus) + (-(sum(minus)))
print(result)









# pre = '+'
# cur = '+'
# for j in range(len(lst)):
#     if lst[j] == '-' or lst[j] == '+':
#         pre = cur
#         cur = lst[j]
#         if (pre == '-' and cur == '+'):
#             lst[j] = '-'
#
# # print(lst)
#
# result = int(lst.pop(0))
# while lst:
#     value = lst.pop(0)
#
#     if value == '-':
#         value = int(lst.pop(0))
#         result -= value
#     elif value == '+':
#         value = int(lst.pop(0))
#         result += value
#
# print(result)


