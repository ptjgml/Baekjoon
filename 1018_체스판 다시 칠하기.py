# 문제
# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다.
# 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다.
# 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.
#
# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다.
# 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고,
# 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.
# 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다.
# 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
#
# 보드가 체스판처럼 칠해져 있다는 보장이 없어서,
# 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
# 당연히 8*8 크기는 아무데서나 골라도 된다.
# 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다.
# 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.
#
# 출력
# 첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.


'''
def first_B(i, j, cnt, check_board):
    if check_board[i][j] == 'W':
        cnt += 1
    check_board[i][j] = 'B'
    return check(i, j, cnt, check_board)


def first_W(i, j, cnt, check_board):
    if check_board[i][j] == 'B':
        cnt += 1
    check_board[i][j] = 'W'
    return check(i, j, cnt, check_board)


def check(i, j, cnt, check_board):
    for n in range(i, i + 8):
        for m in range(j, j + 8):
            for k in range(4):
                newR = n + di[k]
                newC = m + dj[k]

                if check_board[n][m] == 'B':  # 내가 'B'인데
                    if i <= newR < i + 8 and j <= newC < j + 8:
                        if check_board[newR][newC] == 'B':  # 내 상하좌우에 'B'가 있으면
                            cnt += 1  # new_count +1
                            check_board[newR][newC] = 'W'  # 중복되어 계산되지 않도록 'W'로 바꿔줌

                else:
                    if i <= newR < i + 8 and j <= newC < j + 8:
                        if check_board[newR][newC] == 'W':
                            cnt += 1
                            check_board[newR][newC] = 'B'

    return cnt

import copy
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]
check_board = copy.deepcopy(board)      # deepcopy 이용하여 원래 입력받은 board 건들이지 않음

count = 64

for i in range(0, N - 8 + 1):
    for j in range(0, M - 8 + 1):
        check_board = copy.deepcopy(board)      # deepcopy 이용하여 원래 입력받은 board 건들이지 않음
        result1 = first_B(i, j, 0, check_board)
        check_board = copy.deepcopy(board)
        result2 = first_W(i, j, 0, check_board)

        if count > min(result1, result2):
            count = min(result1, result2)

print(count)
'''




#2025.01.15
def start_W(i, j, cnt, check_board):
    if check_board[i][j] == 'B':
        cnt += 1
        check_board[i][j] = 'W'
    return check(i, j, cnt, check_board)

def start_B(i, j, cnt, check_board):
    if check_board[i][j] == 'W':
        cnt += 1
        check_board[i][j] = 'B'
    return check(i, j, cnt, check_board)

def check(i, j, cnt, check_board):

    for a in range(i, i+8):
        for b in range(j, j+8):
            for k in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_a = a + k[0]
                new_b = b + k[1]

                if check_board[a][b] == 'B':
                    if i <= new_a < i+8 and j <= new_b < j+8:
                        if check_board[new_a][new_b] == 'B':
                            cnt += 1
                            check_board[new_a][new_b] = 'W'

                if check_board[a][b] == 'W':
                    if i <= new_a < i+8 and j <= new_b < j+8:
                        if check_board[new_a][new_b] == 'W':
                            cnt += 1
                            check_board[new_a][new_b] = 'B'

    return cnt


import copy

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
result = 10e9

for i in range(0, N-8+1):
    for j in range(0, M-8+1):
        check_board = copy.deepcopy(board)
        result1 = start_W(i, j, 0, check_board)
        check_board = copy.deepcopy(board)
        result2 = start_B(i, j, 0, check_board)

        result = min(result, result1, result2)

print(result)
