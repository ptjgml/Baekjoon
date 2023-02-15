C, R = map(int, input().split())
K = int(input())

# di = [-1, 0, 1, 0]
# dj = [0, 1, 0, -1]
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]



if K > (C*R):
    result = 0

else:
    row = 1
    col = 1
    i = 0
    row_start = 1
    row_end = R
    col_start = 1
    col_end = C
    while True:
        newR = row + di[i]
        newC = col + dj[i]

        if row_start <= newR < row_end and col_start <= newC < col_end:
            K -= 1
            row = newR
            col = newC

        elif newR == R :
            i += 1
            row_start += 1
            row_end -= 1
            K -= 1
            row = newR
            col = newC

        elif newC == C:
            i+= 1
            col_start += 1
            col_end -= 1
            K -= 1
            row = newR
            col = newC

        if i == 4:
            i = 0

        if K == 0:
            break


    result = (row, col)

print(result)







# C, R = map(int, input().split())
# K = int(input())
#
# di = [0, 0, -1, 1]
# dj = [1, -1, 0, 0]
#
# if K > (C * R):
#     result = 0
#
# else:
#     row = 0
#     col = 0
#     ARR = [[0] * C for _ in range(R)]
#     d = 0
#
#     for n in range(1, K+1):
#         ARR[row][col] = n
#         newR = row + di[d]
#         newC = col + dj[d]
#
#         if newR < 0 or newR >= R or newC >= C or ARR[newR][newC] != 0:
#             d = (d+1)%4
#
#             K -= 1
#             row = row + di[d]
#             col = col + dj[d]
#
#         # elif newR == R:
#         #     i += 1
#         #     row_start += 1
#         #     row_end -= 1
#         #     K -= 1
#         #     row = newR
#         #     col = newC
#         #
#         # elif newC == C:
#         #     i += 1
#         #     col_start += 1
#         #     col_end -= 1
#         #     K -= 1
#         #     row = newR
#         #     col = newC
#         #
#         # if i == 4:
#         #     i = 0
#         #
#         # if K == 0:
#         #     break
#
#     result = (row, col)
#
# print(result)
#
#





#
#
# T = int(input())
#
# for t in range(T):
#     N = int(input())
#     row = 0
#     col = 0
#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]
#     ARR = [[0] * N for _ in range(N)]
#
#     d = 0
#     for i in range(1, N*N+1):
#         ARR[row][col] = i
#         newR = row + dr[d]
#         newC = col + dc[d]
#         if newR < 0 or newR >= N or newC >= N or ARR[newR][newC] != 0:
#             d = (d+1) % 4
#         row = row + dr[d]
#         col = col + dc[d]
#
#     print(f'#{t+1}')
#     for j in range(N):
#         for k in range(N):
#             print(f'{ARR[j][k]}', end=' ')
#         print()















