# 토마토 7576
from collections import deque
import sys
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(row, col):

    deque.append((row, col))
    visited[row][col] = 1
    lst[row][col] = 1

    while deque:
        row, col = deque.pop(0)
        for k in range(4):
            newR = row + di[k]
            newC = col + dj[k]
            if 0<= newR < N and 0<= newC < M and visited[newR][newC] == 0 and lst[newR][newC] == 0 and lst[row][col] == 1:
                visited[newR][newC] = visited[row][col] + 1
                lst[newR][newC] = 1
                deque.append((newR, newC))


M, N = map(int, sys.stdin.readline().split())

lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
check = 0
to_cnt = 0
deque = []

for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            deque.append((i,j))
        elif lst[i][j] == 0:
            to_cnt += 1

if to_cnt == (N*M):
    print(-1)
elif len(deque) == 0:
    print(0)
else:
    bfs(deque[0][0], deque[0][1])

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



