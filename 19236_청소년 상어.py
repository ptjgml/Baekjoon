# 문제
# 아기 상어가 성장해 청소년 상어가 되었다.

# 4×4크기의 공간이 있고, 
# 크기가 1×1인 정사각형 칸으로 나누어져 있다. 
# 공간의 각 칸은 (x, y)와 같이 표현하며, 
# x는 행의 번호, y는 열의 번호이다. 
# 한 칸에는 물고기가 한 마리 존재한다. 
# 각 물고기는 번호와 방향을 가지고 있다. 
# 번호는 1보다 크거나 같고, 
# 16보다 작거나 같은 자연수이며, 
# 두 물고기가 같은 번호를 갖는 경우는 없다. 
# 방향은 8가지 방향(상하좌우, 대각선) 중 하나이다.

# 오늘은 청소년 상어가 이 공간에 들어가 
# 물고기를 먹으려고 한다. 
# 청소년 상어는 (0, 0)에 있는 물고기를 먹고, 
# (0, 0)에 들어가게 된다. 
# 상어의 방향은 (0, 0)에 있던 물고기의 방향과 같다. 
# 이후 물고기가 이동한다.

# 물고기는 번호가 작은 물고기부터 순서대로 이동한다. 
# 물고기는 한 칸을 이동할 수 있고, 
# 이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸,
#  이동할 수 없는 칸은 상어가 있거나, 
# 공간의 경계를 넘는 칸이다. 
# 각 물고기는 방향이 이동할 수 있는 칸을 
# 향할 때까지 방향을 45도 반시계 회전시킨다.
#  만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 
# 그 외의 경우에는 그 칸으로 이동을 한다. 
# 물고기가 다른 물고기가 있는 칸으로 이동할 때는 
# 서로의 위치를 바꾸는 방식으로 이동한다.

# 물고기의 이동이 모두 끝나면 상어가 이동한다. 
# 상어는 방향에 있는 칸으로 이동할 수 있는데, 
# 한 번에 여러 개의 칸을 이동할 수 있다. 
# 상어가 물고기가 있는 칸으로 이동했다면, 
# 그 칸에 있는 물고기를 먹고, 
# 그 물고기의 방향을 가지게 된다. 
# 이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않는다. 
# 물고기가 없는 칸으로는 이동할 수 없다. 
# 상어가 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로 간다. 
# 상어가 이동한 후에는 다시 물고기가 이동하며, 
# 이후 이 과정이 계속해서 반복된다.



# <그림 1>

# <그림 1>은 청소년 상어가 공간에 들어가기 전 초기 상태이다. 상어가 공간에 들어가면 (0, 0)에 있는 7번 물고기를 먹고, 상어의 방향은 ↘이 된다. <그림 2>는 상어가 들어간 직후의 상태를 나타낸다.



# <그림 2>

# 이제 물고기가 이동해야 한다. 1번 물고기의 방향은 ↗이다. ↗ 방향에는 칸이 있고, 15번 물고기가 들어있다. 물고기가 있는 칸으로 이동할 때는 그 칸에 있는 물고기와 위치를 서로 바꿔야 한다. 따라서, 1번 물고기가 이동을 마치면 <그림 3>과 같아진다.



# <그림 3>

# 2번 물고기의 방향은 ←인데, 그 방향에는 상어가 있으니 이동할 수 없다. 방향을 45도 반시계 회전을 하면 ↙가 되고, 이 칸에는 3번 물고기가 있다. 물고기가 있는 칸이니 서로 위치를 바꾸고, <그림 4>와 같아지게 된다.



# <그림 4>

# 3번 물고기의 방향은 ↑이고, 존재하지 않는 칸이다. 45도 반시계 회전을 한 방향 ↖도 존재하지 않으니, 다시 회전을 한다. ← 방향에는 상어가 있으니 또 회전을 해야 한다. ↙ 방향에는 2번 물고기가 있으니 서로의 위치를 교환하면 된다. 이런 식으로 모든 물고기가 이동하면 <그림 5>와 같아진다.



# <그림 5>

# 물고기가 모두 이동했으니 이제 상어가 이동할 순서이다. 상어의 방향은 ↘이고, 이동할 수 있는 칸은 12번 물고기가 있는 칸, 15번 물고기가 있는 칸, 8번 물고기가 있는 칸 중에 하나이다. 만약, 8번 물고기가 있는 칸으로 이동하면, <그림 6>과 같아지게 된다.



# <그림 6>

# 상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 구해보자.

