# 문제
# 차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다. 
# 농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 
# 보호하는 것이 중요하기 때문에, 
# 한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다. 
# 이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다. 
# 특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 
# 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 
# 그 배추들 역시 해충으로부터 보호받을 수 있다. 
# 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.

# 한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다. 
# 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 
# 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 
# 총 몇 마리의 지렁이가 필요한지 알 수 있다. 
# 예를 들어 배추밭이 아래와 같이 구성되어 있으면 
# 최소 5마리의 배추흰지렁이가 필요하다. 
# 0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.

# 1	1	0	0	0	0	0	0	0	0
# 0	1	0	0	0	0	0	0	0	0
# 0	0	0	0	1	0	0	0	0	0
# 0	0	0	0	1	0	0	0	0	0
# 0	0	1	1	0	0	0	1	1	1
# 0	0	0	0	1	0	0	1	1	1
# 입력
# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 
# 그 다음 줄부터 각각의 테스트 케이스에 대해 
# 첫째 줄에는 
# 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 
# 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 
# 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 
# 두 배추의 위치가 같은 경우는 없다.

# 출력
# 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

#
# # bfs + Q 사용
# import sys
# di = [-1, 1, 0, 0]
# dj = [0, 0, -1, 1]
#
# def bfs(s_y, s_x):
#
#     Q.append((s_y, s_x))
#     visited[s_y][s_x] = True
#     check[s_y][s_x] = 0
#     count = 0
#     while Q:
#         v_y, v_x = Q.pop(0)
#         for k in range(4):
#             newR = v_y + di[k]
#             newC = v_x + dj[k]
#
#             if 0 <= newR < N and 0<= newC < M and visited[newR][newC] == False and check[newR][newC] == 1:
#                 Q.append((newR,newC))
#                 visited[newR][newC] = True
#                 check[newR][newC] = 0
#     else:
#         count += 1
#     # if not Q and cabbage:
#     #     v_y, v_x = cabbage.pop(0)
#     #     Q.append((v_y, v_x))
#
#     return count
#
# T = int(sys.stdin.readline())
#
# for t in range(T):
#     M, N, K = map(int, sys.stdin.readline().split())
#
#     # cabbage = []
#     check = [[0] * M for _ in range(N)]
#     count = 0
#     Q = []
#     visited = [[False] * M for _ in range(N)]
#
#     for i in range(K):
#         x, y = map(int, input().split())
#         # cabbage.append((y, x))
#         check[y][x] = 1
#
#     # for i in cabbage:
#     #     y, x = i[0], i[1]
#     #     if check[y][x] == 1:
#     #         count = count + bfs(y, x)
#     for i in range(M):
#         for j in range(N):
#             if check[j][i] == 1:
#                 count = count+bfs(j,i)
#     print(count)
#
#


# 2023.08.25 풀이
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

def check():
    global count, Q
    while Q:
        nowI, nowJ = Q.pop(0)
        for k in range(4):
            newI = nowI + di[k]
            newJ = nowJ + dj[k]
            if 0 <= newI < N and 0 <= newJ < M and lst[newI][newJ] == 1:
                lst[newI][newJ] = 0
                Q.append((newI, newJ))

    count += 1


T = int(input())

for t in range(T):
    M, N, K = map(int, input().split())
    lst = [[0] * M for _ in range(N)]
    # print(lst)
    inputlst = [list(map(int, input().split())) for _ in range(K)]
    # print(inputlst)
    count = 0
    Q = []

    for a in range(K):
        # print(int(inputlst[a][0]))
        lst[inputlst[a][1]][inputlst[a][0]] = 1

    for i in range(N):
        for j in range(M):
            if lst[i][j] == 1:
                Q.append((i, j))
                lst[i][j] = 0
                check()

    print(count)
