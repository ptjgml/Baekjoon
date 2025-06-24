N = int(input())
room = [list(input()) for _ in range(N)]

row_cnt = 0
col_cnt = 0

for i in range(N):
    rcnt = ccnt = 0
    for j in range(N):
        # 가로 방향
        if room[i][j] == '.':
            rcnt += 1
        else:
            if rcnt >= 2:
                row_cnt += 1
            rcnt = 0
        if j == N - 1 and rcnt >= 2:
            row_cnt += 1

        # 세로 방향
        if room[j][i] == '.':
            ccnt += 1
        else:
            if ccnt >= 2:
                col_cnt += 1
            ccnt = 0
        if j == N - 1 and ccnt >= 2:
            col_cnt += 1

print(row_cnt, col_cnt)
