# 문제
# 크기가 N×N인 지도가 있다. 지도의 각 칸에는 그 곳의 높이가 적혀져 있다.
#
# 오늘은 이 지도에서 지나갈 수 있는 길이 몇 개 있는지 알아보려고 한다. 길이란 한 행 또는 한 열 전부를 나타내며, 한쪽 끝에서 다른쪽 끝까지 지나가는 것이다.
#
# 다음과 같은 N=6인 경우 지도를 살펴보자.
#
#
#
# 이때, 길은 총 2N개가 있으며, 아래와 같다.
#
#
#
# 길을 지나갈 수 있으려면 길에 속한 모든 칸의 높이가 모두 같아야 한다. 또는, 경사로를 놓아서 지나갈 수 있는 길을 만들 수 있다.
# 경사로는 높이가 항상 1이며, 길이는 L이다. 또, 개수는 매우 많아 부족할 일이 없다. 경사로는 낮은 칸과 높은 칸을 연결하며, 아래와 같은 조건을 만족해야한다.
#
# 경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.
# 낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
# 경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 한다.
# 아래와 같은 경우에는 경사로를 놓을 수 없다.
#
# 경사로를 놓은 곳에 또 경사로를 놓는 경우
# 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
# 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
# 경사로를 놓다가 범위를 벗어나는 경우
# L = 2인 경우에 경사로를 놓을 수 있는 경우를 그림으로 나타내면 아래와 같다.
#
#
# 경사로를 놓을 수 없는 경우는 아래와 같다.
#
#
# 위의 그림의 가장 왼쪽부터 1번, 2번, 3번, 4번 예제라고 했을 때, 1번은 높이 차이가 1이 아니라서, 2번은 경사로를 바닥과 접하게 놓지 않아서, 3번은 겹쳐서 놓아서, 4번은 기울이게 놓아서 불가능한 경우이다.
#
# 가장 위에 주어진 그림 예의 경우에 지나갈 수 있는 길은 파란색으로, 지나갈 수 없는 길은 빨간색으로 표시되어 있으며, 아래와 같다. 경사로의 길이 L = 2이다.
#
#
#
# 지도가 주어졌을 때, 지나갈 수 있는 길의 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N (2 ≤ N ≤ 100)과 L (1 ≤ L ≤ N)이 주어진다. 둘째 줄부터 N개의 줄에 지도가 주어진다. 각 칸의 높이는 10보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄에 지나갈 수 있는 길의 개수를 출력한다.

# def check(one):
#     global result
#     slide = [False] * N
#     for i in range(N-1):
#
#         if abs(one[i] - one[i+1]) > 1:
#             result -= 1
#             return
#
#         elif i > 0 and L > 1 and one[i-1] != one[i] and one[i] != one[i+1]:
#             result -= 1
#             return
#
#         elif i>0 and L == 1 and one[i-1] != one[i] and one[i] != one[i+1]:
#             if (one[i-1] > one[i] and one[i] < one[i+1]) or (one[i-1] < one[i] and one[i] > one[i+1]):
#                 result -= 1
#                 return
#
#         elif one[i] != one[i+1]:
#             if one[i] > one[i+1]:
#                 if one[i+1:i+L+1].count(one[i+1]) >= L:
#                     continue
#                 else:
#                     result -= 1
#                     return
#             else:
#                 if one[i-L+1 : i+1].count(one[i]) >= L:
#                     continue
#                 else:
#                     result -= 1
#                     return
#
#
# N, L = map(int, input().split())
# map_lst = [list(map(int, input().split())) for _ in range(N)]
#
# result = 2*N
# for i in range(N):
#     row = map_lst[i]
#     print('row : ', row)
#     check(row)
#     print('result : ', result)
# print(result)
#
# print()
# for b in range(N):
#     col = []
#     for a in range(N):
#         col.append(map_lst[a][b])
#     print('col : ', col)
#     check(col)
#     print('result : ', result)
#
# print(result)




<<<<<<< HEAD
=======
# # 반례
# 6 1
# 3 3 3 3 3 3
# 3 3 4 3 3 3
# 2 3 3 3 3 3
# 2 2 3 4 3 2
# 2 3 3 4 3 2
# 3 3 3 3 3 2
# ---> 답 : 11



# 6 1
# 4 4 4 5 5 4
# 3 3 4 4 4 3
# 2 3 3 4 3 2
# 2 3 4 4 3 2
# 3 4 4 4 3 3
# 4 4 4 4 4 4
# ---> 답: 11



# 6 1
# 4 4 4 4 3 3
# 4 4 4 4 3 4
# 4 4 4 4 4 4
# 3 3 4 4 4 3
# 3 4 5 5 4 3
# 3 4 5 4 3 3
# ---> 답 : 10




