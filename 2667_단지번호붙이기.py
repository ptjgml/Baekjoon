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