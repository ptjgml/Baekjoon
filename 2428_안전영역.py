
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(a, b, i):
    global cnt
    stack.append((a, b))
    while stack:
        si, sj = stack.pop()
        for k in range(4):
            ni = si + dx[k]
            nj = sj + dy[k]

            if 0<= ni < N and 0<= nj < N and visited[ni][nj] == 0 and lst[ni][nj] > i:
                visited[ni][nj] = 1
                stack.append((ni, nj))

    cnt += 1

N = int(input())

lst = [list(map(int,input().split())) for _ in range(N)]
stack = []
cnt = 0
result = 0

for i in range(101):
    visited = [[0]*N for _ in range(N)]
    for a in range(N):
        for b in range(N):
            if lst[a][b] > i and visited[a][b] == 0:
                visited[a][b] = 1
                check(a, b, i)

    if cnt > result:
        result = cnt
    cnt = 0

print(result)