# 7 1
# 3 3 4 4 4 4 3
# 2 3 3 3 3 3 2
# 2 2 3 2 2 2 2
# 3 3 3 2 2 3 3
# 4 3 3 3 3 4 4
# 4 4 4 3 4 4 4
# 4 4 4 4 4 4 4
# ---> 답: 11



# 6 1
# 4 4 4 4 3 3
# 4 4 4 4 4 4
# 3 3 3 4 3 3
# 2 2 3 3 2 2
# 2 2 2 2 2 2
# 2 3 3 3 3 3
# ---> 답 : 10




# 5 1
# 4 4 4 4 4
# 3 3 4 3 3
# 3 4 3 3 3
# 4 4 3 3 3
# 4 4 3 4 4
# ---> 답 : 8




# 5 1
# 6 6 5 3 4
# 6 5 4 4 5
# 4 4 3 3 4
# 3 4 3 4 3
# 4 5 5 4 3
# ---> 답 : 5


# 6 1
# 5 3 3 4 6 6
# 5 4 3 4 6 6
# 4 3 3 4 5 5
# 3 3 3 4 4 4
# 3 3 3 3 4 4
# 5 3 3 4 5
# ---> 답 : 7


# 5 1
# 4 4 4 4 4
# 3 3 3 3 3
# 4 4 4 3 4
# 5 5 5 5 5
# 5 6 5 5 5
# ---> 답 : 4



# 6 1
# 4 5 5 4 3 3
# 4 4 4 3 3 3
# 3 3 3 3 2 2
# 3 4 3 3 3 2
# 4 4 4 4 3 3
# 4 5 5 4 3 3
# ---> 답 : 10



# 3 1
# 3 2 3
# 2 3 2
# 3 2 3
# ---> 답 : 2   내리막 완성 후 이후의 잠재적인 오르막까지 체크를 해야하는데 잘못 처리한 경우



>>>>>>> 6680d50d5f5bc5559973eb4393c1917a36f77fd1

def check(one):
    global result
    slide = [0] * N
<<<<<<< HEAD
    print('slide : ', slide)
    for i in range(N-1):

=======
    # print('slide : ', slide)
    for i in range(N-1):
>>>>>>> 6680d50d5f5bc5559973eb4393c1917a36f77fd1
        if abs(one[i] - one[i+1]) > 1:
            result -= 1
            return

<<<<<<< HEAD
        elif i > 0 and (one[i-1] > one[i] and one[i] > one[i+1]) or (one[i-1] < one[i] and one[i] < one[i+1]):
=======
        elif i > 0 and ((one[i-1] > one[i] and one[i] > one[i+1]) or (one[i-1] < one[i] and one[i] < one[i+1])):
>>>>>>> 6680d50d5f5bc5559973eb4393c1917a36f77fd1
            if L != 1:
                result -= 1
                return

<<<<<<< HEAD
        elif i > 0 and L == 1 and (one[i-1] > one[i] and one[i] < one[i+1]) or (one[i-1] < one[i] and one[i] > one[i+1]):
=======
        elif i > 0 and L == 1 and (one[i-1] > one[i] and one[i] < one[i+1]):
>>>>>>> 6680d50d5f5bc5559973eb4393c1917a36f77fd1
                result -= 1
                return

        # elif i > 0 and L > 1 and one[i-1] != one[i] and one[i] != one[i+1]:
        #     result -= 1
        #     return

        elif one[i] != one[i+1]:
            if one[i] > one[i+1]:
                if one[i+1:i+L+1].count(one[i+1]) >= L:
                    for j in range(i+1, i+L+1):
                        if slide[j] == 1:
                            result -= 1
                            return
                        slide[j] = 1
                    continue
                else:
                    result -= 1
                    return
            else:
                if one[i-L+1 : i+1].count(one[i]) >= L:
                    for j in range(i-L+1, i+1):
                        if slide[j] == 1:
                            result -= 1
                            return
                        slide[j] = 1

                    continue
                else:
                    result -= 1
                    return


N, L = map(int, input().split())
map_lst = [list(map(int, input().split())) for _ in range(N)]

result = 2*N
<<<<<<< HEAD
for i in range(N):
    row = map_lst[i]
    print('row : ', row)
    check(row)
    print('result : ', result)
    print()
print(result)

print()
=======
for ii in range(N):
    row = map_lst[ii]
    # print('row : ', row)
    check(row)
#     print('result : ', result)
#     print()
# print(result)
#
# print()
>>>>>>> 6680d50d5f5bc5559973eb4393c1917a36f77fd1
for b in range(N):
    col = []
    for a in range(N):
        col.append(map_lst[a][b])
<<<<<<< HEAD
    print('col : ', col)
    check(col)
    print('result : ', result)
=======
    # print('col : ', col)
    check(col)
    # print('result : ', result)
>>>>>>> 6680d50d5f5bc5559973eb4393c1917a36f77fd1

print(result)




















<<<<<<< HEAD



=======
>>>>>>> 6680d50d5f5bc5559973eb4393c1917a36f77fd1

