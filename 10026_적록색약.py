# 문제
# 적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.
#
# 크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)
#
# 예를 들어, 그림이 아래와 같은 경우에
#
# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR
# 적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)
#
# 그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)
#
# 둘째 줄부터 N개 줄에는 그림이 주어진다.
#
# 출력
# 적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def no(i, j, color):
    global no_cnt

    no_stack.append((i, j))
    while no_stack:
        now_i, now_j = no_stack.pop()
        for k in range(4):
            new_i = now_i + di[k]
            new_j = now_j + dj[k]
            if 0 <= new_i < N and 0 <= new_j < N and no_visited[new_i][new_j] == False and lst[new_i][new_j] == color:
                no_stack.append((new_i, new_j))
                no_visited[new_i][new_j] = True

    no_cnt += 1



def yes(i, j, color):
    global yes_cnt

    yes_stack.append((i, j))
    while yes_stack:
        now_a, now_b = yes_stack.pop()
        for k in range(4):
            new_a = now_a + di[k]
            new_b = now_b + dj[k]
            if 0 <= new_a < N and 0 <= new_b < N and yes_visited[new_a][new_b] == False and (lst[new_a][new_b] == color or (lst[new_a][new_b] == 'R' and color == 'G') or (lst[new_a][new_b] == 'G' and color == 'R')):
                yes_stack.append((new_a, new_b))
                yes_visited[new_a][new_b] = True

    yes_cnt += 1

N = int(input())

lst = [list(input()) for _ in range(N)]

no_visited  = [[False]*N for _ in range(N)]
no_stack = []
no_cnt = 0

yes_visited  = [[False]*N for _ in range(N)]
yes_stack = []
yes_cnt = 0

for i in range(N):
    for j in range(N):
        if no_visited[i][j] == False:
            no_visited[i][j] = True
            no(i, j, lst[i][j])


for a in range(N):
    for b in range(N):
        if yes_visited[a][b] == False:
            yes_visited[a][b] = True
            yes(a, b, lst[a][b])


print(no_cnt, yes_cnt)