# 문제
# <그림 1>과 같이 정사각형 모양의 지도가 있다.
# 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
# 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
# 대각선상에 집이 있는 경우는 연결된 것이 아니다.
# <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
#
#
#
# 입력
# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
# 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
#
# 출력
# 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def bfs(s_row, s_col):
    global count
    Q.append((s_row, s_col))
    visited[s_row][s_col] = True
    house_cnt = 1

    while Q:
        v_row, v_col = Q.pop(0)
        for k in range(4):
            newR = v_row + di[k]
            newC = v_col + dj[k]
            if 0 <= newR < num and 0 <= newC < num and visited[newR][newC] == False and lst[newR][newC] == 1:
                visited[newR][newC] = True
                Q.append((newR, newC))
                lst[newR][newC] = 0
                house_cnt += 1
    count += 1
    house_cnt_lst.append(house_cnt)

    return count

num = int(input())

lst = [list(map(int, input())) for _ in range(num)]
count = 0
visited = [[False] * num for _ in range(num)]
Q = []
house_cnt_lst = []

for row in range(num):
    for col in range(num):
        if lst[row][col] == 1:
            bfs(row, col)

house_cnt_lst.sort()

print(count)
for j in house_cnt_lst:
    print(j)