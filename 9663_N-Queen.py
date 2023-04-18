# 문제
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
#
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)
#
# 출력
# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

import sys

def per(idx):
    global cnt

    if idx == N:
        cnt += 1
        return

    for i in range(N):
            p[idx] = i
            if check(p, idx) == True:
                per(idx+1)
                # p[idx] = -99

def check(p, idx):
    for k in range(0, idx):
        if p[idx] == p[k] or abs(p[idx] - p[k]) == abs(idx-k):
            return False
    return True

N = int(sys.stdin.readline())

cnt = 0
p = [-99] * N

per(0)
print(cnt)
