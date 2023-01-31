# 달팽이
# 높이가 V인 나무를 올라가는데
# 낮에 A미터 올라가고, 밤에 B미터 내려간다.
# 정상에 올라간 후에는 미끄러지지 않는다 
# 달팽이가 나무 막대를 모두 올라가려면, 며칠이 거리는지 구하라
# 입력
# 첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)

# 출력
# 첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.


from sys import stdin
import math
A, B, V = map(int, stdin.readline().split())

total = 0
day = 0
today = A-B

day = math.ceil((V - A)/today) + 1
print(day)

