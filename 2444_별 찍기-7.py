# 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
#
# 출력
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

'''
import sys

N = int(sys.stdin.readline())
for i in range(2 * N - 1):
    tmp = abs(i - N + 1)
    print(' ' * tmp + '*' * (2 *(N - tmp) - 1))
'''



#2024.12.20

import sys

N = int(sys.stdin.readline())
for i in range(2 * N - 1):
    tmp = abs(i - N + 1)
    print(' ' * tmp + '*' * (2 *(N - tmp) - 1))