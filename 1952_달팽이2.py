# 문제
# M줄
# N칸으로
# 되어
# 있는
# 표
# 위에, 달팽이
# 모양으로
# 선을
# 그리려고
# 한다.
#
# ㅇ
#
# 위의
# 그림은
# M = 5, N = 3
# 의
# 예이다.이제
# 표의
# 왼쪽
# 위
# 칸(ㅇ)
# 에서
# 시작하여, 오른쪽으로
# 선을
# 그려
# 나간다.표의
# 바깥
# 또는
# 이미
# 그려진
# 칸에
# 닿아서
# 더
# 이상
# 이동할
# 수
# 없게
# 되면, 시계방향으로
# 선을
# 꺾어서
# 그려나간다.
#
# ㅇ    →    ↘
# ↗    ↘    ↓
# ↑    ↓    ↓
# ↑    끝    ↓
# ↖    ←    ↙
# 위의
# 표는
# 선을
# 그려
# 나간
# 모양을
# 나타낸
# 것이다.선이
# 꺾어진
# 부분은
# 대각선으로
# 나타내었다.표의
# 모든
# 칸이
# 채워질
# 때까지, 선을
# 몇
# 번
# 꺾게
# 될까?
#
# 입력
# 첫째
# 줄에
# M과
# N이
# 빈
# 칸을
# 사이에
# 두고
# 주어진다.(2 ≤ M, N ≤ 100)
#
# 출력
# 첫째
# 줄에
# 표의
# 모든
# 칸이
# 채워질
# 때까지
# 선이
# 꺾어지는
# 횟수를
# 출력한다.
#
# 예제
# 입력
# 1
# 5
# 3
# 예제
# 출력
# 1
# 5



M, N = map(int, input().split())

visited = [[False] * N for _ in range(M)]
visited[0][0] = True

# →, ↘, ↓, ↙, ←, ↖, ↑, ↗ (시계 방향)
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

x, y = 0, 0
direction = 0
turn_count = 0

while True:
    nx, ny = x + dx[direction], y + dy[direction]

    if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
        # 이동 가능하면 이동
        x, y = nx, ny
        visited[x][y] = True
    else:
        # 이동 불가능하면 방향 바꾸기
        old_direction = direction
        moved = False
        for _ in range(8):
            direction = (direction + 1) % 8
            nx, ny = x + dx[direction], y + dy[direction]
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
                turn_count += 1  # 실제 이동 가능한 방향으로 바꿨을 때만 꺾음 카운트 증가
                moved = True
                break
        if not moved:
            break
        # 이동 가능한 방향 찾았으면 바로 이동
        x, y = nx, ny
        visited[x][y] = True

print(turn_count)



