# 방향: 북(0), 동(1), 남(2), 서(3)
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N, M = map(int, input().split())
r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]  # 청소 여부 체크

cnt = 0

while True:
    # 1. 현재 칸이 청소되지 않았으면 청소
    if visited[r][c] == 0:
        visited[r][c] = 1
        cnt += 1

    cleaned = False #주변 4칸 중 청소되지 않은 빈 칸이 있는지 확인인
    for _ in range(4):
        # 2. 반시계 방향으로 회전
        d = (d + 3) % 4
        nr = r + direction[d][0]
        nc = c + direction[d][1]
        
        # 청소 안 한 빈 칸이면 이동
        if room[nr][nc] == 0 and visited[nr][nc] == 0:
            r, c = nr, nc
            cleaned = True  #주변 4칸 중 청소되지 않은 빈 칸이 있다는 뜻뜻
            break
    
    if not cleaned:
        # 3. 후진
        back_d = (d + 2) % 4
        br = r + direction[back_d][0]
        bc = c + direction[back_d][1]
        # 뒤가 벽이면 종료
        if room[br][bc] == 1:
            break
        else:
            r, c = br, bc

print(cnt)
