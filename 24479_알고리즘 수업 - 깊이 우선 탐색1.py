# 문제
# 오늘도 서준이는 깊이 우선 탐색(DFS) 수업 조교를 하고 있다. 
# 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

# N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다.
# 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다.
# 정점 R에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 
# 노드의 방문 순서를 출력하자.

# 깊이 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 오름차순으로 방문한다.

# dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
#     visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
#     for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
#         if (visited[x] = NO) then dfs(V, E, x);
# }
# 입력
# 첫째 줄에 정점의 수 N (5 ≤ N ≤ 100,000), 
# 간선의 수 M (1 ≤ M ≤ 200,000), 
# 시작 정점 R (1 ≤ R ≤ N)이 주어진다.

# 다음 M개 줄에 간선 정보 u v가 주어지며 
# 정점 u와 정점 v의 가중치 1인 양방향 간선을 나타낸다. 
# (1 ≤ u < v ≤ N, u ≠ v) 모든 간선의 (u, v) 쌍의 값은 서로 다르다.

# 출력
# 첫째 줄부터 N개의 줄에 정수를 한 개씩 출력한다. 
# i번째 줄에는 정점 i의 방문 순서를 출력한다. 
# 시작 정점의 방문 순서는 1이다. 
# 시작 정점에서 방문할 수 없는 경우 0을 출력한다.


'''
# 함수 안쓴 풀이
N, M, R = map(int, input().split())     # N : , M : , R : 
visited = [False] * (N+1)   # 방문했었는지 체크
stack = []  # 시작 노드 체크할 스택
lst = [[0]*(N+1) for _ in range(N+1)]   # 연결된 정점 표시할 리스트

for i in range(M):
    u, v = map(int, input().split())    # 방문할 정점들
    lst[u][v] = 1   # 양방향이므로 u에서 v 갔을 때
    lst[v][u] = 1   # v에서 u 갔을 때 모두 1로 체크

v = R   # 시작점 v에 첫 시작점 R 넣어줌
visited[v] = True   # 시작점 방문했으므로 visited에 True로 체크
stack.append(v) # 시작점 stack에 넣어줌

while stack:    # 스택이 차있는 동안
    v = stack.pop() # 시작을 어디서 했는지 알기 위해 스택에서 마지막으로 방문한 지점 꺼냄
    for i in range(N+1):    
        if lst[v][i] == 1 and visited[i] == False:  # 시작하는 곳에서 끝점이 1이고 끝점에 간적이 없다면
            stack.append(i) # 스택에 끝점 넣어줌
            visited[i] = True   # 끝점도 방문했었다고 체크

for j in range(1, N+1):
    if visited[j] == 1:
        print(j)
    else:
        print(0)
'''




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