# 입력
# 첫째 줄부터 4개의 줄에 각 칸의 들어있는 물고기의 정보가 1번 행부터 순서대로 주어진다. 물고기의 정보는 두 정수 ai, bi로 이루어져 있고, ai는 물고기의 번호, bi는 방향을 의미한다. 방향 bi는 8보다 작거나 같은 자연수를 의미하고, 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 의미한다.

# 출력
# 상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 출력한다.


'''
arr = [list(map(int, input().split())) for _ in range(4)]
check_arr = [[(arr[i][j], arr[i][j+1]) for j in range(0, 8, 2)] for i in range(4)]
fish_arr = [(0, 0, 0)] * 17 #각 물고기별로 (현재 행, 현재 열, 방향) 저장
dir_arr = [(), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1),(0, 1), (-1, 1)] #각 방향별 행, 열 이동


for i in range(4):
    for j in range(0, 8, 2):
        fish_arr[arr[i][j]] = (i, j//2, arr[i][j+1])

shark = (0, 0, arr[0][1])
fish_arr[arr[0][1]] = -1
shark_eaten = arr[0][0]

while True:
    for num in range(1, 17):
        now_d = fish_arr[i][2]
        new_r = fish_arr[i][0] + dir_arr[now_d][0]
        new_c = fish_arr[i][0] + dir_arr[now_d][1]

        if 0 <= new_r < 4 and 0 <= new_c < 4 and check_arr[new_r][new_c] != -1:
            new_fish = check_arr[new_r][new_c][0]
            temp = fish_arr[new_fish]
            fish_arr[new_fish] = fish_arr[i]
            fish_arr[i] = temp
        else:
            for n in range(now_d+1, 9):

    
print(fish_arr)
'''



# arr = [list(map(int, input().split())) for _ in range(4)]

di = [5, -1, -1, 0, 1, 1, 1, 0, -1]
dj = [5, 0, -1, -1, -1, 0, 1, 1, 1]

def find(idx, visited):
    for i in range(4):
        for j in range(4):
            if visited[i][j][0] == idx:
                return i, j, visited[i][j][1]

def dfs(shark_r, shark_c, shark_dir, shark_eaten, visited):
    global ans

    #정답 갱신
    ans = max(ans, shark_eaten)

    #[2].1~16번 물고기 이동
    for idx in range(1, 17):
        fish_r, fish_c, fish_dir = find(idx, visited)

        if fish_dir == -1:  #물고기가 없는 경우
            continue
        for j in range(8):  #현재 방향부터 8방향 체크
            direction = (fish_dir + j - 1) % 8 + 1
            if direction == 0:
                direction = 8
            new_r, new_c = fish_r + di[direction], fish_c + dj[direction]

            if 0 <= new_r < 4 and 0 <= new_c < 4 and (new_r, new_c) != (shark_r, shark_c):  #범위내이고 상어가 아니면
                visited[fish_r][fish_c][1] = direction    #회전한 후의 방향 적용
                visited[fish_r][fish_c], visited[new_r][new_c] = visited[new_r][new_c], visited[fish_r][fish_c] #현재 물고기 위치와 갈 수 있는 위치 교환
                break
        
    #[3].상어 이동(1칸 ~ 3칸) : 범위내이고 빈칸 아니면 이동
    for mul in range(1, 4):
        next_r, next_c = shark_r + di[shark_dir] * mul, shark_c + dj[shark_dir] * mul

        if 0 <= next_r < 4 and 0<= next_c < 4 and visited[next_r][next_c][1] != -1:
            fish_n, fish_d = visited[next_r][next_c]
            visited[next_r][next_c][1] = -1
            new_visited = [[x[:] for x in lst] for lst in visited]

            dfs(next_r, next_c, fish_d, shark_eaten+fish_n, new_visited)
            visited[next_r][next_c][1] = fish_d



#[0]. 물고기 입력받기, visited 초기화화
visited = [[[0] * 2 for _ in range(4)] for _ in range(4)]

for i in range(4):
    fish_lst = list(map(int, input().split()))
    for j in range(4):
        visited[i][j] = [fish_lst[j*2], fish_lst[j*2+1]]


#[1]. 상어가 (0,0) 물고기 먹음
ans = 0
zfish_num, zfish_dir = visited[0][0]    #(0,0) 물고기 번호와 방향향
visited[0][0][1] = -1   #(0, 0) 위치 물고기 먹기 처리 -> 물고기 방향 -1로 처리리해서 먹혔음을 표시
dfs(0, 0, zfish_dir, zfish_num, visited)  #상어의 행 위치, 상어의 열 위치, 상어의 방향, 상어가 지금까지 먹은 물고기 합, visited
print(ans)