# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

import sys
M, N = map(int, sys.stdin.readline().split())

if M > 1:
    for num in range(M, N +1):
        count = 0
        for check in range(2, num):
            if num % check == 0:
                count += 1
                break
        if count == 0:
            print(num)
