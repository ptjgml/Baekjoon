# 문제
# W대학교 미술대학 조소과에서는 지루한 목판화 작업을 하는 학생들을 돕기 위해 판화 기계를 제작하였다.

# 기계는 로봇 팔이 쥔 조각도를 상하좌우 네 방향으로 움직일 수 있는 구조로서, 조각도 아래에 목판을 놓으면 그 위에 선들을 자동으로 그어주는 기능을 가지고 있다.

# 목판에는 N2개의 점들이 일정한 간격으로 N행 N열의 격자모양을 이루며 찍혀있다. 처음 로봇의 조각도를 올려놓는 위치는 항상 이 점들 중 맨 왼쪽 맨 위의 꼭짓점이다.

# 로봇 팔을 움직이는 명령의 순서가 주어졌을 때, 목판 위에 패인 조각도의 혼적을 출력하는 프로그램을 작성하시오.

# 판화 기계는 작동 도중 로봇 팔이 격자 바깥으로 나가도록 하는 움직임 명령을 만나면, 무시하고 그 다음 명령을 진행한다.

# 입력
# 첫째 줄에 목판의 크기 N (2 ≤ N ≤ 10)이 주어진다. 행 열의 점들이 찍혀 있다는 의미이다. 둘째 줄에 로봇팔의 움직임이 한 줄로 공백 없이 입력된다. 위쪽으로 이동은 'U', 아래쪽으로 이동은 'D', 왼쪽으로 이동은 'L', 오른쪽으로 이동은 'R'로 표시된다. 로봇팔의 움직임을 나타내는 이 문자열의 길이는 최대 250이다.

# 출력
# 로봇팔이 지나지 않은 점은 '.'으로, 로봇팔이 수직 방향으로만 지난 점은 '|'으로, 로봇팔이 수평 방향으로만 지난 점은 '-'으로, 수직과 수평 방향 모두로 지난 점은 '+'로 표기하도록 한다. 네 문자의 ASCII 코드는 각각 46, 124, 45, 43이다.

# 예제 입력 1 
# 5
# DRDRRUU
# 예제 출력 1 
# |..|.
# ++.|.
# .+-+.
# .....
# .....
# 예제 입력 2 
# 4
# RRRDDDDULL
# 예제 출력 2 
# ---+
# ...|
# .--+
# ...|
# 예제 입력 3 
# 5
# RRDDLLUURRDDLLUUR
# 예제 출력 3 
# +-+..
# |.|..
# +-+..
# .....
# .....


N = int(input())
move = list(input())

board = [['.'] * N for _ in range(N)]
now_r = now_c = 0

for i in range(len(move)):
    match move[i]:
        case 'U':
            new_r, new_c = now_r - 1, now_c
        
        case 'D':
            new_r, new_c = now_r + 1, now_c

        case 'L':
            new_r, new_c = now_r, now_c - 1
       
        case 'R':
            new_r, new_c = now_r, now_c + 1


    if not(0 <= new_r < N and 0 <= new_c < N):
        continue

    
    match move[i]:
        case 'U' | 'D':
            if board[new_r][new_c] in ['-', '+']:
                board[new_r][new_c] = '+'
            else:
                board[new_r][new_c] = '|'

            if board[now_r][now_c] in ['-', '+']:
                board[now_r][now_c] = '+'
            else:
                board[now_r][now_c] = '|'

        case 'L' | 'R':
            if board[new_r][new_c] in ['|', '+']:
                board[new_r][new_c] = '+'
            else:
                board[new_r][new_c] = '-'

            if board[now_r][now_c] in ['|', '+']:
                board[now_r][now_c] = '+'
            else:
                board[now_r][now_c] = '-'

    now_r, now_c = new_r, new_c

for r in board:
    print(''.join(r))


