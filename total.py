# 토마토 7576
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(row, col):

    Q.append((row, col))
    visited[row][col] = 1
    lst[row][col] = 1

    while Q:
        row, col = Q.pop(0)
        for k in range(4):
            newR = row + di[k]
            newC = col + dj[k]
            if 0<= newR < N and 0<= newC < M and visited[newR][newC] == 0 and lst[newR][newC] == 0 and lst[row][col] == 1:
                visited[newR][newC] = visited[row][col] + 1
                lst[newR][newC] = 1
                Q.append((newR, newC))


M, N = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
check = 0
to_cnt = 0
Q = []

for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            Q.append((i,j))
        elif lst[i][j] == 0:
            to_cnt += 1

if to_cnt == (N*M):
    print(-1)
elif len(Q) == 0:
    print(0)
else:
    for n in range(len(Q)):
        bfs(Q[n][0], Q[n][1])

    for a in range(N):
        if 0 in lst[a]:
            check = -1

    if check == -1:
        print(-1)
    else:
        print(max(max(visited))-1)

print(visited)



