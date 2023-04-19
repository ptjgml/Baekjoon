# 문제
# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다.
# 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다.
# 지민이는 이 보드를 잘라서 K×K 크기의 체스판으로 만들려고 한다.
#
# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다.
# 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고,
# 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.
# 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다.
# 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
#
# 보드가 체스판처럼 칠해져 있다는 보장이 없어서,
# 지민이는 K×K 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
# 당연히 K×K 크기는 아무데서나 골라도 된다.
# 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정수 N, M, K가 주어진다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다.
# B는 검은색이며, W는 흰색이다.
#
# 출력
# 첫째 줄에 지민이가 잘라낸 K×K 보드를 체스판으로 만들기 위해 다시 칠해야 하는
# 정사각형 개수의 최솟값을 출력한다.


# import sys
#
# di = [-1, 1, 0, 0]
# dj = [0, 0, -1, 1]
#
# def start_B(new_board, i, j, cnt):
#     if new_board[i][j] == 'W':
#         cnt += 1
#     return check(new_board, i, j, cnt, 'B')
#
# def start_W(new_board, i, j, cnt):
#     if new_board[i][j] == 'B':
#         cnt += 1
#     return check(new_board, i, j, cnt, 'W')
#
# def check(new_board, i, j, cnt, first):
#     global minV
#
#     visited = [[False] * M for _ in range(N)]
#     visited[i][j] = first
#
#     for row in range(i,i+K):
#         for col in range(j, j+K):
#             for n in range(4):
#                 if cnt >= minV:
#                     return
#                 new_row = row+di[n]
#                 new_col = col+dj[n]
#
#                 if visited[row][col] == 'B':
#                     if i <= new_row < i + K and j <= new_col < j + K and visited[new_row][new_col] == False:
#                         if new_board[new_row][new_col] == 'B':
#                             cnt += 1
#                         visited[new_row][new_col] = 'W'
#
#                 elif visited[row][col] == 'W':
#                     if i <= new_row < i + K and j <= new_col < j + K and visited[new_row][new_col] == False:
#                         if new_board[new_row][new_col] == 'W':
#                             cnt += 1
#                         visited[new_row][new_col] = 'B'
#
#     minV = min(cnt, minV)
#
# N, M, K = map(int, sys.stdin.readline().split())
# board = [list(sys.stdin.readline()) for _ in range(N)]
# minV = 100
#
# for i in range(0, N-K+1):
#     for j in range(0, M-K+1):
#         start_B(board, i, j, 0)
#         start_W(board, i, j, 0)
#
# print(minV)




N, M, K = map(int, input().split())
board = [list(input()) for _ in range(N)]

lst_black = [[0]*(M+1) for _ in range(N+1)]
lst_white = [[0]*(M+1) for _ in range(N+1)]
sum_lst_black = [[0]*(M+1) for _ in range(N+1)]
sum_lst_white = [[0]*(M+1) for _ in range(N+1)]
minV = 10e9

for i in range(1, N+1):
    for j in range(1, M+1):
        if (i+j) % 2 == 0:
            if 'B' != board[i-1][j-1]:
                lst_black[i][j] = int(not lst_black[i][j])

            if 'W' != board[i-1][j-1]:
                lst_white[i][j] = int(not lst_white[i][j])

        else:
            if 'B' == board[i-1][j-1]:
                lst_black[i][j] = int(not lst_black[i][j])

            if 'W' == board[i-1][j-1]:
                lst_white[i][j] = int(not lst_white[i][j])

        sum_lst_black[i][j] = sum_lst_black[i][j - 1] + sum_lst_black[i - 1][j] - sum_lst_black[i - 1][j - 1] + lst_black[i][j]
        sum_lst_white[i][j] = sum_lst_white[i][j - 1] + sum_lst_white[i - 1][j] - sum_lst_white[i - 1][j - 1] + lst_white[i][j]

for a in range(1, N - K + 2):
    for b in range(1, M - K + 2):
        minV = min(minV, sum_lst_black[a+K-1][b+K-1] - sum_lst_black[a+K-1][b-1] - sum_lst_black[a-1][b+K-1] + sum_lst_black[a-1][b-1],
                   sum_lst_white[a+K-1][b+K-1] - sum_lst_white[a+K-1][b-1] - sum_lst_white[a-1][b+K-1] + sum_lst_white[a-1][b-1])


print(minV)
#
# for k in range(N+1):
#     print(*sum_lst_white[k])
# print()
# for l in range(N+1):
#     print(*sum_lst_black[l])






























