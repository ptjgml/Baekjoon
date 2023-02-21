

'''
# 24479 알고리즘 수업- 깊이 우선 탐색1
# ---- dfs 방법 -----
# def dfs(R):
#     count = [0] * (N+1)
#     v = R
#     stack.append(v)
#     visited[v] = True
#     num = 1

#     count[v] = num
#     while stack:
#         for w in adjL[v]:
#             if visited[w] == False:
#                 visited[w] = True
#                 v = w       
#                 stack.append(v)
#                 num += 1
#                 count[v] = num
#                 break
#             else:
#                 if stack:
#                     v = stack.pop()
#     return count[1:]

# N, M, R = map(int, input().split())
# adjL = [[] for _ in range(N+1)]
# stack = []
# visited = [False] * (N+1)
# for i in range(M):
#     u, v = map(int, input().split())
#     adjL[u].append(v)
#     adjL[v].append(u)
#     adjL[u].sort()
#     adjL[v].sort()

# result = dfs(R)
# for i in result:
#     print(i)



# ---- 재귀 방법 -----
import sys
sys.setrecursionlimit(10**9)
def dfs(v):    
    global num
    visited[v] = num
    for w in adjL[v]:
        if visited[w] == 0:  
            num += 1
            dfs(w)

N, M, R = map(int, sys.stdin.readline().split())
adjL = [[] for _ in range(N+1)]
visited = [0] * (N+1)    
num = 1

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adjL[u].append(v)   # 양 방향이므로 다 append
    adjL[v].append(u)
for j in adjL:
    j.sort()    # 

dfs(R)
for i in range(1, N+1):
    print(visited[i])

'''






'''
#1012 유기농 배추
import sys
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(s_y, s_x):

    Q.append((s_y, s_x))
    visited[s_y][s_x] = True
    check[s_y][s_x] = 0
    count = 0
    while Q:
        v_y, v_x = Q.pop(0)
        for k in range(4):
            newR = v_y + di[k]                    
            newC = v_x + dj[k]

            if 0 <= newR < N and 0<= newC < M and visited[newR][newC] == False and check[newR][newC] == 1:
                Q.append((newR,newC))
                visited[newR][newC] = True
                check[newR][newC] = 0
    else:
        count += 1
    # if not Q and cabbage:
    #     v_y, v_x = cabbage.pop(0)
    #     Q.append((v_y, v_x))
                
    return count

T = int(sys.stdin.readline())

for t in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    # cabbage = []
    check = [[0] * M for _ in range(N)]
    count = 0
    Q = []
    visited = [[False] * M for _ in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        # cabbage.append((y, x))
        check[y][x] = 1

    # for i in cabbage:
    #     y, x = i[0], i[1]
    #     if check[y][x] == 1:
    #         count = count + bfs(y, x)
    for i in range(M):
        for j in range(N):
            if check[j][i] == 1:
                count = count+bfs(j,i)
    print(count)
'''



# 2578 빙고
def check(a, count):
    cnt = 0
    for i in range(5):
        for j in range(5):
            if bingo [i][j] == a:
                bingo[i][j] = 0

    for c in range(5):
        if bingo[c][:] == 0:
            count+= 1
        elif bingo[:][c] == 0:
            count+= 1

    for n in range(5):
        if bingo[n][n] == 0:
            cnt += 1
        if cnt == 5:
            count += 1

        if bingo[n][4-n] == 0:
            cnt += 1
        if cnt == 5:
            count += 1
    return count    

lst = [list(map(int, input().split())) for _ in range(10)]
bingo = lst[0:5]
call = lst[5:]
count = 0
call_count = 0

for i in call:
    for num in range(5):
        a = i[num]
        check(a, count)
        call_count += 1
        if count == 3:
            print(call_count)
        break
    if count == 3:
        break

        
