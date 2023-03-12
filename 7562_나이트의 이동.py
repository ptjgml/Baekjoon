# 문제
# 체스판 위에 한 나이트가 놓여져 있다.
# 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다.
# 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?
#
# 입력
# 입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.
#
# 각 테스트 케이스는 세 줄로 이루어져 있다.
# 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다.
# 체스판의 크기는 l × l이다.
# 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다.
# 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.
#
# 출력
# 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.


di = [-2,-1,1,2,2,1,-1,-2]
dj = [1,2,2,1,-1,-2,-2,-1]

def bfs(row, col):
    Q = []
    count = 0

    Q.append((row,col))
    while Q:
        Q.pop(0)
        if row == future[0] and col == future[1]:
            return visited[row][col]
        else:
            for k in range(8):
                row = row + di[k]
                col = col + dj[k]
                if 0 <= row < I and 0 <= col < I and visited[row][col] == 0:
                    visited[row][col] = 1
                    Q.append((row, col))

T = int(input())

for t in range(T):
    I = int(input())

    lst = [[0]*I for _ in range(I)]
    current = list(map(int,input().split()))
    future = list(map(int, input().split()))
    visited = [[0]*I for _ in range(I)]

    result = 100


    for k in range(8):
        count = 0
        newR = current[0] + di[k]
        newC = current[0] + dj[k]

        if 0<=newR < I and 0<=newC < I and visited[newR][newC] == 0:
            visited[newR][newC] = 1
            bfs(newR, newC)
            if result > count:
                result = count

    print(result)




