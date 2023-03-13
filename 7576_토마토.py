# 토마토 7576
from collections import deque
import sys
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs():
    while Q:
        row, col = Q.popleft()
        for k in range(4):
            newR = row + di[k]
            newC = col + dj[k]
            if 0<= newR < N and 0<= newC < M and visited[newR][newC] == 0 and lst[newR][newC] == 0:
                visited[newR][newC] = visited[row][col] + 1
                lst[newR][newC] = 1
                Q.append((newR, newC))

M, N = map(int, sys.stdin.readline().split())

lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
check = 0
to_cnt = 0
Q = deque()

for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            Q.append((i,j))
            visited[i][j] = 1
            lst[i][j] = 1

        elif lst[i][j] == 0:
            to_cnt += 1

if to_cnt == (N*M):
    print(-1)
elif len(Q) == 0:
    print(0)
else:
    bfs()
    for a in range(N):
        if 0 in lst[a]:
            check = -1

    if check == -1:
        print(-1)
    else:
        maxV = 0
        for n in range(N):
            result = max(visited[n])
            if result > maxV:
                maxV = result
        print(maxV-1)


