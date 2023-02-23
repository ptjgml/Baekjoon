di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(s_row, s_col):
    global tomato_count
    global day_count

    Q = []





M, N = map(int,input().split())

lst = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
tomato_count = 0
day_count = 0
for i in range(N):
    tomato_count += lst[i].count(0)

for row in range(N):
    for col in range(M):
        if lst[row][col] == 1:
            bfs(row, col)